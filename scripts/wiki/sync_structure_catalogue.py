"""Render artifact-verified structures into the shared Structures directory."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data/structure_reference.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def generate():
    manifest = load_manifest()
    builds = manifest["reference_builds"]
    result = {}
    for page in manifest["pages"]:
        build = builds[page["source_key"]]
        title = page["display_title"]
        stats = {
            "Source": f'{build["label"]} {build["version"]}',
            "Registry ID": page["registry_id"],
            "Placement": "Random spread",
            "Spacing": page["spacing"],
            "Separation": page["separation"],
            "Biomes": page["biomes"],
        }
        if page.get("variants"):
            stats["Variants"] = page["variants"]
        lines = [
            "---",
            f"title: {json.dumps(title)}",
            f"description: {json.dumps(page['summary'])}",
            "---",
            "",
            f"# {title}",
            "",
            f'<span class="reference-badge">{html.escape(build["label"])} reference</span> <span class="reference-category">Structures</span>',
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
            '<a href="#where-it-appears">Where it appears</a>',
            '<a href="#what-this-reference-confirms">What is verified</a>',
            '</nav>',
            '</div>',
            '</section>',
            '',
            '!!! info "Pinned Minecraft 1.21.1 build"',
            '',
            f'    Verified against **{build["label"]} {build["version"]}** selected by the TSR pack manifest. This confirms packaged registration and placement data, not a live-server discovery rate.',
            '',
            '<div class="tensura-reference-article">',
            '<div class="druid-container reference-release-stats"><aside class="druid-infobox">',
            f'<div class="druid-title">{html.escape(title)}</div>',
        ]
        for label, value in stats.items():
            lines.append(f'<div class="druid-row"><div class="druid-label">{html.escape(label)}</div><div class="druid-data">{html.escape(value)}</div></div>')
        lines.extend([
            '</aside></div></div>',
            '',
            '## Where it appears',
            '',
            page["details"][0],
            '',
            '## What this reference confirms',
            '',
        ])
        for paragraph in page["details"][1:]:
            lines.extend([paragraph, ''])
        lines.extend([
            'The structure, structure set, and applicable biome tag are present in the pinned artifact. Server configuration, pregenerated terrain, or an existing world border can still affect what players encounter.',
            '',
            '??? info "Sources and verification"',
            '',
            f'    [{build["label"]} {build["version"]} release]({build["source_url"]}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]})',
            '',
            f'    Artifact SHA-1: `{build["sha1"]}`.',
            '',
            '    Packaged registry evidence:',
            '',
        ])
        for name in page["evidence_paths"]:
            lines.append(f'    - `{name}`')
        lines.extend([
            '',
            '    Original TSR environment artwork is used because no verified in-game screenshot is packaged with this reference.',
            '',
            '[Back to Structures](index.md)',
            '',
        ])
        result[page["local_page"]] = "\n".join(lines)
    return result


def records():
    manifest = load_manifest()
    builds = manifest["reference_builds"]
    rendered = generate()
    result = []
    for page in manifest["pages"]:
        build = builds[page["source_key"]]
        result.append({
            **page,
            "source_title": page["display_title"],
            "source_url": build["source_url"],
            "category": "structures",
            "_supplementary": True,
            "_html": rendered[page["local_page"]],
            "_primary_media": {"local_path": page["media_asset"], "kind": "original"},
            "_stat_source_note": f'{build["label"]} {build["version"]} artifact; server terrain may differ.',
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
                raise SystemExit(f"Stale structure reference page: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f'Structure reference pages {"checked" if args.check else "generated"}: {len(pages)}')


if __name__ == "__main__":
    main()
