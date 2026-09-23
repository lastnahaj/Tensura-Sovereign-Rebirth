"""Refresh curated race portraits with per-file provenance and license checks."""
from collections import Counter
import hashlib
import json

from sync_tensura_wiki import (
    ROOT, ApiClient, fetch_media_metadata, prepare_media,
    verify_file_page_license, write_json,
)

PORTRAITS = {
    'Beastfolk': 'RaceBeastfolk.webp',
    'Lesser Daemon': 'RaceDaemon.webp',
    'Dwarf': 'RaceDwarf.webp',
    'Ghoul': 'RaceGhoul.webp',
    'Giant': 'RaceGiant.webp',
    'Goblin': 'RaceGoblin.webp',
    'Harpy': 'RaceHarpy.webp',
    'Ogre': 'RaceOgre.webp',
    'Wight': 'RaceWight.webp',
}


def main():
    client = ApiClient(ROOT / '.build/race-portraits', refresh=True)
    records = fetch_media_metadata(client, list(PORTRAITS.values()))
    by_title = {record['source_title']: record for record in records}
    if set(by_title) != set(PORTRAITS.values()):
        raise ValueError('The curated portrait inventory did not resolve completely')
    imported = []
    overrides_path = ROOT / 'data/race_family_media.json'
    overrides = json.loads(overrides_path.read_text(encoding='utf-8'))
    for family, title in PORTRAITS.items():
        record = by_title[title]
        license_info = verify_file_page_license(client, [record])
        slug = family.casefold().replace(' ', '-')
        placements = [
            {'category': 'races', 'image_titles': [title], 'local_page': page}
            for page in (f'tensura-reference/races/races-{slug}.md',
                         f'tensura-reference/races/families/{slug}.md')
        ]
        result, _, _ = prepare_media(client, [record], placements, license_info)
        record = result[0]
        if record['import_status'] != 'imported':
            raise ValueError(f'Portrait import failed: {title}')
        content = (ROOT / 'docs' / record['local_path']).read_bytes()
        if hashlib.sha1(content).hexdigest() != record['sha1']:
            raise ValueError(f'Portrait checksum mismatch: {title}')
        overrides[family] = record['local_path']
        imported.append(record)
        print(f'Verified {family}: {title}', flush=True)
    manifest_path = ROOT / 'data/upstream_tensura_media.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    previous = {record['source_title']: record for record in manifest['media']}
    added = sum(record['source_title'] not in previous for record in imported)
    previous.update({record['source_title']: record for record in imported})
    manifest['media'] = list(previous.values())
    write_json(manifest_path, manifest)
    write_json(overrides_path, overrides)
    coverage_path = ROOT / 'data/upstream_tensura_coverage.json'
    coverage = json.loads(coverage_path.read_text(encoding='utf-8'))
    counts = Counter(record['import_status'] for record in manifest['media'])
    coverage['images_discovered'] += added
    coverage['image_file_records_resolved'] = len(manifest['media'])
    coverage['images_imported'] = counts['imported']
    coverage['images_failed'] = counts['failed']
    coverage['images_skipped_due_to_licensing'] = counts['skipped-license']
    coverage['media_statuses'] = dict(sorted(counts.items()))
    coverage['media_categories'] = dict(sorted(Counter(record['category'] for record in manifest['media']).items()))
    write_json(coverage_path, coverage)


if __name__ == '__main__':
    main()
