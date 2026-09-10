"""Check encyclopedia navigation and rendered stat-card coverage."""
import json
from pathlib import Path
import tomllib

from bs4 import BeautifulSoup
import yaml

ROOT = Path(__file__).resolve().parents[2]
expected = ['Main page', 'Abilities', 'Races', 'Items', 'Blocks', 'Mobs', 'Biomes', 'Structures', 'Config', 'Commands', 'Mechanics']
nav = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))['nav']
assert [next(iter(item)) for item in nav] == expected, 'Unexpected top-level wiki navigation'
site = ROOT / 'site'
home = BeautifulSoup((site / 'index.html').read_text(encoding='utf-8'), 'html.parser')
assert [link.get_text(' ', strip=True) for link in home.select('.md-tabs__link')] == expected
for section in ('items', 'blocks', 'mobs', 'biomes', 'structures', 'bosses'):
    page = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    assert page.select('.reference-card'), f'Empty directory: {section}'
media_overrides = json.loads((ROOT / 'data/reference_card_media.json').read_text(encoding='utf-8'))
for local_page, asset in media_overrides.items():
    asset_path = ROOT / 'docs' / asset
    assert asset_path.exists(), f'Missing card artwork: {asset}'
    section = Path(local_page).parts[1]
    directory = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    route = Path(local_page).stem + '/'
    matching = [
        card
        for card in directory.select('.reference-card')
        if card.select_one('a[href]') and card.select_one('a[href]').get('href', '').endswith(route)
    ]
    assert len(matching) == 1, f'Missing or duplicate media override card: {local_page}'
    image = matching[0].select_one('img')
    assert image and Path(image.get('src', '')).name == asset_path.name, f'Stale card artwork: {local_page}'
    assert 'reference-' not in image.get('src', ''), f'Generic placeholder remains: {local_page}'
    article_path = site / local_page.replace('.md', '/index.html')
    article = BeautifulSoup(article_path.read_text(encoding='utf-8'), 'html.parser')
    article_image = article.select_one('.reference-overview-media img')
    assert article_image and Path(article_image.get('src', '')).name == asset_path.name, f'Stale article artwork: {local_page}'
mobs = BeautifulSoup((site / 'tensura-reference/mobs/index.html').read_text(encoding='utf-8'), 'html.parser')
wasp = next(card for card in mobs.select('.reference-card') if card.h2.get_text(strip=True) == 'Army Wasp')
pairs = dict(zip([x.get_text(strip=True) for x in wasp.select('dt')], [x.get_text(strip=True) for x in wasp.select('dd')]))
assert pairs['Health'] == '60' and pairs['Spiritual Health'] == '120' and pairs['Armor'] == '4'
assert pairs['Minimum EP'] == '10000' and pairs['Maximum EP'] == '15000'
assert 'Flower Forest' in pairs['Biome'] and pairs['Spawn Count'] == '1-2'
commands = (site / 'tensura-reference/commands/index.html').read_text(encoding='utf-8')
assert 'Commands by Source' in commands and 'historical reference' in commands
assert 'Tensura Nightmares' in commands and 'oldid=378' in commands
from sync_nightmares_world import generate as generate_nightmares_world, load_manifest
world = load_manifest()
assert world['reference_build']['installed_version_verified'] is False
for local_page, expected_content in generate_nightmares_world().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale page: {local_page}'
for record in world['pages']:
    directory = BeautifulSoup((site / f'tensura-reference/{record["category"]}/index.html').read_text(encoding='utf-8'), 'html.parser')
    matching = [card for card in directory.select('.reference-card') if card.h2.get_text(strip=True) == record['display_title']]
    assert len(matching) == 1, f'Missing or duplicate Nightmares card: {record["display_title"]}'
    card = matching[0]
    assert card.select_one('.skill-reference-status') and not card.select('img'), 'Missing version notice or placeholder image'
    card_pairs = dict(zip([x.get_text(strip=True) for x in card.select('dt')], [x.get_text(strip=True) for x in card.select('dd')]))
    assert card_pairs == dict(list(record['stats'].items())[:8]), 'Stale release stat card'
    article = BeautifulSoup((site / record['local_page'].replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
    assert record['registry_id'] in article.get_text() and article.select('details summary'), 'Missing identity or expandable source panel'
    article_pairs = dict(zip([x.get_text(strip=True) for x in article.select('.druid-label')], [x.get_text(strip=True) for x in article.select('.druid-data')]))
    assert article_pairs == record['stats'], 'Stale rendered reference stats'
    if record['category'] == 'bosses':
        spawn_section = next(section for section in record['sections'] if section['title'] == 'Finding the boss')
        for paragraph in spawn_section['paragraphs']:
            assert paragraph in article.get_text(' ', strip=True), 'Missing boss spawn guidance'
policy = json.loads((ROOT / 'data/race_reference.json').read_text(encoding='utf-8'))
for page, decision in policy['pages'].items():
    if decision['status'] != 'registered':
        continue
    config = decision['configuration']
    actual = tomllib.loads((ROOT / config['path']).read_text(encoding='utf-8'))[config['section']]
    assert config['values'] == actual, f'Stale recorded configuration: {page}'
print('Wiki section checks passed: 11 navigation sections, populated directories, Army Wasp stat card, command source notices, and recorded race configurations')
