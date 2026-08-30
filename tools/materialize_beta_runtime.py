#!/usr/bin/env python3
"""Materialize a tested client or server runtime from the Packwiz source."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import tomllib
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
BUILD = ROOT / ".build"
PLAYABLE_BLOCKED = {
    "grieflogger.pw.toml",
    "tensura-grief-logger.pw.toml",
    "iceandfire-ce.pw.toml",
    "tensura-compat-ice-fire.pw.toml",
}
FORBIDDEN = (
    "traddon",
    "tensurauniquemonsters",
    "tsr-unique-monsters-compat",
    "tensura-trainer",
    "c2me-neoforge",
    "tensura_fancymenu",
    "grieflogger",
    "trgrieflogger",
    "iceandfire",
    "tensura_ice",
)
PACK_OWNED = {
    "both": ("tsr-sgear-metalworks-compat-1.0.0.jar",),
    "client": ("tsr-client-stability-1.0.0.jar",),
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", choices=("client", "server"), required=True)
    parser.add_argument("--base-runtime", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-mods", type=Path, action="append", default=[])
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def digest(path: Path, algorithm: str) -> str:
    value = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def matches(path: Path, download: dict[str, object]) -> bool:
    algorithm = str(download.get("hash-format", ""))
    expected = str(download.get("hash", ""))
    return not algorithm or not expected or digest(path, algorithm) == expected


def verify(path: Path, download: dict[str, object]) -> None:
    if not matches(path, download):
        raise RuntimeError(f"Hash mismatch for {path.name}")


def find_source(
    filename: str, sources: list[Path], download: dict[str, object]
) -> Path | None:
    for source in sources:
        candidate = source / filename
        if candidate.is_file() and matches(candidate, download):
            return candidate
    return None


def main() -> int:
    args = arguments()
    base = args.base_runtime.resolve()
    output = args.output.resolve()
    if not base.is_relative_to(BUILD.resolve()):
        raise SystemExit("Base runtime must be inside .build")
    if not output.is_relative_to(BUILD.resolve()):
        raise SystemExit("Output runtime must be inside .build")
    if output.exists() and not args.resume:
        raise SystemExit(f"Output already exists: {output}")

    output.mkdir(parents=True, exist_ok=True)
    base_items = (
        ("libraries", "natives", "versions", "launch_client_smoke.py")
        if args.side == "client"
        else ("libraries",)
    )
    for name in base_items:
        source = base / name
        if source.is_dir():
            shutil.copytree(source, output / name, dirs_exist_ok=True)
        elif source.is_file():
            shutil.copy2(source, output / name)

    for name in ("config", "defaultconfigs", "kubejs"):
        source = PACK / name
        if source.is_dir():
            shutil.copytree(source, output / name, dirs_exist_ok=True)
    if args.side == "client":
        shutil.copy2(PACK / "options.txt", output / "options.txt")
    else:
        accepted_eula = base / "eula.txt"
        shutil.copy2(
            accepted_eula if accepted_eula.is_file() else ROOT / "server" / "eula.txt",
            output / "eula.txt",
        )
        shutil.copy2(ROOT / "server" / "user_jvm_args.txt", output / "user_jvm_args.txt")
        shutil.copy2(ROOT / "server" / "server.properties.template", output / "server.properties")

    mods = output / "mods"
    mods.mkdir(exist_ok=True)
    sources = [path.resolve() for path in args.source_mods]
    sources.extend(
        ((mods.resolve()), (base / "mods").resolve(), (PACK / "mods").resolve())
    )
    selected: list[tuple[Path, dict[str, object]]] = []
    for metadata_path in sorted((PACK / "mods").glob("*.pw.toml")):
        if metadata_path.name in PLAYABLE_BLOCKED:
            continue
        metadata = tomllib.loads(metadata_path.read_text(encoding="utf-8"))
        side = str(metadata.get("side", "both"))
        if side not in ("both", args.side):
            continue
        selected.append((metadata_path, metadata))

    for metadata_path, metadata in selected:
        filename = str(metadata["filename"])
        lowered = filename.lower()
        if any(value in lowered for value in FORBIDDEN):
            raise RuntimeError(f"Forbidden playable-profile mod selected: {filename}")
        destination = mods / filename
        download = metadata.get("download", {})
        if not isinstance(download, dict):
            raise RuntimeError(f"Invalid download metadata: {metadata_path.name}")
        source = find_source(filename, sources, download)
        if source:
            if source.resolve() != destination.resolve():
                shutil.copy2(source, destination)
        elif download.get("url"):
            print(f"Downloading {filename}", flush=True)
            urllib.request.urlretrieve(str(download["url"]), destination)
        else:
            raise RuntimeError(
                f"No exact local artifact or direct URL for {filename} ({metadata_path.name})"
            )
        verify(destination, download)

    local_names = [*PACK_OWNED["both"]]
    if args.side == "client":
        local_names.extend(PACK_OWNED["client"])
    for filename in local_names:
        source = PACK / "mods" / filename
        destination = mods / filename
        shutil.copy2(source, destination)

    expected_names = {
        str(metadata["filename"]) for _, metadata in selected
    } | set(local_names)
    for stale in sorted(mods.glob("*.jar")):
        if stale.name not in expected_names:
            stale.unlink()

    filenames = sorted(path.name for path in mods.glob("*.jar"))
    forbidden = [
        name for name in filenames if any(value in name.lower() for value in FORBIDDEN)
    ]
    if forbidden:
        raise RuntimeError("Forbidden runtime artifacts: " + ", ".join(forbidden))
    print(f"Materialized {args.side} runtime: {len(filenames)} JARs at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
