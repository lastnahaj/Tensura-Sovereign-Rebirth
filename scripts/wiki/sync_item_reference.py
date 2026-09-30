"""Render curated consumables and preserve unsupported source names as archives."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def manifest():
    return json.loads((ROOT / 'data/item_reference.json').read_text(encoding='utf-8'))


def apply(records):
    entries = {page['local_page']: page for page in manifest()['pages']}
    for record in records:
        page = entries.get(record['local_page'])
        if not page:
            continue
        record['display_title'] = page['display_title']
        record['_summary_override'] = page['summary']
        record['_catalogue_entry'] = page['catalogue_entry']
        record['_availability_status'] = page.get('status')
        record['_stat_source_note'] = 'Pinned Tensura 2.0.1.2 artifact; survival acquisition unverified.'
        if page.get('asset'):
            record['_primary_media'] = {'local_path': page['asset'], 'kind': 'original'}
        else:
            record['_primary_media'] = None


def generate():
    data = manifest()
    build = data['reference_build']
    sources = {
        record['local_page']: record
        for record in json.loads((ROOT / 'data/upstream_tensura_pages.json').read_text(encoding='utf-8'))['pages']
    }
    output = {}
    for page in data['pages']:
        source = sources[page['local_page']]
        title = html.escape(page['display_title'])
        lines = ['---', f'title: {json.dumps(page["display_title"])}', f'description: {json.dumps(page["summary"])}', '---', '', f'# {page["display_title"]}', '',
                 '<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>', '',
                 '<section class="reference-overview reference-theme-world' + ('' if page.get('asset') else ' reference-overview--text-only') + '">']
        if page.get('asset'):
            lines.extend(['<figure class="reference-overview-media reference-overview-media--source">',
                          f'<img src="../../../{page["asset"]}" alt="{title} illustration" loading="eager" decoding="async">',
                          '<figcaption>TSR item illustration · not the in-game texture</figcaption>', '</figure>'])
        lines.extend(['<div class="reference-overview-copy">', '<p class="reference-eyebrow">At a glance</p>', f'<p>{html.escape(page["summary"])}</p>',
                      '<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a>' + ('<a href="#how-to-use">How to use</a>' if page['catalogue_entry'] else '') + '</nav>',
                      '</div>', '</section>', ''])
        if page['catalogue_entry']:
            lines.extend([f'!!! warning "{page["status"]}"', f'    {page["warning"]}', '',
                          '<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">',
                          f'<div class="druid-title">{title}</div>',
                          f'<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">{page["registry_id"]}</div></div>',
                          f'<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura {build["version"]} · Minecraft {build["minecraft"]}</div></div>',
                          '<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Survival route not verified</div></div>', '</aside></div></div>', '',
                          '## Availability', '', page['obtainment'], '', '## How to use', '', page['use'], '', '## Behavior and limits', '', page['effects'], ''])
        else:
            lines.extend(['!!! warning "Source archive · not verified for current play"', '    This name is preserved for existing links, not recommended as an obtainable item.', '',
                          '<div class="tensura-reference-article">', '<p>This upstream article does not contain usable obtainment or effect documentation.</p>', '</div>', '',
                          '## Availability', '', page['detail'], ''])
        lines.extend(['[Return to Items](index.md)', '', '## Source and licensing', '',
                      f'Upstream reference: [{source["source_title"]}]({source["source_url"]}) on the Tensura: Reincarnated Wiki, recorded revision `{source["revision_id"]}`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The unfinished source artwork is not reproduced.', '',
                      f'Implementation check: [Tensura {build["version"]} release]({build["source_url"]}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]}). Artifact SHA-1: `{build["sha1"]}`. Registration and code checks are not live-server gameplay tests.', ''])
        if page.get('asset'):
            lines.extend(['The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.', ''])
        if page.get('evidence_paths'):
            lines.extend(['??? info "Artifact evidence"', ''])
            lines.extend(f'    - `{path}`' for path in page['evidence_paths'])
            lines.append('')
        output[page['local_page']] = '\n'.join(lines)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in generate().items():
        path = ROOT / 'docs' / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Stale item reference: {name}')
        else:
            path.write_text(content, encoding='utf-8', newline='\n')
    print('Curated item references checked' if args.check else 'Curated item references generated')


if __name__ == '__main__':
    main()
