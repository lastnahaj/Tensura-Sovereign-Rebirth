"""Validate rendered progression destinations, fragments, and artwork."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
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

    manifest = json.loads((ROOT / "data/ascension_reference.json").read_text(encoding="utf-8"))
    routes = [page.removesuffix(".md") + "/" for page in manifest["pages"]]
    routes += ["ascension-and-awakening/", "hyperbolic-chamber/", "getting-started/", "tensura-reference/races/evolution-trees/"]
    for route in routes:
        page = SITE / route / "index.html"
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            if urlsplit(link).fragment:
                check(link, page.parent)
    if errors:
        raise SystemExit("Progression validation failed:\n- " + "\n- ".join(sorted(set(errors))))
    print(f"Progression destinations OK: {len(graph['nodes'])} nodes, {len(graph['edges'])} connections, {checked} targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
