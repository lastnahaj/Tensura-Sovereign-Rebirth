"""Render implementation-verified add-on blocks into the shared Blocks directory."""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data/block_reference.json"

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
WIP_LIST_ITEM = re.compile(r"<li>[^<]*(?:\([^)]*WIP[^)]*\)|\bWIP\b)[^<]*</li>", re.IGNORECASE)

IMPORTED_SUMMARIES = {
    "blocks.md": "A source catalogue of Tensura: Reincarnated building materials, ores, workstations, resource blocks, and special-purpose blocks.",
    "blocks-charybdis-core.md": "A boss-summoning core found in Charybdis Cave that must absorb 100,000 EP from nearby kills before activation.",
    "blocks-kiln.md": "A processing station that melts Magic Ore Shards into Molten Magisteel and refines that material into ingots.",
    "blocks-magic-engine.md": "A switchable block family that reduces area Magicules while enabled; crafted around a High Quality Magic Crystal and Pure Magisteel.",
    "blocks-smithing-bench.md": "The workstation used to craft Tensura armor, weapons, tools, and other schematic-gated equipment.",
}

MAGIC_ENGINE_NOTE = '''<!-- block-verification:start -->
!!! info "Verified 1.21.1 behavior"
    The pinned `MagicEngineBlock` implementation toggles an area-Magicule reduction modifier when used. It is functional, not just decoration. The tracked configuration sets a **1,000 area-Magicule reduction** and **16-block range** for ordinary engines. This is area Magicules, not a direct deduction from a player's MP.

    Values come from [the tracked area configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/area_magicule_config.toml) and Tensura 2.0.1.2's `MagicEngineBlock` and `MagicEngineHelper`. Mob-spawn suppression depends on the resulting area level and spawn threshold; it is not a blanket guarantee of safety. These are artifact/configuration checks, not a live-server test.
<!-- block-verification:end -->'''

SMITHING_NOTE = '''<!-- block-verification:start -->
!!! note "Recipe coverage"
    The imported catalogue lists some set names without full recipes. Those names are preserved for reference, not treated as verified crafting instructions or proof of availability in this pack. Check the in-game recipe browser before gathering materials for an undocumented set.
<!-- block-verification:end -->'''


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
        source_media = bool(page.get("media_source_url"))
        illustration = page.get("artwork_kind") == "original-illustration"
        media_caption = (
            f'<a href="{page["media_source_url"]}">{html.escape(page["media_credit"])}</a>'
            if source_media else "TSR block illustration" if illustration else "TSR reference symbol"
        )
        media_alt = f'{title} source reference' if source_media else f'{title} illustration' if illustration else f'{title} reference symbol'
        lines = [
            "---", f"title: {json.dumps(title)}", f"description: {json.dumps(page['summary'])}", "---", "", f"# {title}", "",
            f'<span class="reference-badge">{html.escape(build["label"])} reference</span> <span class="reference-category">Blocks</span>', "",
            '<section class="reference-overview reference-theme-world">',
            '<figure class="reference-overview-media reference-overview-media--source">',
            f'<img src="../../../{page["asset"]}" alt="{html.escape(media_alt)}" loading="eager" decoding="async">',
            f'<figcaption>{media_caption}</figcaption>', '</figure>',
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
            *(['## Source and licensing', ''] if page.get('source_article_url') else []),
            '??? info "Sources and verification"', '', f'    [{build["label"]} {build["version"]} release]({build["source_url"]})', '',
        ])
        if build.get("pack_manifest"):
            lines[-2] = lines[-2] + f' · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]})'
        digest_label = "SHA-1" if build.get("sha1") else "SHA-256"
        digest = build.get("sha1") or build["sha256"]
        lines.extend([f'    Artifact {digest_label}: `{digest}`.', ''])
        if page.get("source_article_url"):
            lines.extend([
                f'    Upstream article: [TR Mysticism Wiki revision {page["source_revision"]}]({page["source_article_url"]}?oldid={page["source_revision"]}). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).',
                '',
            ])
        lines.extend(['    Packaged implementation evidence:', ''])
        lines.extend(f'    - `{path}`' for path in page['evidence_paths'])
        if not source_media:
            credit = 'The illustration on this page is original TSR artwork; it is not the in-game texture.' if illustration else 'The symbol on this page is original TSR interface art; it is not presented as an in-game texture.'
            lines.extend(['', '    ' + credit])
        back_link = "../../tensura-reference/blocks/index.md" if page.get("catalogue_entry") is False else "index.md"
        lines.extend(['', f'[Back to Blocks]({back_link})', ''])
        result[page['local_page']] = "\n".join(lines)
    return result


