#!/usr/bin/env python3
"""Build a deterministic private-beta dedicated-server archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import tomllib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
SERVER = ROOT / "server"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
EXPECTED_MOD_COUNT = 175
FORBIDDEN_MOD_PATTERNS = (
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
REQUIRED_SERVER_FILES = (
    "run.bat",
    "run.sh",
    "user_jvm_args.txt",
    "eula.txt",
    "README.md",
)
EXCLUSIONS = (
    {
        "system": "TR Addon 2.0.1",
        "status": "DEFERRED-BLOCKED",
        "reason": "ManasCore race/skill registry construction race",
    },
    {
        "system": "Tensura: Unique Monsters 1.0.2",
        "status": "DEFERRED-BLOCKED",
        "reason": "ManasCore skill registry construction race",
    },
    {
        "system": "Tensura Skill Trainer 2.0.5",
        "status": "USER-OPTIONAL-NOT-SHIPPED",
        "reason": "player-managed optional mod",
    },
    {
        "system": "C2ME 0.4.0-alpha.0.120",
        "status": "DEFERRED-BLOCKED",
        "reason": "clean dedicated-server shutdown hang",
    },
    {
        "system": "GriefLogger + Tensura: Grief Logger",
        "status": "PLAYABLE-PROFILE-BLOCKED",
        "reason": "required bootstrap mixin injection failure",
    },
    {
        "system": "IceAndFire CE + Tensura Compat: Ice & Fire",
        "status": "PLAYABLE-PROFILE-BLOCKED",
        "reason": "compatibility mixin targets removed upstream registry classes",
    },
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("runtime", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def archive_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name.replace("\\", "/"), FIXED_TIMESTAMP)
    info.create_system = 3
    mode = 0o755 if name.endswith(".sh") else 0o644
    info.external_attr = (stat.S_IFREG | mode) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    return info


def collect_tree(source: Path, destination: Path) -> list[tuple[Path, str]]:
    return [
        (path, (destination / path.relative_to(source)).as_posix())
        for path in sorted(source.rglob("*"))
        if path.is_file() and path.name != ".gitkeep"
    ]


def main() -> int:
    args = arguments()
    build_root = (ROOT / ".build").resolve()
    runtime = args.runtime.resolve()
    if not runtime.is_relative_to(build_root):
        raise SystemExit(f"Runtime must be inside {build_root}")

    pack = tomllib.loads((PACK / "pack.toml").read_text(encoding="utf-8"))
    version = pack["version"]
    output = (
        args.output.resolve()
        if args.output
        else (ROOT / "dist" / f"Tensura-Sovereign-Rebirth-{version}-Playable-Server.zip")
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    mods = sorted(path for path in (runtime / "mods").glob("*.jar") if path.is_file())
    if len(mods) != EXPECTED_MOD_COUNT:
        raise SystemExit(f"Expected {EXPECTED_MOD_COUNT} server JARs; found {len(mods)}")
    forbidden = sorted(
        path.name
        for path in mods
        if any(pattern in path.name.lower() for pattern in FORBIDDEN_MOD_PATTERNS)
    )
    if forbidden:
        raise SystemExit("Forbidden playable-profile JARs: " + ", ".join(forbidden))

    beyond = runtime / "mods" / "Beyond_Adventures-Neoforge-1.1.9.jar"
    expected_beyond_sha256 = "4d2b4e3277bd2fd2209422666e8b63a203bf093f9847c8fbd96d09f20469e39c"
    if not beyond.is_file() or sha256(beyond) != expected_beyond_sha256:
        raise SystemExit("Beyond Adventures 1.1.9 is missing or has changed")

    required_runtime = (
        runtime / "libraries/net/neoforged/neoforge/21.1.248/win_args.txt",
        runtime / "libraries/net/neoforged/neoforge/21.1.248/unix_args.txt",
    )
    for path in required_runtime:
        if not path.is_file():
            raise SystemExit(f"Missing NeoForge runtime file: {path}")
    for name in REQUIRED_SERVER_FILES:
        if not (SERVER / name).is_file():
            raise SystemExit(f"Missing server source file: {name}")

    files: list[tuple[Path, str]] = []
    files.extend(collect_tree(runtime / "libraries", Path("libraries")))
    files.extend((path, f"mods/{path.name}") for path in mods)
    for directory in ("config", "defaultconfigs", "kubejs"):
        tree = collect_tree(PACK / directory, Path(directory))
        if directory == "config":
            tree = [
                item
                for item in tree
                if not item[1].startswith(("config/fancymenu/", "config/drippyloadingscreen/"))
            ]
        files.extend(tree)
    for name in REQUIRED_SERVER_FILES:
        destination = "SERVER_README.md" if name == "README.md" else name
        files.append((SERVER / name, destination))
    files.append((SERVER / "server.properties.template", "server.properties"))

    lock = {
        "name": pack["name"],
        "version": version,
        "minecraft": pack["versions"]["minecraft"],
        "neoforge": pack["versions"]["neoforge"],
        "java": 21,
        "profile": "playable-beta",
        "mod_count": len(mods),
        "mods": [{"file": path.name, "sha256": sha256(path)} for path in mods],
        "exclusions": EXCLUSIONS,
    }
    lock_bytes = (json.dumps(lock, indent=2) + "\n").encode("utf-8")

    temporary = output.with_name(output.name + ".building")
    if temporary.exists():
        temporary.unlink()
    with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source, destination in sorted(files, key=lambda item: item[1]):
            archive.writestr(archive_info(destination), source.read_bytes(), compresslevel=6)
        archive.writestr(archive_info("server-lock.json"), lock_bytes, compresslevel=6)
    temporary.replace(output)

    with zipfile.ZipFile(output) as archive:
        names = set(archive.namelist())
        if any(name.startswith(("world/", "logs/", "crash-reports/", "ftbbackups3/")) for name in names):
            raise SystemExit("Generated server archive contains mutable runtime state")
        if "config/ftbquests/quests/chapters/sovereign_rebirth.snbt" not in names:
            raise SystemExit("Generated server archive is missing the onboarding quests")
        if "kubejs/assets/tsr/textures/gui/quests/sovereign_rebirth.png" not in names:
            raise SystemExit("Generated server archive is missing the quest background")

    print(
        f"Server export OK: {output} ({len(mods)} mods, "
        f"sha256={sha256(output)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
