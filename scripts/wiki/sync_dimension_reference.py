"""Build the combined, artifact-verified dimension catalogue."""
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
MANIFEST = ROOT / "data/dimension_reference.json"


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def rendered_route(page: str) -> str:
    return page[:-8] if page.endswith("index.md") else page[:-3] + "/"


def relative(page: str, target: str) -> str:
    return posixpath.relpath(rendered_route(target), rendered_route(page)).rstrip("/") + "/"


def asset_relative(page: str, asset: str) -> str:
    return posixpath.relpath(asset, rendered_route(page))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.casefold()).strip("-")


def card_stats(stats: dict[str, str]) -> str:
    return '<dl class="reference-card-stats">' + "".join(
        f"<dt>{html.escape(label)}</dt><dd>{html.escape(str(value))}</dd>"
        for label, value in stats.items()
    ) + "</dl>"


def generate_index(manifest: dict) -> str:
    page = "tensura-reference/dimensions/index.md"
    entries = sorted(manifest["pages"], key=lambda item: item["display_title"].casefold())
    letters = sorted({item["display_title"][0].upper() for item in entries})
    lines = [
        '<section class="reference-directory" data-reference-directory="dimensions">',
        '<header class="reference-directory-hero reference-theme-world">',
        '<img src="../../assets/images/reference-world-equipment.png" alt="" loading="eager" decoding="async">',
        '<div class="reference-directory-hero-copy">',
        '<p class="reference-eyebrow">World travel and encounter spaces</p>',
        '<h1>Dimensions</h1>',
        '<p>Every dimension registered by TSR\'s pinned Tensura, Mysticism, and Ascension builds, with entry routes and version evidence.</p>',
        '<div class="reference-directory-hero-actions">',
        f'<span class="reference-count"><strong>{len(entries)}</strong> verified realms</span>',
        '<a class="reference-directory-overview-link" href="../biomes/">Browse their biomes →</a>',
        '</div>',
        '</div>',
        '</header>',
        '<aside class="skill-evidence-note"><strong>Scope:</strong> This catalogue covers registered dimensions in the pinned Minecraft 1.21.1 pack. The separate Tensura: Dungeon project is not installed and is not included.</aside>',
        '<div class="reference-directory-tools">',
        '<label class="reference-filter-label"><span>Find a realm</span><input type="search" class="reference-filter-input" placeholder="Search realms, routes, and registry IDs…" autocomplete="off"></label>',
        '<div class="reference-letter-filters" aria-label="Filter by first letter">',
        '<button type="button" class="is-active" data-letter="all" aria-pressed="true">All</button>',
    ]
    lines.extend(f'<button type="button" data-letter="{letter}" aria-pressed="false">{letter}</button>' for letter in letters)
    lines.extend([
        '</div>',
        f'<p class="reference-filter-status" aria-live="polite">Showing {len(entries)} of {len(entries)} realms</p>',
        '</div>',
        '<div class="reference-card-grid reference-dimension-grid">',
    ])
    for entry in entries:
        title = entry["display_title"]
        source = manifest["reference_builds"][entry["source_key"]]["name"]
        media_class = "reference-card-media--portrait" if entry.get("external_page") else "reference-card-media--theme"
        search = " ".join([title, source, entry["summary"], *entry["stats"].keys(), *map(str, entry["stats"].values())]).casefold()
        lines.extend([
            f'<article class="reference-card reference-dimension-card" data-letter="{html.escape(title[0].upper())}" data-search="{html.escape(search)}">',
            f'<a href="{relative(page, entry["local_page"])}" aria-label="Open {html.escape(title)}">',
            f'<figure class="reference-card-media {media_class}">',
            f'<img src="{asset_relative(page, entry["media_asset"])}" alt="" loading="lazy" decoding="async">',
            f'<figcaption>{html.escape(source)}</figcaption>',
            '</figure>',
            '<div class="reference-card-copy">',
            f'<p class="reference-eyebrow">{html.escape(source)}</p>',
            f'<h2>{html.escape(title)}</h2>',
            f'<p>{html.escape(entry["summary"])}</p>',
            card_stats(entry["stats"]),
            '<small class="reference-card-source-note">Verified against the pinned 1.21.1 artifact and pack selection.</small>',
            '<span class="reference-card-action">Open travel guide <span aria-hidden="true">→</span></span>',
            '</div>',
            '</a>',
            '</article>',
        ])
    lines.extend([
        '</div>',
        '<p class="reference-no-results" hidden>No matching realms. Try a broader search.</p>',
        '</section>',
        '',
    ])
    return "\n".join(lines)


