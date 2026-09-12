"""Render implementation-verified add-on blocks into the shared Blocks directory."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data/block_reference.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def generate():
    manifest = load_manifest()
    builds = manifest["reference_builds"]
    result = {}
    for page in manifest["pages"]:
        build = builds[page["source_key"]]
        title = page["display_title"]
        confirmed = build["installed_version_verified"]
        notice = "Pinned Minecraft 1.21.1 build" if confirmed else "1.21.1 reference — server build match pending"
        notice_kind = "info" if confirmed else "warning"
        status_text = (
            f'Verified against **{build["label"]} {build["version"]}** selected by the TSR pack manifest.'
            if confirmed else
            f'Verified against **{build["label"]} {build["version"]}** as a reference artifact. The server\'s exact Nightmares release has not been confirmed.'
        )
        lines = [
            "---", f"title: {json.dumps(title)}", f"description: {json.dumps(page['summary'])}", "---", "", f"# {title}", "",
            f'<span class="reference-badge">{html.escape(build["label"])} reference</span> <span class="reference-category">Blocks</span>', "",
            '<section class="reference-overview reference-theme-world">',
            '<figure class="reference-overview-media reference-overview-media--source">',
            f'<img src="../../../{page["asset"]}" alt="{html.escape(title)} reference symbol" loading="eager" decoding="async">',
            '<figcaption>TSR reference symbol</figcaption>', '</figure>',
            '<div class="reference-overview-copy">', '<p class="reference-eyebrow">At a glance</p>', f'<p>{html.escape(page["summary"])}</p>',
            '<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>',
            '</div>', '</section>', '', f'!!! {notice_kind} "{notice}"', '', f'    {status_text}', '',
            '<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">',
            f'<div class="druid-title">{html.escape(title)}</div>',
        ]
        stats = {"Source": f'{build["label"]} {build["version"]}', "Registry ID": page["registry_id"], "Role": page["role"], "Visual": page["visual"], "Player access": page["access"]}
        for label, value in stats.items():
            lines.append(f'<div class="druid-row"><div class="druid-label">{html.escape(label)}</div><div class="druid-data">{html.escape(value)}</div></div>')
        lines.extend([
            '</aside></div></div>', '', '## What it does', '', page['details'][0], '', '## Player access', '', page['details'][1], '',
            '??? info "Sources and verification"', '', f'    [{build["label"]} {build["version"]} release]({build["source_url"]})', '',
        ])
        if build.get("pack_manifest"):
            lines[-2] = lines[-2] + f' · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]})'
        digest_label = "SHA-1" if build.get("sha1") else "SHA-256"
        digest = build.get("sha1") or build["sha256"]
        lines.extend([f'    Artifact {digest_label}: `{digest}`.', '', '    Packaged implementation evidence:', ''])
        lines.extend(f'    - `{path}`' for path in page['evidence_paths'])
        lines.extend(['', '    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.', '', '[Back to Blocks](index.md)', ''])
        result[page['local_page']] = "\n".join(lines)
    return result


def records():
    manifest = load_manifest()
    builds = manifest['reference_builds']
    rendered = generate()
    result = []
    for page in manifest['pages']:
        build = builds[page['source_key']]
        result.append({
            **page, "source_title": page['display_title'], "source_url": build['source_url'], "category": "blocks",
            "reference_build_only": not build['installed_version_verified'], "_supplementary": True, "_html": rendered[page['local_page']],
            "_primary_media": {"local_path": page['asset'], "kind": "emblem"},
            "_stat_source_note": (f'Pinned {build["label"]} {build["version"]} artifact.' if build['installed_version_verified'] else 'Reference release; server build match pending.'),
        })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    pages = generate()
    for name, content in pages.items():
        path = ROOT / 'docs' / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Stale block reference page: {name}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    print(f'Block reference pages {"checked" if args.check else "generated"}: {len(pages)}')


if __name__ == '__main__':
    main()