def records():
    manifest = load_manifest()
    builds = manifest['reference_builds']
    rendered = generate()
    result = []
    for page in manifest['pages']:
        if page.get('catalogue_entry') is False:
            continue
        build = builds[page['source_key']]
        result.append({
            **page, "source_title": page['display_title'], "source_url": build['source_url'], "category": "blocks",
            "reference_build_only": not build['installed_version_verified'], "_supplementary": True, "_html": rendered[page['local_page']],
            "_primary_media": {"local_path": page['asset'], "kind": "emblem"},
            "_stat_source_note": (f'Pinned {build["label"]} {build["version"]} artifact.' if build['installed_version_verified'] else 'Reference release; server build match pending.'),
        })
    return result


def clean_imported_text(text: str, path: Path) -> str:
    """Remove source-wiki maintenance copy from imported block articles."""
    text = WIP_BANNER.sub("", text)
    text = WIP_TAG.sub("", text)
    text = WIP_CREDIT.sub("", text)
    text = WIP_LIST_ITEM.sub(lambda match: re.sub(r'\s*\([^)]*WIP[^)]*\)|\bWIP\b', '', match[0], flags=re.IGNORECASE), text)
    text = text.replace("Click to show more", "")
    text = re.sub(r"<ul>\s*</ul>", "", text, flags=re.IGNORECASE)
    notes = {'blocks-magic-engine.md': MAGIC_ENGINE_NOTE, 'blocks-smithing-bench.md': SMITHING_NOTE}
    if path.name in notes:
        text = re.sub(r'<!-- block-verification:start -->.*?<!-- block-verification:end -->\s*', '', text, flags=re.DOTALL)
        text = text.replace('<div class="tensura-reference-article">', notes[path.name] + '\n\n<div class="tensura-reference-article">', 1)
    summary = IMPORTED_SUMMARIES.get(path.name)
    if summary:
        text = re.sub(r"(?m)^description:.*$", f"description: {json.dumps(summary)}", text, count=1)
        text = re.sub(
            r'(<p class="reference-eyebrow">At a glance</p>\s*)<p>.*?</p>',
            rf'\1<p>{html.escape(summary)}</p>',
            text,
            count=1,
            flags=re.DOTALL,
        )
    return text


def imported_paths() -> list[Path]:
    return sorted((ROOT / "docs/tensura-reference/blocks").glob("*.md"))


def sanitize_imported(*, check: bool) -> list[Path]:
    changed = []
    generated = {ROOT / "docs" / name for name in generate()}
    for path in imported_paths():
        if path in generated:
            continue
        original = path.read_text(encoding="utf-8")
        cleaned = clean_imported_text(original, path)
        if cleaned == original:
            continue
        changed.append(path)
        if not check:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
    return changed


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
    dirty_imports = sanitize_imported(check=args.check)
    if dirty_imports and args.check:
        raise SystemExit("Stale imported block cleanup: " + ", ".join(str(path.relative_to(ROOT)) for path in dirty_imports[:10]))
    print(f'Block reference pages {"checked" if args.check else "generated"}: {len(pages)}')


if __name__ == '__main__':
    main()
