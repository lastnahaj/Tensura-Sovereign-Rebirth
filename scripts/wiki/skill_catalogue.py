"""Resolve skill articles against the pinned pack's exported registry inventory."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POOL = ROOT / "pack/config/tensura_skill_books/tensura_skill_books-random-skills.txt"
TYPES = {name.upper(): "skills/" + name for name in ("common", "extra", "intrinsic", "unique", "ultimate")}
TYPES.update({"COMBAT": "battlewill", "MAGIC_ASPECTUAL": "magic", "MAGIC_SPIRITUAL": "magic", "MAGIC_SUMMONING": "magic", "RESISTANCE": "resistances"})
GUIDES = {"Abilities", "Abilities/Skills", "Bypass/Degrade Skills", "Mastery Boost Skills", "Ultimate Skill Aquisition", "Spellbinding Table", "Items/Misc/Battlewill Manual"}
ALIASES = {
    "ascension:shadowdummy": "ascension:image_training",
    "tensura:doublecherryblossomseightpetalsflash": "tensura:eight_petals_flash",
    "tensura:cherryblossomseightpetalsflash": "tensura:eight_petals_flash",
    "tensura:plumblossomsfivepetalsthrust": "tensura:five_petals_thrust",
}
# Spell aliases are scoped to magic infoboxes, never similarly named skills.
MAGIC_ALIASES = {
    "tensura:possession": "tensura:possession_magic",
    "tensura:strength": "tensura:strength_aspectual",
    "tensura:dimensionalcutter": "tensura:dimension_cutter",
    "tensura:firespiritual": "tensura:fire",
    "tensura:waterspiritual": "tensura:water",
}
# Registration alone is not a completed gameplay feature.
HELD = {
    "mysticism:embryo": "The pinned implementation is an unfinished skill; no completed effect is documented.",
    "tensura:holy_attack_nullification": "The upstream article describes Holy Attack Nullification as obtainable only through commands. No normal player acquisition route has been verified; this entry is reference-only.",
    "tensura:magic_nullification": "The upstream article describes Magic Nullification as unobtainable without cheats. No normal player acquisition route has been verified; this entry is reference-only.",
}
ACTIVE = {"registered", "reference"}


def nightmares_manifest():
    path = ROOT / "data/nightmares_skill_reference.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"pages": [], "registry": {}}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold().replace("&", "and"))


def inventory() -> dict[str, dict]:
    result = {}
    category = ""
    for line in POOL.read_text(encoding="utf-8").splitlines():
        if line.startswith("# Category:"):
            category = line.split(":", 1)[1].split("|", 1)[0].strip()
        elif re.fullmatch(r"[a-z0-9_]+:[a-z0-9_]+@\d+", line):
            identifier, weight = line.split("@")
            result[identifier] = {"id": identifier, "category": TYPES.get(category, "skills/other"), "registry_type": category, "weight": int(weight)}
    return result


def identify(namespace: str, title: str, pool: dict) -> str | None:
    name = normalize(title.split("/")[-1].split(",")[0])
    alias = ALIASES.get(namespace + ":" + name)
    if alias:
        return alias
    matches = [key for key in pool if key.startswith(namespace + ":") and normalize(key.split(":")[1]) in {name, name.removeprefix("the")}]
    return matches[0] if len(matches) == 1 else None


def catalogue() -> dict:
    pool = inventory()
    pages = {}
    for namespace in ("tensura", "mysticism"):
        manifest = json.loads((ROOT / f"data/upstream_{namespace}_pages.json").read_text(encoding="utf-8"))
        for record in manifest["pages"]:
            identifier = identify(namespace, record["display_title"], pool) or identify(namespace, record["source_title"], pool)
            is_skill = record["category"].startswith("skills/") or record["category"] in {"resistances", "battlewill"}
            if not is_skill:
                if record["category"] != "magic" and not any(tag.endswith('_Magic') for tag in record.get('upstream_categories', [])):
                    continue
                body = (ROOT / "docs" / record["local_page"]).read_text(encoding="utf-8")
                if "druid-container-magic" in body:
                    spells = {key: value for key, value in pool.items() if value["category"] == "magic"}
                    alias_key = namespace + ":" + normalize(record["display_title"])
                    identifier = MAGIC_ALIASES.get(alias_key) or identify(namespace, record["display_title"], spells) or identify(namespace, record["source_title"], spells)
                    if identifier and identifier not in spells:
                        raise ValueError(f"Spell alias does not match the magic inventory: {identifier}")
                elif "druid-container-skill" in body and identifier and pool[identifier]["category"] != "magic":
                    # Resistances and skills can be misfiled under Magic upstream.
                    pass
                else:
                    # Keep items and collection guides in their own references.
                    continue
            status = "registered" if identifier else "historical"
            if record["source_title"] in GUIDES:
                status = "guide"
            if identifier in HELD or (identifier and pool[identifier]["weight"] == 0):
                status = "unavailable"
            pages[record["local_page"]] = {
                "id": identifier, "status": status,
                "category": pool[identifier]["category"] if identifier else record["category"],
                "title": record["display_title"], "source": record["source_url"],
                "revision": record["revision_id"], "namespace": namespace,
                **({"availability_reason": HELD[identifier]} if identifier in HELD else {}),
                **({"availability_reason": "Battlewill Manual is a consumable learning item, not an ability. Its item reference is retained here; it is excluded from ability cards and mastery paths."} if record["source_title"] == "Items/Misc/Battlewill Manual" else {}),
            }
    maintained = json.loads((ROOT / "data/ascension_reference.json").read_text(encoding="utf-8"))
    for entry in maintained["entries"]:
        if entry["category"] == "races":
            continue
        identifier = identify("ascension", entry["display_title"], pool)
        if not identifier:
            raise ValueError(f"Unmapped maintained ability: {entry['display_title']}")
        pages[entry["local_page"]] = {
            "id": identifier, "status": "registered", "category": pool[identifier]["category"],
            "title": entry["display_title"], "namespace": "ascension",
            "source": "https://www.curseforge.com/minecraft/mc-mods/tensura-ascensions",
            "maintained": True,
        }
    for entry in json.loads((ROOT / "data/skill_reference.json").read_text(encoding="utf-8"))["entries"]:
        identifier = entry["registry_id"]
        if identifier not in pool or entry["category"] != pool[identifier]["category"]:
            raise ValueError(f"Unmapped maintained skill: {identifier}")
        pages[entry["local_page"]] = {
            "id": identifier, "status": "registered", "category": pool[identifier]["category"],
            "title": entry["display_title"], "namespace": identifier.split(":")[0],
            "source": entry["source_url"], "maintained": True,
        }
    nightmares = nightmares_manifest()
    for entry in nightmares["pages"]:
        identifier = entry["registry_id"]
        if nightmares["registry"][identifier]["registry_category"] != entry["category"]:
            raise ValueError(f"Nightmares reference type mismatch: {identifier}")
        pages[entry["local_page"]] = {
            "id": identifier, "status": "unavailable" if entry.get("normal_acquisition_unverified") else "reference", "category": entry["category"],
            "title": entry["display_title"], "namespace": "trnightmare",
            "source": entry["source_url"], "revision": entry["revision_id"],
            "reference_build": nightmares["reference_build"],
            "source_partial": entry.get("source_partial", False),
            **({"availability_reason": entry["availability_reason"]} if entry.get("normal_acquisition_unverified") else {}),
        }
    artwork = json.loads((ROOT / 'data/skill_artwork.json').read_text(encoding='utf-8'))['entries']
    for decision in pages.values():
        if decision['category'] == 'magic' and decision['id'] in pool:
            decision['magic_school'] = {'MAGIC_ASPECTUAL': 'Aspectual', 'MAGIC_SPIRITUAL': 'Spiritual', 'MAGIC_SUMMONING': 'Summoning'}.get(pool[decision['id']]['registry_type'])
        if decision['id'] in artwork:
            decision['asset'] = artwork[decision['id']]['asset']
            decision['artwork_kind'] = artwork[decision['id']]['kind']
    return {"pages": pages, "inventory": pool}


def active_record(record: dict, policy: dict) -> dict | None:
    decision = policy["pages"].get(record["local_page"])
    if not decision:
        return record
    if decision["status"] not in ACTIVE:
        return None
    return {**record, "category": decision["category"], "registry_id": decision["id"]}
