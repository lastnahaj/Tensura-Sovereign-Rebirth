#!/usr/bin/env python3
"""Run repeatable clean-world dedicated-server starts for Unique Monsters compat."""

from __future__ import annotations

import argparse
import json
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path


READY_PATTERN = re.compile(r"Done \([0-9.]+s\)! For help")
SKILL_VERIFIED = (
    "Unique Monsters skills registered successfully: "
    "tr_unique_monsters:appraisal_eye."
)
DEFERRED = (
    "Deferred Unique Monsters skill registration until ManasCore skill "
    "registry initialization."
)
SUBMITTED = (
    "Unique Monsters skill registration submitted after ManasCore "
    "SkillRegistry construction."
)
MISSING_REGISTRY = (
    "Registry ResourceKey[minecraft:root / manascore_skill:skills] does not exist"
)
FATAL_MARKERS = (
    MISSING_REGISTRY,
    "MixinApplyError",
    "InjectionError",
    "InvalidInjectionException",
    "Cannot register a deferred register twice",
    "Duplicate key",
    "already registered: tr_unique_monsters:appraisal_eye",
    "frozen registry",
)
SAVE_COMPLETE = "Saved the game"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("server_dir", type=Path)
    parser.add_argument("--runs", type=int, default=20)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument(
        "--preserve-world",
        action="store_true",
        help="Reuse the existing test world instead of creating a clean world for each run.",
    )
    parser.add_argument(
        "--java",
        type=Path,
        default=Path(r"C:\Program Files\Common Files\Oracle\Java\javapath\java.exe"),
    )
    return parser.parse_args()


def validate_server_dir(server_dir: Path, java: Path) -> tuple[Path, Path]:
    workspace = Path(__file__).resolve().parents[1]
    build_root = (workspace / ".build").resolve()
    server_dir = server_dir.resolve()
    if not server_dir.is_relative_to(build_root):
        raise ValueError(f"Server directory must be inside {build_root}")
    for relative in (
        "eula.txt",
        "server.properties",
        "user_jvm_args.txt",
        "libraries/net/neoforged/neoforge/21.1.248/win_args.txt",
        "mods/tensurauniquemonsters-neoforge-1.0.2.jar",
        "mods/tsr-unique-monsters-compat-1.0.0.jar",
    ):
        if not (server_dir / relative).is_file():
            raise ValueError(f"Missing required test input: {relative}")
    if not java.is_file():
        raise ValueError(f"Java executable not found: {java}")

    properties = {}
    for line in (server_dir / "server.properties").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            properties[key] = value
    level_name = properties.get("level-name", "world")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", level_name) or level_name in {".", ".."}:
        raise ValueError(f"Unsafe level-name in server.properties: {level_name!r}")
    world_dir = (server_dir / level_name).resolve()
    if world_dir.parent != server_dir:
        raise ValueError(f"World directory escapes the server directory: {world_dir}")
    return server_dir, world_dir


def reader_thread(process: subprocess.Popen[str], output: queue.Queue[str | None]) -> None:
    assert process.stdout is not None
    for line in process.stdout:
        output.put(line)
    output.put(None)


def terminate_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=10)


