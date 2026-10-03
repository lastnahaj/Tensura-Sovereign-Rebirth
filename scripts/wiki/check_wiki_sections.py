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
from sync_block_catalogue import load_manifest as load_block_manifest
curated_block_categories = {entry['local_page']: 'blocks' for entry in load_block_manifest()['pages'] if entry.get('reclassify_import')}
for local_page, asset in media_overrides.items():
    metadata = asset if isinstance(asset, dict) else {}
    if isinstance(asset, dict):
        asset = asset['asset']
    asset_path = ROOT / 'docs' / asset
    assert asset_path.exists(), f'Missing card artwork: {asset}'
    if metadata.get('sha256'):
        assert hashlib.sha256(asset_path.read_bytes()).hexdigest() == metadata['sha256'], f'Artwork checksum mismatch: {local_page}'
    section = metadata.get('category', curated_block_categories.get(local_page, curated_item_categories.get(local_page, Path(local_page).parts[1])))
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
hipokute = curated_items['hipokute']
assert hipokute['ages'] == {'seed': 0, 'sprout': 1, 'grass': 2, 'flower': 3}, 'Hipokute growth states changed'
assert hipokute['flower_pick']['reset_age'] == 1 and hipokute['flower_pick']['output_count'] == 1, 'Flower picking contract changed'
assert hipokute['sprout_branches'] == {'grass': .5, 'flower': .5}, 'Hipokute branch probabilities changed'
hipokute_guide = BeautifulSoup((site / 'tensura-reference/core-mechanics/mechanics-hipokute-farming/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(hipokute_guide.select('.hipokute-harvest-card img')) == 3 and len(hipokute_guide.select('.hipokute-harvest-card details')) == 3, 'Hipokute harvest guide incomplete'
assert hipokute_guide.select_one('[data-hipokute-magicules]') and hipokute_guide.select_one('[data-hipokute-result]'), 'Hipokute comparison controls missing'
assert all(fact in hipokute_guide.get_text() for fact in ('conditional', 'growth-speed gate', 'not measured yields', 'not arbitrary stone', '50% grass / 50% flower')), 'Hipokute scope or growth limits missing'
for kind in ('grass', 'flower', 'seeds'):
    assert 'Hipokute ' + kind.title() in item_titles, 'Hipokute item missing from Items'
    page = (ROOT / f'docs/tensura-reference/items/hipokute-{kind}.md').read_text(encoding='utf-8')
    assert 'mechanics-hipokute-farming.md' in page and all('id="' + anchor + '"' in page for anchor in ('Usage', 'Obtainment')), 'Hipokute routes or legacy anchors lost'
hipokute_config = tomllib.loads((ROOT / 'pack/config/tensura/entity/entity_config.toml').read_text(encoding='utf-8'))
assert hipokute_config['Dwarf']['alchemistPriceMultiplier'] == hipokute['alchemist_flower_trade']['tracked_price_multiplier'], 'Alchemist price configuration changed'
grimoire_tiers = curated_items['grimoire_tiers']
assert [(tier['base_slots'], tier['cooldown_ticks'], tier['durability']) for tier in grimoire_tiers] == [(3,40,100),(4,30,200),(5,20,300),(6,15,400),(7,10,500)], 'Grimoire constructor values changed'
assert [tier['rarity'] for tier in grimoire_tiers] == ['Common','Uncommon','Uncommon','Rare','Rare'], 'Grimoire rarity mismatch'
assert [tier['max_ep'] for tier in grimoire_tiers] == [2500,5000,8000,80000,2000000], 'Base grimoire evolution thresholds or terminal codec default changed'
for tier in grimoire_tiers:
    article = (ROOT / 'docs/tensura-reference/items' / (tier['slug'] + '.md')).read_text(encoding='utf-8')
    assert f'Grimoire {tier["tier"]}' in item_titles, 'Grimoire missing from Items'
    assert all(fact in article for fact in ('Magic Capacity', 'not a percentage', 'EP_DURABILITY', 'Gear Evolution', 'grimoire.webp')), 'Grimoire casting or scope limits missing'
    assert all('id="' + anchor + '"' in article for anchor in ('Description','Usage','Obtainment')), 'Legacy grimoire fragments lost'
grimoire_guide = BeautifulSoup((site / 'tensura-reference/items/grimoires/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(grimoire_guide.select('.staff-tier-card')) == 5 and len(grimoire_guide.select('.staff-tier-card details')) == 5, 'Grimoire tier comparison incomplete'
assert '80,000' in grimoire_guide.get_text() and 'not a live-server guarantee' in grimoire_guide.get_text() and 'Stagnation' in grimoire_guide.get_text(), 'Grimoire base-chain limits missing'
assert '2,000,000' in grimoire_guide.get_text() and 'codec' in grimoire_guide.get_text(), 'Terminal grimoire codec default omitted'
assert [card.select_one('h2 a')['href'] for card in grimoire_guide.select('.staff-tier-card')] == ['../' + tier['slug'] + '/' for tier in grimoire_tiers], 'Grimoire card routes mismatch'
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
for material in ('low_magisteel', 'high_magisteel', 'pure_magisteel'):
    entry = next(entry for entry in curated_items['pages'] if entry.get('registry_id') == f'tensura:{material}_gear_schematic')
    article = (ROOT / 'docs' / entry['local_page']).read_text(encoding='utf-8')
    assert all(text in article for text in ('inventory_changed', 'advancement reward', 'use', '16')), 'Material schematic reward or learning guidance missing'
    assert f'data/tensura/advancement/{material}.json' in entry['evidence_paths'] and f'data/tensura/loot_table/advancement_reward/{material}.json' in entry['evidence_paths'], 'Advancement reward evidence missing'
assert 'matching ingot inventory advancements' in staff_guide.get_text(), 'Material schematic route missing from staff guide'
magic_evidence = json.loads((ROOT / 'data/magic_reference.json').read_text(encoding='utf-8'))
caster = magic_evidence['caster_tools']
magic_config = tomllib.loads((ROOT / caster['configuration']).read_text(encoding='utf-8'))
assert magic_config['unlearntCostMultiplier'] == caster['unlearned_cost_multiplier'] and magic_config['unlearntCastMultiplier'] == caster['unlearned_chant_multiplier'], 'Casting modifiers disagree with the checked-in configuration'
caster_guide = BeautifulSoup((site / 'tensura-reference/tools/caster-tools-tutorial/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(caster_guide.select('.caster-step details summary')) == 3 and len(caster_guide.select('.caster-cost-grid > article')) == 2, 'Casting walkthrough lost its step controls or cost comparison'
assert len(caster_guide.select('.caster-exclusions li')) == 7, 'Unlearned casting exclusion list is incomplete'
assert all(text in caster_guide.get_text() for text in ('Possession', 'Next Ability Mode', 'Previous Ability Mode', 'EP_DURABILITY', 'Reset-scroll')), 'Casting exclusions, controls, or scope missing'
assert 'will remain even after' not in caster_guide.get_text(), 'Unverified reset retention claim remains'
for tome_id in ('magic_tome', 'unbound_tome'):
    tome = next(entry for entry in curated_items['pages'] if entry.get('registry_id') == 'tensura:' + tome_id)
    assert tome['display_title'] in item_titles and tome['display_title'] not in magic_titles, 'Tome is missing from Items or appears as a spell'
    article = (ROOT / 'docs' / tome['local_page']).read_text(encoding='utf-8')
    required = ('Rare', 'Wizard Tower', 'Spellbinding', 'Source and licensing') if tome_id == 'unbound_tome' else ('Rare', 'Wizard Tower', 'ten ticks', '200-tick', 'fails')
    assert all(text in article for text in required), 'Tome item facts or learning scope missing'
    assert '???' not in article.replace('??? info', ''), 'Unfinished tome infobox remains'
assert magic_evidence['unbound_copy_reference']['copy_exclusions'] == ['#tensura:spiritual_magic', 'tensura:summon_medium_elemental', 'tensura:summon_greater_elemental'], 'Tome copying exclusions changed'
insanity = (ROOT / 'docs/tensura-reference/core-mechanics/effects-insanity.md').read_text(encoding='utf-8')
assert 'Work In Progress' not in insanity and 'href="#Causes"' not in insanity, 'Editorial banner or nonexistent cause link remains'
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
assert len(biome_cards) == 16 and len(set(biome_titles)) == len(biome_titles), 'Unexpected biome directory size or duplicate title'
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
assert len(block_cards) == 32 and len(set(block_titles)) == len(block_titles), 'Unexpected block directory size or duplicate title'
from underworld_biome_reference import generate as generate_underworld_biomes, manifest as underworld_manifest, NAMES as underworld_names, baseline as underworld_baseline, spawn_entries as underworld_spawn_entries
underworld_data = underworld_manifest()
assert underworld_data['artifact_sha1'] in (ROOT / underworld_data['pack_manifest']).read_text(encoding='utf-8'), 'Underworld artifact selection changed'
underworld_config = ROOT / underworld_data['area_configuration']['path']
assert hashlib.sha256(underworld_config.read_bytes()).hexdigest() == underworld_data['area_configuration']['sha256'], 'Underworld baseline configuration changed'
assert len(underworld_data['resources']) == 28
for local_page, expected_content in generate_underworld_biomes().items():
    assert (ROOT / 'docs' / local_page).read_text(encoding='utf-8') == expected_content, f'Stale Underworld guide: {local_page}'
    assert 'data-reference-section="biomes"' in expected_content and 'Special:Upload' not in expected_content
for slug, title in underworld_names.items():
    assert title in biome_titles and title not in block_titles, f'Underworld biome misclassified: {title}'
    card = next(card for card in biome_cards if card.h2.get_text(' ', strip=True) == title)
    pairs = dict(zip([node.get_text(strip=True) for node in card.select('dt')], [node.get_text(' ', strip=True) for node in card.select('dd')]))
    assert pairs['Magicule baseline'] == f'{underworld_baseline(underworld_data, slug):,.0f}'
    assert 'Arch Daemon' in pairs['Mobs'], 'Tagged Arch Daemon addition lost'
    entries = underworld_spawn_entries(underworld_data, slug)
    assert len(entries) == 6 and any(item['type'] == 'tensura:arch_daemon' and item['weight'] == 1 and route == 'Hell-tag spawn addition' for item, route in entries)
    assert card.select_one('a')['href'].endswith(f'/blocks/{slug.replace("_", "-")}/'), 'Legacy biome route changed'
assert 'Hound Dog' in next(card for card in biome_cards if card.h2.get_text(' ', strip=True) == 'Underworld Spikes').get_text(' ', strip=True)
required_blocks = {
    'Spellbinding Table',
    'Elemental Realm Portal', 'Cadence Acceleration Glass', 'Domicile Door',
    'Domicile Trapdoor', 'Gabriel Snow Crystal', 'Stasis Lattice',
}
assert required_blocks.issubset(block_titles), 'A registered add-on block is missing'
spellbinding = (ROOT / 'docs/tensura-reference/resistances/spellbinding-table.md').read_text(encoding='utf-8')
for fact in ('spellbinding-table.webp', '1 Magic Stone', '2 Silver Ingots', '4 Crying Obsidian', '1,200', 'Light level', 'one item', 'diamond-tier', 'not live-server'):
    assert fact in spellbinding, f'Spellbinding Table verification detail missing: {fact}'
assert 'skill-availability' not in spellbinding and 'Invicon_Diamond_Pickaxe' not in spellbinding and 'exclude: true' not in spellbinding, 'Workstation still treated as an archived resistance'
assert all('id="' + anchor + '"' in spellbinding for anchor in ('Description', 'Usage')), 'Legacy workstation fragments lost'
assert 'data-reference-section="blocks"' in spellbinding, 'Workstation navigation context missing'
assert '["items", "blocks", "biomes"].includes(section)' in (ROOT / 'docs/assets/javascripts/server-status.js').read_text(encoding='utf-8'), 'Curated legacy-route sidebar override missing'
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
from smithing_reference import manifest as smithing_manifest
smithing_data = smithing_manifest()
assert len(smithing_data['recipes']) == smithing_data['recipe_count'] == 298, 'Smithing recipe count changed'
assert len({r['resource'] for r in smithing_data['recipes']}) == 298, 'Duplicate smithing recipes'
assert len({s['id'] for r in smithing_data['recipes'] for s in r['schematics']}) == smithing_data['schematic_count'] == 33, 'Smithing schematic count changed'
smithing_rendered = BeautifulSoup((site / 'tensura-reference/blocks/blocks-smithing-bench/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(smithing_rendered.select('[data-smithing-recipe]')) == 298, 'Smithing browser lost recipes'
assert smithing_rendered.select_one('[data-smithing-search]') and smithing_rendered.select_one('[data-smithing-clear]'), 'Smithing browser controls missing'
assert len(smithing_rendered.select('.smithing-pattern td')) == 6, 'Bench crafting layout changed'
for fact in ('player inventory', 'all required schematics', 'axe-mineable', 'live crafting untested'):
    assert fact in smithing_rendered.get_text(), f'Smithing behavior or scope missing: {fact}'
for recipe in smithing_data['recipes']:
    assert all(i['count'] > 0 for i in recipe['ingredients']), 'Invalid smithing ingredient quantity'
    assert recipe['resource'].startswith('data/tensura/recipe/smithing/') and len(recipe['sha256']) == 64, 'Smithing resource provenance missing'
starter_text = (ROOT / 'docs/tensura-reference/core-mechanics/getting-started.md').read_text(encoding='utf-8')
assert '2 iron, 3 paper' not in starter_text and '2 paper, a crafting table, a smithing table, and 2 planks' in starter_text, 'Outdated beginner bench recipe'
from kiln_reference import manifest as kiln_manifest, molten_outputs
kiln_data = kiln_manifest()
assert kiln_data['recipe_counts'] == {'melting': 272, 'mixing': 14}, 'Kiln recipe coverage changed'
assert len(kiln_data['recipes']) == len({r['resource'] for r in kiln_data['recipes']}) == 286, 'Duplicate or missing Kiln recipe'
assert [t['capacity_per_bar'] for t in kiln_data['tiers']] == [144, 288, 576], 'Kiln tier capacity changed'
kiln_config = tomllib.loads((ROOT / 'pack/config/tensura/block_config.toml').read_text(encoding='utf-8'))['Kiln']
assert [kiln_config[k] for k in ('moltenDefault', 'moltenMithril', 'moltenOrichalcum')] == [t['capacity_per_bar'] for t in kiln_data['tiers']], 'Stale recorded Kiln capacity'
assert kiln_config['fireCoreCost'] == 100 and kiln_config['chargeDuration'] == 2400, 'Kiln boost guide needs config review'
assert sum(r['kind'] == 'melting' and r['definition'].get('primary_count', 0) == 0 for r in kiln_data['recipes']) == 15, 'Zero-default recycling coverage changed'
assert all(len(r['sha256']) == 64 for r in kiln_data['recipes']), 'Kiln resource checksums missing'
kiln_rendered = BeautifulSoup((site / 'tensura-reference/blocks/blocks-kiln/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(kiln_rendered.select('[data-kiln-kind="melting"]')) == 272 and len(kiln_rendered.select('[data-kiln-kind="mixing"]')) == 14, 'Rendered Kiln recipe coverage changed'
assert len(kiln_rendered.select('.kiln-tier-grid > article')) == 3, 'Kiln tier panels missing'
assert len(kiln_rendered.select('.kiln-tier-grid td')) == 27, 'Kiln crafting patterns missing'
assert kiln_rendered.select_one('[data-smithing-search]') and kiln_rendered.select_one('[data-smithing-clear]'), 'Kiln recipe search controls missing'
for fact in ('per molten bar', 'diamond-tier', 'light level 13', '100 remaining durability', '2,400 ticks', 'does not replace fuel', '0 units', 'live processing untested'):
    assert fact in kiln_rendered.get_text(' ', strip=True), f'Kiln behavior or scope missing: {fact}'
alloy_table = next(table for table in kiln_rendered.select('table') if [th.get_text(strip=True) for th in table.select('th')] == ['Output', 'Left bar units', 'Right bar units', 'Minimum capacity tier'])
alloy_rows = alloy_table.select('tbody tr')
assert len(alloy_rows) == 14, 'Kiln alloy comparison missing rows'
pure_block = next(r for r in alloy_rows if 'Block of Pure Magisteel' in r.get_text())
assert '324 Magisteel' in pure_block.get_text() and 'Orichalcum Kiln' in pure_block.get_text(), 'Pure Magisteel block capacity gate is wrong'
from chilled_reference import manifest as chilled_manifest
chilled_data = chilled_manifest()
assert len(chilled_data['recipes']) == 10 and len(chilled_data['refining_recipes']) == 36 and len(chilled_data['loot_tables']) == 3, 'Chilled-material recipe or loot coverage changed'
assert chilled_data['block_stuck_multiplier'] == {'x': 0.5, 'y': 0.7, 'z': 0.5}, 'Chilled-block movement multiplier changed'
assert chilled_data['spawn_chilled_biome_tag'] == 'minecraft:spawns_cold_variant_frogs' and chilled_data['spawn_structure_path_excluded'], 'Cold-variant initialization scope changed'
assert chilled_data['food'] == {'nutrition': 1, 'saturation_modifier': 2.0, 'always_edible': True}, 'Chilled food properties changed'
chilled_block = BeautifulSoup((site / 'tensura-reference/blocks/blocks-chilled-slime-block/index.html').read_text(encoding='utf-8'), 'html.parser')
chilled_item = BeautifulSoup((site / 'tensura-reference/items/chilled-slime/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(chilled_block.select('.smithing-pattern td')) == 18, 'Chilled-block crafting arrangements missing'
for fact in ('8 Snow Blocks', '9 chilled items', 'fall distance greater than 2.5', '0.9-block-high', 'slime_walkable_mobs', 'live behavior untested'):
    assert fact in chilled_block.get_text(' ', strip=True), f'Chilled-block behavior or scope missing: {fact}'
for fact in ('8 Snowballs', '9 Chilled Slime', 'spawns_cold_variant_frogs', 'Structure spawns', '36 refining', 'not proof of an ordinary Brewing Stand recipe'):
    assert fact in chilled_item.get_text(' ', strip=True), f'Chilled item behavior or scope missing: {fact}'
assert '(T.B.A)' not in chilled_item.get_text() and 'Lua error' not in chilled_block.get_text(), 'Unfinished chilled-material copy remains'
assert Path(chilled_block.select_one('.reference-overview-media img')['src']).name == 'chilled-slime-block.webp'
assert Path(chilled_item.select_one('.reference-overview-media img')['src']).name == 'chilled-slime.webp'
from slime_material_reference import manifest as slime_material_manifest
slime_material_data = slime_material_manifest()
assert len(slime_material_data['recipes']) == 11 and len(slime_material_data['loot_tables']) == 3 and len(slime_material_data['tags']) == 3, 'Ordinary slime-material evidence coverage changed'
assert slime_material_data['item_registration']['food_properties'] is False, 'Ordinary material must not inherit chilled food properties'
slime_material_block = BeautifulSoup((site / 'tensura-reference/blocks/blocks-slime-chunk-block/index.html').read_text(encoding='utf-8'), 'html.parser')
slime_material_item = BeautifulSoup((site / 'tensura-reference/items/slime-chunk/index.html').read_text(encoding='utf-8'), 'html.parser')
assert len(slime_material_block.select('.smithing-pattern td')) == 18, 'Ordinary packing or chilling arrangement missing'
for fact in ('9 chunks', '8 Snow Blocks', 'fall distance greater than 2.5', '0.9-block-high', 'slime_walkable_mobs', 'live behavior untested'):
    assert fact in slime_material_block.get_text(' ', strip=True), f'Ordinary block rule missing: {fact}'
for fact in ('4 chunks', '8 Snowballs', 'no standard food properties', '#c:slime_balls', 'chilled: false'):
    assert fact in slime_material_item.get_text(' ', strip=True), f'Ordinary material rule missing: {fact}'
assert Path(slime_material_block.select_one('.reference-overview-media img')['src']).name == 'slime-chunk-block.webp'
assert Path(slime_material_item.select_one('.reference-overview-media img')['src']).name == 'slime-chunk.webp'
from moth_egg_reference import manifest as moth_egg_manifest
moth_data = moth_egg_manifest()
assert not moth_data['crafting_recipes'] and moth_data['hatching']['stages'] == [0, 1, 2], 'Moth crafting or hatch stages changed'
assert moth_data['hatching']['spawn_registry_id'] == 'tensura:hell_caterpillar' and moth_data['hatching']['initial_age'] == -24000, 'Moth hatchling changed'
assert moth_data['hatching']['substrate_tags'] == ['minecraft:leaves', 'minecraft:wool'] and moth_data['item_stack_limit'] == 64, 'Moth substrate or item stack properties changed'
moth_page = BeautifulSoup((site / 'tensura-reference/blocks/blocks-moth-egg/index.html').read_text(encoding='utf-8'), 'html.parser')
for fact in ('Silk Touch level 1 or higher', '1–4 eggs', '#minecraft:wool', '#minecraft:leaves', '0.65', '0.69', 'nextInt(300)', 'Hell Caterpillar', '64-item stack limit', 'one in 100', 'live lifecycle untested'):
    assert fact in moth_page.get_text(' ', strip=True), f'Moth lifecycle rule missing: {fact}'
assert len(moth_page.select('.hipokute-growth li')) == 3, 'Moth hatching route must have three steps'
assert Path(moth_page.select_one('.reference-overview-media img')['src']).name == 'moth-egg.webp'
from charybdis_core_reference import manifest as core_manifest, generate as generate_core
core_data = core_manifest()
assert core_data['artifact_sha1'] in (ROOT / core_data['pack_manifest']).read_text(encoding='utf-8'), 'Core artifact selection changed'
assert core_data['configuration']['sha256'] == hashlib.sha256((ROOT / core_data['configuration']['path']).read_bytes()).hexdigest(), 'Core configuration needs review'
assert not core_data['recipes_referencing_core'] and len(core_data['resources']) == 2 and len(core_data['class_sha256']) == 8, 'Core evidence coverage changed'
assert core_data['light_levels'] == {'inactive': 2, 'active': 12, 'inert': 8}, 'Core phase light levels changed'
assert core_data['charge']['listener_radius'] == 16 and core_data['activation']['primed_fuse_ticks'] == 200 and core_data['activation']['explosion_strength'] == 10, 'Core encounter parameters changed'
assert (ROOT / 'docs/tensura-reference/blocks/blocks-charybdis-core.md').read_text(encoding='utf-8') == generate_core(), 'Stale core lifecycle guide'
core_page = BeautifulSoup((site / 'tensura-reference/blocks/blocks-charybdis-core/index.html').read_text(encoding='utf-8'), 'html.parser')
for fact in ('100,000', '16 blocks', '200-tick fuse', 'strength-10', 'empty hand', 'all calls fail', 'empty resolved list', '12 active', 'live encounter untested'):
    assert fact in core_page.get_text(' ', strip=True), f'Core lifecycle rule missing: {fact}'
assert len(core_page.select('.hipokute-growth li')) == 3 and len(core_page.select('.chilled-crafting-grid article')) == 3, 'Core lifecycle panels missing'
for slug, artwork, status in [('charybdis-core', 'charybdis-core.webp', 'Block recovery checked'), ('inert-charybdis-core', 'inert-charybdis-core.webp', 'Boss death callback checked')]:
    item_page = BeautifulSoup((site / f'tensura-reference/items/{slug}/index.html').read_text(encoding='utf-8'), 'html.parser')
    assert Path(item_page.select_one('.reference-overview-media img')['src']).name == artwork, 'Core item artwork mismatched'
    assert status in item_page.get_text(' ', strip=True) and 'untested' in item_page.get_text(), 'Core item verification scope missing'
from charybdis_cave_reference import manifest as cave_manifest, generate as generate_cave, PAGE as cave_page_path
cave_data = cave_manifest()
assert cave_data['artifact_sha1'] in (ROOT / cave_data['pack_manifest']).read_text(encoding='utf-8'), 'Cave artifact selection changed'
assert len(cave_data['resources']) == 17 and len(cave_data['template_summaries']) == 25, 'Cave resource coverage changed'
assert all(len(item['sha256']) == 64 for item in cave_data['resources'].values()) and all(len(item['sha256']) == 64 for item in cave_data['template_summaries'].values()), 'Cave checksums missing'
active_room = cave_data['template_summaries']['data/tensura/structure/charybdis_cave/charybdis_room_2.nbt']
assert active_room['core_blocks'][0]['nbt']['EP'] == 100000 and active_room['core_palette_entries'][0]['Properties']['sculk_sensor_phase'] == 'active', 'Already-active cave core warning needs review'
assert (ROOT / 'docs' / cave_page_path).read_text(encoding='utf-8') == generate_cave(), 'Stale cave guide'
cave_page = BeautifulSoup((site / cave_page_path.replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
for fact in ('90-chunk spacing', '20-chunk separation', 'already-active core', '100,000 stored EP', 'not a fixed Y=0', 'not a guaranteed room count', '25 packaged cave templates', 'live generation untested'):
    assert fact in cave_page.get_text(' ', strip=True), f'Cave rule or scope missing: {fact}'
assert len(cave_page.select('table tbody tr')) == 4 and len(cave_page.select('.hipokute-growth li')) == 3, 'Cave variant or preparation panels missing'
assert Path(cave_page.select_one('.reference-overview-media img')['src']).name == 'charybdis-cave.webp' and 'Work In Progress' not in cave_page.get_text(), 'Cave non-content media remains'
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
from mechanics_handbook import PAGE as handbook_page_path, generate as generate_handbook
assert (ROOT / 'docs' / handbook_page_path).read_text(encoding='utf-8') == generate_handbook(), 'Stale mechanics handbook'
handbook = BeautifulSoup((site / handbook_page_path.replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
assert len(handbook.select('.mechanics-guide-card > a')) == 6 and len(handbook.select('.mechanics-guide-card img')) == 6, 'Handbook visual routes missing'
assert len(handbook.select('.mechanics-topic-grid article')) == 3 and len(handbook.select('.mechanics-topic-grid a')) == 18, 'Handbook source topics missing'
assert handbook.select_one('#Ingame_Mechanics') and handbook.select_one('#Gamerule_Mechanics'), 'Legacy mechanics anchors missing'
assert Path(handbook.select_one('.reference-overview-media img')['src']).name == 'magic-tome.webp', 'Handbook original artwork missing'
for fact in ('not live gameplay tests', 'does not certify every linked mechanic', 'WIP2 editor portrait is omitted', 'SlimeThrone Extras'):
    assert fact in handbook.get_text(' ', strip=True), f'Handbook source or scope detail missing: {fact}'
assert not any('wip2-56493556c2.png' in page.read_text(encoding='utf-8') for page in (ROOT / 'docs').rglob('*.md')), 'Withdrawn editorial portrait remains in distribution'
from soul_energy_reference import PAGE as soul_page, generate_all as generate_soul_pages
soul_data = json.loads((ROOT / 'data/soul_energy_reference.json').read_text(encoding='utf-8'))
soul_pack = tomllib.loads((ROOT / soul_data['pack_manifest']).read_text(encoding='utf-8'))
assert soul_pack['download']['hash'] == soul_data['artifact_sha1'], 'Stale selected Soul Energy artifact'
assert sum(band['probability_percent'] for band in soul_data['initial_roll']['bands']) == 100, 'Incorrect initial-roll distribution'
assert soul_data['configuration']['General'] == tomllib.loads((ROOT / soul_data['configuration']['path']).read_text(encoding='utf-8'))['General'], 'Stale Soul Energy configuration'
for page, content in generate_soul_pages().items():
    assert (ROOT / 'docs' / page).read_text(encoding='utf-8') == content, f'Stale soul-system page: {page}'
soul_article = BeautifulSoup((site / soul_page.replace('.md', '/index.html')).read_text(encoding='utf-8'), 'html.parser')
assert Path(soul_article.select_one('.reference-overview-media img')['src']).name == 'soul-energy.webp', 'Soul Energy artwork missing'
assert len(soul_article.select('details summary')) >= 2, 'Soul Energy evidence disclosures missing'
for fact in ('uniqueSECost', '100,000–249,999', '500,000–999,999', 'equal to the cost', 'not a complete reset outcome', 'not an in-game icon'):
    assert fact in soul_article.get_text(' ', strip=True), f'Soul Energy detail missing: {fact}'
assert not any('mysticism-wip-6c2780ef0a.png' in page.read_text(encoding='utf-8') for page in (ROOT / 'docs').rglob('*.md')), 'Withdrawn Mysticism portrait remains in distribution'
print('Wiki section checks passed: 11 navigation sections, populated directories, corrected media, source-backed stats and commands, and race configurations')
