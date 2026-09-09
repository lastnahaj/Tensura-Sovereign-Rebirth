"""Export reviewed registry identities without including artifact bytecode."""
from __future__ import annotations

import json
import tomllib
from pathlib import Path

from race_catalogue import PARTITION_BY_PAGE, RACE_GUIDES
from audit_race_inventory import BUILDS

ROOT = Path(__file__).resolve().parents[2]
CONFIG_FAMILIES = {'daemon': 'Lesser Daemon', 'vampire': 'Ghoul', 'daemon_doll': 'Greater Doll', 'angel': 'Lesser Angel', 'elemental': 'Lesser Elemental', 'wyrm': 'Attuned Wyrm', 'sculk': 'Sculk Worm', 'special_direwolf': 'Direwolf'}


def main():
    audit = json.loads((ROOT / '.build/race-inventory-audit.json').read_text(encoding='utf-8'))
    result = {'schema': 1, 'minecraft': '1.21.1', 'builds': {}, 'pages': {}}
    for source, inventory in audit.items():
        if inventory['build']['sha1'] != BUILDS[source]['sha1']:
            raise ValueError(f'Unexpected registry audit artifact: {source}')
        result['builds'][source] = {key: inventory['build'][key] for key in ('version', 'sha1', 'source_url')}
        for page in inventory['pages']:
            status = 'registered' if page['registry_id'] else 'unmatched'
            if page['local_page'] in RACE_GUIDES:
                status = 'guide'
            if page['registry_id'] == 'mysticism:insect':
                status = 'incomplete'
            family = None
            configuration = None
            if page['registry_id']:
                configs = inventory['implementation_review'][page['registry_id']]['config']
                if len(configs) != 1:
                    raise ValueError(f'Ambiguous race configuration: {page["registry_id"]}')
                stem = Path(configs[0]['path']).stem.removesuffix('_config')
                family = PARTITION_BY_PAGE.get(page['local_page']) or CONFIG_FAMILIES.get(stem, stem.replace('_', ' ').title())
                config = configs[0]
                values = tomllib.loads((ROOT / config['path']).read_text(encoding='utf-8'))[config['section']]
                configuration = {'path': config['path'], 'section': config['section'], 'values': values}
            result['pages'][page['local_page']] = {'status': status, 'registry_id': page['registry_id'], 'title': page['title'], 'family': family, 'source': source, 'source_url': page['source_url'], 'revision_id': page['revision_id']}
            if configuration:
                result['pages'][page['local_page']]['configuration'] = configuration
    (ROOT / 'data/race_reference.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('Race reference export: ' + ', '.join(f'{status}={sum(page["status"] == status for page in result["pages"].values())}' for status in ('registered', 'unmatched', 'guide', 'incomplete')))


if __name__ == '__main__':
    main()
