"""Validate rendered progression destinations, fragments, and artwork."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from race_catalogue import FAMILY_PARTITIONS, is_race_form, race_reference


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids = set()
        self.links = []
        self.unrendered_markdown = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "markdown" in attrs:
            self.unrendered_markdown = True
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])


def main() -> int:
    graph = json.loads((SITE / "assets/data/progression.json").read_text(encoding="utf-8"))
    pages = {}
    errors = []
    checked = 0

    def check(target: str, base: Path = SITE) -> None:
        nonlocal checked
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            return
        destination = (base / unquote(parsed.path).lstrip("/")).resolve()
        if destination.is_dir():
            destination /= "index.html"
        checked += 1
        if not destination.is_relative_to(SITE.resolve()) or not destination.is_file():
            errors.append(f"Missing local progression destination: {target}")
            return
        if parsed.fragment:
            if destination not in pages:
                parser = PageParser()
                parser.feed(destination.read_text(encoding="utf-8"))
                pages[destination] = parser
            if unquote(parsed.fragment) not in pages[destination].ids:
                errors.append(f"Missing progression fragment: {target}")

    for key, node in graph["nodes"].items():
        check(key)
        if node.get("image"):
            check(node["image"])
    for edge in graph["edges"]:
        if edge["from"] not in graph["nodes"] or edge["to"] not in graph["nodes"]:
            errors.append(f"Unknown progression endpoint: {edge}")

    for source, destination in json.loads((SITE / "assets/data/skill-redirects.json").read_text(encoding="utf-8")).items():
        check(destination)
    race_families = json.loads((SITE / "assets/data/race-families.json").read_text(encoding="utf-8"))
    expected_races = set()
    for source in ("tensura", "mysticism"):
        source_manifest = json.loads((ROOT / f"data/upstream_{source}_pages.json").read_text(encoding="utf-8"))
        for record in source_manifest["pages"]:
            if is_race_form(record):
                expected_races.add(record["local_page"].removesuffix(".md") + "/")
    if set(race_families["destinations"]) != expected_races:
        errors.append("Race family coverage differs from the imported race manifest")
    if any(family["title"] == "Angel reference" for family in race_families["families"]):
        errors.append("Angel overview must not appear as a race family")
    if "mysticism-reference/races/angel/" in graph["nodes"]:
        errors.append("Angel overview must not appear as an evolution stage")
    if sum(family["title"] == "Angel" for family in race_families["families"]) != 1:
        errors.append("Expected one maintained Angel family")
    by_title = {family['title']: family for family in race_families['families']}
    for title, (source, slugs) in FAMILY_PARTITIONS.items():
        current_slugs = [slug for slug in slugs.split() if race_reference()['pages'].get(f"{source}-reference/races/{'races-' if source == 'tensura' else ''}{slug}.md", {}).get('status') == 'registered']
        family = by_title.get(title)
        if not current_slugs:
            if family:
                errors.append(f'Unverified family in current directory: {title}')
            continue
        if not family:
            errors.append(f"Missing independent race family: {title}")
            continue
        for slug in current_slugs:
            source_route = f"{source}-reference/races/{'races-' if source == 'tensura' else ''}{slug}/"
            destination = race_families['destinations'].get(source_route, '')
            if not destination.startswith(family['route'] + '#'):
                errors.append(f"Race assigned to wrong family: {source_route}")
    for title, asset in json.loads((ROOT / 'data/race_family_media.json').read_text(encoding='utf-8')).items():
        if by_title.get(title, {}).get('image') != asset:
            errors.append(f"Reviewed family image replaced: {title}")
    check("tensura-reference/races/families/angel-reference/#angel")
    for old_route, anchor in (('human-undead', 'races-human'), ('mantis-scorpion-spider', 'mantis'), ('poison-soul-insect', 'poison-soul-insect')):
        check(f"tensura-reference/races/families/{old_route}/#{anchor}")
    for destination in race_families["destinations"].values():
        check(destination)

    manifest = json.loads((ROOT / "data/ascension_reference.json").read_text(encoding="utf-8"))
    routes = [page.removesuffix(".md") + "/" for page in manifest["pages"]]
    routes += ["ascension-and-awakening/", "hyperbolic-chamber/", "getting-started/", "tensura-reference/races/evolution-trees/"]
    routes += [family["route"] for family in race_families["families"]]
    for route in routes:
        page = SITE / route / "index.html"
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        if parser.unrendered_markdown:
            errors.append(f"Unrendered Markdown container: {route}")
        for link in parser.links:
            if urlsplit(link).fragment:
                check(link, page.parent)
    if errors:
        raise SystemExit("Progression validation failed:\n- " + "\n- ".join(sorted(set(errors))))
    print(f"Progression destinations OK: {len(graph['nodes'])} nodes, {len(graph['edges'])} connections, {checked} targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
