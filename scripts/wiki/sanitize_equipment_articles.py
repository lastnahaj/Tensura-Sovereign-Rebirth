"""Remove upstream maintenance artwork from player-facing equipment articles."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFERENCE_ROOT = ROOT / "docs" / "tensura-reference"
EQUIPMENT_SECTIONS = ("items", "weapons", "armor", "tools")

WIP_BANNER = re.compile(
    r"<div>\s*<table\b[^>]*>\s*<tbody>\s*<tr>\s*"
    r"<td>\s*<a\b[^>]*(?:File:WIP\d*\.png|File:Work[_ ]In[_ ]Progress)[^>]*>"
    r".*?</table>\s*</div>\s*",
    flags=re.IGNORECASE | re.DOTALL,
)
WIP_TAG = re.compile(r"(?m)^- Work_in_Progress\s*\r?\n")
WIP_CREDIT = re.compile(
    r"(?im)^<li><a\b[^>]*(?:File:WIP\d*\.png|File:Work[_ ]In[_ ]Progress)[^>]*>"
    r".*?</li>\s*\r?\n?"
)
THIN_WIP_COPY = re.compile(
    r"This page is a Work In Progress!!!(?: Big Things Coming Soon!!)?",
    flags=re.IGNORECASE,
)
SOURCE_GAP_COPY = "The upstream reference does not yet document this item's obtainment or use."
EXPLORER_SUMMARY = (
    "Master-level Dwarf Cartographers can offer maps to Hell Gates for 5–15 Gold Coins "
    "or Charybdis Caves for 5–25 Gold Coins."
)
EXPLORER_BODY = re.compile(
    r"Master level <a class=\"text\" href=\"\.\./\.\./mobs/mobs-dwarf/\">Dwarf Cartographer</a>"
    r" have a chance to have a .*?</p>",
    flags=re.IGNORECASE | re.DOTALL,
)
EXPLORER_RELATED = re.compile(
    r"Master level Dwarf Cartographer have a chance to have a Hell Gate Explorer Map or a "
    r"Labyrinth Explorer Map as an…",
    flags=re.IGNORECASE,
)
EXPLORER_IMAGE = re.compile(
    r"\.\./\.\./\.\./assets/upstream/tensura/items/invicon-labyrinth-explorer-map-[a-f0-9]+\.png",
    flags=re.IGNORECASE,
)
LEGACY_MAP_CELLS = re.compile(
    r"<td><span class=\"nowrap\"><span class=\"sprite-file\"><a href=\"\.\./explorer-maps/\" "
    r"title=\"Labyrinth Explorer Map\"></a></span>.*?</td>\s*"
    r"<td></td>\s*<td></td>\s*",
    flags=re.IGNORECASE | re.DOTALL,
)
LEGACY_MAP_CREDIT = re.compile(
    r"(?im)^<li><a\b[^>]*File:Invicon_Labyrinth_Explorer_Map\.png[^>]*>.*?</li>\s*\r?\n?"
)


def clean_text(text: str, path: Path | None = None) -> str:
    """Strip non-content maintenance banners while preserving article material."""
    text = WIP_BANNER.sub("", text)
    text = WIP_TAG.sub("", text)
    text = WIP_CREDIT.sub("", text)
    text = THIN_WIP_COPY.sub(SOURCE_GAP_COPY, text)
    text = EXPLORER_RELATED.sub(EXPLORER_SUMMARY, text)
    text = EXPLORER_IMAGE.sub("../../../assets/images/items/explorer-map.svg", text)
    text = LEGACY_MAP_CELLS.sub("", text)
    text = LEGACY_MAP_CREDIT.sub("", text)
    if path and path.name == "explorer-maps.md":
        text = re.sub(r"(?m)^- Labyrinth Explorer Map\s*\r?\n", "- Charybdis Cave Explorer Map\n", text)
        text = re.sub(
            r"\*\*Also known as:\*\* Hell Gate Explorer Map, Labyrinth Explorer Map",
            "**Also known as:** Hell Gate Explorer Map, Charybdis Cave Explorer Map",
            text,
        )
        text = EXPLORER_BODY.sub(f"{EXPLORER_SUMMARY}</p>", text)
    return text


def article_paths() -> list[Path]:
    return sorted(
        path
        for section in EQUIPMENT_SECTIONS
        for path in (REFERENCE_ROOT / section).glob("*.md")
    )


def run(*, check: bool) -> tuple[int, list[Path]]:
    changed: list[Path] = []
    for path in article_paths():
        original = path.read_text(encoding="utf-8")
        cleaned = clean_text(original, path)
        if cleaned == original:
            continue
        changed.append(path)
        if not check:
            path.write_text(cleaned, encoding="utf-8")
    return len(article_paths()), changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if any equipment article still needs sanitizing.",
    )
    args = parser.parse_args()
    total, changed = run(check=args.check)
    if changed:
        action = "need cleanup" if args.check else "cleaned"
        print(f"{len(changed)} of {total} equipment articles {action}")
        if args.check:
            for path in changed[:20]:
                print(path.relative_to(ROOT))
            return 1
    else:
        print(f"All {total} equipment articles are clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