def generate_page(manifest: dict, entry: dict) -> str:
    page = entry["local_page"]
    build = manifest["reference_builds"][entry["source_key"]]
    lines = [
        '---',
        f'title: {entry["display_title"]}',
        'description: ' + json.dumps(entry["summary"], ensure_ascii=False),
        '---',
        '',
        f'# {entry["display_title"]}',
        '',
        f'<span class="reference-badge">{html.escape(build["name"])}</span> <span class="reference-category">Dimensions</span>',
        '',
        '<section class="reference-overview reference-theme-world">',
        '<figure class="reference-overview-media reference-overview-media--source">',
        f'<img src="{asset_relative(page, entry["media_asset"])}" alt="{html.escape(entry["display_title"])} reference artwork" loading="eager" decoding="async">',
        '<figcaption>Verified realm reference</figcaption>',
        '</figure>',
        '<div class="reference-overview-copy">',
        '<p class="reference-eyebrow">At a glance</p>',
        f'<p>{html.escape(entry["summary"])}</p>',
        '<nav class="reference-quick-jumps" aria-label="Article sections">',
    ]
    for section in entry["sections"]:
        lines.append(f'<a href="#{slug(section["title"])}">{html.escape(section["title"])}</a>')
    lines.extend([
        '</nav>',
        '</div>',
        '</section>',
        '',
        '!!! info "Pinned Minecraft 1.21.1 build"',
        '',
        f'    Registered by **{build["name"]} {build["version"]}**, the release selected by TSR. Registry and code paths were checked directly; claims that still require live gameplay are labeled.',
        '',
        '<div class="tensura-reference-article">',
        '<div class="druid-container reference-release-stats"><aside class="druid-infobox">',
        f'<div class="druid-title">{html.escape(entry["display_title"])}</div>',
    ])
    for label, value in entry["stats"].items():
        lines.append(f'<div class="druid-row"><div class="druid-label">{html.escape(label)}</div><div class="druid-data">{html.escape(str(value))}</div></div>')
    lines.extend(['</aside></div></div>', ''])
    for section in entry["sections"]:
        lines.extend([f'## {section["title"]}', ''])
        for paragraph in section["paragraphs"]:
            lines.extend([paragraph, ''])
    if entry.get("links"):
        lines.extend(['## Continue exploring', '', '<div class="race-map-directory">'])
        for link in entry["links"]:
            lines.append(f'<a href="{relative(page, link["target"])}"><strong>{html.escape(link["label"])}</strong><span>Open the connected reference.</span></a>')
        lines.extend(['</div>', ''])
    lines.extend([
        '??? info "Sources and verification"',
        '',
        f'    [{build["name"]} {build["version"]}]({build.get("source_url", "https://www.curseforge.com/minecraft/mc-mods/tensura-ascensions")}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]})',
        '',
    ])
    if build.get("sha1"):
        lines.extend([f'    Artifact SHA-1: `{build["sha1"]}`.', ''])
    if entry.get("upstream_url"):
        lines.extend([f'    Gameplay route cross-check: [{entry["display_title"]} upstream reference]({entry["upstream_url"]}).', ''])
    lines.extend(['    Packaged evidence:', ''])
    lines.extend(f'    - `{path}`' for path in entry["evidence_paths"])
    lines.extend(['', '[Back to Dimensions](index.md)', ''])
    return "\n".join(lines)


def generate() -> dict[str, str]:
    manifest = load_manifest()
    result = {"tensura-reference/dimensions/index.md": generate_index(manifest)}
    for entry in manifest["pages"]:
        if not entry.get("external_page"):
            result[entry["local_page"]] = generate_page(manifest, entry)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    pages = generate()
    for name, content in pages.items():
        destination = DOCS / name
        if args.check:
            if not destination.exists() or destination.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale dimension reference: {name}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding="utf-8", newline="\n")
    print(f'Dimension reference pages {"checked" if args.check else "generated"}: {len(pages)}')


if __name__ == "__main__":
    main()
