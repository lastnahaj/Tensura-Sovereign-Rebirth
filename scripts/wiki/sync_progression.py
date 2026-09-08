"""Build local race and skill progression cards from documented relationships."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
OUTPUT = DOCS / "assets" / "data" / "progression.json"


def route(page: str) -> str:
    return page[:-8] if page.endswith("index.md") else page[:-3] + "/"


def build() -> dict:
    nodes = {}
    documents = {}
    document_sources = {}
    titles = {}
    from skill_catalogue import ACTIVE, nightmares_manifest
    manifests = {source: json.loads((ROOT / "data" / f"upstream_{source}_pages.json").read_text(encoding="utf-8")) for source in ("tensura", "mysticism")}
    manifests["nightmares"] = nightmares_manifest()
    for source, manifest in manifests.items():
        for record in manifest["pages"]:
            category = record["category"]
            if category not in {"races", "battlewill", "magic", "resistances"} and not category.startswith("skills/"):
                continue
            page = record["local_page"]
            key = route(page)
            text = (DOCS / page).read_text(encoding="utf-8")
            soup = BeautifulSoup(text, "html.parser")
            overview = soup.select_one(".reference-overview img")
            asset = posixpath.normpath(posixpath.join(key, overview["src"])) if overview else ""
            nodes[key] = {"title": record["display_title"], "image": asset, "category": category}
            documents[key] = soup
            document_sources[key] = source
            titles.setdefault((source, record["display_title"].casefold()), []).append(key)

    edges = {}

    def connect(start: str, end: str, kind: str, requirement: str = "") -> None:
        if start == end or start not in nodes or end not in nodes:
            return
        pair = (start, end)
        edge = edges.setdefault(pair, {"from": start, "to": end, "kinds": [], "requirements": []})
        if kind not in edge["kinds"]:
            edge["kinds"].append(kind)
        if requirement and requirement not in edge["requirements"]:
            edge["requirements"].append(requirement)

    for key, soup in documents.items():
        for row in soup.select(".druid-row"):
            label_node = row.select_one(".druid-label")
            data = row.select_one(".druid-data")
            if not label_node or not data:
                continue
            label = label_node.get_text(" ", strip=True)
            previous = bool(re.fullmatch(r"Previous|Predecessor|Evolv(?:ed|ing) From", label, re.I))
            successor = bool(re.fullmatch(r"Next|Successor|Evolution|Evolutions|Named|Naming|Harvest Festival|Awakening", label, re.I))
            combination = label.casefold() == "combination of skills"
            if not (previous or successor or combination):
                continue
            values = []
            for anchor in data.select("a[href]"):
                href = anchor["href"]
                if urlsplit(href).scheme:
                    continue
                target = posixpath.normpath(posixpath.join(key, unquote(href.split("#")[0]))).rstrip("/") + "/"
                if target in nodes:
                    values.append(target)
            if not values:
                for value in re.split(r"[,·/]|\bor\b", data.get_text(" ", strip=True)):
                    choices = titles.get((document_sources[key], value.strip().casefold()), [])
                    if len(choices) == 1:
                        values.append(choices[0])
            for target in values:
                same_kind = (nodes[key]["category"] == "races") == (nodes[target]["category"] == "races")
                if not same_kind:
                    continue
                if previous or combination:
                    connect(target, key, "Mastery / combination" if combination else "Evolution", data.get_text(" ", strip=True))
                else:
                    connect(key, target, label)

    extra = json.loads((ROOT / "data" / "ascension_reference.json").read_text(encoding="utf-8"))
    for entry in extra["entries"]:
        key = route(entry["local_page"]) + ("#" + entry["fragment"] if entry["fragment"] else "")
        nodes[key] = {"title": entry["display_title"], "image": entry["asset"], "category": entry["category"]}
    for entry in json.loads((ROOT / "data/skill_reference.json").read_text(encoding="utf-8"))["entries"]:
        nodes[route(entry["local_page"])] = {"title": entry["display_title"], "image": entry["asset"], "category": entry["category"]}
    for page in extra["pages"]:
        soup = BeautifulSoup((DOCS / page).read_text(encoding="utf-8"), "html.parser")
        family_route = route(page)
        for card in soup.select(".race-stage-card"):
            key = family_route + "#" + card["id"]
            nodes[key] = {"title": card.h2.get_text(strip=True), "image": nodes[family_route]["image"], "category": "races"}
        for card in soup.select(".race-stage-card"):
            start = family_route + "#" + card["id"]
            links = card.select(".race-card-route > :last-child a[href], .race-card-route > a:last-child[href]")
            for link in links:
                parsed = urlsplit(link["href"])
                target = posixpath.normpath(posixpath.join(family_route, parsed.path)).rstrip("/") + "/#" + parsed.fragment
                connect(start, target, "Evolution")

    skill = {Path(entry["local_page"]).stem: route(entry["local_page"]) for entry in extra["entries"] if entry["category"] != "races"}
    connect(skill["energy-charge"], skill["maximum-charge"], "Mastery")
    connect(skill["energy-charge"], skill["magicule-attunement"], "Mastery / combination", "Master Energy Charge, possess unmastered Haki, and reach 20,000 EP.")
    connect(skill["magicule-attunement"], skill["magicule-resonance"], "Mastery")
    connect(skill["magicule-resonance"], skill["magicule-dominion"], "Mastery")
    for start, end in (("great-mage", "the-timeless-mage"), ("imprisoned-jester", "the-unbound-jester"), ("bubble-majin", "the-evil-majin"), ("dragon-slayer", "the-slayer-of-dragons"), ("sealer", "the-one-who-seals")):
        connect(skill[start], skill[end], "Ultimate awakening", "Master the Unique and satisfy the altar's universal and Ultimate-specific gates.")
    for start, end, requirement in (
        ("tensura-reference/magic/magic-jamming/", "blockade", "Master Magic Jamming and kill 30 Vexes."),
        ("tensura-reference/magic/gate/", "hyperbolic-passage", "Master Gate and Sacred Haki."),
        ("tensura-reference/magic/gate/", "hell-passage", "Master Gate while Demon Lord Haki is active."),
        ("tensura-reference/skills/extra/sacred-haki/", "hyperbolic-passage", "Master Sacred Haki and Gate."),
        ("tensura-reference/skills/extra/demon-lord-haki/", "hell-passage", "Master Gate while Demon Lord Haki is active."),
    ):
        connect(start, skill[end], "Unlock requirement", requirement)
    from skill_catalogue import catalogue
    policy = catalogue()
    for page, decision in policy["pages"].items():
        key = route(page)
        if decision["status"] not in ACTIVE:
            nodes.pop(key, None)
        elif key in nodes:
            nodes[key]["category"] = decision["category"]
            if decision["namespace"] in {"mysticism", "trnightmare"}:
                nodes[key]["image"] = "assets/icons/skills/" + decision["id"].replace(":", "-") + ".svg"
            if decision["status"] == "reference":
                nodes[key]["verification"] = "reference-build-only"
    current_edges = [edge for edge in edges.values() if edge["from"] in nodes and edge["to"] in nodes]
    return {"nodes": nodes, "edges": sorted(current_edges, key=lambda edge: (edge["from"], edge["to"]))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit("Progression data is stale; run scripts/wiki/sync_progression.py")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Progression map OK: {len(data['nodes'])} nodes, {len(data['edges'])} documented connections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
