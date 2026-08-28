#!/usr/bin/env python3
"""Validate a NeoForge dedicated-server start, save, and clean shutdown."""

from __future__ import annotations

import argparse
import queue
import re
import shutil
import subprocess
import threading
import time
from pathlib import Path


READY = re.compile(r"Done \(([0-9.]+)s\)! For help")
QUESTS = re.compile(
    r"Loaded\s+1\s+(?:chapter\s+)?groups?,\s+1\s+chapters?,\s+([0-9]+)\s+quests?",
    re.I,
)
FATAL_MARKERS = (
    "Failed to create mod instance",
    "MixinApplyError",
    "InjectionError",
    "InvalidInjectionException",
    "Exception caught during firing event",
    "Registry ResourceKey[minecraft:root / manascore_",
    "A fatal error has been detected by the Java Runtime Environment",
)
FORBIDDEN_MOD_PATTERNS = (
    "traddon",
    "tensurauniquemonsters",
    "tsr-unique-monsters-compat",
    "grieflogger",
    "trgrieflogger",
    "iceandfire",
    "tensura_ice",
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("server_dir", type=Path)
    parser.add_argument("--mode", choices=("cold", "warm"), required=True)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--minimum-quests", type=int, default=8)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--java", type=Path, default=Path("java"))
    return parser.parse_args()


def read_output(process: subprocess.Popen[str], output: queue.Queue[str | None]) -> None:
    assert process.stdout is not None
    for line in process.stdout:
        output.put(line)
    output.put(None)


def stop_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=10)


def validated_paths(server_dir: Path, log_path: Path) -> tuple[Path, Path, Path]:
    repository = Path(__file__).resolve().parents[1]
    build_root = (repository / ".build").resolve()
    server_dir = server_dir.resolve()
    log_path = log_path.resolve()
    if not server_dir.is_relative_to(build_root):
        raise ValueError(f"Server directory must be inside {build_root}")
    if not log_path.is_relative_to(build_root):
        raise ValueError(f"Log path must be inside {build_root}")

    required = (
        "eula.txt",
        "server.properties",
        "user_jvm_args.txt",
        "libraries/net/neoforged/neoforge/21.1.248/win_args.txt",
    )
    for relative in required:
        if not (server_dir / relative).is_file():
            raise ValueError(f"Missing server input: {relative}")

    properties: dict[str, str] = {}
    for line in (server_dir / "server.properties").read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            properties[key] = value
    level_name = properties.get("level-name", "world")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", level_name) or level_name in {".", ".."}:
        raise ValueError(f"Unsafe level-name: {level_name!r}")
    world_dir = (server_dir / level_name).resolve()
    if world_dir.parent != server_dir:
        raise ValueError("World directory escapes the server directory")
    return server_dir, world_dir, log_path


def main() -> int:
    args = arguments()
    server_dir, world_dir, log_path = validated_paths(args.server_dir, args.log)
    if args.mode == "cold" and world_dir.exists():
        shutil.rmtree(world_dir)

    mod_names = [path.name.lower() for path in (server_dir / "mods").glob("*") if path.is_file()]
    forbidden = sorted(
        name for name in mod_names if any(pattern in name for pattern in FORBIDDEN_MOD_PATTERNS)
    )
    if forbidden:
        raise RuntimeError("Forbidden playable-profile mods are present: " + ", ".join(forbidden))
    if not any("beyond_adventures-neoforge-1.1.9.jar" == name for name in mod_names):
        raise RuntimeError("Beyond Adventures 1.1.9 is missing")

    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(args.java),
        "@user_jvm_args.txt",
        "@libraries/net/neoforged/neoforge/21.1.248/win_args.txt",
        "nogui",
    ]
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
    output: queue.Queue[str | None] = queue.Queue()
    thread = threading.Thread(target=read_output, args=(process, output), daemon=True)
    thread.start()

    started = time.monotonic()
    deadline = started + args.timeout
    lines: list[str] = []
    ready_match: re.Match[str] | None = None
    quest_count = 0
    save_sent = False
    saved = False
    stop_sent = False
    stream_closed = False

    while not stream_closed:
        if time.monotonic() > deadline:
            stop_process(process)
            log_path.write_text("".join(lines), encoding="utf-8")
            raise RuntimeError(f"Server {args.mode} test timed out; log={log_path}")
        try:
            line = output.get(timeout=0.5)
        except queue.Empty:
            continue
        if line is None:
            stream_closed = True
            continue
        lines.append(line)
        if ready_match is None:
            ready_match = READY.search(line)
        quest_match = QUESTS.search(line)
        if quest_match:
            quest_count = max(quest_count, int(quest_match.group(1)))
        if ready_match is not None and not save_sent:
            assert process.stdin is not None
            process.stdin.write("save-all flush\n")
            process.stdin.flush()
            save_sent = True
            deadline = time.monotonic() + 90
        if save_sent and "Saved the game" in line:
            saved = True
        if saved and not stop_sent:
            assert process.stdin is not None
            process.stdin.write("stop\n")
            process.stdin.flush()
            stop_sent = True
            deadline = time.monotonic() + 90

    exit_code = process.wait(timeout=5)
    text = "".join(lines)
    log_path.write_text(text, encoding="utf-8")
    failures: list[str] = []
    if exit_code != 0:
        failures.append(f"exit code {exit_code}")
    if ready_match is None:
        failures.append("server did not reach Done")
    if not saved:
        failures.append("save-all flush did not complete")
    if "Stopping server" not in text or "All dimensions are saved" not in text:
        failures.append("clean shutdown markers are missing")
    if quest_count < args.minimum_quests:
        failures.append(f"loaded {quest_count} quests; expected at least {args.minimum_quests}")
    lower_text = text.lower()
    for marker in FATAL_MARKERS:
        if marker.lower() in lower_text:
            failures.append(f"fatal marker: {marker}")
    if failures:
        raise RuntimeError("; ".join(failures) + f"; log={log_path}")

    elapsed = time.monotonic() - started
    assert ready_match is not None
    print(
        f"Server {args.mode} test passed: startup={ready_match.group(1)}s, "
        f"quests={quest_count}, elapsed={elapsed:.1f}s, log={log_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
