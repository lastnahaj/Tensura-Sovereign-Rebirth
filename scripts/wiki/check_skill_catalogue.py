"""Check skill eligibility, acquisition panels, regeneration, and rendered search."""
from __future__ import annotations

import argparse
import json
import posixpath
import re
from functools import lru_cache
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from skill_catalogue import ACTIVE, ROOT, catalogue, inventory, nightmares_manifest
from sync_skill_catalogue import DOCS, LABELS, generate, render_acquisition_markdown, route
from skill_presentation import CATEGORIES


class FragmentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'id':
                self.ids.add(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-only", action="store_true")
    args = parser.parse_args()
    outputs = generate()
    generated_pages = json.loads(outputs["assets/data/skill-catalogue.json"])["pages"]
    progression = json.loads((DOCS / 'assets/data/progression.json').read_text(encoding='utf-8'))['nodes']
    errors = []
    for name, content in outputs.items():
        if not (DOCS / name).exists() or (DOCS / name).read_text(encoding="utf-8") != content:
            errors.append(f"Stale skill output: {name}")
    policy = catalogue()
    pool = inventory()
    nightmares = nightmares_manifest()
    active = {p: d for p, d in policy["pages"].items() if d["status"] in ACTIVE}
    active_routes = {route(p): d for p, d in active.items()}
    ability_search = json.loads(outputs['assets/data/skill-search.json'])
    if {entry['route'] for entry in ability_search} != set(active_routes) or len(ability_search) != len(active_routes):
        errors.append('Ability search must contain each active skill exactly once')
    for entry in ability_search:
        decision = active_routes.get(entry['route'])
        if decision and any(entry[key] != decision[key] for key in ('title', 'category', 'status')):
            errors.append(f'Ability search loses catalogue metadata: {entry["route"]}')
        if not entry['image'] or not (DOCS / entry['image']).is_file():
            errors.append(f'Ability search image missing: {entry["route"]}')
    hub_page = 'tensura-reference/skills/index.md'
    hub = BeautifulSoup(outputs[hub_page], 'html.parser')
    tiles = hub.select('.skill-category-tile')
    targets = {posixpath.normpath(posixpath.join(route(hub_page), tile['href'])).rstrip('/') for tile in tiles}
    if targets != {'tensura-reference/' + category for category in CATEGORIES} or len(tiles) != 8:
        errors.append('Ability hub must link to all eight unified categories')
    for tile in tiles:
        destination = posixpath.normpath(posixpath.join(route(hub_page), tile['href']))
        directory = BeautifulSoup(outputs[destination.rstrip('/') + '/index.md'], 'html.parser')
        if tile.select_one('.skill-category-count').get_text() != f'{len(directory.select(".reference-card"))} entries':
            errors.append(f'Ability hub category count mismatch: {destination}')
    if not BeautifulSoup(outputs['tensura-reference/battlewill/index.md'], 'html.parser').select_one('.reference-directory-overview-link'):
        errors.append('Battlewill overview link missing')
    if not hub.select_one('label[for="skill-hub-search"]') or not hub.select_one('.skill-finder-status[role="status"]'):
        errors.append('Ability search lacks its accessible label or status')
    if not hub.select_one('.reference-media-credits a[href]'):
        errors.append('Ability hub lacks image attribution')
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
        if soup.select_one('.reference-directory-hero') or not soup.select_one('.skill-directory-heading'):
            errors.append(f'Legacy ability banner remains: {page}')
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
            asset = generated_pages[page].get("asset")
            if decision['namespace'] == 'mysticism' and progression.get(route(page), {}).get('image') != asset:
                errors.append(f'Skill progression image differs from its verified article icon: {page}')
            if not previews or not asset or any(
                posixpath.normpath(posixpath.join(route(page), image["src"])) != asset
                for image in previews
            ):
                errors.append(f"Missing verified skill icon: {page}")
            if asset and asset.startswith("assets/upstream/") and not soup.select_one(".reference-overview-media figcaption a[href]"):
                errors.append(f"Missing source-icon credit: {page}")
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
        @lru_cache(maxsize=None)
        def fragment_ids(path):
            parser = FragmentParser()
            parser.feed(path.read_text(encoding='utf-8'))
            return parser.ids

        site = ROOT / "site"
        for page in [hub_page] + ['tensura-reference/' + category + '/index.md' for category in LABELS]:
            document = site / route(page) / 'index.html'
            section = BeautifulSoup(document.read_text(encoding='utf-8'), 'html.parser')
            for element in section.select('.skill-hub a[href], .skill-hub img[src], .skill-type-nav a[href]'):
                value = element.get('href') or element['src']
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                destination = (document.parent / unquote(url.path)).resolve()
                if destination.is_dir():
                    destination /= 'index.html'
                if not destination.is_relative_to(site.resolve()) or not destination.is_file():
                    errors.append(f'Missing ability hub destination: {page} -> {value}')
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
                    if unquote(url.fragment) not in fragment_ids(destination):
                        errors.append(f"Missing skill reading fragment: {key} -> {anchor['href']}")
    if errors:
        raise SystemExit("\n".join(errors))
    pinned = sum(d["status"] == "registered" for d in active.values())
    print(f"Skill catalogue checks passed: {len(active)} pages, {len(seen)} unique entries ({pinned} pinned, {len(active) - pinned} reference-build); " + ("source checks" if args.source_only else "source, rendered links, and search checks"))


if __name__ == "__main__":
    main()
