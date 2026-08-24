#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
PACK_FILE = PACK / "pack.toml"
CONFIG = PACK / "config"
EXPECTED = {
    "minecraft": "1.21.1",
    "neoforge": "21.1.248",
}
PACK_OWNED_JARS = {
    Path("pack/mods/tsr-unique-monsters-compat-1.0.0.jar"):
        "e5b9799bb648d1933c7e50b980ecbfc4a8bc24e91008f46380133d49a85a5a65",
}
ALLOWED_TOOL_JARS = {
    Path("compat/tsr-unique-monsters-compat/gradle/wrapper/gradle-wrapper.jar"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


errors: list[str] = []

try:
    pack = tomllib.loads(PACK_FILE.read_text(encoding="utf-8"))
except (OSError, tomllib.TOMLDecodeError) as exc:
    raise SystemExit(f"Invalid Packwiz pack metadata: {exc}") from None

if pack.get("pack-format") != "packwiz:1.1.0":
    errors.append(f"Unexpected pack format: {pack.get('pack-format')!r}")
if pack.get("version") != "1.0.0-beta.1":
    errors.append(f"Unexpected pack version: {pack.get('version')!r}")

versions = pack.get("versions", {})
for key, expected in EXPECTED.items():
    if versions.get(key) != expected:
        errors.append(f"{key} is {versions.get(key)!r}; expected {expected!r}")

index_data = pack.get("index", {})
index_path = PACK / index_data.get("file", "")
if not index_path.is_file():
    errors.append(f"Missing Packwiz index: {index_path.relative_to(ROOT)}")
    index: dict = {}
else:
    actual_index_hash = sha256(index_path)
    if index_data.get("hash-format") != "sha256":
        errors.append("Packwiz index hash format must be sha256")
    if index_data.get("hash") != actual_index_hash:
        errors.append(
            f"Packwiz index hash is stale: {index_data.get('hash')!r}; "
            f"expected {actual_index_hash!r}"
        )
    try:
        index = tomllib.loads(index_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"Invalid Packwiz index: {exc}")
        index = {}
    if index.get("hash-format") != "sha256":
        errors.append("Indexed file hash format must be sha256")
    for entry in index.get("files", []):
        relative = entry.get("file", "")
        indexed_path = PACK / relative
        if not indexed_path.is_file():
            errors.append(f"Indexed file is missing: {relative}")
        elif entry.get("hash") != sha256(indexed_path):
            errors.append(f"Indexed file hash is stale: {relative}")

repository_jars = [
    path.relative_to(ROOT)
    for path in ROOT.rglob("*.jar")
    if ".build" not in path.parts
    and ".git" not in path.parts
    and "build" not in path.relative_to(ROOT).parts
]
unexpected_jars = [
    path for path in repository_jars
    if path not in PACK_OWNED_JARS and path not in ALLOWED_TOOL_JARS
]
if unexpected_jars:
    errors.append("Repository contains unexpected JARs: " + ", ".join(map(str, unexpected_jars)))

for relative, expected_hash in PACK_OWNED_JARS.items():
    artifact = ROOT / relative
    if not artifact.is_file():
        errors.append(f"Missing pack-owned JAR: {relative}")
    elif sha256(artifact) != expected_hash:
        errors.append(f"Pack-owned JAR hash changed: {relative}")

config_files = [path for path in CONFIG.rglob("*") if path.is_file()]
if len(config_files) < 109:
    errors.append(f"Expected at least 109 promoted config files; found {len(config_files)}")

runtime_state = CONFIG / "stextras" / "internal" / "tensura_config_patcher_state.toml"
if runtime_state.exists():
    errors.append("Mutable SlimeThrone config-patcher state must not be packaged")

origins_general = CONFIG / "trorigins" / "general.toml"
reincarnation_config = CONFIG / "tensura" / "reincarnation_config.toml"
try:
    origins = tomllib.loads(origins_general.read_text(encoding="utf-8"))
    if origins.get("General", {}).get("refresh") is not False:
        errors.append("Tensura: Origins automatic starter-pool refresh must remain disabled")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Origins config: {exc}")

try:
    reincarnation = tomllib.loads(reincarnation_config.read_text(encoding="utf-8"))
    race_config = reincarnation.get("Races", {})
    for pool in ("startingRaces", "randomRaces"):
        gated = [race for race in race_config.get(pool, []) if race.startswith("trorigins:")]
        if gated:
            errors.append(f"Origins races leaked into {pool}: {', '.join(gated)}")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Tensura reincarnation config: {exc}")

if errors:
    raise SystemExit("Pack validation failed:\n- " + "\n- ".join(errors))

print(
    f"Pack OK: Minecraft {versions['minecraft']}, NeoForge {versions['neoforge']}, "
    f"{len(index.get('files', []))} indexed files"
)
