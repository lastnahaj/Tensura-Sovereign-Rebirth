"""Render verified item references and preserve unsupported source names as archives."""
from __future__ import annotations

import argparse
import html
import json
import posixpath
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
        record['category'] = page.get('category', record['category'])
        record['_summary_override'] = page['summary']
        record['_catalogue_entry'] = page['catalogue_entry']
        record['_availability_status'] = page.get('status')
        record['_stat_source_note'] = 'Pinned Tensura 2.0.1.2 artifact.'
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
        items_link = posixpath.relpath('tensura-reference/items/index.md', posixpath.dirname(page['local_page']))
        guide_link = posixpath.relpath('tensura-reference/items/healing-potions.md', posixpath.dirname(page['local_page']))
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
            lines.extend([f'!!! {page.get("notice_kind", "warning")} "{page["status"]}"', f'    {page["warning"]}', '',
                          '<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">',
                          f'<div class="druid-title">{title}</div>',
                          f'<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">{page["registry_id"]}</div></div>',
                          f'<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura {build["version"]} · Minecraft {build["minecraft"]}</div></div>',
                          '<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">' + (html.escape(page['status']) if page.get('acquisition_verified') else 'Survival route not verified') + '</div></div>', '</aside></div></div>', '',
                          '## Availability', '', page['obtainment'], '', '## How to use', '', page['use'], '', '## Behavior and limits', '', page['effects'], ''])
            if page.get('related_guide'):
                related = posixpath.relpath('tensura-reference/items/' + page['related_guide'], posixpath.dirname(page['local_page']))
                lines.extend([f'[Compare Magic Crystal tiers]({related})', ''])
            elif page.get('brew_routes') or 'magic_bottle' in page['registry_id']:
                lines.extend([f'[Compare recipes in the healing-potion guide]({guide_link})', ''])
        else:
            lines.extend(['!!! warning "Source archive · not verified for current play"', '    This name is preserved for existing links, not recommended as an obtainable item.', '',
                          '<div class="tensura-reference-article">', '<p>This upstream article does not contain usable obtainment or effect documentation.</p>', '</div>', '',
                          '## Availability', '', page['detail'], ''])
        lines.extend([f'[Return to Items]({items_link})', '', '## Source and licensing', '',
                      f'Upstream reference: [{source["source_title"]}]({source["source_url"]}) on the Tensura: Reincarnated Wiki, recorded revision `{source["revision_id"]}`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.', '',
                      f'Implementation check: [Tensura {build["version"]} release]({build["source_url"]}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{build["pack_manifest"]}). Artifact SHA-1: `{build["sha1"]}`. Registration and code checks are not live-server gameplay tests.', ''])
        if page.get('asset'):
            lines.extend(['The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.', ''])
        if page.get('evidence_paths'):
            lines.extend(['??? info "Artifact evidence"', ''])
            lines.extend(f'    - `{path}`' for path in page['evidence_paths'])
            lines.append('')
        output[page['local_page']] = '\n'.join(lines)
    output['tensura-reference/items/healing-potions.md'] = generate_guide(data)
    output['tensura-reference/items/magic-crystals.md'] = generate_crystal_guide(data)
    return output


