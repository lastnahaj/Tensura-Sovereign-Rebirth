"""Polish imported biome articles and pin Mysticism elemental biomes to 1.21.1."""
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
BEGIN, END = "<!-- biome-build:start -->", "<!-- biome-build:end -->"
MAINTENANCE_BLOCK = re.compile(r"<div>\s*<table\b.*?</table>\s*</div>\s*", re.I | re.S)
MAINTENANCE_CREDIT = re.compile(
    r'(?im)^<li><a\b[^>]*File:(?:Mysticism_WIP|WIP7|Placeholder)\.png[^>]*>.*?</li>\s*\r?\n?'
)
COLLECTION_PAGES = {
    "tensura-reference/biomes/biomes.md",
    "mysticism-reference/biomes/structures-and-biomes.md",
}
MYSTICISM_BIOMES = {
    "mysticism-reference/biomes/structures-and-biomes-dark-biome.md": "mysticism:darkness_biome",
    "mysticism-reference/biomes/structures-and-biomes-earth-biome.md": "mysticism:earth_biome",
    "mysticism-reference/biomes/structures-and-biomes-fire-biome.md": "mysticism:fire_biome",
    "mysticism-reference/biomes/structures-and-biomes-light-biome.md": "mysticism:light_biome",
    "mysticism-reference/biomes/structures-and-biomes-space-biome.md": "mysticism:space_biome",
    "mysticism-reference/biomes/structures-and-biomes-water-biome.md": "mysticism:water_biome",
    "mysticism-reference/biomes/structures-and-biomes-wind-biome.md": "mysticism:wind_biome",
}
MYSTICISM_MEDIA = {
    "mysticism-reference/biomes/structures-and-biomes-dark-biome.md": "assets/upstream/mysticism/biomes/dark-biome-895efd6cde.png",
    "mysticism-reference/biomes/structures-and-biomes-earth-biome.md": "assets/upstream/mysticism/biomes/earth-biome-a682dcadee.png",
    "mysticism-reference/biomes/structures-and-biomes-fire-biome.md": "assets/upstream/mysticism/biomes/fire-biome-ead4504af1.png",
    "mysticism-reference/biomes/structures-and-biomes-light-biome.md": "assets/upstream/mysticism/biomes/light-biome-a74478c8ea.png",
    "mysticism-reference/biomes/structures-and-biomes-space-biome.md": "assets/upstream/mysticism/biomes/space-biome-fb41cdebe6.png",
    "mysticism-reference/biomes/structures-and-biomes-water-biome.md": "assets/upstream/mysticism/biomes/water-biome-c602cba8eb.png",
    "mysticism-reference/biomes/structures-and-biomes-wind-biome.md": "assets/upstream/mysticism/biomes/wind-biome-ec10b1f6fb.png",
}


def relative(page: str, asset: str) -> str:
    rendered_route = page[:-8] if page.endswith("index.md") else page[:-3] + "/"
    return posixpath.relpath(asset, rendered_route)


def tidy_media_credits(text: str) -> str:
    text = MAINTENANCE_CREDIT.sub("", text)

    def replace(match: re.Match[str]) -> str:
        block = match.group(0)
        count = len(re.findall(r"<li\b", block, flags=re.I))
        if not count:
            return ""
        noun = "file" if count == 1 else "files"
        return re.sub(r"Media credits \(\d+ source files?\)", f"Media credits ({count} source {noun})", block)

    return re.sub(r'<details class="reference-media-credits">.*?</details>', replace, text, flags=re.I | re.S)


def strip_maintenance(text: str) -> str:
    text = MAINTENANCE_BLOCK.sub(
        lambda match: ""
        if "work in progress" in BeautifulSoup(match.group(0), "html.parser").get_text(" ", strip=True).casefold()
        else match.group(0),
        text,
    )
    text = re.sub(r"(?m)^- Work_in_Progress\s*\r?\n", "", text)
    text = re.sub(r"<small>\s*(?:Only the strong survive\.|Upstream reference information for Structures and Biomes\.)\s*</small>", "", text, flags=re.I)
    return tidy_media_credits(text)