def run_once(
    server_dir: Path,
    world_dir: Path,
    java: Path,
    timeout: int,
    run_number: int,
    total_runs: int,
    log_dir: Path,
    preserve_world: bool,
) -> dict[str, object]:
    if world_dir.exists() and not preserve_world:
        shutil.rmtree(world_dir)

    command = [
        str(java),
        "@user_jvm_args.txt",
        "@libraries/net/neoforged/neoforge/21.1.248/win_args.txt",
        "nogui",
    ]
    started = time.monotonic()
    run_type = "warm-restart" if preserve_world else "cold-start"
    log_path = log_dir / f"{run_type}-{run_number:02d}.log"
    process = subprocess.Popen(
        command,
        cwd=server_dir,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )
    output_queue: queue.Queue[str | None] = queue.Queue()
    thread = threading.Thread(target=reader_thread, args=(process, output_queue), daemon=True)
    thread.start()

    lines: list[str] = []
    ready = False
    skill_seen = False
    labyrinth_complete = False
    save_requested = False
    save_complete = False
    stop_sent = False
    stream_closed = False
    startup_deadline = started + timeout
    save_deadline: float | None = None
    shutdown_deadline: float | None = None

    while not stream_closed:
        now = time.monotonic()
        if stop_sent:
            deadline = shutdown_deadline
            phase = "shutdown"
        elif save_requested:
            deadline = save_deadline
            phase = "save flush"
        else:
            deadline = startup_deadline
            phase = "startup"
        if deadline is not None and now > deadline:
            terminate_process(process)
            log_path.write_text("".join(lines), encoding="utf-8")
            raise RuntimeError(f"Run {run_number} exceeded the {phase} timeout")
        try:
            line = output_queue.get(timeout=0.5)
        except queue.Empty:
            if process.poll() is not None:
                continue
            continue
        if line is None:
            stream_closed = True
            continue
        lines.append(line)
        if READY_PATTERN.search(line):
            ready = True
        if SKILL_VERIFIED in line:
            skill_seen = True
        if "[Tensura/LabyrinthStorage/]" in line and "Generation took" in line:
            labyrinth_complete = True
        if save_requested and SAVE_COMPLETE in line:
            save_complete = True
        lifecycle_ready = labyrinth_complete or preserve_world
        if ready and skill_seen and lifecycle_ready and not save_requested:
            assert process.stdin is not None
            process.stdin.write("save-all flush\n")
            process.stdin.flush()
            save_requested = True
            save_deadline = time.monotonic() + timeout
        if save_complete and not stop_sent:
            assert process.stdin is not None
            process.stdin.write("stop\n")
            process.stdin.flush()
            stop_sent = True
            shutdown_deadline = time.monotonic() + 60

    exit_code = process.wait(timeout=5)
    elapsed = time.monotonic() - started
    log_text = "".join(lines)
    log_path.write_text(log_text, encoding="utf-8")

    failures: list[str] = []
    if exit_code != 0:
        failures.append(f"exit code {exit_code}")
    if not ready:
        failures.append("server did not reach Done")
    if not labyrinth_complete and not preserve_world:
        failures.append("Tensura labyrinth generation did not complete")
    if not save_complete:
        failures.append("save-all flush did not complete")
    if log_text.count(SKILL_VERIFIED) != 1:
        failures.append(f"skill verification count was {log_text.count(SKILL_VERIFIED)}")
    if log_text.count(DEFERRED) != 1:
        failures.append(f"premature-call interception count was {log_text.count(DEFERRED)}")
    if log_text.count(SUBMITTED) != 1:
        failures.append(f"safe registration count was {log_text.count(SUBMITTED)}")
    if "Stopping server" not in log_text or "All dimensions are saved" not in log_text:
        failures.append("clean shutdown markers missing")
    for marker in FATAL_MARKERS:
        if marker.lower() in log_text.lower():
            failures.append(f"fatal log marker found: {marker}")
    if failures:
        raise RuntimeError(f"Run {run_number} failed: {'; '.join(failures)}; log={log_path}")

    label = "Warm restart" if preserve_world else "Cold start"
    print(f"{label} {run_number:02d}/{total_runs}: PASS ({elapsed:.1f}s)", flush=True)
    return {
        "run": run_number,
        "result": "PASS",
        "elapsed_seconds": round(elapsed, 3),
        "log": str(log_path),
    }


def main() -> int:
    args = parse_args()
    if args.runs < 1:
        raise ValueError("--runs must be positive")
    server_dir, world_dir = validate_server_dir(args.server_dir, args.java)
    log_dir = server_dir / "compat-stress-logs"
    log_dir.mkdir(exist_ok=True)

    results = []
    for run_number in range(1, args.runs + 1):
        try:
            results.append(
                run_once(
                    server_dir,
                    world_dir,
                    args.java,
                    args.timeout,
                    run_number,
                    args.runs,
                    log_dir,
                    args.preserve_world,
                )
            )
        except Exception as exception:
            results.append({"run": run_number, "result": "FAIL", "reason": str(exception)})
            summary_name = "summary-warm.json" if args.preserve_world else "summary.json"
            (log_dir / summary_name).write_text(
                json.dumps(results, indent=2) + "\n", encoding="utf-8"
            )
            print(exception, file=sys.stderr, flush=True)
            return 1

    summary_name = "summary-warm.json" if args.preserve_world else "summary.json"
    (log_dir / summary_name).write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8"
    )
    label = "Warm restarts" if args.preserve_world else "Cold starts"
    print(f"{label}: {len(results)}/{args.runs} PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
