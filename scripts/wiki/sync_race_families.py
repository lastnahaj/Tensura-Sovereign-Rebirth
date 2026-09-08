"""Present documented race families as connected evolution maps and stat cards."""
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from sync_progression import build, route

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"


def generate() -> dict[str, str]:
    graph = build()
    nodes = {}
    source_pages = {}
    for source in ("tensura", "mysticism"):
        manifest = json.loads((ROOT / "data" / f"upstream_{source}_pages.json").read_text(encoding="utf-8"))
        for record in manifest["pages"]:
            if record["category"] != "races" or record["display_title"].strip().casefold() == "races":
                continue
            key = route(record["local_page"])
            nodes[key] = graph["nodes"][key]
            source_pages[key] = record["local_page"]
    adjacency = {key: set() for key in nodes}
    incoming = {key: [] for key in nodes}
    outgoing = {key: [] for key in nodes}
    for edge in graph["edges"]:
        start, end = edge["from"], edge["to"]
        if start in nodes and end in nodes:
            adjacency[start].add(end)
            adjacency[end].add(start)
            incoming[end].append(edge)
            outgoing[start].append(edge)
    groups = []
    seen = set()
    for key in sorted(nodes):
        if key in seen:
            continue
        todo = [key]
        group = []
        while todo:
            current = todo.pop()
            if current in seen:
                continue
            seen.add(current)
            group.append(current)
            todo.extend(sorted(adjacency[current] - seen, reverse=True))
        groups.append(group)

    outputs = {}
    families = []
    destinations = {}
    for group in groups:
        roots = sorted([key for key in group if not incoming[key]], key=lambda key: nodes[key]["title"])
        anchors = {key: key.rstrip("/").split("/")[-1] for key in group}
        first = roots[0] if roots else sorted(group)[0]
        title = " / ".join(nodes[key]["title"] for key in roots) if roots else nodes[first]["title"] + " connected forms"
        if title == "Angel" and len(group) == 1:
            title = "Angel reference"
        if "tensura-reference/races/races-human/" in group:
            title = "Human & Undead"
        slug = re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
        page = f"tensura-reference/races/families/{slug}.md"
        if page in outputs:
            raise ValueError(f"Duplicate race family destination: {page}")
        page_route = route(page)
        for key in group:
            destinations[key] = page_route + "#" + anchors[key]
        # Order prerequisites before their successors, keeping documented shortcuts.
        distance = {key: 0 for key in roots}
        todo = list(roots)
        remaining = {key: len(incoming[key]) for key in group}
        while todo:
            key = todo.pop(0)
            for edge in outgoing[key]:
                target = edge["to"]
                distance[target] = max(distance.get(target, 0), distance[key] + 1)
                remaining[target] -= 1
                if remaining[target] == 0:
                    todo.append(target)
        ordered = sorted(group, key=lambda key: (distance.get(key, 999), nodes[key]["title"]))
        images = [nodes[key]["image"] for key in ordered if nodes[key]["image"] and not any(marker in nodes[key]["image"] for marker in ("wip-", "invicon-", "essence-"))]
        image = next((value for value in images if "/upstream/" in value), "assets/images/reference-races-evolution.png")
        image_url = posixpath.relpath(image, page_route)
        lines = ["---", f"title: {json.dumps(title + ' Evolution', ensure_ascii=False)}", f"description: {len(group)} connected race forms with documented stats, abilities, and evolution links.", "---", "",
                 f'<section class="race-family-hero"><img src="{image_url}" alt="{html.escape(title)} race reference artwork"><div><p class="reference-eyebrow">Race family · {len(group)} forms</p><h1>{html.escape(title)} evolution</h1><p>Compare each documented form, follow its branches, and open the full reference for detailed evolution conditions.</p></div></section>', "",
                 "[All race families](../index.md)", "", "## Evolution path", "",
                 '<div class="family-connection-grid" aria-label="Documented evolution paths">']
        connections = [edge for key in ordered for edge in outgoing[key]]
        for edge in connections:
            start, end = edge["from"], edge["to"]
            labels = " / ".join(edge["kinds"])
            lines.append(f'<div><a href="#{anchors[start]}">{html.escape(nodes[start]["title"])}</a><span>{html.escape(labels)} →</span><a href="#{anchors[end]}">{html.escape(nodes[end]["title"])}</a></div>')
        if not connections:
            lines.append('<p>No connected evolution is documented in this reference.</p>')
        lines.extend(['</div>', "", "## Race stages", "", '<div class="race-stage-grid">'])
        for key in ordered:
            soup = BeautifulSoup((DOCS / source_pages[key]).read_text(encoding="utf-8"), "html.parser")
            rows = []
            for row in soup.select(".druid-row"):
                label, value = row.select_one(".druid-label"), row.select_one(".druid-data")
                if not label or not value:
                    continue
                label_text = label.get_text(" ", strip=True)
                if re.fullmatch(r"Previous|Next|Named|Naming|Harvest Festival|Awakening", label_text, re.I):
                    continue
                for anchor in value.select("a[href]"):
                    parsed = urlsplit(anchor["href"])
                    if parsed.scheme or parsed.netloc:
                        continue
                    absolute = posixpath.normpath(posixpath.join(key, unquote(parsed.path)))
                    anchor["href"] = posixpath.relpath(absolute, page_route) + ("/" if not posixpath.splitext(absolute)[1] else "") + ("#" + parsed.fragment if parsed.fragment else "")
                rows.append((label_text, value.get_text(" ", strip=True), value.decode_contents()))
            stats = [(label, text) for label, text, _ in rows if label in {"HP", "SHP", "Attack DMG", "Movement Speed", "MP Range", "AP Range"}]
            tier = "Divine evolution" if any(label == "Divine" and text.casefold() == "yes" for label, text, _ in rows) else "Race form"
            stage = [f'<article class="race-stage-card" id="{anchors[key]}"><p class="race-stage-kicker">{tier}</p><h2>{html.escape(nodes[key]["title"])}</h2><div class="race-stats">']
            stage.extend(f'<span><b>{html.escape(text)}</b> {html.escape(label)}</span>' for label, text in stats)
            stage.append('</div><dl>')
            primary_labels = {"Difficulty", "Alignment", "Spiritual", "Divine", "Intrinsics", "Skills", "Learnable", "Learnables"}
            stage.extend(f'<dt>{html.escape(label)}</dt><dd>{value}</dd>' for label, _, value in rows if label in primary_labels)
            if not rows:
                stage.append('<dt>Stats</dt><dd>No structured race stats are published in this reference.</dd>')
            source_link = posixpath.relpath(key, page_route) + "/"
            stage.append(f'<dt>Requirements &amp; abilities</dt><dd><a href="{source_link}">Open full {html.escape(nodes[key]["title"])} reference</a></dd></dl>')
            secondary = [(label, value) for label, _, value in rows if label not in primary_labels and label not in {item[0] for item in stats}]
            if secondary:
                stage.append('<details class="race-secondary-stats"><summary>More race stats</summary><dl>')
                stage.extend(f'<dt>{html.escape(label)}</dt><dd>{value}</dd>' for label, value in secondary)
                stage.append('</dl></details>')
            previous = " · ".join(f'<a href="#{anchors[e["from"]]}">← {html.escape(nodes[e["from"]]["title"])}</a>' for e in incoming[key]) or 'No previous form documented'
            following = " · ".join(f'<a href="#{anchors[e["to"]]}">{html.escape(nodes[e["to"]]["title"])} →</a>' for e in outgoing[key]) or 'No further evolution documented'
            stage.append(f'<p class="race-card-route"><span>{previous}</span><span>{following}</span></p></article>')
            lines.append("".join(stage))
        lines.extend(['</div>', "", "Stats and relationships retain their source-page context. Evolution methods can have separate EP, naming, awakening, or other requirements; a connecting arrow alone is not an unlock condition.", "",
                      "Source pages credit the [Tensura: Reincarnated Wiki](https://tensura.wiki.gg/) and [TR Mysticism Wiki](https://trmysticism.wiki.gg/) contributors under CC BY-SA 4.0. See [upstream attribution](../../../project/upstream-attribution.md) and [Mysticism attribution](../../../project/mysticism-upstream-attribution.md).", ""])
        if len(connections) > 12:
            start = lines.index('<div class="family-connection-grid" aria-label="Documented evolution paths">')
            end = lines.index('</div>', start)
            lines.insert(end + 1, '</details>')
            lines.insert(start, f'<details class="family-map-details"><summary>Explore all {len(connections)} documented connections</summary>')
        outputs[page] = "\n".join(lines)
        families.append({"title": title, "route": page_route, "image": image, "forms": len(group), "search": " ".join(nodes[key]["title"] for key in ordered)})
    extra = json.loads((ROOT / "data/ascension_reference.json").read_text(encoding="utf-8"))
    for entry in extra["entries"]:
        if entry["category"] == "races":
            soup = BeautifulSoup((DOCS / entry["local_page"]).read_text(encoding="utf-8"), "html.parser")
            stages = soup.select('.race-stage-card h2')
            families.append({"title":entry["display_title"].removesuffix(" evolution"), "route":route(entry["local_page"]), "image":entry["asset"], "forms":len(stages), "search":" ".join(stage.get_text(strip=True) for stage in stages)})
    index_route = "tensura-reference/races/"
    lines = ['---', 'title: Race Families', 'description: Explore race families, their evolution stages, and their documented stat cards.', '---', '', '# Race Families', '',
             'Choose a race family to see its connected evolution path and compare stage cards. Divine forms are advanced stages within these families, not a separate list of starting races.', '',
             '<section class="reference-directory" data-reference-directory="races"><div class="reference-directory-tools"><label class="reference-filter-label"><span>Find a family or any evolution stage</span><input type="search" class="reference-filter-input" placeholder="Search Monkey, Divine Human, Wolf…" autocomplete="off"></label><p class="reference-filter-status" aria-live="polite"></p></div><div class="reference-card-grid">']
    for family in sorted(families, key=lambda value: value["title"].casefold()):
        target = posixpath.relpath(family["route"], index_route) + "/"
        image = posixpath.relpath(family["image"], index_route)
        search = html.escape((family["title"] + " " + family["search"]).casefold(), quote=True)
        lines.append(f'<article class="reference-card" data-search="{search}" data-letter="{family["title"][0].upper()}"><a href="{target}" aria-label="Open {html.escape(family["title"])} evolution"><figure class="reference-card-media"><img src="{image}" alt="" loading="lazy"></figure><div class="reference-card-copy"><h2>{html.escape(family["title"])}</h2><p>{family["forms"]} documented forms · Evolution map and stat cards</p></div></a></article>')
    lines.extend(['</div><p class="reference-no-results" hidden>No race families match this search.</p></section>', '', '[Complete evolution relationship index](evolution-trees.md)', ''])
    outputs['tensura-reference/races/index.md'] = "\n".join(lines).replace('data-reference-directory="races"', 'data-reference-directory="races" data-reference-unit="race families"')
    outputs['assets/data/race-families.json'] = json.dumps({"families":families,"destinations":destinations},ensure_ascii=False,indent=2) + "\n"
    reference_index = DOCS / 'tensura-reference/index.md'
    if reference_index.exists():
        outputs['tensura-reference/index.md'] = re.sub(r'<a href="races/">(?:Races|Race families) <span>\d+</span>', f'<a href="races/">Race families <span>{len(families)}</span>', reference_index.read_text(encoding='utf-8'))
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = generate()
    for name, content in outputs.items():
        path = DOCS / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Race family output is stale: {name}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    print(f'Race families OK: {sum("/races/families/" in name for name in outputs)} generated family pages, six maintained family maps')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
