"""Check encyclopedia navigation and rendered stat-card coverage."""
import json
import hashlib
from pathlib import Path
import tomllib
import posixpath
from urllib.parse import unquote

from bs4 import BeautifulSoup
import yaml

ROOT = Path(__file__).resolve().parents[2]
expected = ['Main page', 'Abilities', 'Races', 'Items', 'Blocks', 'Mobs', 'Biomes', 'Structures', 'Config', 'Commands', 'Mechanics']
nav = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))['nav']
assert [next(iter(item)) for item in nav] == expected, 'Unexpected top-level wiki navigation'
site = ROOT / 'site'
home = BeautifulSoup((site / 'index.html').read_text(encoding='utf-8'), 'html.parser')
assert [link.get_text(' ', strip=True) for link in home.select('.md-tabs__link')] == expected
first_hour_cards = home.select('.homepage-first-hour > a')
assert len(first_hour_cards) == 3 and all(card.select_one('img') for card in first_hour_cards), 'Homepage first-hour route lost its visual cards'
getting_started = BeautifulSoup((site / 'getting-started/index.html').read_text(encoding='utf-8'), 'html.parser')
assert Path(getting_started.select_one('.onboarding-hero > img')['src']).name == 'onboarding-realm-arrival.webp'
assert Path(getting_started.select_one('#path-power > img')['src']).name == 'onboarding-character-paths.webp'
assert Path(getting_started.select_one('#path-nation > img')['src']).name == 'onboarding-found-a-nation.webp'
for section in ('items', 'blocks', 'mobs', 'biomes', 'structures', 'bosses'):
    page = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    assert page.select('.reference-card'), f'Empty directory: {section}'
    prefixed_titles = [heading.get_text(' ', strip=True) for heading in page.select('.reference-card h2') if '/' in heading.get_text()]
    assert not prefixed_titles, f'Upstream namespace leaked into {section} card titles: {prefixed_titles}'
