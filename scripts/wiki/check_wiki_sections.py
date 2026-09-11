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
    prefixed_titles = [heading.get_text(' ', strip=True) for heading in page.select('.reference-card h2') if '/' in heading.get_text()]
    assert not prefixed_titles, f'Upstream namespace leaked into {section} card titles: {prefixed_titles}'
media_overrides = json.loads((ROOT / 'data/reference_card_media.json').read_text(encoding='utf-8'))
for local_page, asset in media_overrides.items():
    if isinstance(asset, dict):
        asset = asset['asset']
    asset_path = ROOT / 'docs' / asset
    assert asset_path.exists(), f'Missing card artwork: {asset}'
    section = Path(local_page).parts[1]
    directory = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    route = Path(local_page).stem
    matching = [
        card
        for card in directory.select('.reference-card')
        if card.select_one('a[href]') and card.select_one('a[href]').get('href', '').rstrip('/').split('/')[-1] == route
    ]
    assert len(matching) == 1, f'Missing or duplicate media override card: {local_page}'
    image = matching[0].select_one('img')
    assert image and Path(image.get('src', '')).name == asset_path.name, f'Stale card artwork: {local_page}'
    assert 'reference-' not in image.get('src', ''), f'Generic placeholder remains: {local_page}'
    article_path = site / local_page.replace('.md', '/index.html')
    article = BeautifulSoup(article_path.read_text(encoding='utf-8'), 'html.parser')
    article_image = article.select_one('.reference-overview-media img')
    assert article_image and Path(article_image.get('src', '')).name == asset_path.name, f'Stale article artwork: {local_page}'
items = BeautifulSoup((site / 'tensura-reference/items/index.html').read_text(encoding='utf-8'), 'html.parser')
broken_item_textures = {
    'adamantite-bone-golem-8562a7acd4.png',
    'hihiirokane-bone-golem-aff91127e7.png',
    'mithril-bone-golem-c6ea8016b6.png',
    'orichalcum-bone-golem-a6df50b104.png',
    'pure-magisteel-bone-golem-d502e56934.png',
}
rendered_item_images = {Path(image.get('src', '')).name for image in items.select('.reference-card-media img')}
assert broken_item_textures.isdisjoint(rendered_item_images), 'A model texture strip is still rendered as item-card artwork'
item_cards = items.select('.reference-card')
assert all(card.select_one('.reference-card-media img') for card in item_cards), 'An item card is missing artwork'
item_titles = {card.h2.get_text(' ', strip=True) for card in item_cards}
non_items = {'Items', 'Armours', 'Consumables', 'Gear', 'Learnable', 'Misc', 'Mob Drops', 'Ores', 'CargoTest'}
assert item_titles.isdisjoint(non_items), 'A collection page or debug entry is still rendered as an item card'
nightmares_item_art = {
    'nightmares-elder-essence': 'nightmares-elder-essence.webp',
    'nightmares-life-essence': 'nightmares-life-essence.webp',
    'nightmares-soul-essence': 'nightmares-soul-essence.webp',
}
for page, asset in nightmares_item_art.items():
    card = next(card for card in item_cards if card.h2.get_text(' ', strip=True).casefold() == page.removeprefix('nightmares-').replace('-', ' ').title().casefold())
    assert Path(card.select_one('.reference-card-media img')['src']).name == asset
    article = BeautifulSoup((site / f'tensura-reference/items/{page}/index.html').read_text(encoding='utf-8'), 'html.parser')
    assert Path(article.select_one('.reference-overview-media img')['src']).name == asset
