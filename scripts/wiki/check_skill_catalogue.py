"""Check skill eligibility, acquisition panels, regeneration, and rendered search."""
from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
from functools import lru_cache
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from skill_catalogue import ACTIVE, ROOT, catalogue, inventory, nightmares_manifest
from sync_skill_catalogue import DOCS, LABELS, MAGIC_SUMMARIES, acquisition, generate, render_acquisition_markdown, route
from skill_presentation import CATEGORIES


class FragmentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'id':
                self.ids.add(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-only", action="store_true")
    args = parser.parse_args()
    outputs = generate()
    generated_pages = json.loads(outputs["assets/data/skill-catalogue.json"])["pages"]
    progression = json.loads((DOCS / 'assets/data/progression.json').read_text(encoding='utf-8'))['nodes']
    errors = []
    nested_routes = '<h2>Obtainment Method</h2><h3 id="first-route">First route</h3><p>Two other Ultimate Skills.</p><h3 id="second-route">Second route</h3><ul><li>Alter Uriel for another player.</li></ul><h2>Usage</h2><p>Not an acquisition condition.</p>'
    nested, documented = acquisition(nested_routes, 'test.md', {'namespace': 'trnightmare', 'category': 'skills/ultimate'})
    if not documented or any(part not in nested for part in ('Two other Ultimate Skills.', 'Alter Uriel for another player.')) or 'Not an acquisition condition.' in nested or 'id=' in nested:
        errors.append('Nested source acquisition routes must remain complete without duplicate IDs or usage text')
    artwork = json.loads((ROOT / 'data/skill_artwork.json').read_text(encoding='utf-8'))['entries']
    for skill_id, entry in artwork.items():
        asset = DOCS / entry['asset']
        if not asset.is_file():
            errors.append(f'Missing reviewed artwork: {skill_id}')
        elif entry['kind'] == 'verified-source' and hashlib.sha256(asset.read_bytes()).hexdigest() != entry['media']['sha256']:
            errors.append(f'Source artwork checksum mismatch: {skill_id}')
        elif entry.get('sha256') and hashlib.sha256(asset.read_bytes()).hexdigest() != entry['sha256']:
            errors.append(f'Original artwork checksum mismatch: {skill_id}')
        original_asset = entry.get('media', {}).get('original_asset')
        if original_asset:
            original_path = DOCS / original_asset
            if not original_path.is_file() or hashlib.sha256(original_path.read_bytes()).hexdigest() != entry['media']['original_sha256']:
                errors.append(f'Original source artwork checksum mismatch: {skill_id}')
    for name, content in outputs.items():
        if not (DOCS / name).exists() or (DOCS / name).read_text(encoding="utf-8") != content:
            errors.append(f"Stale skill output: {name}")
    policy = catalogue()
    pool = inventory()
    nightmares = nightmares_manifest()
    from nightmares_acquisition import review as acquisition_review
    nightmare_review = acquisition_review()
    if nightmare_review['reference_build']['sha256'] != nightmares['reference_build']['sha256']:
        errors.append('Nightmares acquisition review artifact drifted')
    if nightmare_review['reference_build']['installed_version_verified'] is not False:
        errors.append('Nightmares reference acquisition promoted to installed verification')
    if len(nightmare_review['class_sha256']) != 10 or nightmare_review['asmodeus']['resource_check'] != 'EnergyHelper.getMaxMagicule(player) + 0.000001 >= getDefaultAcquiringMagiculeCost()':
        errors.append('Asmodeus acquisition evidence or capacity metric drifted')
    if nightmare_review['asmodeus']['reference_gamerule_defaults'] != {'nightmare_ultimates': False, 'auto_evolve': False}:
        errors.append('Asmodeus reference evolution defaults drifted')
    client_record = nightmare_review['client_inventory']
    client_inventory = json.loads((ROOT / client_record['record']).read_text(encoding='utf-8'))
    matched = [entry for entry in client_inventory['mods'] if entry['filename'] == nightmare_review['reference_build']['filename']]
    if len(matched) != 1 or not matched[0]['enabled'] or client_inventory['captured_on'] != client_record['captured_on']:
        errors.append('Nightmares client filename evidence drifted')
    asmodeus = BeautifulSoup(outputs['tensura-reference/skills/ultimate/nightmares-asmodeus.md'], 'html.parser')
    reviewed_panel = asmodeus.select_one('.nightmares-acquisition-review')
    if not reviewed_panel or len(reviewed_panel.select('.skill-reading-guide > div')) != 3:
        errors.append('Asmodeus acquisition route panels missing')
    reviewed_text = reviewed_panel.get_text(' ', strip=True) if reviewed_panel else ''
    for phrase in ('1,200,000', 'maximum Magicules', '25 entities named', '100 animals bred', 'ENTITY_NAMED', 'ANIMALS_BRED', 'auto_evolve', 'nightmare_ultimates', 'forgets Lust', 'not a complete effect audit'):
        if phrase not in reviewed_text:
            errors.append(f'Asmodeus acquisition fact missing: {phrase}')
    lust_article = BeautifulSoup(outputs['tensura-reference/skills/unique/lust.md'], 'html.parser')
    successor_link = lust_article.select_one('.skill-successor-note a')
    if not successor_link or 'nightmares-asmodeus' not in successor_link['href']:
        errors.append('Lust successor guidance missing')
    from lucifer_acquisition import review as lucifer_review
    lucifer_data = lucifer_review()
    if lucifer_data['reference_build']['sha256'] != nightmares['reference_build']['sha256'] or lucifer_data['reference_build']['installed_version_verified'] is not False:
        errors.append('Lucifer acquisition artifact identity or coverage drifted')
    import tomllib
    base_predicate = lucifer_data['base_predicate_reference']
    base_manifest = tomllib.loads((ROOT / base_predicate['manifest']).read_text(encoding='utf-8'))
    if base_predicate['sha1'] != base_manifest['download']['hash'] or len(lucifer_data['class_sha256']) != 6:
        errors.append('Lucifer predecessor or configuration evidence drifted')
    lucifer = BeautifulSoup(outputs['tensura-reference/skills/ultimate/nightmares-lucifer.md'], 'html.parser')
    lucifer_panel = lucifer.select_one('.nightmares-acquisition-review')
    if not lucifer_panel or len(lucifer_panel.select('.skill-reading-guide > div')) != 3:
        errors.append('Lucifer acquisition route panels missing')
    lucifer_text = lucifer_panel.get_text(' ', strip=True) if lucifer_panel else ''
    for phrase in ('non-temporary', '100 mastered skill instances', '1,700,000 maximum Magicules', '40% of maximum health', 'getHealth() / getMaxHealth() <= configured percentage', 'No Ultimate-skill hit condition', 'removes Pride', '15,000'):
        if phrase not in lucifer_text:
            errors.append(f'Lucifer acquisition fact missing: {phrase}')
    mastery_cell = lucifer.select_one('.druid-data-PointstoMaster')
    if not mastery_cell or mastery_cell.get_text(' ', strip=True) != '15,000 (reference default)':
        errors.append('Lucifer mastery infobox retained the older source value')
    pride_article = BeautifulSoup(outputs['tensura-reference/skills/unique/pride.md'], 'html.parser')
    pride_successor = pride_article.select_one('.skill-successor-note a')
    if not pride_successor or 'nightmares-lucifer' not in pride_successor['href']:
        errors.append('Pride successor guidance missing')
    from belphegor_acquisition import review as belphegor_review
    belphegor_data = belphegor_review()
    if belphegor_data['reference_build']['sha256'] != nightmares['reference_build']['sha256'] or belphegor_data['reference_build']['installed_version_verified'] is not False or len(belphegor_data['class_sha256']) != 8:
        errors.append('Belphegor acquisition identity, scope, or class coverage drifted')
    bed_facts = belphegor_data['belphegor']
    if bed_facts['default_bed_ticks'] != bed_facts['default_bed_minutes'] * 60 * 20 or bed_facts['default_designer_bed_minutes'] != 60:
        errors.append('Belphegor bed threshold confused with shared tracker configuration')
    belphegor = BeautifulSoup(outputs['tensura-reference/skills/ultimate/nightmares-belphegor.md'], 'html.parser')
    bed_panel = belphegor.select_one('.nightmares-acquisition-review')
    if not bed_panel or len(bed_panel.select('.skill-reading-guide > div')) != 3:
        errors.append('Belphegor acquisition route panels missing')
    bed_text = bed_panel.get_text(' ', strip=True) if bed_panel else ''
    for phrase in ('permanent', '25,000 stored Magicules', '12,000 recorded ticks', 'standing still on a bed', '1,000 recorded mob kills', '1,000,000 maximum Magicules', 'does not reset', 'nonpositive value resets', 'Stats.MOB_KILLS', 'removes Sloth', '15,000', 'auto_evolve', 'nightmare_ultimates'):
        if phrase not in bed_text:
            errors.append(f'Belphegor acquisition fact missing: {phrase}')
    bed_mastery = belphegor.select_one('.druid-data-PointstoMaster')
    bed_row = belphegor.select_one('.druid-data-Other2')
    if not bed_mastery or bed_mastery.get_text(' ', strip=True) != '15,000 (reference default)' or not bed_row or 'standing-still-on-bed' not in bed_row.get_text():
        errors.append('Belphegor infobox retains older mastery or sleeping wording')
    sloth_article = BeautifulSoup(outputs['tensura-reference/skills/unique/sloth.md'], 'html.parser')
    sloth_successor = sloth_article.select_one('.skill-successor-note a')
    if not sloth_successor or 'nightmares-belphegor' not in sloth_successor['href']:
        errors.append('Sloth successor guidance missing')
    resistance_records = json.loads((ROOT / "data/upstream_tensura_pages.json").read_text(encoding="utf-8"))["pages"]
    resistance_entries = {page: decision for page, decision in policy["pages"].items() if decision["namespace"] == "tensura" and decision["category"] == "resistances" and decision["status"] in ACTIVE}
    if len(resistance_entries) != 42:
        errors.append("Core resistance catalogue must include 42 matched player entries, excluding command-only Holy Attack Nullification and Magic Nullification")
    if policy["pages"].get("tensura-reference/resistances/holy-attack-nullification.md", {}).get("status") != "unavailable":
        errors.append("Command-only Holy Attack Nullification must remain reference-only")
    for record in resistance_records:
        if record["category"] == "resistances" and record["local_page"] not in policy["pages"] and record['local_page'] != 'tensura-reference/resistances/spellbinding-table.md':
            errors.append(f'Resistance article missing a registry decision: {record["local_page"]}')
    if 'tensura-reference/resistances/spellbinding-table.md' in policy['pages']:
        errors.append("Spellbinding Table must not be presented as a resistance skill")
    battlewill_entries = {page: decision for page, decision in policy['pages'].items() if decision['namespace'] == 'tensura' and decision['category'] == 'battlewill' and decision['status'] in ACTIVE}
    if len(battlewill_entries) != 23 or len({decision['id'] for decision in battlewill_entries.values()}) != 23:
        errors.append('Core Battlewill catalogue must include 23 distinct registry-matched techniques')
    if policy['pages'].get('tensura-reference/battlewill/items-misc-battlewill-manual.md', {}).get('status') != 'guide':
        errors.append('Battlewill Manual must not be presented as an ability')
    for page, decision in battlewill_entries.items():
        panel = BeautifulSoup(outputs[page], 'html.parser').select_one('.skill-obtainment')
        if not panel:
            errors.append(f'Battlewill learning panel missing: {page}')
        elif decision['id'] == 'tensura:five_petals_thrust' and 'Normal acquisition unverified' not in panel.get_text():
            errors.append('Five Petals Thrust must not invent a random-manual or mastery acquisition route')
    active = {p: d for p, d in policy["pages"].items() if d["status"] in ACTIVE}
    for page, decision in active.items():
        if generated_pages[page].get('asset', '').startswith('assets/icons/skills/'):
            errors.append(f'Legacy emblem returned to a completed skill category: {page}')
        article = BeautifulSoup(outputs[page], 'html.parser')
        if any(re.fullmatch(r'x|\?{2,}|TBD|Coming soon', cell.get_text(strip=True), re.I) for cell in article.select('.druid-data')):
            errors.append(f'Undefined infobox placeholder in active skill: {page}')
    sandalphon = BeautifulSoup(outputs['tensura-reference/skills/ultimate/nightmares-sandalphon-judgment.md'], 'html.parser')
    flame_nullification = BeautifulSoup(outputs['tensura-reference/resistances/flame-attack-nullification.md'], 'html.parser')
    if any(value not in flame_nullification.select_one('.skill-obtainment').get_text(' ', strip=True) for value in ('Ghast', 'Flame Attack Resistance')):
        errors.append('Flame Attack Nullification acquisition panel omits a reviewed source route')
    if sandalphon.select_one('#Passive_2').get_text(strip=True) != 'Active abilities':
        errors.append('Sandalphon active abilities mislabeled as passives')
    active_routes = {route(p): d for p, d in active.items()}
    ability_search = json.loads(outputs['assets/data/skill-search.json'])
    if {entry['route'] for entry in ability_search} != set(active_routes) or len(ability_search) != len(active_routes):
        errors.append('Ability search must contain each active skill exactly once')
    for entry in ability_search:
        decision = active_routes.get(entry['route'])
        if decision and any(entry[key] != decision[key] for key in ('title', 'category', 'status')):
            errors.append(f'Ability search loses catalogue metadata: {entry["route"]}')
        if not entry['image'] or not (DOCS / entry['image']).is_file():
            errors.append(f'Ability search image missing: {entry["route"]}')
    hub_page = 'tensura-reference/skills/index.md'
    hub = BeautifulSoup(outputs[hub_page], 'html.parser')
    tiles = hub.select('.skill-category-tile')
    targets = {posixpath.normpath(posixpath.join(route(hub_page), tile['href'])).rstrip('/') for tile in tiles}
    if targets != {'tensura-reference/' + category for category in CATEGORIES} or len(tiles) != 8:
        errors.append('Ability hub must link to all eight unified categories')
    for tile in tiles:
        destination = posixpath.normpath(posixpath.join(route(hub_page), tile['href']))
        directory = BeautifulSoup(outputs[destination.rstrip('/') + '/index.md'], 'html.parser')
        if tile.select_one('.skill-category-count').get_text() != f'{len(directory.select(".reference-card"))} entries':
            errors.append(f'Ability hub category count mismatch: {destination}')
    if not BeautifulSoup(outputs['tensura-reference/battlewill/index.md'], 'html.parser').select_one('.reference-directory-overview-link'):
        errors.append('Battlewill overview link missing')
    if not hub.select_one('label[for="skill-hub-search"]') or not hub.select_one('.skill-finder-status[role="status"]'):
        errors.append('Ability search lacks its accessible label or status')
    if not hub.select_one('.reference-media-credits a[href]'):
        errors.append('Ability hub lacks image attribution')
    for page in ("mysticism-reference/core-mechanics/effects-lightning-mode.md", "tensura-reference/magic/magic-tome.md", "tensura-reference/magic/anti-magic-mask.md"):
        if page in policy["pages"]:
            errors.append(f"Non-skill name collision: {page}")
    for page, identifier in {
        "tensura-reference/magic/aspectual-possession.md": "tensura:possession_magic",
        "tensura-reference/magic/aspectual-strength.md": "tensura:strength_aspectual",
        "tensura-reference/magic/fire-spiritual.md": "tensura:fire",
        "tensura-reference/magic/water-spiritual.md": "tensura:water",
    }.items():
        if active.get(page, {}).get("id") != identifier:
            errors.append(f"Spell registry mapping mismatch: {page}")
    if policy['pages']['tensura-reference/magic/magic-nullification.md']['status'] != 'unavailable':
        errors.append('Command-only Magic Nullification must be reference-only')
    magic = BeautifulSoup(outputs['tensura-reference/magic/index.md'], 'html.parser')
    magic_cards = magic.select('.reference-card')
    if len(magic_cards) != 121 or any(card.get('data-school') not in {'Aspectual', 'Spiritual', 'Summoning'} for card in magic_cards):
        errors.append('Magic directory must contain 121 registry-matched, school-classified spells')
    if len(magic.select('[data-school-filter]')) != 4:
        errors.append('Magic directory needs all three accessible school filters and an all-schools reset')
    for name, summary in MAGIC_SUMMARIES.items():
        page = 'tensura-reference/core-mechanics/reincarnation.md' if name == 'reincarnation' else 'tensura-reference/magic/' + name + '.md'
        article = BeautifulSoup(outputs[page], 'html.parser')
        overview = article.select_one('.reference-overview-copy > p:not(.reference-eyebrow)')
        body_intro = article.select_one('.tensura-reference-article .mw-parser-output').find('p', recursive=False)
        if any(node is None or node.get_text(' ', strip=True) != summary for node in (overview, body_intro)):
            errors.append(f'Magic editorial summary mismatch: {page}')
        if summary not in magic.get_text(' ', strip=True):
            errors.append(f'Magic directory lost its editorial summary: {page}')
    for identifier in ('tensura:reincarnation', 'tensura:summon_hound_dog'):
        if sum(decision['id'] == identifier and decision['category'] == 'magic' for decision in active.values()) != 1:
            errors.append(f'Missing or duplicate recovered spell: {identifier}')
    registered_magic = {identifier for identifier, entry in pool.items() if entry['category'] == 'magic' and entry['weight'] > 0 and identifier not in {'tensura:magic_nullification'}}
    represented_magic = {decision['id'] for decision in active.values() if decision['category'] == 'magic' and decision['namespace'] != 'trnightmare'}
    if registered_magic != represented_magic:
        errors.append(f'Magic inventory coverage mismatch: {sorted(registered_magic ^ represented_magic)}')
    reincarnation = outputs['tensura-reference/core-mechanics/reincarnation.md']
    hound = outputs['tensura-reference/magic/summon-hound-dog.md']
    for phrase in ('Reincarnation is not prestige', 'temporary skills', 'warp points', 'live-server reset test'):
        if phrase not in reincarnation:
            errors.append(f'Reincarnation safety note missing: {phrase}')
    if 'POST_TAME_EVENT' not in hound or 'snake-tailed variant' not in hound or '50 MP' not in hound or '10 MP per second' not in hound:
        errors.append('Hound Dog acquisition or configured upkeep evidence missing')
    for page, decision in active.items():
        if decision['category'] != 'magic':
            continue
        for anchor in BeautifulSoup(outputs[page], 'html.parser').select('.reference-related-card'):
            target = posixpath.normpath(posixpath.join(route(page), urlsplit(anchor['href']).path)).rstrip('/') + '.md'
            if target not in active:
                errors.append(f'Magic recommendation is not an available ability: {page} -> {target}')
    for guide in ('magic-learning.md',):
        if not (DOCS / guide).is_file():
            errors.append(f'Magic learning guide missing: {guide}')
    if active["tensura-reference/skills/intrinsic/angel-wings.md"]["category"] != "skills/extra":
        errors.append("Angel Wings must use its Extra classification")
    if active["tensura-reference/skills/extra/purple-lightning.md"]["category"] != "magic":
        errors.append("Purple Lightning must use its Magic classification")
    ultimate = BeautifulSoup(outputs["tensura-reference/skills/ultimate/index.md"], "html.parser")
    if "Ultimate Skill Aquisition" in ultimate.get_text() or "Angel evolution" in ultimate.get_text():
        errors.append("Guide or race card in Ultimate Skills")
    seen = set()
    for category in LABELS:
        page = "tensura-reference/" + category + "/index.md"
        soup = BeautifulSoup(outputs[page], "html.parser")
        if soup.select_one('.reference-directory-hero') or not soup.select_one('.skill-directory-heading'):
            errors.append(f'Legacy ability banner remains: {page}')
        for link in soup.select(".reference-card > a[href]"):
            target = posixpath.normpath(posixpath.join(route(page), urlsplit(link["href"]).path)).rstrip("/") + "/"
            decision = active_routes.get(target)
            if not decision:
                if category.startswith("skills/"):
                    errors.append(f"Unregistered skill card: {target}")
                continue
            if decision["category"] != category:
                errors.append(f"Incorrect class: {target}")
            if decision.get('artwork_kind') == 'original-illustration' and 'TSR artwork' not in link.get_text():
                errors.append(f'Original skill card mislabeled as source media: {target}')
            if decision['id'] in artwork:
                preview = link.select_one('img[src]')
                if not preview or posixpath.normpath(posixpath.join(route(page), preview['src'])) != artwork[decision['id']]['asset']:
                    errors.append(f'Reviewed skill artwork differs on its directory card: {target}')
            if decision["id"] in seen:
                errors.append(f"Duplicate skill card: {decision['id']}")
            seen.add(decision["id"])
    for page, decision in active.items():
        expected = pool if decision["status"] == "registered" else nightmares["registry"]
        if decision["id"] not in expected or decision["id"] not in seen:
            errors.append(f"Registered skill missing from directories: {page}")
        soup = BeautifulSoup(outputs[page], "html.parser")
        if len(soup.select(".skill-obtainment #how-to-obtain")) != 1:
            errors.append(f"Missing or duplicate obtainment panel: {page}")
        if not decision.get("maintained"):
            if outputs[page].find('<section class="reference-overview ') > outputs[page].find('<section class="skill-obtainment"'):
                errors.append(f"Obtainment panel obscures visual overview: {page}")
            if not soup.select_one('.reference-quick-jumps a[href="#how-to-obtain"]'):
                errors.append(f"Missing obtainment jump: {page}")
        if decision["namespace"] in {"mysticism", "trnightmare"} or decision['id'] in artwork:
            previews = soup.select(".reference-overview img, .skill-detail-hero img")
            asset = generated_pages[page].get("asset")
            if progression.get(route(page), {}).get('image') != asset:
                errors.append(f'Skill progression image differs from its verified article icon: {page}')
            if not previews or not asset or any(
                posixpath.normpath(posixpath.join(route(page), image["src"])) != asset
                for image in previews
            ):
                errors.append(f"Missing verified skill icon: {page}")
            if asset and asset.startswith("assets/upstream/") and not soup.select_one(".reference-overview-media figcaption a[href]"):
                errors.append(f"Missing source-icon credit: {page}")
            if any("wip" in image.get("src", "").casefold() for image in soup.select("img")):
                errors.append(f"Editorial placeholder remains: {page}")
            if decision.get('artwork_kind') == 'original-illustration':
                if not asset.startswith('assets/illustrations/skills/') or 'TSR skill artwork' not in soup.get_text():
                    errors.append(f'Original skill artwork missing its identity: {page}')
                old_asset = 'assets/icons/skills/' + decision['id'].replace(':', '-') + '.svg'
                if old_asset in outputs[page] or any(entry['route'] == route(page) and entry['image'] != asset for entry in ability_search):
                    errors.append(f'Skill illustration reverted to a legacy emblem: {page}')
            if decision['id'] in artwork:
                reviewed = artwork[decision['id']]
                if asset != reviewed['asset'] or any(entry['route'] == route(page) and entry['image'] != asset for entry in ability_search):
                    errors.append(f'Reviewed skill artwork differs between surfaces: {page}')
                if 'assets/icons/skills/' + decision['id'].replace(':', '-') + '.svg' in outputs[page]:
                    errors.append(f'Legacy skill emblem remains: {page}')
                if '<!-- skill-artwork-credit:start -->' not in outputs[page]:
                    errors.append(f'Reviewed artwork lacks its article credit: {page}')
                if reviewed['kind'] == 'verified-source':
                    media = reviewed['media']
                    if any(media[key] not in outputs[page] for key in ('source_file_page', 'uploader', 'license_url', 'modifications')):
                        errors.append(f'Incomplete source artwork attribution: {page}')
        if decision["status"] == "reference":
            if "Server build match pending." not in soup.get_text() or "Pinned pack inventory" in soup.get_text():
                errors.append(f"Reference build presented as installed: {page}")
            if "<strong>:</strong>" in outputs[page]:
                errors.append(f"Empty acquisition label: {page}")
            if decision["source"] not in outputs[page] or "## Source and licensing" not in outputs[page]:
                errors.append(f"Missing Nightmares attribution: {page}")
            if not soup.select_one('.skill-category-nav a[href]'):
                errors.append(f"Missing unified skill navigation: {page}")
    if "trnightmare:sandalphon_punishment" in seen:
        errors.append("Non-gameplay Sandalphon variant in normal directories")
    for record in nightmares["pages"]:
        soup = BeautifulSoup(outputs[record["local_page"]], "html.parser")
        if policy['pages'][record['local_page']]['status'] not in ACTIVE:
            if soup.select_one('.skill-obtainment') or not soup.select_one('.skill-availability') or record['registry_id'] in seen or route(record['local_page']) in progression:
                errors.append(f'Unavailable Nightmares skill promoted as normal progression: {record["registry_id"]}')
            continue
        panel_text = re.sub(r"\s+", "", soup.select_one(".skill-obtainment").get_text(" ", strip=True))
        # The reviewed route supersedes the older vague resource/headcount wording.
        reviewed_routes = {nightmare_review['asmodeus']['registry_id'], lucifer_data['lucifer']['registry_id'], bed_facts['registry_id']}
        source_rows = [] if record['registry_id'] in reviewed_routes else record['obtainment_rows']
        for row in source_rows:
            if re.sub(r"\s+", "", row["text"]) not in panel_text:
                errors.append(f"Source obtainment condition dropped: {record['registry_id']} / {row['label']}")
        if record['registry_id'] == 'trnightmare:shub_niggurath' and any(condition not in panel_text for condition in ('100SkillsMastered', 'MethodTwo:', 'Raguel')):
            errors.append('Shub-Niggurath acquisition panel omits a documented route')
    sample = render_acquisition_markdown("[Skill](../unique/great-mage.md#great-mage)", "tensura-reference/skills/ultimate/the-timeless-mage.md")
    if 'href="../../unique/great-mage/#great-mage"' not in sample:
        errors.append("Markdown acquisition route conversion failed")
    if not args.source_only:
        @lru_cache(maxsize=None)
        def fragment_ids(path):
            parser = FragmentParser()
            parser.feed(path.read_text(encoding='utf-8'))
            return parser.ids

        site = ROOT / "site"
        for page in [hub_page] + ['tensura-reference/' + category + '/index.md' for category in LABELS]:
            document = site / route(page) / 'index.html'
            section = BeautifulSoup(document.read_text(encoding='utf-8'), 'html.parser')
            for element in section.select('.skill-hub a[href], .skill-hub img[src], .skill-type-nav a[href]'):
                value = element.get('href') or element['src']
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                destination = (document.parent / unquote(url.path)).resolve()
                if destination.is_dir():
                    destination /= 'index.html'
                if not destination.is_relative_to(site.resolve()) or not destination.is_file():
                    errors.append(f'Missing ability hub destination: {page} -> {value}')
        search = json.loads((site / "search/search_index.json").read_text(encoding="utf-8"))
        indexed = {entry["location"].split("#")[0] for entry in search["docs"]}
        parsed = {}
        graph = json.loads((site / "assets/data/progression.json").read_text(encoding="utf-8"))
        by_id = {d["id"]: route(page) for page, d in active.items()}
        connections = {(edge["from"], edge["to"]) for edge in graph["edges"]}
        for start, end in (("trnightmare:raphael_knowledge", "trnightmare:raphael_wisdom"), ("trnightmare:babylon", "trnightmare:gilgamesh_lord_of_treasures"), ("trnightmare:gilgamesh_lord_of_treasures", "trnightmare:gilgamesh_king_of_uruk")):
            if start not in by_id or end not in by_id or (by_id[start], by_id[end]) not in connections:
                errors.append(f"Missing variant progression: {start} -> {end}")
        for page, decision in active.items():
            if decision["status"] == "reference" and graph["nodes"].get(route(page), {}).get("verification") != "reference-build-only":
                errors.append(f"Progression loses reference-build status: {page}")
        for page, decision in policy["pages"].items():
            key = route(page)
            if decision["status"] not in ACTIVE:
                if key in indexed:
                    errors.append(f"Historical skill or guide appears in search: {key}")
                continue
            document = site / key / "index.html"
            soup = BeautifulSoup(document.read_text(encoding="utf-8"), "html.parser")
            parsed[key] = soup
            if len(soup.select("#how-to-obtain")) != 1:
                errors.append(f"Rendered obtainment heading mismatch: {key}")
            for anchor in soup.select(".skill-obtainment a[href], .skill-category-nav a[href], .reference-related a[href], .reference-quick-jumps a[href]"):
                url = urlsplit(anchor["href"])
                if url.scheme or url.netloc:
                    continue
                destination = (document.parent / unquote(url.path)).resolve()
                if destination.is_dir():
                    destination /= "index.html"
                if not destination.is_relative_to(site.resolve()) or not destination.is_file():
                    errors.append(f"Missing skill reading link: {key} -> {anchor['href']}")
                elif url.fragment:
                    if unquote(url.fragment) not in fragment_ids(destination):
                        errors.append(f"Missing skill reading fragment: {key} -> {anchor['href']}")
    if errors:
        raise SystemExit("\n".join(errors))
    pinned = sum(d["status"] == "registered" for d in active.values())
    print(f"Skill catalogue checks passed: {len(active)} pages, {len(seen)} unique entries ({pinned} pinned, {len(active) - pinned} reference-build); " + ("source checks" if args.source_only else "source, rendered links, and search checks"))


if __name__ == "__main__":
    main()
