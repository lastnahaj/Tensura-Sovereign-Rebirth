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
    Path("pack/mods/tsr-sgear-metalworks-compat-1.0.0.jar"):
        "57155d3ffe03155029bb3c04b09fbb1b2a1e427cb9c5ef7f32a64af601d20514",
    Path("pack/mods/tsr-client-stability-1.0.0.jar"):
        "e044e888ca8169681c02453daa5969771a519e8c169cd1ed990edea71f2d251e",
}
DIRECT_DEPENDENCIES = {
    Path("mods/beyond-adventures.pw.toml"): {
        "name": "Beyond Adventures",
        "filename": "Beyond_Adventures-Neoforge-1.1.9.jar",
        "side": "both",
        "url": "https://cdn.modrinth.com/data/8gmeH2WM/versions/Ybm5N8pk/Beyond_Adventures-Neoforge-1.1.9.jar",
        "hash-format": "sha512",
        "hash": "db5951096dceba302ae36cea58d140c462fbe91b92948c7e57266e63988afb9a5ac584f7d7cacc8e5c5f7bdf69a12d32c8d1abd71dd9ac988264d3fe5e95876b",
    },
    Path("mods/ponder.pw.toml"): {
        "name": "Ponder",
        "filename": "ponder-neoforge-1.0.81+mc1.21.1.jar",
        "side": "both",
        "url": "https://maven.createmod.net/net/createmod/ponder/ponder-neoforge/1.0.81%2Bmc1.21.1/ponder-neoforge-1.0.81%2Bmc1.21.1.jar",
        "hash-format": "sha256",
        "hash": "b94099a82d51fa378f6ce30d788ca3f8cf0699fe16bbb536b516b03025301a42",
    },
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
REQUIRED_PHASE_3_CONFIGS = {
    Path("curios-common.toml"),
    Path("curios-server.toml"),
    Path("irons_spellbooks-server.toml"),
    Path("irons_spellbooks_spell_config/global_config.json"),
    Path("minecolonies-common.toml"),
    Path("minecolonies-server.toml"),
    Path("minecoloniesmages-common.toml"),
    Path("nightmareutils/autocast.json"),
    Path("nightmareutils/mob_trading.json"),
    Path("nightmareutils/skill_rewards.json"),
    Path("nightmareutils/spawn_profiles.json"),
    Path("structurize-server.toml"),
    Path("tensura/iron_spell_config.toml"),
    Path("tensura_minecolonies-common.toml"),
    Path("tensura_minecolonies-server.toml"),
}
REQUIRED_PHASE_4_CONFIGS = {
    Path("almostunified/duplicates.json"),
    Path("almostunified/startup.json"),
    Path("almostunified/tags.json"),
    Path("almostunified/unification/materials.json"),
    Path("gearevolution-common.toml"),
    Path("productivelib-server.toml"),
    Path("productivemetalworks-common.toml"),
    Path("silentgear-common.toml"),
    Path("sophisticatedbackpacks-common.toml"),
    Path("sophisticatedbackpacks-server.toml"),
    Path("sophisticatedcore-common.toml"),
    Path("sophisticatedstorage-common.toml"),
    Path("sophisticatedstorage-server.toml"),
    Path("tenmetalworks-common.toml"),
    Path("toms_storage-common.toml"),
    Path("toms_storage-server.toml"),
}
EXPECTED_CLIENT_OPTIONS = {
    "enableVsync": "false",
    "gamma": "1.0",
    "guiScale": "2",
    "maxFps": "150",
    "renderDistance": "8",
    "simulationDistance": "8",
    "bobView": "false",
    "resourcePacks": "[]",
    "incompatibleResourcePacks": "[]",
    "key_key.playerlist": "key.keyboard.tab",
    "key_tensura.keybinding.ability.slot_1": "key.keyboard.z",
    "key_tensura.keybinding.ability.slot_2": "key.keyboard.x",
    "key_tensura.keybinding.ability.slot_3": "key.keyboard.c",
    "key_tensura.keybinding.next_mode": "key.keyboard.grave.accent",
    "key_key.sophisticatedbackpacks.open_backpack": "key.keyboard.o",
    "key_key.walkers": "key.keyboard.h",
    "key_key.irons_spellbooks.spell_wheel": "key.keyboard.k",
    "key_key.irons_spellbooks.spellbook_cast": "key.keyboard.j",
    "key_key.greatsage.menu": "key.keyboard.g",
    "key_key.greatsage.assess": "key.keyboard.comma",
    "key_key.greatsage.scan": "key.keyboard.period",
    "key_key.toms_storage.open_terminal": "key.keyboard.apostrophe",
}
UNBOUND_CLIENT_OPTIONS = {
    "key_key.saveToolbarActivator",
    "key_key.loadToolbarActivator",
    "key_key.sophisticatedbackpacks.inventory_interaction",
    "key_key.sophisticatedbackpacks.toggle_upgrade_1",
    "key_key.sophisticatedbackpacks.toggle_upgrade_2",
    "key_key.sophisticatedcore.transfer_to_storage",
    "key_key.sophisticatedcore.transfer_to_inventory",
    "key_key.twilightforest.item_display_map_cycle",
    "key_key.twilightforest.zoom",
    "key_key.twilightforest.swap_hotbar",
    "key_supplementaries.keybind.quiver",
    "key_key.block_factorys_bosses.dodge_roll",
    "key_key.silentgear.cycle.back",
    "key_key.silentgear.cycle.next",
    "key_key.silentgear.openItem",
    "key_key.walkers_ability",
    "key_key.walkers_variants",
    "key_key.aether.invisibility_toggle.desc",
    "key_key.cataclysm.ability",
    "key_key.cataclysm.helmet_ability",
    "key_key.cataclysm.chestplate_ability",
    "key_key.cataclysm.boots_ability",
    "key_key.curios.open.desc",
    "key_accessories.key.open_accessories_screen",
    "key_nightmareutils.keybinding.ability.deep_slot_a",
    "key_nightmareutils.keybinding.ability.deep_slot_b",
    "key_nightmareutils.keybinding.ability.deep_slot_c",
    "key_key.tensura_minecolonies.open_roster",
    "key_framedblocks.key.update_cull",
    "key_key.kubejs.kubedex",
    "key_key.ftbchunks.map",
    "key_gui.xaero_open_settings",
    "key_gui.xaero_minimap_settings",
    "key_gui.xaero_new_waypoint",
    "key_gui.xaero_waypoints_key",
    "key_gui.xaero_enlarge_map",
    "key_gui.xaero_instant_waypoint",
    "key_key.legendary_monsters.fiery_boots_ability",
    "key_key.legendary_monsters.mossy_chestplate_ability",
    "key_key.legendary_monsters.roar_ability",
    "key_key.legendary_monsters.helmet_ability",
    "key_key.jei.cheatOneItem",
    "key_key.jei.cheatOneItem2",
    "key_key.jei.cheatItemStack",
    "key_key.jei.cheatItemStack2",
    "key_key.jei.toggleCheatModeConfigButton",
    "key_key.jei.toggleHideIngredient",
    "key_key.jei.toggleWildcardHideIngredient",
    "key_key.ftbquests.gui.extended_info",
    "key_key.ftbquests.gui_editor.undo",
    "key_key.ftbquests.gui_editor.redo",
    "key_key.ftbquests.gui_editor.select_all",
    "key_key.ftbquests.gui_editor.select_none",
    "key_key.ftbquests.gui_editor.delete",
    "key_key.ftbquests.gui_editor.force_delete",
    "key_key.ftbquests.gui_editor.toggle_crosshairs",
    "key_key.ftbquests.gui_editor.copy",
    "key_key.ftbquests.gui_editor.paste",
    "key_key.ftbquests.gui_editor.reward_tables",
    "key_key.ftbquests.gui_editor.reload_theme",
    "key_key.ftbquests.gui_quest_panel.edit_title",
    "key_key.ftbquests.gui_quest_panel.edit_subtitle",
    "key_key.ftbquests.gui_quest_panel.edit_desc",
    "key_key.ftbquests.gui_quest_panel.add_page_break",
    "key_key.ftbquests.gui_quest_panel.add_line",
    "key_key.ftbquests.gui_quest_panel.add_image",
    "key_key.ftbquests.gui_quest_panel.edit_quest_props",
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

for relative, expected in DIRECT_DEPENDENCIES.items():
    metadata_path = PACK / relative
    try:
        metadata = tomllib.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"Invalid direct dependency metadata {relative}: {exc}")
        continue
    actual = {
        "name": metadata.get("name"),
        "filename": metadata.get("filename"),
        "side": metadata.get("side"),
        "url": metadata.get("download", {}).get("url"),
        "hash-format": metadata.get("download", {}).get("hash-format"),
        "hash": metadata.get("download", {}).get("hash"),
    }
    if actual != expected:
        errors.append(f"Direct dependency lock changed: {relative}")

config_files = [path for path in CONFIG.rglob("*") if path.is_file()]
if len(config_files) < 159:
    errors.append(f"Expected at least 159 promoted config files; found {len(config_files)}")

for relative in sorted(REQUIRED_PHASE_2_CONFIGS):
    if not (CONFIG / relative).is_file():
        errors.append(f"Missing reviewed Phase 2 config: {relative}")

for relative in sorted(REQUIRED_PHASE_3_CONFIGS):
    if not (CONFIG / relative).is_file():
        errors.append(f"Missing reviewed Phase 3 config: {relative}")

for relative in sorted(REQUIRED_PHASE_4_CONFIGS):
    if not (CONFIG / relative).is_file():
        errors.append(f"Missing reviewed Phase 4 config: {relative}")

for path in config_files:
    try:
        if path.suffix == ".toml":
            tomllib.loads(path.read_text(encoding="utf-8"))
        elif path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid config {path.relative_to(CONFIG)}: {exc}")

client_options_path = PACK / "options.txt"
try:
    client_options = dict(
        line.split(":", 1)
        for line in client_options_path.read_text(encoding="utf-8").splitlines()
        if ":" in line
    )
    for key, expected in EXPECTED_CLIENT_OPTIONS.items():
        if client_options.get(key) != expected:
            errors.append(f"Client option {key} must remain {expected!r}")
    for key in sorted(UNBOUND_CLIENT_OPTIONS):
        if client_options.get(key) != "key.keyboard.unknown":
            errors.append(f"Conflicting client keybind must remain unbound: {key}")
except OSError as exc:
    errors.append(f"Missing client options baseline: {exc}")

xaero_profile_path = CONFIG / "xaero" / "minimap" / "profiles" / "default.cfg"
try:
    xaero_profile = xaero_profile_path.read_text(encoding="utf-8")
    if not re.search(r"^minimap_shape\s*=\s*1\s*$", xaero_profile, re.MULTILINE):
        errors.append("Xaero's Minimap default profile must use the circular shape (minimap_shape = 1)")
except OSError as exc:
    errors.append(f"Missing Xaero's Minimap default profile: {exc}")

xaero_hud_path = CONFIG / "xaerohud.txt"
try:
    xaero_hud = xaero_hud_path.read_text(encoding="utf-8")
    if not re.search(r"module;id=xaerominimap:minimap;[^\n]*fromRight=true;", xaero_hud):
        errors.append("Xaero's Minimap HUD layout must be anchored from the right")
except OSError as exc:
    errors.append(f"Missing Xaero HUD layout baseline: {exc}")

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

random_skill_config = CONFIG / "tensura_skill_books" / "tensura_skill_books-random-skills.txt"
for line_number, line in enumerate(random_skill_config.read_text(encoding="utf-8").splitlines(), 1):
    stripped = line.strip()
    if stripped.startswith("nightmareutils:") and not stripped.endswith("@0"):
        errors.append(
            "Nightmare Utils test skills must remain excluded from Skill Books rewards: "
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

try:
    minecolonies = tomllib.loads(
        (CONFIG / "minecolonies-server.toml").read_text(encoding="utf-8")
    )
    gameplay = minecolonies.get("gameplay", {})
    combat = minecolonies.get("combat", {})
    pathfinding = minecolonies.get("pathfinding", {})
    expected_minecolonies = {
        "maxcitizenpercolony": 150,
        "forceloadcolony": False,
        "loadtime": 5,
        "colonyloadstrictness": 6,
        "maxtreesize": 300,
    }
    for key, expected in expected_minecolonies.items():
        if gameplay.get(key) != expected:
            errors.append(f"MineColonies {key} must remain {expected!r}")
    if combat.get("maxBarbarianSize") != 60:
        errors.append("MineColonies maximum raid size must remain 60")
    if pathfinding.get("pathfindingmaxthreadcount") != 1:
        errors.append("MineColonies pathfinding thread count must remain 1")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid MineColonies server config: {exc}")

try:
    structurize = tomllib.loads(
        (CONFIG / "structurize-server.toml").read_text(encoding="utf-8")
    ).get("gameplay", {})
    expected_structurize = {
        "maxOperationsPerTick": 500,
        "maxCachedChanges": 25,
        "maxCachedSchematics": 64,
        "maxBlocksChecked": 500,
    }
    for key, expected in expected_structurize.items():
        if structurize.get(key) != expected:
            errors.append(f"Structurize {key} must remain {expected}")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Structurize server config: {exc}")

try:
    tensura_colonies_common = tomllib.loads(
        (CONFIG / "tensura_minecolonies-common.toml").read_text(encoding="utf-8")
    )
    expected_common = {
        "enableAssassins": False,
        "citizenAggression": "OFF",
        "rivalNaturalGeneration": False,
    }
    for key, expected in expected_common.items():
        if tensura_colonies_common.get(key) != expected:
            errors.append(f"Tensura x MineColonies {key} must remain {expected!r}")

    tensura_colonies_server = tomllib.loads(
        (CONFIG / "tensura_minecolonies-server.toml").read_text(encoding="utf-8")
    )
    expected_server = {
        "enableFactionSystem": False,
        "enableDefenseSwap": False,
        "enableRaids": False,
        "protectColoniesFromMobGriefing": True,
        "protectColoniesFromSkillGriefing": True,
    }
    for key, expected in expected_server.items():
        if tensura_colonies_server.get(key) != expected:
            errors.append(f"Tensura x MineColonies {key} must remain {expected!r}")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Tensura x MineColonies config: {exc}")

for relative in (
    Path("nightmareutils/autocast.json"),
    Path("nightmareutils/mob_trading.json"),
    Path("nightmareutils/skill_rewards.json"),
    Path("nightmareutils/spawn_profiles.json"),
):
    try:
        nightmare_config = json.loads((CONFIG / relative).read_text(encoding="utf-8"))
        if nightmare_config.get("enabled") is not False:
            errors.append(f"Nightmare library feature must remain disabled: {relative}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid Nightmare Utils config {relative}: {exc}")

try:
    iron_spells = tomllib.loads(
        (CONFIG / "irons_spellbooks-server.toml").read_text(encoding="utf-8")
    )
    if iron_spells.get("Misc", {}).get("spellGriefing") is not False:
        errors.append("Iron's Spells terrain griefing must remain disabled")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Iron's Spells server config: {exc}")

try:
    toms_storage = tomllib.loads(
        (CONFIG / "toms_storage-server.toml").read_text(encoding="utf-8")
    )
    expected_toms_storage = {
        "inventoryConnectorRange": 12,
        "invCableConnectorMaxScanSize": 256,
        "wirelessReach": 12,
        "advWirelessRange": 64,
        "wirelessTermBeaconLvl": -1,
        "wirelessTermBeaconLvlDim": -1,
        "invLinkBeaconLvl": -1,
        "invLinkBeaconRange": 128,
        "invLinkBeaconLvlSameDim": -1,
        "invLinkBeaconLvlCrossDim": -1,
        "runMultithreaded": False,
    }
    for key, expected in expected_toms_storage.items():
        if toms_storage.get(key) != expected:
            errors.append(f"Tom's Storage {key} must remain {expected!r}")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Tom's Storage server config: {exc}")

try:
    productive_metalworks = tomllib.loads(
        (CONFIG / "productivemetalworks-common.toml").read_text(encoding="utf-8")
    )
    expected_foundry_limits = {
        "foundryMaxVolume": 256,
        "foundryMaxCircumference": 96,
        "foundryMaxHeight": 12,
        "foundryRenderInventory": False,
    }
    for key, expected in expected_foundry_limits.items():
        if productive_metalworks.get(key) != expected:
            errors.append(f"Productive Metalworks {key} must remain {expected!r}")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Productive Metalworks config: {exc}")

try:
    silent_gear = tomllib.loads(
        (CONFIG / "silentgear-common.toml").read_text(encoding="utf-8")
    )
    if silent_gear.get("item", {}).get("blueprint", {}).get("spawn_with_starter_blueprints") is not False:
        errors.append("Silent Gear starter blueprints must remain disabled")
    if silent_gear.get("item", {}).get("material_book", {}).get("spawn_with_material_book") is not False:
        errors.append("Silent Gear starter material book must remain disabled")
except (OSError, tomllib.TOMLDecodeError) as exc:
    errors.append(f"Invalid Silent Gear config: {exc}")

toms_script_path = PACK / "kubejs" / "server_scripts" / "toms_terminal_only.js"
try:
    toms_script = toms_script_path.read_text(encoding="utf-8")
    disabled_toms_recipes = set(re.findall(r"'toms_storage:([^']+)'", toms_script))
    expected_disabled_toms_recipes = {
        "basic_inventory_hopper",
        "filing_cabinet",
        "inventory_cable_connector_framed",
        "inventory_cable_connector_framed_clean",
        "inventory_cable_framed",
        "inventory_cable_framed_clean",
        "inventory_configurator",
        "inventory_interface",
        "inventory_proxy",
        "inventory_proxy_clean",
        "item_filter",
        "level_emitter",
        "open_crate",
        "paint_kit",
        "poly_item_filter",
        "tag_item_filter",
        "trim",
        "trim_clean",
    }
    if disabled_toms_recipes != expected_disabled_toms_recipes:
        errors.append("Tom's terminal-only recipe policy changed")
except OSError as exc:
    errors.append(f"Invalid Tom's terminal-only script: {exc}")

unit_map_path = PACK / "kubejs" / "data" / "productivemetalworks" / "data_maps" / "fluid" / "unit_map.json"
try:
    unit_map = json.loads(unit_map_path.read_text(encoding="utf-8"))
    unit_values = unit_map.get("values", {})
    if unit_map.get("replace") is not True:
        errors.append("Metalworks fluid unit map must replace lower-priority contributions")
    if len(unit_values) != 76:
        errors.append(f"Metalworks fluid unit map must contain 76 source entries; found {len(unit_values)}")
    required_sgear_fluids = {
        "sgearmetalworks:molten_azure_electrum",
        "sgearmetalworks:molten_azure_silver",
        "sgearmetalworks:molten_blaze_gold",
        "sgearmetalworks:molten_crimson_iron",
        "sgearmetalworks:molten_crimson_steel",
        "sgearmetalworks:molten_tyrian_steel",
        "sgearmetalworks:molten_uru_metal",
    }
    missing_sgear_fluids = sorted(required_sgear_fluids - set(unit_values))
    if missing_sgear_fluids:
        errors.append("Missing installed Silent Gear fluid mappings: " + ", ".join(missing_sgear_fluids))
    silent_gems_conditions = [
        value.get("neoforge:conditions")
        for key, value in unit_values.items()
        if key.startswith("sgearmetalworks:") and key not in required_sgear_fluids
    ]
    if len(silent_gems_conditions) != 21 or any(
        conditions != [{"type": "neoforge:mod_loaded", "modid": "silentgems"}]
        for conditions in silent_gems_conditions
    ):
        errors.append("All 21 optional Silent Gems fluid mappings must remain conditionally gated")
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"Invalid Metalworks fluid unit map: {exc}")

if errors:
    raise SystemExit("Pack validation failed:\n- " + "\n- ".join(errors))

print(
    f"Pack OK: Minecraft {versions['minecraft']}, NeoForge {versions['neoforge']}, "
    f"{len(index.get('files', []))} indexed files"
)