item_css = (ROOT / 'docs/assets/stylesheets/extra.css').read_text(encoding='utf-8')
item_js = (ROOT / 'docs/assets/javascripts/reference.js').read_text(encoding='utf-8')
assert 'reference-item-media--inventory' in item_css
assert 'setupItemMedia' in item_js and 'reference-item-media--inventory' in item_js
mobs = BeautifulSoup((site / 'tensura-reference/mobs/index.html').read_text(encoding='utf-8'), 'html.parser')
mob_cards = mobs.select('.reference-card')
assert len(mob_cards) == 60, 'Unexpected mob directory size'
assert len({card.h2.get_text(' ', strip=True) for card in mob_cards}) == len(mob_cards), 'Duplicate mob card title'
assert all(card.select_one('.reference-card-media img') for card in mob_cards), 'A mob card is missing artwork'
misleading_mob_art = {
    'invicon-daemon-essence-135b621f1f.png',
    'invicon-beast-horn-d658a03dd4.png',
    'invicon-unicorn-horn-725a312d5e.png',
    'dwarf.png',
    'goblin.png',
}
rendered_mob_images = {Path(image.get('src', '')).name for image in mobs.select('.reference-card-media img')}
assert misleading_mob_art.isdisjoint(rendered_mob_images), 'An item icon or race portrait is still rendered as mob artwork'
mob_directory_text = mobs.get_text(' ', strip=True).casefold()
assert 'needs confirmation' not in mob_directory_text and 'mind goblin' not in mob_directory_text, 'Editorial source text leaked into mob-card summaries'
wasp = next(card for card in mobs.select('.reference-card') if card.h2.get_text(strip=True) == 'Army Wasp')
pairs = dict(zip([x.get_text(strip=True) for x in wasp.select('dt')], [x.get_text(strip=True) for x in wasp.select('dd')]))
assert pairs['Health'] == '60' and pairs['Spiritual Health'] == '120' and pairs['Armor'] == '4'
assert pairs['Minimum EP'] == '10000' and pairs['Maximum EP'] == '15000'
assert 'Flower Forest' in pairs['Biome'] and pairs['Spawn Count'] == '1-2'
from sync_mysticism_world import generate as generate_mysticism_world, load_manifest as load_mysticism_world_manifest
mysticism_world = load_mysticism_world_manifest()
mysticism_build = mysticism_world['reference_build']
pack_manifest = (ROOT / mysticism_build['pack_manifest']).read_text(encoding='utf-8')
assert mysticism_build['version'] == '2.1.2' and mysticism_build['minecraft'] == '1.21.1'
assert mysticism_build['sha1'] in pack_manifest and 'file-id = 8379529' in pack_manifest, 'Mysticism pack selection changed'
for local_page, expected_content in generate_mysticism_world().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale page: {local_page}'
biomes = BeautifulSoup((site / 'tensura-reference/biomes/index.html').read_text(encoding='utf-8'), 'html.parser')
biome_cards = biomes.select('.reference-card')
biome_titles = [card.h2.get_text(' ', strip=True) for card in biome_cards]
assert len(biome_cards) == 12 and len(set(biome_titles)) == len(biome_titles), 'Unexpected biome directory size or duplicate title'
assert 'Kamui Biome' in biome_titles and 'Structures and Biomes' not in biome_titles, 'Biome catalogue includes a collection page or omits Kamui'
assert all(card.select_one('.reference-card-media img') for card in biome_cards), 'A biome card is missing artwork'
assert all('placeholder' not in Path(image.get('src', '')).name.casefold() for image in biomes.select('.reference-card-media img')), 'A biome card uses placeholder artwork'
kamui = next(card for card in biome_cards if card.h2.get_text(' ', strip=True) == 'Kamui Biome')
assert Path(kamui.select_one('.reference-card-media img')['src']).name == 'kamui-biome.webp'
kamui_pairs = dict(zip([x.get_text(strip=True) for x in kamui.select('dt')], [x.get_text(strip=True) for x in kamui.select('dd')]))
assert kamui_pairs['Registry ID'] == 'mysticism:kamui_biome' and kamui_pairs['Natural spawns'] == 'None'
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
    assert card.select_one('.skill-reference-status'), 'Missing version notice'
    if record.get('media_asset'):
        asset = ROOT / 'docs' / record['media_asset']
        assert asset.exists(), f'Missing Nightmares artwork: {record["media_asset"]}'
        image = card.select_one('img')
        assert image and Path(image.get('src', '')).name == asset.name, 'Missing Nightmares card artwork'
    else:
        assert not card.select('img'), 'Unexpected unverified Nightmares artwork'
    card_pairs = dict(zip([x.get_text(strip=True) for x in card.select('dt')], [x.get_text(strip=True) for x in card.select('dd')]))
    assert card_pairs == dict(list(record['stats'].items())[:8]), 'Stale release stat card'
    article = BeautifulSoup((site / record['local_page'].replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
    assert record['registry_id'] in article.get_text() and article.select('details summary'), 'Missing identity or expandable source panel'
    if record.get('media_asset'):
        image = article.select_one('.reference-overview-media img')
        assert image and Path(image.get('src', '')).name == Path(record['media_asset']).name, 'Missing Nightmares article artwork'
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
print('Wiki section checks passed: 11 navigation sections, populated directories, corrected item, mob, and biome media, source-backed stats, command notices, and race configurations')
