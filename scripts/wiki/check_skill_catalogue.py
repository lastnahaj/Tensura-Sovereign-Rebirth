"""Check skill eligibility, acquisition panels, regeneration, and rendered search."""
from __future__ import annotations

import argparse
import json
import posixpath
import re
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from skill_catalogue import ACTIVE, ROOT, catalogue, inventory, nightmares_manifest
from sync_skill_catalogue import DOCS, LABELS, generate, render_acquisition_markdown, route


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-only", action="store_true")
    args = parser.parse_args()
    outputs = generate()
    errors = []
    for name, content in outputs.items():
        if not (DOCS / name).exists() or (DOCS / name).read_text(encoding="utf-8") != content:
            errors.append(f"Stale skill output: {name}")
    policy = catalogue()
    pool = inventory()
    nightmares = nightmares_manifest()
    active = {p: d for p, d in policy["pages"].items() if d["status"] in ACTIVE}
    active_routes = {route(p): d for p, d in active.items()}
    for page in ("tensura-reference/magic/aspectual-possession.md", "tensura-reference/magic/aspectual-strength.md", "mysticism-reference/core-mechanics/effects-lightning-mode.md"):
        if page in policy["pages"]:
            errors.append(f"Non-skill name collision: {page}")
    if active["tensura-reference/skills/intrinsic/angel-wings.md"]["category"] != "skills/extra":
        errors.append("Angel Wings must use its Extra classification")
    if active["tensura-reference/skills/extra/purple-lightning.md"]["category"] != "magic":
        errors.append("Purple Lightning must use its Magic classification")
    ultimate = BeautifulSoup(outputs["tensura-reference/skills/ultimate/index.md"], "html.parser")
    if "Ultimate Skill Aquisition" in ultimate.get_text() or "Angel evolution" in ultimate.get_text():
        errors.append("Guide or race card in Ultimate Skills")
    seen = set()
    for category in LABELS:
        page = "tensura-reference/" + category + "/index.md"
        soup = BeautifulSoup(outputs[page], "html.parser")
        for link in soup.select(".reference-card > a[href]"):
            target = posixpath.normpath(posixpath.join(route(page), urlsplit(link["href"]).path)).rstrip("/") + "/"
            decision = active_routes.get(target)
            if not decision:
                if category.startswith("skills/"):
                    errors.append(f"Unregistered skill card: {target}")
                continue
            if decision["category"] != category:
                errors.append(f"Incorrect class: {target}")
            if decision["id"] in seen:
                errors.append(f"Duplicate skill card: {decision['id']}")
            seen.add(decision["id"])
    for page, decision in active.items():
        expected = pool if decision["status"] == "registered" else nightmares["registry"]
        if decision["id"] not in expected or decision["id"] not in seen:
            errors.append(f"Registered skill missing from directories: {page}")
        soup = BeautifulSoup(outputs[page], "html.parser")
        if len(soup.select(".skill-obtainment #how-to-obtain")) != 1:
            errors.append(f"Missing or duplicate obtainment panel: {page}")
        if not decision.get("maintained"):
            if outputs[page].find('<section class="reference-overview ') > outputs[page].find('<section class="skill-obtainment"'):
                errors.append(f"Obtainment panel obscures visual overview: {page}")
            if not soup.select_one('.reference-quick-jumps a[href="#how-to-obtain"]'):
                errors.append(f"Missing obtainment jump: {page}")
        if decision["namespace"] in {"mysticism", "trnightmare"}:
            previews = soup.select(".reference-overview img, .skill-detail-hero img")
            if not previews or any("assets/icons/skills/" not in image["src"] for image in previews):
                errors.append(f"Missing skill emblem: {page}")
            if any("wip" in image.get("src", "").casefold() for image in soup.select("img")):
                errors.append(f"Editorial placeholder remains: {page}")
        if decision["status"] == "reference":
            if "Server build match pending." not in soup.get_text() or "Pinned pack inventory" in soup.get_text():
                errors.append(f"Reference build presented as installed: {page}")
            if "<strong>:</strong>" in outputs[page]:
                errors.append(f"Empty acquisition label: {page}")
            if decision["source"] not in outputs[page] or "## Source and licensing" not in outputs[page]:
                errors.append(f"Missing Nightmares attribution: {page}")
            if not soup.select_one('.skill-category-nav a[href]'):
                errors.append(f"Missing unified skill navigation: {page}")
    if "trnightmare:sandalphon_punishment" in seen:
        errors.append("Non-gameplay Sandalphon variant in normal directories")
    for record in nightmares["pages"]:
        soup = BeautifulSoup(outputs[record["local_page"]], "html.parser")
        panel_text = re.sub(r"\s+", "", soup.select_one(".skill-obtainment").get_text(" ", strip=True))
        for row in record["obtainment_rows"]:
            if re.sub(r"\s+", "", row["text"]) not in panel_text:
                errors.append(f"Source obtainment condition dropped: {record['registry_id']} / {row['label']}")
    sample = render_acquisition_markdown("[Skill](../unique/great-mage.md#great-mage)", "tensura-reference/skills/ultimate/the-timeless-mage.md")
    if 'href="../../unique/great-mage/#great-mage"' not in sample:
        errors.append("Markdown acquisition route conversion failed")
    if not args.source_only:
        site = ROOT / "site"
        search = json.loads((site / "search/search_index.json").read_text(encoding="utf-8"))
        indexed = {entry["location"].split("#")[0] for entry in search["docs"]}
        parsed = {}
        graph = json.loads((site / "assets/data/progression.json").read_text(encoding="utf-8"))
        by_id = {d["id"]: route(page) for page, d in active.items()}
        connections = {(edge["from"], edge["to"]) for edge in graph["edges"]}
        for start, end in (("trnightmare:raphael_knowledge", "trnightmare:raphael_wisdom"), ("trnightmare:babylon", "trnightmare:gilgamesh_lord_of_treasures"), ("trnightmare:gilgamesh_lord_of_treasures", "trnightmare:gilgamesh_king_of_uruk")):
            if start not in by_id or end not in by_id or (by_id[start], by_id[end]) not in connections:
                errors.append(f"Missing variant progression: {start} -> {end}")
        for page, decision in active.items():
            if decision["status"] == "reference" and graph["nodes"].get(route(page), {}).get("verification") != "reference-build-only":
                errors.append(f"Progression loses reference-build status: {page}")
        for page, decision in policy["pages"].items():
            key = route(page)
            if decision["status"] not in ACTIVE:
                if key in indexed:
                    errors.append(f"Historical skill or guide appears in search: {key}")
                continue
            document = site / key / "index.html"
            soup = BeautifulSoup(document.read_text(encoding="utf-8"), "html.parser")
            parsed[key] = soup
            if len(soup.select("#how-to-obtain")) != 1:
                errors.append(f"Rendered obtainment heading mismatch: {key}")
            for anchor in soup.select(".skill-obtainment a[href], .skill-category-nav a[href], .reference-related a[href], .reference-quick-jumps a[href]"):
                url = urlsplit(anchor["href"])
                if url.scheme or url.netloc:
                    continue
                destination = (document.parent / unquote(url.path)).resolve()
                if destination.is_dir():
                    destination /= "index.html"
                if not destination.is_relative_to(site.resolve()) or not destination.is_file():
                    errors.append(f"Missing skill reading link: {key} -> {anchor['href']}")
                elif url.fragment:
                    target_soup = BeautifulSoup(destination.read_text(encoding="utf-8"), "html.parser")
                    if not target_soup.find(id=unquote(url.fragment)):
                        errors.append(f"Missing skill reading fragment: {key} -> {anchor['href']}")
    if errors:
        raise SystemExit("\n".join(errors))
    pinned = sum(d["status"] == "registered" for d in active.values())
    print(f"Skill catalogue checks passed: {len(active)} pages, {len(seen)} unique entries ({pinned} pinned, {len(active) - pinned} reference-build); " + ("source checks" if args.source_only else "source, rendered links, and search checks"))


if __name__ == "__main__":
    main()
