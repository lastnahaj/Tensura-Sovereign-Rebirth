"""Resolve skill articles against the pinned pack's exported registry inventory."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POOL = ROOT / "pack/config/tensura_skill_books/tensura_skill_books-random-skills.txt"
TYPES = {name.upper(): "skills/" + name for name in ("common", "extra", "intrinsic", "unique", "ultimate")}
TYPES.update({"COMBAT": "battlewill", "MAGIC_ASPECTUAL": "magic", "MAGIC_SPIRITUAL": "magic", "MAGIC_SUMMONING": "magic", "RESISTANCE": "resistances"})
GUIDES = {"Abilities", "Abilities/Skills", "Bypass/Degrade Skills", "Mastery Boost Skills", "Ultimate Skill Aquisition"}
ALIASES = {"ascension:shadowdummy": "ascension:image_training"}
# Registration alone is not a completed gameplay feature.
HELD = {"mysticism:embryo": "The pinned implementation is an unfinished skill; no completed effect is documented."}
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
            result[identifier] = {"id": identifier, "category": TYPES.get(category, "skills/other"), "weight": int(weight)}
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
            is_skill = record["category"].startswith("skills/")
            if not is_skill:
                if not (identifier and record["category"] == "magic" and pool[identifier]["category"].startswith("skills/")):
                    continue
                # A spell or status effect can share a skill's display name.
                body = (ROOT / "docs" / record["local_page"]).read_text(encoding="utf-8")
                if "druid-container-skill" not in body:
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
            "id": identifier, "status": "reference", "category": entry["category"],
            "title": entry["display_title"], "namespace": "trnightmare",
            "source": entry["source_url"], "revision": entry["revision_id"],
            "reference_build": nightmares["reference_build"],
            "source_partial": entry.get("source_partial", False),
        }
    return {"pages": pages, "inventory": pool}


def active_record(record: dict, policy: dict) -> dict | None:
    decision = policy["pages"].get(record["local_page"])
    if not decision:
        return record
    if decision["status"] not in ACTIVE:
        return None
    return {**record, "category": decision["category"], "registry_id": decision["id"]}
