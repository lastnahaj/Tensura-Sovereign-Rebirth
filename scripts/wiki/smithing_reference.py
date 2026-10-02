"""Render the pinned smithing workstation walkthrough and recipe browser."""
from __future__ import annotations

from collections import defaultdict
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = 'tensura-reference/blocks/blocks-smithing-bench.md'
ASSET = 'assets/images/blocks/smithing-bench.webp'


def manifest():
    return json.loads((ROOT / 'data/smithing_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Smithing Bench', 'source_key': 'tensura', 'local_page': PAGE,
        'asset': ASSET, 'artwork_kind': 'original-illustration',
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Smithing_Bench',
        'source_revision': 13111, 'catalogue_entry': False, 'reclassify_import': True,
        'registry_id': 'tensura:smithing_bench', 'role': 'Schematic-gated crafting workstation',
        'visual': 'Original illustration; not the in-game texture',
        'access': 'Crafting table; recipes draw from player inventory',
        'summary': 'Build the bench, learn every required schematic, and compare 298 packaged equipment recipes before gathering materials.',
        'stats': {'Hardness': '3', 'Packaged recipes': '298', 'Recipe schematics': '33'},
        'card_stat_labels': ['Player access', 'Packaged recipes', 'Recipe schematics'],
        'details': ['', ''],
        'evidence_paths': ['data/tensura/recipe/smithing_bench.json', 'SmithingBenchBlock', 'SmithingBenchMenu', 'SmithingBenchRecipe'],
    }


def generate():
    data = manifest()
    groups = defaultdict(list)
    for recipe in data['recipes']:
        group = recipe['schematics'][0]['name'] if recipe['schematics'] else 'No schematic required'
        groups[group].append(recipe)
    e = html.escape
    lines = [
        '---', 'title: Smithing Bench', 'description: Build the workstation, learn schematic requirements, and browse the pinned equipment recipes.', '---', '',
        '# Smithing Bench', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original artisan smithing workbench illustration" loading="eager" decoding="async"><figcaption>TSR workstation illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Equipment workshop · Minecraft 1.21.1</p><h2>Turn a blueprint into equipment</h2><p>Build the workstation, learn its recipe gates, and keep the materials in your inventory. Check quantities and every required schematic before committing to a gear set.</p><nav class="reference-quick-jumps" aria-label="Smithing guide"><a href="#build-the-bench">Build the bench</a><a href="#unlock-and-craft">Unlock and craft</a><a href="#browse-packaged-recipes">Recipe browser</a></nav></div></section>', '',
        '!!! note "Pinned recipe definitions · live crafting untested"',
        '    The bench recipe, menu, schematic checks, and **298 packaged smithing recipes** were inspected in Tensura 2.0.1.2. This is not a claim that every recipe is unchanged on the server. Datapacks, scripts, add-ons, and recipe overrides may change availability or ingredients.', '',
        '<span id="Crafting"></span>', '', '## Build the bench', '',
        'At a **Crafting Table**, use **2 Paper**, **1 Crafting Table**, **1 Smithing Table**, and **2 planks**. The shaped recipe uses the two-column arrangement below and produces one Smithing Bench. The material key accepts the `minecraft:planks` tag, not just one wood type.', '',
        '<div class="smithing-build"><table class="smithing-pattern" aria-label="Two-column bench recipe"><caption>Crafting Table recipe · one bench</caption><tbody><tr><td>Paper</td><td>Paper</td></tr><tr><td>Crafting Table</td><td>Smithing Table</td></tr><tr><td>Planks</td><td>Planks</td></tr></tbody></table><aside><strong>Keep the workstations distinct</strong><p>A vanilla Smithing Table is an ingredient. It is not the Tensura Smithing Bench, and neither is the Spellbinding Table used for caster tools.</p><a href="../../resistances/spellbinding-table/">Compare Spellbinding Table →</a></aside></div>', '',
        'The checked block has **hardness 3** and belongs to the **axe-mineable** tag. Although an iron-tool-tier tag also lists it, its constructor does not require a correct tool for drops and its ordinary self-drop loot table has no tool condition. Do not treat the old article’s tool icon as proof that an iron pickaxe is required to recover it. Explosion survival still affects its self-drop.', '',
        '<span id="Usage"></span>', '', '## Unlock and craft', '',
        '<div class="tensura-reference-article"><ol class="hipokute-growth"><li><strong>Learn all required schematics</strong><span>The survival recipe list is filtered against your learned schematic IDs. A material schematic alone is not enough when a weapon also requires a shape schematic.</span></li><li><strong>Carry the ingredients</strong><span>The recipe input is your player inventory, not a separate shaped bench grid. Matching stacks are counted across the container.</span></li><li><strong>Select the recipe and take its output</strong><span>The survival pickup check requires sufficient materials. Taking the output consumes the recipe quantities from your inventory.</span></li></ol></div>', '',
        'Use the bench with an empty hand to open its menu. Recipes without schematic requirements can appear without learning a blueprint. Creative/infinite-materials access bypasses both the schematic gate and the normal ingredient check; that is not a survival obtainment route.', '',
        'A schematic must be **learned**, not merely carried. For example, [Magic Staff Schematic](../magic/magic-staff-schematic.md) is consumed when a new schematic is learned. Blueprint supply is recipe-specific; this browser does not establish how to obtain every listed schematic. [Compare casting staves](../items/magic-staves.md) for checked staff blueprint and material routes.', '',
        '??? warning "Why a recipe may be missing or its output unavailable"', '',
        '    Check that you have learned **every** schematic shown, that the materials are in player inventory rather than a nearby chest, and that counts and ingredient tags match. An output preview does not prove you can take it. If the server differs from this base catalogue, inspect its current in-game recipe browser before spending scarce materials. No automated item transfer or live multiplayer crafting has been verified here.', '',
        '<span id="Gear_Requiring_Smithing_Bench"></span><span id="Monster_Leather"></span><span id="Magisteel"></span><span id="Monster_Drops"></span><span id="Special_Sets/Items"></span><span id="Basic_Material"></span>', '',
        '## Browse packaged recipes', '',
        'Search by output, ingredient, schematic, or registry ID. Expand a group to inspect its recipes. Groups use the **first schematic** for navigation only; each recipe still lists **all** required schematics. Quantities describe one craft, not a full armor set.', '',
        '<section class="smithing-browser" data-smithing-browser aria-label="Packaged smithing recipes">',
        '<div class="smithing-search"><label for="smithing-search">Find a recipe<input id="smithing-search" type="search" data-smithing-search placeholder="Try silver, staff, monster leather, or an item ID" autocomplete="off"></label><button type="button" data-smithing-clear>Clear search</button><p data-smithing-status role="status" aria-live="polite">298 packaged recipes · expand a schematic group below</p></div>',
    ]
    for name, recipes in sorted(groups.items()):
        count_label = 'recipe' if len(recipes) == 1 else 'recipes'
        lines.append(f'<details class="smithing-group"><summary>{e(name)} <span>{len(recipes)} {count_label}</span></summary><div class="smithing-recipe-grid">')
        for recipe in sorted(recipes, key=lambda r: (r['name'], r['resource'])):
            schematics = ' + '.join(s['name'] for s in recipe['schematics']) or 'None in this recipe'
            search = ' '.join([recipe['name'], recipe['output']['id'], schematics, *[i['label'] for i in recipe['ingredients']], *[json.dumps(i['ingredient']) for i in recipe['ingredients']], *[s['id'] for s in recipe['schematics']]])
            lines.extend([
                f'<article class="smithing-recipe" data-smithing-recipe data-search="{e(search.casefold(), quote=True)}">',
                f'<h3>{e(recipe["name"])} <span>×{recipe["output"].get("count", 1)}</span></h3>',
                '<ul class="smithing-ingredients">',
                *[f'<li><strong>{i["count"]}×</strong> {e(i["label"])}</li>' for i in recipe['ingredients']],
                '</ul>', f'<p><strong>Learn all:</strong> {e(schematics)}</p>',
                f'<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>{e(recipe["output"]["id"])}</code></p><p>Resource: <code>{e(recipe["resource"])}</code></p><p>Required IDs: {e(", ".join(s["id"] for s in recipe["schematics"]) or "None")}</p></details>',
                '</article>',
            ])
        lines.append('</div></details>')
    lines.extend([
        '<p data-smithing-empty hidden>No matching recipe. Try a shorter material or schematic name.</p></section>', '',
        '## Recipe coverage', '',
        'The upstream catalogue’s **Dark Set**, **Silver Set**, **Ant Set**, and **Clown Masks** names remain useful starting points. This base recipe register contains Dark equipment, Silver equipment, Ant Carapace equipment, and Pierrot masks with ingredient and schematic definitions. A set label is not a promise that every expected piece exists, and a packaged recipe is not proof of live-server availability.', '',
        '## Source and licensing', '',
        '[Smithing Bench source article, recorded revision 13111](https://tensura.wiki.gg/wiki/Blocks/Smithing_Bench?oldid=13111). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [recipe evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/smithing_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The original workstation illustration is conceptual artwork, not a game texture. The source File page did not establish reusable image permission; the [media ledger](../../project/sources-and-attribution.md) records the review.', '',
        '??? info "Implementation evidence"', '',
        '    - `data/tensura/recipe/smithing_bench.json` and all 298 `data/tensura/recipe/smithing/*.json` resources',
        '    - `SmithingBenchBlock`, `SmithingBenchMenu`, `SmithingBenchMenu$1`, `SmithingBenchRecipe`, and its `Serializer`',
        '    - `data/tensura/loot_table/blocks/smithing_bench.json`',
        '    - `data/minecraft/tags/block/mineable/axe.json` and `needs_iron_tool.json`', '',
        '[Back to Blocks](index.md) · [Browse equipment materials](../items/index.md) · [Learn about Spellbinding Table](../resistances/spellbinding-table.md)', '',
    ])
    return '\n'.join(lines)