media_overrides = json.loads((ROOT / 'data/reference_card_media.json').read_text(encoding='utf-8'))
from sync_item_reference import manifest as item_manifest
curated_item_categories = {entry['local_page']: entry.get('category', 'items') for entry in item_manifest()['pages']}
for local_page, asset in media_overrides.items():
    metadata = asset if isinstance(asset, dict) else {}
    if isinstance(asset, dict):
        asset = asset['asset']
    asset_path = ROOT / 'docs' / asset
    assert asset_path.exists(), f'Missing card artwork: {asset}'
    if metadata.get('sha256'):
        assert hashlib.sha256(asset_path.read_bytes()).hexdigest() == metadata['sha256'], f'Artwork checksum mismatch: {local_page}'
    section = curated_item_categories.get(local_page, Path(local_page).parts[1])
    directory = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    route = local_page.removesuffix('.md')
    matching = [
        card
        for card in directory.select('.reference-card')
        if card.select_one('a[href]') and posixpath.normpath(posixpath.join(f'tensura-reference/{section}/', unquote(card.select_one('a[href]').get('href', '')))).rstrip('/') == route
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
from sync_item_reference import manifest as item_manifest, generate as generate_item_references
curated_items = item_manifest()
item_build = curated_items['reference_build']
item_selection = (ROOT / item_build['pack_manifest']).read_text(encoding='utf-8')
assert item_build['minecraft'] == '1.21.1' and item_build['sha1'] in item_selection and 'file-id = 8665599' in item_selection, 'Curated item build selection changed'
for local_page, expected_content in generate_item_references().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale item reference: {local_page}'
for entry in curated_items['pages']:
    article = BeautifulSoup((site / entry['local_page'].replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
    assert article.select_one('[data-reference-section="items"]'), 'Curated item navigation context missing'
for entry in curated_items['pages']:
    if not entry['catalogue_entry']:
        assert entry['display_title'] not in item_titles, f'Unverified item promoted: {entry["display_title"]}'
    else:
        card = next(card for card in item_cards if card.h2.get_text(' ', strip=True) == entry['display_title'])
        expected_status = entry['status'] if entry.get('acquisition_verified') else 'acquisition unverified'
        assert expected_status in card.get_text(' ', strip=True), 'Item acquisition status missing'
assert all(not Path(image.get('src', '')).name.casefold().startswith('cs') for image in items.select('.reference-card-media img')), 'Coming Soon portrait remains in Items'
elixir = (ROOT / 'docs/tensura-reference/items/revival-elixir.md').read_text(encoding='utf-8')
assert 'does not resurrect' in elixir and '20,000 MP' in elixir and 'fixed' in elixir, 'Elixir healing limits missing'
milk = (ROOT / 'docs/tensura-reference/items/bulldeer-milk-bucket.md').read_text(encoding='utf-8')
assert 'minecraft:milk_bucket' in milk and 'No survival route' in milk, 'Cattledeer milk acquisition is overstated'
potion_routes = {(route['base'], route['reagent']): entry['registry_id'] for entry in curated_items['pages'] for route in entry.get('brew_routes', [])}
assert potion_routes == {('water', 'grass'): 'tensura:low_potion', ('water', 'flower'): 'tensura:high_potion', ('vacuumed', 'grass'): 'tensura:high_potion', ('vacuumed', 'flower'): 'tensura:full_potion'}, 'Brewing combinations changed'
potion_guide = BeautifulSoup((site / 'tensura-reference/items/healing-potions/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(potion_guide.select('[data-potion-result]')) == 3 and potion_guide.select_one('[data-potion-base]') and potion_guide.select_one('[data-potion-reagent]'), 'Potion planner controls or results missing'
assert '16' in potion_guide.get_text() and '180 ticks' in potion_guide.get_text(), 'Potion controls or preparation timing missing'
bottle_pages = [entry for entry in curated_items['pages'] if 'magic_bottle' in entry.get('registry_id', '')]
assert {entry['registry_id'] for entry in bottle_pages} == {'tensura:magic_bottle', 'tensura:magic_bottle_of_water', 'tensura:vacuumed_magic_bottle_of_water'}, 'Bottle reference inventory changed'
magic_directory = BeautifulSoup((site / 'tensura-reference/magic/index.html').read_text(encoding='utf-8'), 'html.parser')
magic_titles = {card.h2.get_text(' ', strip=True) for card in magic_directory.select('.reference-card')}
for entry in bottle_pages:
    assert entry['display_title'] in item_titles and entry['display_title'] not in magic_titles, 'Bottle appears as a spell or is missing from Items'
    article = BeautifulSoup((site / entry['local_page'].replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
    returns = [link for link in article.find_all('a') if link.get_text(strip=True) == 'Return to Items']
    assert len(returns) == 1 and returns[0]['href'] == '../../items/', 'Bottle article returns to the wrong directory'
vacuumed = (ROOT / 'docs/tensura-reference/magic/vacuumed-magic-bottle-of-water.md').read_text(encoding='utf-8')
assert 'fixed 10 MP' in vacuumed and '60 ticks' in vacuumed and '180 ticks' in vacuumed and 'stacks to 16' in vacuumed, 'Vacuumed bottle effects or preparation changed'
crystals = [entry for entry in curated_items['pages'] if entry.get('crystal_tier')]
assert [(entry['crystal_tier'], entry['dissolve_mp'], entry['bottle_yield']) for entry in crystals] == [('Low', 1000, 3), ('Medium', 2500, 6), ('High', 5000, 9)], 'Crystal recovery or bottle yield changed'
crystal_config = tomllib.loads((ROOT / 'pack/config/tensura/ability/skill/intrinsic_config.toml').read_text(encoding='utf-8'))
assert crystal_config['AbsorbDissolve']['magiculeMultiplier'] == 1.0, 'Recorded crystal recovery multiplier is stale'
for entry in crystals:
    assert entry['display_title'] in item_titles and entry['display_title'] not in magic_titles, 'Crystal appears as a spell or is missing from Items'
    article = (ROOT / 'docs' / entry['local_page']).read_text(encoding='utf-8')
    assert 'Smithing Bench' in article and 'Low Magisteel Gear Schematic' in article and 'MOB_SUMMONED' in article and 'TRIGGERED' in article, 'Crystal preparation or loot eligibility is missing'
crystal_guide = BeautifulSoup((site / 'tensura-reference/items/magic-crystals/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(crystal_guide.select('.potion-guide-card img')) == 3 and 'Fractional values' in crystal_guide.get_text(), 'Crystal guide artwork or precise loot boundaries missing'
assert items.find('a', href='magic-crystals/'), 'Crystal comparison guide is missing from the Items directory'
withdrawn_crystal_files = {review['file_page'] for review in json.loads((ROOT / 'data/media-file-reviews.json').read_text(encoding='utf-8'))['reviews'] if 'Quality_Magic_Crystal.png' in review['file_page'] or 'quality_magic_crystal.png' in review['file_page']}
assert len(withdrawn_crystal_files) == 6, 'Crystal File-page reviews are incomplete'
for article in (ROOT / 'docs/tensura-reference').rglob('*.md'):
    text = article.read_text(encoding='utf-8')
    assert not any('<li><a href="' + file_page + '">' in text for file_page in withdrawn_crystal_files), f'Withdrawn crystal image still has a source-media license claim: {article.name}'
materials = [entry for entry in curated_items['pages'] if entry.get('registry_id') in {'tensura:magic_stone', 'tensura:magic_ore_shard'}]
assert len(materials) == 2, 'Magic material references are incomplete'
for entry in materials:
    assert entry['display_title'] in item_titles and entry['display_title'] not in magic_titles, 'Material appears as a spell or is missing from Items'
stone = (ROOT / 'docs/tensura-reference/magic/magic-stone.md').read_text(encoding='utf-8')
assert 'outputs one Magic Stone' in stone and 'eight' in stone and 'Low Magisteel Gear Schematic' in stone, 'Stone yield or schematic requirement changed'
ore = (ROOT / 'docs/tensura-reference/magic/magic-ore-shard.md').read_text(encoding='utf-8')
assert all(text in ore for text in ('Netherite-tier pickaxe', 'Silk Touch', 'Fortune', 'hold Sneak', '100 ore-shard uses', '5,000 base MP')), 'Ore acquisition, refining, or consumption gate missing'
slime_config = tomllib.loads((ROOT / 'pack/config/tensura/race/slime_config.toml').read_text(encoding='utf-8'))
assert slime_config['MetalSlime']['oreRequirement'] == 100, 'Recorded Metal Slime ore requirement is stale'
staff = next(entry for entry in curated_items['pages'] if entry.get('registry_id') == 'tensura:low_magic_staff')
assert staff['display_title'] in item_titles and staff['display_title'] not in magic_titles, 'Low Staff is missing from Items or classified as a spell'
staff_article = (ROOT / 'docs' / staff['local_page']).read_text(encoding='utf-8')
assert 'both listed schematics' in staff_article and 'three spells' in staff_article and 'Magic Capacity' in staff_article, 'Staff crafting gate or slot calculation missing'
assert [(entry['base_slots'], entry['cooldown_ticks'], entry['durability']) for entry in curated_items['staff_tiers']] == [(3, 20, 100), (4, 10, 300), (5, 5, 500)], 'Staff constructor values changed'
staff_guide = BeautifulSoup((site / 'tensura-reference/items/magic-staves/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(staff_guide.select('.staff-tier-card')) == 3 and len(staff_guide.select('.staff-tier-card details summary')) == 3, 'Staff comparison cards or crafting controls missing'
assert items.find('a', href='magic-staves/'), 'Staff guide is missing from Items'
schematic = next(entry for entry in curated_items['pages'] if entry.get('registry_id') == 'tensura:magic_staff_schematic')
assert schematic['display_title'] in item_titles and schematic['display_title'] not in magic_titles, 'Staff schematic is missing from Items or classified as a spell'
schematic_article = (ROOT / 'docs' / schematic['local_page']).read_text(encoding='utf-8')
assert all(text in schematic_article for text in ('level-five (Master)', 'ten Gold Coins', 'consumes one copy', 'stacks to 16', 'already learned')), 'Schematic acquisition or use documentation missing'
entity_config = tomllib.loads((ROOT / 'pack/config/tensura/entity/entity_config.toml').read_text(encoding='utf-8'))
assert entity_config['Dwarf']['magicTrainerPriceMultiplier'] == 1.0, 'Recorded Magic Trainer price multiplier is stale'
assert 'Learn the schematics' in staff_guide.get_text() and 'carrying the item alone' in staff_guide.get_text(), 'Staff learning guidance missing'
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
for section in ('items', 'weapons', 'armor', 'tools'):
    directory = BeautifulSoup((site / f'tensura-reference/{section}/index.html').read_text(encoding='utf-8'), 'html.parser')
    for card in directory.select('.reference-card'):
        href = card.select_one('a[href]')['href']
        article_path = site / f'tensura-reference/{section}' / href / 'index.html'
        article = BeautifulSoup(article_path.read_text(encoding='utf-8'), 'html.parser')
        article_text = article.select_one('.tensura-reference-article').get_text(' ', strip=True).casefold()
        assert 'work in progress' not in article_text, f'Upstream maintenance banner remains: {article_path}'
        assert 'labyrinth' not in article_text and 'dungeon' not in article_text, f'Legacy dungeon content remains: {article_path}'
        visible_images = article.select('.tensura-reference-article img')
        assert all('wip' not in Path(image.get('src', '')).name.casefold() for image in visible_images), f'WIP artwork remains: {article_path}'
        hero = article.select_one('.reference-overview-media img')
        assert hero and 'wip' not in Path(hero.get('src', '')).name.casefold(), f'WIP hero artwork remains: {article_path}'
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
from sync_biome_reference import generate as generate_biome_reference
for local_page, expected_content in generate_biome_reference().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale biome reference: {local_page}'
from sync_dimension_reference import generate as generate_dimension_reference, load_manifest as load_dimension_manifest
dimension_manifest = load_dimension_manifest()
for source_key, build in dimension_manifest['reference_builds'].items():
    selected = (ROOT / build['pack_manifest']).read_text(encoding='utf-8')
    assert build['minecraft'] == '1.21.1'
    if build.get('sha1'):
        assert build['sha1'] in selected, f'Dimension source selection changed: {source_key}'
for local_page, expected_content in generate_dimension_reference().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale dimension reference: {local_page}'
dimensions = BeautifulSoup((site / 'tensura-reference/dimensions/index.html').read_text(encoding='utf-8'), 'html.parser')
dimension_cards = dimensions.select('.reference-dimension-card')
dimension_titles = [card.h2.get_text(' ', strip=True) for card in dimension_cards]
assert dimension_titles == ['Boss Area', 'Elemental Realm', 'Hell', 'Hyperbolic Chamber', 'Kamui', 'Labyrinth']
assert all(card.select_one('.reference-card-media img') for card in dimension_cards), 'A dimension card is missing artwork'
assert 'Tensura: Dungeon project is not installed' in dimensions.get_text(' ', strip=True)
biomes = BeautifulSoup((site / 'tensura-reference/biomes/index.html').read_text(encoding='utf-8'), 'html.parser')
biome_cards = biomes.select('.reference-card')
biome_titles = [card.h2.get_text(' ', strip=True) for card in biome_cards]
assert len(biome_cards) == 12 and len(set(biome_titles)) == len(biome_titles), 'Unexpected biome directory size or duplicate title'
assert 'Kamui Biome' in biome_titles and 'Structures and Biomes' not in biome_titles, 'Biome catalogue includes a collection page or omits Kamui'
assert all(card.select_one('.reference-card-media img') for card in biome_cards), 'A biome card is missing artwork'
assert all('placeholder' not in Path(image.get('src', '')).name.casefold() for image in biomes.select('.reference-card-media img')), 'A biome card uses placeholder artwork'
assert 'Only the strong survive.' not in biomes.get_text(' ', strip=True), 'A thin upstream biome summary remains in the directory'
assert '\ufffd' not in biomes.get_text(' ', strip=True), 'A broken biome-list separator remains'
desert = next(card for card in biome_cards if card.h2.get_text(' ', strip=True) == 'Desert of Death')
assert [tag.get_text(strip=True) for tag in desert.select('.reference-stat-tags > span')] == ['Knight Spider', 'Tempest Serpent', 'Armorsaurus', 'Basilisk']
kamui = next(card for card in biome_cards if card.h2.get_text(' ', strip=True) == 'Kamui Biome')
assert Path(kamui.select_one('.reference-card-media img')['src']).name == 'kamui-biome.webp'
kamui_pairs = dict(zip([x.get_text(strip=True) for x in kamui.select('dt')], [x.get_text(strip=True) for x in kamui.select('dd')]))
assert kamui_pairs['Registry ID'] == 'mysticism:kamui_biome' and kamui_pairs['Natural spawns'] == 'None'
from sync_structure_catalogue import generate as generate_structures, load_manifest as load_structure_manifest
structure_manifest = load_structure_manifest()
structure_builds = structure_manifest['reference_builds']
expected_file_ids = {'tensura': 8665599, 'mysticism': 8379529, 'boss_structure': 8614357}
for key, build in structure_builds.items():
    selected = (ROOT / build['pack_manifest']).read_text(encoding='utf-8')
    assert build['minecraft'] == '1.21.1'
    assert build['sha1'] in selected and f'file-id = {expected_file_ids[key]}' in selected, f'Structure source selection changed: {key}'
for local_page, expected_content in generate_structures().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale page: {local_page}'
structures = BeautifulSoup((site / 'tensura-reference/structures/index.html').read_text(encoding='utf-8'), 'html.parser')
structure_cards = structures.select('.reference-card')
structure_titles = [card.h2.get_text(' ', strip=True) for card in structure_cards]
assert len(structure_cards) == 22 and len(set(structure_titles)) == len(structure_titles), 'Unexpected structure directory size or duplicate title'
assert structure_titles.count('Ruins') == 1 and 'Structures' not in structure_titles, 'Duplicate ruin or collection card leaked into Structures'
required_structures = {
    'Orc Village', 'Warp Pads', 'Dark Elemental Portal', 'Earth Elemental Portal',
    'Wind Elemental Portal', 'Beast Kingdom of Eurazania', 'Hinata Church',
    'Night Rose', 'Orc Disaster Temple', 'Rimuru Ogre Fight', "Shizu's School",
}
assert required_structures.issubset(structure_titles), 'A registered 1.21.1 structure is missing'
assert {'Fire Elemental Portal', 'Space Elemental Portal', 'Water Elemental Portal'}.isdisjoint(structure_titles), 'An unregistered Mysticism portal leaked into Structures'
assert all(card.select_one('.reference-card-media img') for card in structure_cards), 'A structure card is missing artwork'
structure_images = [Path(image.get('src', '')).name.casefold() for image in structures.select('.reference-card-media img')]
assert all('wip' not in name and 'placeholder' not in name for name in structure_images), 'A structure card still uses placeholder artwork'
assert 'Dungeon Structures' not in structures.get_text(' ', strip=True), 'An obsolete dungeon grouping is still promoted'
from block_reference_icons import generate as generate_block_icons
from sync_block_catalogue import generate as generate_blocks, load_manifest as load_block_manifest
block_manifest = load_block_manifest()
for local_page, expected_content in generate_blocks().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale page: {local_page}'
from sync_block_catalogue import sanitize_imported as sanitize_block_articles
assert not sanitize_block_articles(check=True), 'An imported block article still contains maintenance debris'
for icon_path, expected_content in generate_block_icons().items():
    assert icon_path.read_text(encoding='utf-8') == expected_content, f'Stale block symbol: {icon_path}'
block_builds = block_manifest['reference_builds']
mysticism_block_build = block_builds['mysticism']
mysticism_selection = (ROOT / mysticism_block_build['pack_manifest']).read_text(encoding='utf-8')
assert mysticism_block_build['version'] == '2.1.2' and mysticism_block_build['minecraft'] == '1.21.1'
assert mysticism_block_build['sha1'] in mysticism_selection and 'file-id = 8379529' in mysticism_selection, 'Mysticism block source selection changed'
assert block_builds['nightmares']['installed_version_verified'] is False
blocks = BeautifulSoup((site / 'tensura-reference/blocks/index.html').read_text(encoding='utf-8'), 'html.parser')
block_cards = blocks.select('.reference-card')
block_titles = [card.h2.get_text(' ', strip=True) for card in block_cards]
assert len(block_cards) == 35 and len(set(block_titles)) == len(block_titles), 'Unexpected block directory size or duplicate title'
required_blocks = {
    'Elemental Realm Portal', 'Cadence Acceleration Glass', 'Domicile Door',
    'Domicile Trapdoor', 'Gabriel Snow Crystal', 'Stasis Lattice',
}
assert required_blocks.issubset(block_titles), 'A registered add-on block is missing'
assert all(card.select_one('.reference-card-media img') for card in block_cards), 'A block card is missing artwork or a reference symbol'
for page in block_manifest['pages']:
    card = next(card for card in block_cards if card.h2.get_text(' ', strip=True) == page['display_title'])
    assert Path(card.select_one('img')['src']).name == Path(page['asset']).name, f'Stale block icon: {page["display_title"]}'
    assert bool(card.select_one('.skill-reference-status')) == (page['source_key'] == 'nightmares'), f'Incorrect build notice: {page["display_title"]}'
block_text = blocks.get_text(' ', strip=True)
assert 'Upstream reference information for' not in block_text, 'A generic block summary remains'
assert '\ufffd' not in block_text, 'A broken block separator remains'
block_sources = [
    ROOT / 'docs/tensura-reference/blocks/blocks-charybdis-core.md',
    ROOT / 'docs/tensura-reference/blocks/blocks-kiln.md',
    ROOT / 'docs/tensura-reference/blocks/blocks-magic-engine.md',
    ROOT / 'docs/tensura-reference/blocks/blocks-smithing-bench.md',
]
assert all('Work In Progress' not in path.read_text(encoding='utf-8') for path in block_sources), 'A block article still exposes an upstream maintenance banner'
smithing = block_sources[-1].read_text(encoding='utf-8')
assert all(name in smithing for name in ('Dark Set', 'Silver Set', 'Ant Set', 'Clown Masks')), 'Block cleanup discarded source gear-set names'
assert 'Recipe coverage' in smithing, 'Undocumented smithing sets need an explicit recipe-coverage limit'
ice_ore = (ROOT / 'docs/mysticism-reference/blocks/blocks-ice-ore.md').read_text(encoding='utf-8')
for exact_fact in ('Y 55 and 100', 'diamond-tier', 'Silk Touch', 'Fortune'):
    assert exact_fact in ice_ore, f'Ice Ore verification detail missing: {exact_fact}'
assert 'only Minecraft\'s Ice Spikes biome' in ice_ore, 'Ice Ore overstates verified biome generation'
assert 'original TSR artwork' in ice_ore and 'source game texture' not in ice_ore.casefold(), 'Ice Ore illustration mislabeled as in-game media'
magic_engine = (ROOT / 'docs/tensura-reference/blocks/blocks-magic-engine.md').read_text(encoding='utf-8')
assert 'reduces area Magicules' in magic_engine and 'decorative light-emitting' not in magic_engine, 'Magic Engine functional summary is misleading'
bosses = BeautifulSoup((site / 'tensura-reference/bosses/index.html').read_text(encoding='utf-8'), 'html.parser')
boss_cards = bosses.select('.reference-card')
boss_titles = [card.h2.get_text(' ', strip=True) for card in boss_cards]
assert len(boss_cards) == 15 and len(set(boss_titles)) == len(boss_titles), 'Unexpected boss directory size or duplicate title'
assert all(card.select_one('.reference-card-media img') for card in boss_cards), 'A boss card is missing artwork'
assert all('placeholder' not in Path(image.get('src', '')).name.casefold() for image in bosses.select('.reference-card-media img')), 'A boss card uses placeholder artwork'
boss_text = bosses.get_text(' ', strip=True)
assert '\ufffd' not in boss_text and 'Eat, kill, all to satisfy my hunger' not in boss_text, 'A broken or thin boss summary remains'
for card in boss_cards:
    labels = [item.get_text(' ', strip=True) for item in card.select('dt')]
    assert not {'Resistances', 'Nullifications', 'Intrinsic', 'Common', 'Extra'}.intersection(labels), f'Boss card exposes an unreadable ability dump: {card.h2.get_text(strip=True)}'
    if card.select('dt'):
        assert 'EP Range' in labels, f'Boss card is missing its EP range: {card.h2.get_text(strip=True)}'
from sync_command_reference import generate as generate_commands, load_manifest as load_command_manifest
command_manifest = load_command_manifest()
assert (ROOT / 'docs/tensura-reference/commands/index.md').read_text(encoding='utf-8') == generate_commands(), 'Stale command reference'
for source in command_manifest['sources']:
    if source.get('pack_manifest'):
        selection = (ROOT / source['pack_manifest']).read_text(encoding='utf-8')
        assert source['digest'] in selection, f'Command artifact selection changed: {source["name"]}'
commands = BeautifulSoup((site / 'tensura-reference/commands/index.html').read_text(encoding='utf-8'), 'html.parser')
command_entries = commands.select('.command-entry')
assert len(command_entries) == 50, 'Unexpected command family count'
assert len(commands.select('.command-source')) == 7, 'Unexpected command source count'
assert commands.select_one('[data-command-search-input]') and commands.select('.command-access-filters button'), 'Command filters are missing'
command_text = commands.get_text(' ', strip=True)
for source in ('Tensura: Reincarnated', 'Tensura: Mysticism', 'Tensura: Ascension', 'SlimeThrone Extras', 'TR: Beyond Adventures', 'Tensura Nightmares', 'TenSura Boss Structure'):
    assert source in command_text, f'Missing command source: {source}'
assert '2.1.2' in commands.select_one('#mysticism').get_text(' ', strip=True), 'Mysticism commands are not tied to the current build'
assert 'soul-quality' not in ' '.join(entry.get_text(' ', strip=True) for entry in commands.select('#mysticism .command-entry')).casefold(), 'Obsolete Mysticism command leaked into the current list'
assert 'server match pending' in commands.select_one('#nightmares').get_text(' ', strip=True).casefold(), 'Nightmares command status is overstated'
assert 'coverage is not yet verified' not in command_text.casefold() and 'oldid=378' not in command_text, 'Obsolete command notice remains'
command_js = (ROOT / 'docs/assets/javascripts/reference.js').read_text(encoding='utf-8')
assert 'setupCommandReference' in command_js and 'data-command-access-filter' in command_js, 'Command filtering behavior is missing'
from sync_config_reference import generate as generate_config, load_manifest as load_config_manifest, files_for as config_files_for
config_manifest = load_config_manifest()
assert (ROOT / 'docs/tensura-reference/configuration/index.md').read_text(encoding='utf-8') == generate_config(), 'Stale configuration reference'
for source in config_manifest['sources']:
    selection = (ROOT / source['manifest']).read_text(encoding='utf-8')
    assert source['digest'] in selection, f'Configuration source selection changed: {source["name"]}'
config_page = BeautifulSoup((site / 'tensura-reference/configuration/index.html').read_text(encoding='utf-8'), 'html.parser')
config_cards = config_page.select('[data-config-card]')
assert len(config_cards) == 10, 'Unexpected configuration control-group count'
assert config_page.select_one('[data-config-search-input]') and len(config_page.select('[data-config-filter]')) == 6, 'Configuration filters are missing'
assert sum(len(config_files_for(group)) for group in config_manifest['groups']) >= 100, 'Configuration file coverage unexpectedly shrank'
config_text = config_page.get_text(' ', strip=True)
assert 'WIP' not in config_text and 'Configure Configure' not in config_text, 'Upstream placeholder copy leaked into configuration landing page'
assert 'Tensura Nightmares' in config_text and 'not recorded' in config_text, 'Nightmares configuration status is overstated'
assert 'setupConfigReference' in command_js and 'data-config-filter' in command_js, 'Configuration filtering behavior is missing'
from sync_gamerule_reference import generate as generate_gamerules, load_manifest as load_gamerule_manifest
gamerule_manifest = load_gamerule_manifest()
assert (ROOT / 'docs/tensura-reference/gamerules/index.md').read_text(encoding='utf-8') == generate_gamerules(), 'Stale gamerule reference'
gamerules = BeautifulSoup((site / 'tensura-reference/gamerules/index.html').read_text(encoding='utf-8'), 'html.parser')
gamerule_cards = gamerules.select('[data-gamerule-card]')
assert len(gamerule_cards) == 55, 'Unexpected registered gamerule count'
assert len({card.select_one('h3').get_text(' ', strip=True) for card in gamerule_cards}) == 55, 'Duplicate gamerule name'
assert gamerules.select_one('[data-gamerule-search-input]') and len(gamerules.select('[data-gamerule-source-filter]')) == 5, 'Gamerule source filters are missing'
assert len(gamerules.select('[data-gamerule-type-filter]')) == 3, 'Gamerule type filters are missing'
for source in gamerule_manifest['sources']:
    if source.get('pack_manifest'):
        selection = (ROOT / source['pack_manifest']).read_text(encoding='utf-8')
        assert source['digest'] in selection, f'Gamerule source selection changed: {source["name"]}'
gamerule_text = gamerules.get_text(' ', strip=True)
for required in ('noUniqueStart', 'uniqueSECost', 'doAscensionUltimate', 'nightmare_ultimates', 'resetPerSkillLock'):
    assert required in gamerule_text, f'Missing gamerule: {required}'
for obsolete in gamerule_manifest['excluded_obsolete_names']:
    assert not any(card.select_one('h3').get_text(' ', strip=True) == obsolete for card in gamerule_cards), f'Obsolete gamerule leaked into cards: {obsolete}'
nightmare_cards = gamerules.select('[data-gamerule-source="nightmares"]')
assert len(nightmare_cards) == 15 and all('gamerule-card--pending' in card.get('class', []) for card in nightmare_cards), 'Nightmares gamerule status is overstated'
rule_pairs = {card.select_one('h3').get_text(' ', strip=True): card for card in gamerule_cards}
assert 'true' in rule_pairs['trulygodclass'].select_one('.gamerule-values').get_text(' ', strip=True).casefold(), 'Nightmares artifact default drifted'
assert 'Forced to 0 by SlimeThrone Extras' in rule_pairs['resetPerSkillLock'].get_text(' ', strip=True), 'SlimeThrone gamerule override is missing'
assert 'setupGameruleReference' in command_js and 'data-gamerule-copy' in command_js, 'Gamerule filtering or copy behavior is missing'
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
    if record['category'] == 'bosses':
        expected_stats = record['stats']
        assert card_pairs['Health'] == expected_stats['Base health']
        assert card_pairs['Spiritual Health'] == expected_stats['Base spiritual health']
        assert card_pairs['Armor'] == expected_stats['Base armor']
        assert card_pairs['EP Range'] == f'{expected_stats["Minimum EP"]}–{expected_stats["Maximum EP"]}'
    else:
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
print('Wiki section checks passed: 11 navigation sections, populated directories, corrected media, source-backed stats and commands, and race configurations')
