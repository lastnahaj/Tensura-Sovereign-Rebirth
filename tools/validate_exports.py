#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import tomllib
import zipfile
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "pack"
MODRINTH_DOMAINS = {
    "cdn.modrinth.com",
    "github.com",
    "raw.githubusercontent.com",
    "gitlab.com",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--curseforge", type=Path, required=True)
    parser.add_argument("--modrinth", type=Path, required=True)
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--require-publishable-modrinth", action="store_true")
    return parser.parse_args()


def digest(data: bytes, algorithm: str) -> str:
    return hashlib.new(algorithm, data).hexdigest()


def load_pack_sources(pack_dir: Path) -> tuple[dict[str, object], list[dict[str, object]], dict[str, str]]:
    pack_dir = pack_dir.resolve()
    pack = tomllib.loads((pack_dir / "pack.toml").read_text(encoding="utf-8"))
    metadata = []
    for path in sorted(pack_dir.rglob("*.pw.toml")):
        entry = tomllib.loads(path.read_text(encoding="utf-8"))
        entry["source_path"] = str(path)
        entry["pack_path"] = str(
            path.relative_to(pack_dir).parent / entry["filename"]
        ).replace("\\", "/")
        metadata.append(entry)

    index = tomllib.loads((pack_dir / "index.toml").read_text(encoding="utf-8"))
    pack_owned = {
        Path(entry["file"]).name: entry["hash"]
        for entry in index.get("files", [])
        if not entry.get("metafile") and str(entry.get("file", "")).endswith(".jar")
    }
    return pack, metadata, pack_owned


def validate_curseforge(
    artifact: Path,
    pack: dict[str, object],
    metadata: list[dict[str, object]],
    pack_owned: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    expected_files = {
        (entry["update"]["curseforge"]["project-id"], entry["update"]["curseforge"]["file-id"])
        for entry in metadata
        if entry.get("side") != "server" and "curseforge" in entry.get("update", {})
    }
    with zipfile.ZipFile(artifact) as archive:
        names = set(archive.namelist())
        manifest = json.loads(archive.read("manifest.json"))
        actual_files = {
            (entry["projectID"], entry["fileID"])
            for entry in manifest.get("files", [])
        }
        if actual_files != expected_files:
            errors.append("CurseForge project/file references differ from Packwiz metadata")
        if manifest.get("minecraft", {}).get("version") != pack["versions"]["minecraft"]:
            errors.append("CurseForge Minecraft version is incorrect")
        expected_loader = f"neoforge-{pack['versions']['neoforge']}"
        loaders = manifest.get("minecraft", {}).get("modLoaders", [])
        if not any(loader.get("id") == expected_loader and loader.get("primary") for loader in loaders):
            errors.append("CurseForge primary NeoForge version is incorrect")

        override_jars = {
            Path(name).name for name in names
            if name.startswith("overrides/mods/") and name.endswith(".jar")
        }
        external_overrides = {
            entry["filename"]: (entry["download"]["hash-format"], entry["download"]["hash"])
            for entry in metadata
            if entry.get("side") != "server" and "curseforge" not in entry.get("update", {})
        }
        expected_override_jars = set(pack_owned) | set(external_overrides)
        if override_jars != expected_override_jars:
            errors.append("CurseForge overrides contain unexpected or missing JARs")
        for filename, expected_hash in pack_owned.items():
            archive_path = f"overrides/mods/{filename}"
            if archive_path in names and digest(archive.read(archive_path), "sha256") != expected_hash:
                errors.append(f"CurseForge pack-owned JAR hash changed: {filename}")
        for filename, (hash_format, expected_hash) in external_overrides.items():
            archive_path = f"overrides/mods/{filename}"
            if archive_path in names and digest(archive.read(archive_path), hash_format) != expected_hash:
                errors.append(f"CurseForge external override hash changed: {filename}")
    return errors


def validate_modrinth(
    artifact: Path,
    pack: dict[str, object],
    metadata: list[dict[str, object]],
    pack_owned: dict[str, str],
    require_publishable: bool,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    with zipfile.ZipFile(artifact) as archive:
        names = set(archive.namelist())
        index = json.loads(archive.read("modrinth.index.json"))
        if index.get("formatVersion") != 1 or index.get("game") != "minecraft":
            errors.append("Modrinth pack format metadata is invalid")
        if index.get("dependencies") != pack["versions"]:
            errors.append("Modrinth Minecraft/NeoForge dependencies are incorrect")

        downloadable = {entry["path"]: entry for entry in index.get("files", [])}
        for entry in metadata:
            filename = entry["filename"]
            path = entry["pack_path"]
            side = entry.get("side", "both")
            override_prefix = {
                "client": "client-overrides",
                "server": "server-overrides",
                "both": "overrides",
            }.get(side, "overrides")
            override_path = f"{override_prefix}/{path}"
            hash_format = entry["download"]["hash-format"]
            expected_hash = entry["download"]["hash"]
            if override_path in names:
                if digest(archive.read(override_path), hash_format) != expected_hash:
                    errors.append(f"Modrinth embedded artifact hash changed: {filename}")
            elif path in downloadable:
                file_entry = downloadable[path]
                if file_entry.get("hashes", {}).get(hash_format) != expected_hash:
                    errors.append(f"Modrinth download hash changed: {filename}")
                domains = {urlparse(url).hostname for url in file_entry.get("downloads", [])}
                if not domains or not domains.issubset(MODRINTH_DOMAINS):
                    errors.append(f"Modrinth download uses a non-publishable domain: {filename}")
            else:
                errors.append(f"Modrinth artifact is missing: {filename}")

        for filename, expected_hash in pack_owned.items():
            archive_path = f"overrides/mods/{filename}"
            if archive_path not in names:
                errors.append(f"Modrinth pack-owned JAR is missing: {filename}")
            elif digest(archive.read(archive_path), "sha256") != expected_hash:
                errors.append(f"Modrinth pack-owned JAR hash changed: {filename}")

        embedded_third_party = sorted(
            entry["filename"] for entry in metadata
            if any(
                f"{prefix}/{entry['pack_path']}" in names
                for prefix in ("overrides", "client-overrides", "server-overrides")
            )
        )
        if embedded_third_party:
            message = (
                "Modrinth archive embeds third-party artifacts without an allowed-domain "
                "download source: " + ", ".join(embedded_third_party)
            )
            if require_publishable:
                errors.append(message)
            else:
                warnings.append(message)
    return errors, warnings


def main() -> int:
    args = parse_args()
    pack, metadata, pack_owned = load_pack_sources(args.pack_dir)
    errors = validate_curseforge(args.curseforge, pack, metadata, pack_owned)
    modrinth_errors, warnings = validate_modrinth(
        args.modrinth,
        pack,
        metadata,
        pack_owned,
        args.require_publishable_modrinth,
    )
    errors.extend(modrinth_errors)
    if errors:
        raise SystemExit("Export validation failed:\n- " + "\n- ".join(errors))
    print(f"CurseForge export OK: {args.curseforge}")
    print(f"Modrinth format OK: {args.modrinth}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