def replace_collection_art(text: str, page: str) -> str:
    figure = (
        '<figure class="reference-overview-media reference-overview-media--theme">\n'
        f'<img src="{relative(page, "assets/images/reference-world-equipment.png")}" alt="Biome collection artwork" loading="eager" decoding="async">\n'
        '<figcaption>Original TSR world illustration</figcaption>\n'
        '</figure>'
    )
    return re.sub(
        r'<figure class="reference-overview-media[^>]*>.*?(?:wip|placeholder).*?</figure>',
        lambda _match: figure,
        text,
        count=1,
        flags=re.I | re.S,
    )


def hide_collection_page(text: str) -> str:
    text = text.replace(
        "Upstream reference information for Structures and Biomes.",
        "Archived source overview of Mysticism's elemental-realm biomes and their associated structures. Use the combined Biomes directory for current navigation.",
    )
    front, rest = text[4:].split("\n---\n", 1)
    if not re.search(r"^search:", front, re.M):
        front += "\nsearch:\n  exclude: true"
    return "---\n" + front + "\n---\n" + rest


def clean_related_cards(text: str, page: str, media: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        soup = BeautifulSoup(match.group(0), "html.parser")
        for card in soup.select(".reference-related-card"):
            image = card.select_one("img[src]")
            href = card.get("href", "")
            destination = posixpath.normpath(posixpath.join(page.removesuffix(".md") + "/", href)).rstrip("/") + ".md"
            if image and re.search(r"(?:wip|placeholder)", image.get("src", ""), re.I):
                card.decompose()
            elif image and destination in media:
                image["src"] = relative(page, media[destination])
                image["alt"] = ""
        return re.sub(r"\n[ \t]*\n+", "\n", str(soup)) if soup.select(".reference-related-card") else ""

    return re.sub(r'<section class="reference-related">.*?</section>', replace, text, flags=re.I | re.S)


def generate() -> dict[str, str]:
    raw_overrides = json.loads((ROOT / "data/reference_card_media.json").read_text(encoding="utf-8"))
    media = {
        page: value["asset"] if isinstance(value, dict) else value
        for page, value in raw_overrides.items()
        if "/biomes/" in page
    }
    media.update(MYSTICISM_MEDIA)
    pages = [
        path
        for root in (DOCS / "tensura-reference/biomes", DOCS / "mysticism-reference/biomes")
        for path in root.glob("*.md")
        if path.name not in {"index.md", "kamui-biome.md"}
    ]
    outputs: dict[str, str] = {}
    for path in pages:
        page = path.relative_to(DOCS).as_posix()
        text = path.read_text(encoding="utf-8")
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
        text = strip_maintenance(text)
        text = clean_related_cards(text, page, media)
        override = raw_overrides.get(page)
        if isinstance(override, dict) and override.get("summary"):
            summary = override["summary"]
            text = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(summary, ensure_ascii=False), text, count=1)
            text = re.sub(
                r'(<p class="reference-eyebrow">At a glance</p>\s*)<p>.*?</p>',
                lambda match: match.group(1) + f"<p>{html.escape(summary)}</p>",
                text,
                count=1,
                flags=re.I | re.S,
            )
        if page in COLLECTION_PAGES:
            text = hide_collection_page(replace_collection_art(text, page))
        if page in MYSTICISM_BIOMES:
            registry_id = MYSTICISM_BIOMES[page]
            notice = (
                f'{BEGIN}\n<aside class="skill-evidence-note"><strong>1.21.1 build status:</strong> '
                f'<code>{html.escape(registry_id)}</code> is packaged in Mysticism 2.1.2, the release selected by the TSR pack. '
                'Spawn lists and terrain notes below retain their upstream reference context.</aside>\n'
                f'{END}'
            )
            text = re.sub(r"</section>", "</section>\n\n" + notice, text, count=1)
        text = re.sub(r"[ \t]+(?=\r?$)", "", text, flags=re.M)
        outputs[page] = text.rstrip() + "\n"
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for page, content in generate().items():
        destination = DOCS / page
        if args.check:
            if destination.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale biome reference: {page}")
        else:
            destination.write_text(content, encoding="utf-8", newline="\n")
    print(f'Biome reference pages {"checked" if args.check else "polished"}: {len(generate())}')


if __name__ == "__main__":
    main()
