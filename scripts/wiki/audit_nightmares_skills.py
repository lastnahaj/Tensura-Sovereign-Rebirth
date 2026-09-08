"""Review the Nightmares 1.21.1 wiki against a reproducible reference artifact.

Outputs stay in the ignored audit cache. The reference artifact is not evidence
of the server's installed release, and this command never installs the mod.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import zipfile

from bs4 import BeautifulSoup
import sync_tensura_wiki as wiki

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = {
    "filename": "trnightmare-1.0.3.2.8-neoforge-1.21.1.jar",
    "version": "1.0.3.2.8-neoforge-1.21.1",
    "minecraft": "1.21.1",
    "sha256": "94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127",
    "source_url": "https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382",
    "installed_version_verified": False,
}
ROOT_CATEGORIES = {
    **{f"Abilities/1.21.1/Skills/{name.title()} Skills": "skills/" + name for name in ("common", "extra", "intrinsic", "unique")},
    "Abilities/1.21.1/Skills/Resistances": "resistances",
    "Ultimates": "skills/ultimate",
    "King Ultimates": "skills/ultimate",
    "God Ultimates": "skills/ultimate",
    "Dragon Ultimates": "skills/ultimate",
}


def normalized(text):
    text = re.sub(r"§[0-9a-fk-or]", "", text, flags=re.I)
    return re.sub(r"[^a-z0-9]", "", text.casefold().replace("&", "and"))


def inspect_registry(jar, javap):
    if hashlib.sha256(jar.read_bytes()).hexdigest() != REFERENCE["sha256"]:
        raise ValueError("The supplied artifact does not match the recorded reference release")
    with zipfile.ZipFile(jar) as archive:
        language = json.loads(archive.read("assets/trnightmare/lang/en_us.json"))
        metadata = archive.read("META-INF/neoforge.mods.toml").decode()
        if f'version="{REFERENCE["version"]}"' not in metadata:
            raise ValueError("Reference artifact version metadata differs")
    result = {}
    for kind in ("Common", "Extra", "Intrinsic", "Unique", "Ultimate"):
        class_name = "com.github.hvnbael.trnightmare.registry.main." + kind + "Skills"
        output = subprocess.run([javap, "-classpath", str(jar), "-c", "-p", class_name], check=True, capture_output=True, text=True).stdout
        classes = dict((field, implementation) for implementation, field in re.findall(r"DeferredHolder<[^,]+, ([\w.$]+)> (\w+);", output))
        registrations = re.findall(r"// String ([a-z0-9_./-]+)\s*\n(?:(?!// String).)*?// Field (\w+):Lnet/neoforged/neoforge/registries/DeferredHolder;", output, re.S)
        if {field for _, field in registrations} != set(classes):
            raise ValueError(f"Incomplete registry extraction for {kind}: {set(classes) - {field for _, field in registrations}}")
        for identifier, field in registrations:
            if field not in classes:
                raise ValueError(f"No implementation class for {field}")
            key = "trnightmare:" + identifier
            title = language.get("trnightmare.skill." + identifier) or language.get("trnightmare.skill." + kind.lower() + "." + identifier) or identifier.replace("_", " ").title()
            title = re.sub(r"§[0-9a-fk-or]", "", title, flags=re.I).strip("｢｣「」 ")
            category = "skills/" + kind.lower()
            if identifier in {"void_resistance", "nuclear_resistance"}:
                declaration = subprocess.run([javap, "-classpath", str(jar), "-p", classes[field]], check=True, capture_output=True, text=True).stdout
                if "extends io.github.manasmods.tensura.ability.skill.resist.ResistSkill" not in declaration:
                    raise ValueError(f"Resistance type changed: {identifier}")
                category = "resistances"
            result[key] = {"id": key, "title": title, "registry_category": category, "implementation": classes[field]}
    return result


def review(jar, javap, cache, refresh=False):
    registry = inspect_registry(jar, javap)
    wiki.API_URL = "https://tensuranightmares.wiki.gg/api.php"
    client = wiki.ApiClient(cache, refresh=refresh, pace=.2)
    siteinfo = wiki.fetch_siteinfo(client)
    if siteinfo["rightsinfo"]["url"].rstrip("/") != "https://creativecommons.org/licenses/by-sa/4.0":
        raise ValueError("Nightmares text licensing changed; manual review required")
    candidates = {}
    for category, kind in ROOT_CATEGORIES.items():
        continuation = {}
        while True:
            data = client.get_json({"action": "query", "format": "json", "formatversion": 2, "list": "categorymembers", "cmtitle": "Category:" + category, "cmlimit": "max", **continuation}, "categories/" + normalized(category) + ("-" + normalized(str(continuation)) if continuation else "") + ".json")
            for entry in data["query"]["categorymembers"]:
                if entry["ns"] == 0:
                    candidate = candidates.setdefault(entry["pageid"], {**entry, "collection_categories": [], "category": kind})
                    candidate["collection_categories"].append(category)
            continuation = data.get("continue", {})
            if not continuation:
                break
    listing = sorted(candidates.values(), key=lambda entry: entry["pageid"])
    revisions = wiki.fetch_revision_metadata(client, listing)
    pages = []
    for index, entry in enumerate(listing):
        revision = revisions[entry["pageid"]]
        result = client.get_json({"action": "parse", "format": "json", "formatversion": 2, "pageid": entry["pageid"], "prop": "text|displaytitle|categories|revid"}, f'parse/{entry["pageid"]}-{revision["revision_id"]}.json')["parse"]
        if result["revid"] != revision["revision_id"]:
            raise ValueError(f"Source revision changed during review: {entry['title']}")
        soup = BeautifulSoup(result["text"], "html.parser")
        infobox = soup.select_one(".druid-infobox")
        title = infobox.select_one(".druid-title").get_text(" ", strip=True) if infobox and infobox.select_one(".druid-title") else BeautifulSoup(result["displaytitle"], "html.parser").get_text(" ", strip=True)
        rows = []
        if infobox:
            for row in infobox.select(".druid-row"):
                label, value = row.select_one(".druid-label"), row.select_one(".druid-data")
                if label and value:
                    rows.append({"label": label.get_text(" ", strip=True), "section": row.get("data-druid-section-row", ""), "text": value.get_text(" ", strip=True)})
        exact = [key for key, value in registry.items() if normalized(value["title"]) == normalized(title)]
        if not exact:
            exact = [key for key in registry if normalized(key.split(":")[1]) == normalized(entry["title"]) or normalized(key.split(":")[1]) == normalized(title)]
        matches = exact
        if not matches:
            matches = [key for key, value in registry.items() if normalized(value["title"].split(",")[0]) == normalized(entry["title"])]
        identifier = matches[0] if len(matches) == 1 else None
        obtainment = [row for row in rows if row["section"].casefold() == "obtaining" and row["text"] not in {"", "None", "N/A", "[[]]"}]
        pages.append({"page_id": entry["pageid"], "source_title": entry["title"], "display_title": title, "source_url": "https://tensuranightmares.wiki.gg/wiki/" + wiki.quote(entry["title"].replace(" ", "_"), safe="/:(),"), "revision_id": result["revid"], "modified": revision["modified"], "category": entry["category"], "collection_categories": entry["collection_categories"], "registry_id": identifier, "candidate_ids": matches, "rows": rows, "obtainment_documented": bool(obtainment), "has_infobox": bool(infobox)})
        if (index + 1) % 20 == 0:
            print(f"Reviewed {index + 1}/{len(listing)} Nightmares skill sources", flush=True)
    matched = {page["registry_id"] for page in pages if page["registry_id"]}
    report = {"schema": 1, "reference_build": REFERENCE, "text_license": siteinfo["rightsinfo"], "registry": registry, "pages": pages, "registry_without_article": sorted(registry.keys() - matched), "summary": {"source_pages": len(pages), "reference_registry_entries": len(registry), "matched_pages": sum(bool(page["registry_id"]) for page in pages), "unresolved_pages": sum(not page["registry_id"] for page in pages), "obtainment_documented": sum(page["obtainment_documented"] for page in pages)}}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--javap", default=shutil.which("javap"))
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if not args.javap:
        raise SystemExit("Java 21 javap is required")
    cache = ROOT / ".build/nightmares-skill-audit"
    report = review(args.jar, args.javap, cache, args.refresh)
    cache.mkdir(parents=True, exist_ok=True)
    (cache / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report["summary"], indent=2))
    print("Installed build match remains unverified; no game files or wiki pages changed.")


if __name__ == "__main__":
    main()
