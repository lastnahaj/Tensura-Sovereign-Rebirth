"""Render the pinned Kiln tiers, processing walkthrough, and recipe register."""
from __future__ import annotations

from collections import Counter, defaultdict
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = 'tensura-reference/blocks/blocks-kiln.md'
ASSET = 'assets/images/blocks/kiln.webp'


def manifest():
    return json.loads((ROOT / 'data/kiln_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Kiln', 'source_key': 'tensura', 'local_page': PAGE,
        'asset': ASSET, 'artwork_kind': 'original-illustration',
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Kiln', 'source_revision': 12020,
        'catalogue_entry': False, 'reclassify_import': True, 'registry_id': 'tensura:kiln',
        'role': 'Fuel-powered metal melting and mixing', 'visual': 'Original illustration; not the in-game texture',
        'access': 'Crafting Table; three upgrade tiers',
        'summary': 'Melt materials, compare alloy quantities, and plan the Normal, Mithril, and Orichalcum Kiln upgrades.',
        'stats': {'Hardness': '50', 'Blast resistance': '1,200', 'Capacity per bar': '144 / 288 / 576'},
        'card_stat_labels': ['Hardness', 'Blast resistance', 'Capacity per bar'],
        'details': ['', ''], 'evidence_paths': ['KilnBlock', 'KilnBlockEntity', 'KilnMeltingRecipe', 'KilnMixingRecipe'],
    }


def material(identifier):
    return identifier.split(':')[-1].replace('_', ' ').title()


def molten_outputs(recipe):
    return [(recipe[key], recipe.get(key + '_count', 0)) for key in ('primary', 'secondary') if key in recipe]


def generate():
    data = manifest()
    e = html.escape
    groups = defaultdict(list)
    for record in data['recipes']:
        r = record['definition']
        group = 'Mixing · finished materials' if record['kind'] == 'mixing' else 'Melting · ' + material(r['primary'])
        groups[group].append(record)
    lines = [
        '---', 'title: Kiln', 'description: Melt materials, compare alloys, and plan all three pinned Kiln tiers.', '---', '', '# Kiln', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original obsidian kiln workshop illustration" loading="eager" decoding="async"><figcaption>TSR workstation illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Metal workshop · Minecraft 1.21.1</p><h2>From ore to your next alloy</h2><p>Separate melting from mixing, leave room for both molten bars, and choose the right Kiln tier before processing valuable materials.</p><nav class="reference-quick-jumps" aria-label="Kiln guide"><a href="#build-and-upgrade">Build &amp; upgrade</a><a href="#process-materials">Processing</a><a href="#alloy-quantities">Alloy quantities</a><a href="#recipe-browser">Recipe browser</a></nav></div></section>', '',
        '!!! note "Pinned definitions · live processing untested"',
        '    The three block tiers, tracked capacity settings, fuel and boost logic, **272 melting recipes**, and **14 mixing recipes** were inspected in Tensura 2.0.1.2. Datapacks, scripts, add-ons, or server settings can change the result. No live processing, automation, or upgrade-retention test is recorded.', '',
        '<span id="Crafting"></span>', '', '## Build and upgrade', '',
        'Use a **Crafting Table** for each shaped recipe below. Each recipe produces one workstation. Capacity is **per molten bar**, not the sum of both bars, and comes from the [tracked block configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/block_config.toml).', '',
        '<div class="kiln-tier-grid">',
    ]
    for tier in data['tiers']:
        recipe = tier['definition']
        names = {'minecraft:obsidian': 'Obsidian', 'minecraft:netherite_ingot': 'Netherite Ingot', 'minecraft:cauldron': 'Cauldron', 'minecraft:blast_furnace': 'Blast Furnace', 'tensura:kiln': 'Kiln', 'tensura:kiln_mithril': 'Mithril Kiln', 'tensura:mithril_ingot': 'Mithril Ingot', 'tensura:orichalcum_ingot': 'Orichalcum Ingot'}
        counts = Counter(''.join(recipe['pattern']))
        lines.extend([f'<article class="smithing-recipe"><p class="reference-eyebrow">{tier["capacity_per_bar"]} units per bar</p><h3>{e(tier["name"])}</h3>', '<ul class="smithing-ingredients">'])
        for symbol, value in recipe['key'].items():
            lines.append(f'<li><strong>{counts[symbol]}×</strong> {e(names[value["item"]])}</li>')
        lines.extend(['</ul>', f'<details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="{e(tier["name"])} crafting recipe"><tbody>'])
        for row in recipe['pattern']:
            lines.append('<tr>' + ''.join(f'<td>{e(names[recipe["key"][s]["item"]])}</td>' for s in row) + '</tr>')
        lines.extend(['</tbody></table></details>', f'<p class="reference-media-note"><code>{tier["id"]}</code></p></article>'])
    lines.extend([
        '</div>', '',
        'Placement needs **two blocks of vertical space**, with a replaceable block above the base. The checked constructor has **hardness 50**, **blast resistance 1,200**, and requires a correct tool for drops. All three tiers are pickaxe-mineable and diamond-tool-tier tagged: use a **diamond-tier pickaxe or better**. A lit Kiln emits **light level 13**; the old article’s “not luminous” entry does not describe its lit state.', '',
        '!!! warning "Before replacing a workstation"',
        '    Upgrades are Crafting Table recipes using the previous tier as an ingredient, not a verified in-place conversion. Empty the workstation first. Inventory, stored molten material, and boost retention across breaking or upgrading have not been tested; do not assume they transfer intact.', '',
        '<span id="Usage"></span>', '', '## Process materials', '',
        '<div class="tensura-reference-article"><ol class="hipokute-growth"><li><strong>Open and load</strong><span>Use an empty hand to open the Kiln. Put one compatible material stack in its input and furnace-compatible fuel in the fuel slot.</span></li><li><strong>Melt into the bars</strong><span>Melting consumes one input item per completed recipe. The left bar holds non-magical metals; the right bar holds magical material. Keep enough capacity for every listed molten output.</span></li><li><strong>Select and collect</strong><span>Choose an available mixing output using the recipe arrows. Collecting it consumes that mixing recipe’s molten quantities. An item preview is not a new source of materials.</span></li></ol></div>', '',
        'The six packaged molten kinds are **Copper, Gold, Iron, Silver, Magisteel, and Netherite**. Magisteel and Netherite are magical and share the **right** bar; the other four use the **left** bar. Each bar holds one material identity at a time. A different kind already occupying the same bar, or an output exceeding its capacity, prevents that melting recipe from matching.', '',
        'For a basic Magisteel route, each **Magic Ore Shard** contributes **1 Magisteel unit**. The Pure Magisteel Ingot mixing definition needs **36 Magisteel units**; its nugget needs **4**. These are packaged recipe quantities, not a guarantee that an input stack completes while unattended. [Magic Ore Shard](../magic/magic-ore-shard.md) explains checked acquisition and other uses.', '',
        '### Fuel and Fire Core boost', '',
        'Ordinary fuel must pass the furnace fuel check and provide positive burn duration. A Fire Elemental Core boost **does not replace fuel**: melting still checks fuel. While boosted, the implementation advances melting progress by **2 per tick instead of 1**. That is a progress multiplier, not a measured end-to-end throughput claim.', '',
        'Use a **Fire Elemental Core in the main hand** on either part of the Kiln. With the tracked settings, it needs at least **100 remaining durability**, applies **100 durability damage**, and adds **2,400 ticks** to the existing boost timer. That is nominally **120 seconds at 20 TPS**; pauses and server tick rate affect wall-clock duration. A broken core converts to an Empty Elemental Core. The block reads `fireCoreCost` for the eligibility check but hard-codes the 100-damage call, so changing that setting alone would not establish a matching damage cost.', '',
        '??? warning "Why processing can stop"', '',
        '    Check fuel, the actual input ingredient, both stored material identities, and free capacity **per bar**. Recipe times are required progress ticks, not guaranteed wall-clock seconds. Do not use a resource filename to guess its input: the browser below follows the ingredient inside the JSON definition. Equipment recycling is not a verified way to retain abilities, durability, or components.', '',
        '## Alloy quantities', '',
        'Each row describes **one mixing operation**. A dash means that bar is not required by the recipe; it does **not** require the bar to be empty. The minimum tier compares each required bar quantity with tracked capacity and does not prove ingredient acquisition or live availability.', '',
        '| Output | Left bar units | Right bar units | Minimum capacity tier |', '|---|---|---|---|',
    ])
    for record in sorted((r for r in data['recipes'] if r['kind'] == 'mixing'), key=lambda r: r['name']):
        r = record['definition']
        amount = max(r.get('left_count', 0), r.get('right_count', 0))
        tier = next(t['name'] for t in data['tiers'] if t['capacity_per_bar'] >= amount)
        left = f'{r["left_count"]} {material(r["left"])}' if 'left' in r else '—'
        right = f'{r["right_count"]} {material(r["right"])}' if 'right' in r else '—'
        lines.append(f'| {record["name"]} ×{r["output"].get("count", 1)} | {left} | {right} | {tier} |')
    lines.extend([
        '', '## Recipe browser', '',
        'Search an input, finished output, molten material, registry ID, or resource path. This includes both melting and mixing. Melting counts are units returned from **one input item**. Progress ticks include the serializer’s 100-tick default when a recipe omits `smeltTick`.', '',
        '!!! warning "Recycling definitions are not always full material returns"',
        '    Fifteen Low Magisteel recycling definitions name Magisteel but omit `primary_count`. The checked serializer defaults that quantity to **0**, not 1. Those cards explicitly show zero Magisteel units and the defined Iron return. Other resource names also differ from their actual ingredients; the displayed input follows the definition rather than silently correcting or guessing it.', '',
        '<section class="smithing-browser" data-smithing-browser data-group-label="material group" aria-label="Packaged Kiln recipes"><div class="smithing-search"><label for="kiln-search">Find a processing recipe<input id="kiln-search" type="search" data-smithing-search placeholder="Try ore shard, mithril, silver, or an item ID" autocomplete="off"></label><button type="button" data-smithing-clear>Clear search</button><p data-smithing-status role="status" aria-live="polite">286 packaged recipes · expand a material group below</p></div>',
    ])
    for name, records in sorted(groups.items()):
        lines.append(f'<details class="smithing-group"><summary>{e(name)} <span>{len(records)} recipes</span></summary><div class="smithing-recipe-grid">')
        for record in sorted(records, key=lambda r: (r['name'], r['resource'])):
            r = record['definition']
            definition = json.dumps(r)
            search = ' '.join([record['kind'], record['name'], record['resource'], definition, definition.replace('_', ' ')]).casefold()
            lines.extend([f'<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="{record["kind"]}" data-search="{e(search, quote=True)}"><p class="reference-eyebrow">{record["kind"]}</p><h3>{e(record["name"])}</h3>', '<ul class="smithing-ingredients">'])
            if record['kind'] == 'melting':
                for identifier, count in molten_outputs(r):
                    suffix = ' · omitted count defaults to zero' if count == 0 else ''
                    unit = 'unit' if count == 1 else 'units'
                    lines.append(f'<li><strong>{count} {unit}</strong> {e(material(identifier))}{suffix}</li>')
                lines.append(f'</ul><p><strong>Required progress:</strong> {r.get("smeltTick", 100)} ticks</p>')
            else:
                for key in ('left', 'right'):
                    if key in r:
                        count = r[key + '_count']
                        unit = 'unit' if count == 1 else 'units'
                        lines.append(f'<li><strong>{count} {unit}</strong> {e(material(r[key]))} · {key} bar</li>')
                lines.append(f'</ul><p><strong>Output per operation:</strong> {r["output"].get("count", 1)}</p>')
            lines.extend([f'<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>{e(record["resource"])}</code></p><pre><code>{e(json.dumps(r, indent=2))}</code></pre></details>', '</article>'])
        lines.append('</div></details>')
    lines.extend([
        '<p data-smithing-empty hidden>No matching processing recipe. Try a shorter input or material name.</p></section>', '',
        '## Source and licensing', '',
        '[Kiln source article, recorded revision 12020](https://tensura.wiki.gg/wiki/Blocks/Kiln?oldid=12020). Adapted article text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [recipe evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/kiln_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The workstation illustration is original TSR conceptual artwork, not a game texture or GUI screenshot. The reviewed Kiln and Kiln GUI File pages did not establish reusable image permission; their withdrawal is recorded in the [source and media ledger](../../project/sources-and-attribution.md).', '',
        '??? info "Implementation evidence"', '',
        '    - `KilnBlock`, `KilnBlockEntity`, `KilnBlockEntity$1`, `KilnMenu`, `TensuraMixingSlot`, `KilnMeltingRecipe`, its `Serializer`, and `KilnMixingRecipe`',
        '    - Three workstation crafting recipes, 272 melting definitions, 14 mixing definitions, and six `data/tensura/kiln_molten/*.json` resources',
        '    - `data/minecraft/tags/block/mineable/pickaxe.json`, `needs_diamond_tool.json`, and `data/tensura/loot_table/blocks/kiln.json`',
        '    - Tracked `pack/config/tensura/block_config.toml` Kiln settings', '',
        '[Back to Blocks](index.md) · [Smithing Bench](blocks-smithing-bench.md) · [Equipment materials](../items/index.md)', '',
    ])
    return '\n'.join(lines)
