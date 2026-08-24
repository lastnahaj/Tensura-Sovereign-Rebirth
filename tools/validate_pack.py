#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
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
REQUIRED_PHASE_2_CONFIGS = {
    Path("craftedcore.json5"),
    Path("greatsage-client.toml"),
    Path("greatsage-common.toml"),
    Path("remorphed.json5"),
    Path("stextras/client/general.json"),
    Path("tensura/neb_config.toml"),
    Path("tensura_boss_structure-common.toml"),
    Path("tensura_guild-common.toml"),
    Path("tensura_skill_books/tensura_skill_books-common.toml"),
    Path("tensura_skill_books/tensura_skill_books-loot-skills.txt"),
    Path("tensura_skill_books/tensura_skill_books-loot-tables.txt"),
    Path("tensura_skill_books/tensura_skill_books-random-skills.txt"),
    Path("tensuramorph-common.toml"),
    Path("walkers.json5"),
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
if len(config_files) < 124:
    errors.append(f"Expected at least 124 promoted config files; found {len(config_files)}")

for relative in sorted(REQUIRED_PHASE_2_CONFIGS):
    if not (CONFIG / relative).is_file():
        errors.append(f"Missing reviewed Phase 2 config: {relative}")

for path in config_files:
    try:
        if path.suffix == ".toml":
            tomllib.loads(path.read_text(encoding="utf-8"))
        elif path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid config {path.relative_to(CONFIG)}: {exc}")

runtime_state = CONFIG / "stextras" / "internal" / "tensura_config_patcher_state.toml"
if runtime_state.exists():
    errors.append("Mutable SlimeThrone config-patcher state must not be packaged")

craftedcore_cache = CONFIG / "craftedcore" / "cache" / "patreons.txt"
if craftedcore_cache.exists():
    errors.append("CraftedCore's generated supporter cache must not be packaged")

craftedcore_text = (CONFIG / "craftedcore.json5").read_text(encoding="utf-8")
if not re.search(r'"enableVersionChecking"\s*:\s*false', craftedcore_text):
    errors.append("CraftedCore background version checking must remain disabled")

remorphed_text = (CONFIG / "remorphed.json5").read_text(encoding="utf-8")
if not re.search(r'"creativeUnlockAll"\s*:\s*false', remorphed_text):
    errors.append("ReMorphed creative automatic unlocks must remain disabled")
if not re.search(r'"killToUnlock"\s*:\s*100000', remorphed_text):
    errors.append("ReMorphed ordinary-kill unlock threshold must remain 100000")

try:
    tensuramorph = tomllib.loads(
        (CONFIG / "tensuramorph-common.toml").read_text(encoding="utf-8")
    )
    if tensuramorph.get("unlockThreshold") != 100000:
        errors.append("TensuraMorph unlock threshold must remain 100000")
    if tensuramorph.get("disableRemorphedCreativeUnlockAll") is not True:
        errors.append("TensuraMorph must disable ReMorphed creative unlocks")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid TensuraMorph config: {exc}")

loot_table_config = CONFIG / "tensura_skill_books" / "tensura_skill_books-loot-tables.txt"
for line_number, line in enumerate(loot_table_config.read_text(encoding="utf-8").splitlines(), 1):
    stripped = line.strip()
    if stripped and not stripped.startswith("#") and not stripped.endswith("()"):
        errors.append(
            "Skill Books natural loot must remain empty before authored rewards are validated: "
            f"line {line_number}"
        )
        break

try:
    greatsage_client = tomllib.loads(
        (CONFIG / "greatsage-client.toml").read_text(encoding="utf-8")
    )
    if greatsage_client.get("general", {}).get("voiceInput") != "off":
        errors.append("Great Sage voice input must remain off by default")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Great Sage client config: {exc}")

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
