"""Check registry-scoped race recommendations, hidden imports, and family maps."""
import argparse
import hashlib
import json
from pathlib import Path

from bs4 import BeautifulSoup
from race_catalogue import race_reference
from sync_race_reference import generate, replace_placeholder_figure
from refresh_race_portraits import PORTRAITS

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    policy = race_reference()
    errors = []
    # Item links later in an article must never extend the portrait replacement.
    tail = '<section><a href="../../items/dragon-essence/">Evolution requirement</a></section><figure class="embedvideo">Video</figure>'
    retained = '<figure class="reference-overview-media"><img src="../../../assets/upstream/tensura/mobs/lizardman.png"></figure>'
    args_media = ('tensura-reference/races/races-lizardman.md', {'title': 'Lizardman'}, 'assets/images/races/example.svg', {})
    if replace_placeholder_figure(retained + tail, *args_media) != retained + tail:
        errors.append('Portrait replacement changes a valid source figure or subsequent article content')
    placeholder = '<figure class="reference-overview-media">Original TSR section artwork</figure>'
    if not replace_placeholder_figure(placeholder + tail, *args_media).endswith(tail):
        errors.append('Portrait replacement removes content after the first figure')
    outputs = generate()
    source_pages = {record['local_page'] for source in ('tensura', 'mysticism') for record in json.loads((ROOT / f'data/upstream_{source}_pages.json').read_text(encoding='utf-8'))['pages'] if record['category'] == 'races'}
    if set(policy['pages']) != source_pages:
        errors.append('Race registry policy must cover every imported race article')
    active_ids = []
    for page, decision in policy['pages'].items():
        text = (ROOT / 'docs' / page).read_text(encoding='utf-8')
        if outputs[page] != text:
            errors.append(f'Stale race status: {page}')
        if decision['status'] == 'registered':
            active_ids.append(decision['registry_id'])
        elif 'search:\n  exclude: true' not in text or 'Reference status' not in text:
            errors.append(f'Unverified race lacks status or search exclusion: {page}')
    if len(active_ids) != len(set(active_ids)):
        errors.append('Duplicate registered race identities')
    families = json.loads((ROOT / 'docs/assets/data/race-families.json').read_text(encoding='utf-8'))
    overrides = json.loads((ROOT / 'data/race_family_media.json').read_text(encoding='utf-8'))
    media = {entry['source_title']: entry for entry in json.loads((ROOT / 'data/upstream_tensura_media.json').read_text(encoding='utf-8'))['media']}
    for family, title in PORTRAITS.items():
        record = media.get(title, {})
        asset = record.get('local_path')
        if not asset or overrides.get(family) != asset or not record.get('license'):
            errors.append(f'Missing curated portrait or credit: {family}')
            continue
        image = ROOT / 'docs' / asset
        if not image.is_file() or hashlib.sha1(image.read_bytes()).hexdigest() != record.get('sha1'):
            errors.append(f'Portrait checksum mismatch: {family}')
        slug = family.casefold().replace(' ', '-')
        article = BeautifulSoup((ROOT / f'docs/tensura-reference/races/races-{slug}.md').read_text(encoding='utf-8'), 'html.parser')
        portrait = article.select_one('.reference-overview-media img')
        if not portrait or not portrait.get('src', '').endswith(asset):
            errors.append(f'Race article is not using its curated portrait: {family}')
    directory_source = (ROOT / 'docs/tensura-reference/races/index.md').read_text(encoding='utf-8')
    for family in families['families']:
        credit = next((entry for entry in media.values() if entry.get('local_path') == family['image']), None)
        if credit and credit['source_file_page'] not in directory_source:
            errors.append(f'Missing directory image attribution: {family["title"]}')
    expected = {page.removesuffix('.md') + '/' for page, decision in policy['pages'].items() if decision['status'] == 'registered'}
    if set(families['destinations']) != expected:
        errors.append('Family stages differ from registered article inventory')
    graph = json.loads((ROOT / 'docs/assets/data/progression.json').read_text(encoding='utf-8'))
    for page, decision in policy['pages'].items():
        route = page.removesuffix('.md') + '/'
        if decision['status'] != 'registered' and route in graph['nodes']:
            errors.append(f'Unverified race in progression: {page}')
    if not args.source_only:
        search = json.loads((ROOT / 'site/search/search_index.json').read_text(encoding='utf-8'))
        locations = {item['location'].split('#')[0] for item in search['docs']}
        for page, decision in policy['pages'].items():
            if decision['status'] != 'registered' and page.removesuffix('.md') + '/' in locations:
                errors.append(f'Unverified race remains searchable: {page}')
        directory = BeautifulSoup((ROOT / 'site/tensura-reference/races/index.html').read_text(encoding='utf-8'), 'html.parser')
        if len(directory.select('.reference-card')) != len(families['families']):
            errors.append('Rendered race directory count differs')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Race scope checks passed: {len(active_ids)} registry-matched imported forms, {len(families["families"])} families; unmatched imports excluded')


if __name__ == '__main__':
    main()
