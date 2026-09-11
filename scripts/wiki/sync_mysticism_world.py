"""Render implementation-backed Mysticism world references into shared directories."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data/mysticism_world_reference.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def generate():
    manifest = load_manifest()
    build = manifest["reference_build"]
    result = {}
    for page in manifest["pages"]:
        title = page["display_title"]
        lines = [
            "---",
            f"title: {title}",
            f"description: {page['summary']}",
            "---",
            "",
            f"# {title}",
            "",
            '<span class="reference-badge">TR Mysticism reference</span> <span class="reference-category">Biomes</span>',
            "",
            '<section class="reference-overview reference-theme-world">',
            '<figure class="reference-overview-media reference-overview-media--theme">',
            f'<img src="../../../{page["media_asset"]}" alt="{html.escape(title)} reference artwork" loading="eager" decoding="async">',
            '<figcaption>Original TSR article artwork</figcaption>',
            '</figure>',
            '<div class="reference-overview-copy">',
            '<p class="reference-eyebrow">At a glance</p>',
            f'<p>{html.escape(page["summary"])}</p>',
            '<nav class="reference-quick-jumps" aria-label="Article sections">',
        ]
        for section in page["sections"]:
            anchor = section["title"].lower().replace(" ", "-")
            lines.append(f'<a href="#{anchor}">{html.escape(section["title"])}</a>')
        lines.extend([
            '</nav>',
            '</div>',
            '</section>',
            '',
            '!!! info "Pinned Minecraft 1.21.1 build"',
            '',
            f'    Verified against Mysticism **{build["version"]}** selected by the TSR pack manifest. This is an artifact and configuration check, not a live-server terrain test.',
            '',
            '<div class="tensura-reference-article">',
            '<div class="druid-container reference-release-stats"><aside class="druid-infobox">',
            f'<div class="druid-title">{html.escape(title)}</div>',
        ])
        for label, value in page["stats"].items():
            lines.append(f'<div class="druid-row"><div class="druid-label">{html.escape(label)}</div><div class="druid-data">{html.escape(value)}</div></div>')
        lines.extend(['</aside></div></div>', ''])
        for section in page["sections"]:
            lines.extend([f'## {section["title"]}', ''])
            for paragraph in section["paragraphs"]:
                lines.extend([paragraph, ''])
        lines.extend([
            '??? info "Sources and verification"',
            '',
            f'    [Mysticism {build["version"]} release]({build["source_url"]}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]})',
            '',
            f'    Artifact SHA-1: `{build["sha1"]}`.',
            '',
            '    Packaged registry evidence:',
            '',
        ])
        for name in page["evidence_paths"]:
            lines.append(f'    - `{name}`')
        lines.extend(['', f'    {page["media_note"]}', '', '[Back to the collection](index.md)', ''])
        result[page["local_page"]] = "\n".join(lines)
    return result


def records():
    result = []
    for page in load_manifest()["pages"]:
        result.append({
            **page,
            "_supplementary": True,
            "_html": f'<p>{html.escape(page["summary"])}</p>',
            "_primary_media": {"local_path": page["media_asset"], "kind": "original"},
            "_stat_source_note": "Pinned Mysticism 2.1.2 pack data; server settings may differ.",
        })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    pages = generate()
    for name, content in pages.items():
        path = ROOT / "docs" / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale Mysticism world page: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f'Mysticism world pages {"checked" if args.check else "generated"}: {len(pages)}')


if __name__ == "__main__":
    main()