def generate_crystal_guide(data):
    crystals = [page for page in data['pages'] if page.get('crystal_tier')]
    lines = ['---', 'title: Magic Crystals', 'description: Compare crystal loot rules, absorption, bottle yields, storage, and schematic-gated downgrades for Minecraft 1.21.1.', '---', '',
             '<section class="potion-guide">', '<header class="potion-guide-heading">', '<p class="reference-eyebrow">Materials field guide · Minecraft 1.21.1</p>',
             '<h1>Choose how to use your crystals</h1>', '<p>Keep crystals for crafting, turn them into brewing containers, or recover MP with Absorb &amp; Dissolve. These values are checked against Tensura 2.0.1.2 and TSR’s checked-in configuration.</p>', '</header>', '<div class="potion-guide-grid">']
    for page in crystals:
        route = Path(page['local_page']).stem
        lines.extend(['<article class="potion-guide-card">', f'<a href="../../magic/{route}/" aria-label="Read {page["display_title"]}"><img src="../../../{page["asset"]}" alt="{page["display_title"]} illustration" loading="lazy" decoding="async"><h2>{page["crystal_tier"]} Quality</h2></a>',
                      f'<dl><div><dt>Absorption</dt><dd>{page["dissolve_mp"]:,} <small>base MP per crystal</small></dd></div><div><dt>Bottle recipe</dt><dd>{page["bottle_yield"]} <small>bottles per crystal + 3 Glass</small></dd></div></dl>',
                      '<p>' + html.escape(page['loot_band']) + '</p>', '</article>'])
    lines.extend(['</div>', '</section>', '', '## Find eligible drops', '',
                  'The shared loot rule requires membership in the `tensura:drop_crystal` entity tag. It tests maximum EP after the namespace multiplier, excludes `MOB_SUMMONED` and `TRIGGERED` spawn types, and requires named-evolution entities to permit crystal drops. A species name or boss label alone is not enough.', '',
                  'The rule checks Medium at **3,000–8,999 inclusive**, then High at **9,000 or more**, then Low as a fallback at **1 or more**. The usual whole-number Low range is 1–2,999. Fractional values between 8,999 and 9,000 fall through to Low; zero EP does not pass the shared rule. Other entity-specific or add-on loot is outside this check.', '',
                  '## Recover MP, not maximum MP', '',
                  'Hold one crystal in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md). The implementation consumes one item. Base recovery is 1,000 / 2,500 / 5,000 MP for Low / Medium / High, multiplied by the skill’s `magiculeMultiplier`. TSR’s checked-in value is **1.0**. This does not grant permanent maximum MP.', '',
                  '## Store or downgrade', '',
                  'Fill a 3×3 crafting grid with nine same-quality crystals to craft their storage block. Unpacking that block gives nine crystals of the same quality.', '',
                  'At a **Smithing Bench**, with the [Low Magisteel Gear Schematic](items-schematics-low-magisteel-gear-schematic.md):', '',
                  '- One High crystal becomes **two Medium** crystals.', '- One Medium crystal becomes **two Low** crystals.', '',
                  'These checked recipes run downward only; they do not prove an upgrade recipe. Without the required schematic, the downgrade route is incomplete.', '',
                  '## Prepare your brewing kit', '',
                  'Combine one crystal with three Glass: Glass–Crystal–Glass across a row, then Glass beneath the crystal. Low produces **3**, Medium **6**, and High **9** [Magic Bottles](../magic/magic-bottle.md). Continue with the [healing-potion guide](healing-potions.md) for filling, cooking, and brewing.', '',
                  '!!! note "Verification scope"', '    Registry, recipe, loot-predicate, and configuration checks are not live-server gameplay tests. Server overrides and unreviewed trading routes are not guaranteed here.', '',
                  '[Return to Items](index.md)', '', '## Sources and artwork', '',
                  'The individual [Low](../magic/low-quality-magic-crystal.md), [Medium](../magic/medium-quality-magic-crystal.md), and [High](../magic/high-quality-magic-crystal.md) references cite upstream revisions and exact artifact evidence. Adapted text remains under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
                  'Implementation: [Tensura 2.0.1.2 release](' + data['reference_build']['source_url'] + ') · [TSR item evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json). The original illustrations are not in-game texture or appearance guarantees.', ''])
    return '\n'.join(lines)


