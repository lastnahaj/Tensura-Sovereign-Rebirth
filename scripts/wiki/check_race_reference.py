"""Check registry-scoped race recommendations, hidden imports, and family maps."""
import argparse
import json
from pathlib import Path

from bs4 import BeautifulSoup
from race_catalogue import race_reference
from sync_race_reference import generate

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    policy = race_reference()
    errors = []
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