def generate_guide(data):
    potions = [page for page in data['pages'] if page.get('brew_routes')]
    bases = {'water': 'Magic Bottle of Water', 'vacuumed': 'Vacuumed Magic Bottle of Water'}
    reagents = {'grass': 'Hipokute Grass', 'flower': 'Hipokute Flower'}
    lines = ['---', 'title: Healing Potions', 'description: Compare verified brewing routes, healing, MP recovery, and bottle preparation for the pinned 1.21.1 build.', '---', '',
             '<section class="potion-guide" data-potion-planner>', '<header class="potion-guide-heading">', '<p class="reference-eyebrow">Field alchemy · Minecraft 1.21.1</p>',
             '<h1>Build your recovery kit</h1>', '<p>Match the bottle and Hipokute ingredient to the potion you need. These four brewing combinations are checked against Tensura 2.0.1.2.</p>', '</header>',
             '<div class="potion-planner-controls">',
             '<label for="potion-base">Bottle base<select id="potion-base" data-potion-base><option value="water">Magic Bottle of Water</option><option value="vacuumed">Vacuumed Magic Bottle of Water</option></select></label>',
             '<label for="potion-reagent">Ingredient<select id="potion-reagent" data-potion-reagent><option value="grass">Hipokute Grass</option><option value="flower">Hipokute Flower</option></select></label>', '</div>',
             '<p class="potion-planner-status" aria-live="polite" data-potion-status>Choose a bottle and ingredient to highlight the matching brewing result.</p>', '<div class="potion-guide-grid">']
    for page in potions:
        combos = ' '.join(route['base'] + ':' + route['reagent'] for route in page['brew_routes'])
        route = Path(page['local_page']).stem
        recipes = ''.join(f'<li><span>{bases[recipe["base"]]}</span><b aria-hidden="true">+</b><span>{reagents[recipe["reagent"]]}</span></li>' for recipe in page['brew_routes'])
        lines.extend([f'<article class="potion-guide-card" data-potion-result="{combos}" data-potion-title="{page["display_title"]}">',
                      '<span class="potion-selected" data-potion-selected hidden>Matching brew</span>',
                      f'<a href="../{route}/" aria-label="Read {page["display_title"]}"><img src="../../../{page["asset"]}" alt="{page["display_title"]} illustration" loading="lazy" decoding="async"><h2>{page["display_title"]}</h2></a>',
                      f'<dl><div><dt>Health restored</dt><dd>{page["hp_percent"]}% <small>of maximum HP</small></dd></div><div><dt>MP restored</dt><dd>{page["mp"]:,} <small>fixed MP</small></dd></div></dl>',
                      f'<ul class="potion-recipe-list" aria-label="{page["display_title"]} brewing recipes">{recipes}</ul>', '</article>'])
    lines.extend(['</div>', '<p class="potion-guide-footnote">Original TSR illustrations, not in-game textures. Healing values assume full effect strength; thrown splash strength can be lower. MP recovery is capped at maximum MP.</p>', '</section>', '',
                  '<div class="tensura-reference-article"><p>Brewing recipes are distinct from Tensura Refining recipes. The planner only represents the ordinary brewing registrations.</p></div>', '',
                  '## Prepare the bottles', '',
                  '1. Craft Magic Bottles from three Glass and one Magic Crystal. The pinned recipes yield **3** bottles with a Low Quality crystal, **6** with Medium Quality, or **9** with High Quality. Place Glass around the crystal in the top row and a third Glass below it.',
                  '2. Use an empty Magic Bottle on a water source to fill it. The item checks interaction permission and source-water targeting.',
                  '3. For a vacuumed base, cook the filled bottle: **60 ticks** in a furnace or smoker, or **180 ticks** on a campfire. That is 3 or 9 seconds at 20 TPS, excluding setup and any fuel requirements.', '',
                  '**Ingredient references:** [Hipokute Grass](hipokute-grass.md) · [Hipokute Flower](hipokute-flower.md) · [Magic Bottle](../magic/magic-bottle.md) · [Filled bottle](../magic/magic-bottle-of-water.md)', '',
                  '## Use the potion safely', '',
                  'Drink normally, sneak-use to throw, or interact directly with a living target. Drinking takes **16 ticks** and returns an empty Magic Bottle in survival. The pinned potion stack limit is **16**. These items restore current health and MP; they do not raise permanent maximums or resurrect dead players.', '',
                  '!!! note "Server recipe check"', '    The recipes, values, and controls above are artifact-verified. Server-specific recipe changes and gameplay interactions have not been tested here. Check the in-game recipe browser before collecting materials.', '',
                  '[Return to Items](index.md) · [Revival Elixir and its acquisition limits](revival-elixir.md)', '',
                  '## Source and licensing', '',
                  'Recipe and effect verification: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `' + data['reference_build']['sha1'] + '`.', '',
                  'The source articles and recorded revisions are cited in the individual [Low](low-potion.md), [High](high-potion.md), and [Full](full-potion.md) potion references. Adapted text remains under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Original illustrations and File-page reviews are recorded in the public artwork register.', '',
                  '??? info "Artifact evidence"', '',
                  '    - `SpecialRecipeRegister`: four potion container mixes.',
                  '    - `TensuraConsumableItems`, `HealingPotionItem`, `ManaPotionItem`: heal fractions, fixed MP, stack size, controls, and living-target checks.',
                  '    - `MagicBottleItem`: source-water filling.',
                  '    - `data/minecraft/recipe/bottles_of_low_crystal.json`, `bottles_of_medium_crystal.json`, `bottles_of_high_crystal.json`: bottle crafting.',
                  '    - `data/minecraft/recipe/vacuumed_magic_bottle_of_water_from_smelting.json` and matching Tensura smoking/campfire recipes: preparation times.', ''])
    return '\n'.join(lines)


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
