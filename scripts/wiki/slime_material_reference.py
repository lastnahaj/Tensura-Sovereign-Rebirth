"""Render ordinary slime materials without conflating chunks, food, or vanilla blocks."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOCK_PAGE = 'tensura-reference/blocks/blocks-slime-chunk-block.md'
BLOCK_ASSET = 'assets/images/blocks/slime-chunk-block.webp'
ITEM_PAGE = 'tensura-reference/items/slime-chunk.md'
ITEM_ASSET = 'assets/images/items/slime-chunk.webp'


def manifest():
    return json.loads((ROOT / 'data/slime_material_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Slime Chunk Block', 'source_key': 'tensura', 'local_page': BLOCK_PAGE,
        'asset': BLOCK_ASSET, 'artwork_kind': 'original-illustration',
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Slime_Chunk_Block', 'source_revision': 7897,
        'catalogue_entry': False, 'reclassify_import': True, 'registry_id': 'tensura:slime_chunk_block',
        'role': 'Slime Chunk storage and entity slowdown', 'visual': 'Original illustration; not the in-game texture',
        'access': 'Pack nine Slime Chunks, or warm a Chilled Slime Block',
        'summary': 'Store nine Slime Chunks, recover the ingredients, convert to chilled material, and check the unusual collision rules before building.',
        'stats': {'Packing cost': '9 Slime Chunks', 'Unpacking return': '9 Slime Chunks', 'Stuck multiplier': 'Approximately 0.7 per axis'},
        'details': ['', ''], 'evidence_paths': ['SlimeChunkBlock', 'TensuraBlocks', 'data/tensura/loot_table/blocks/slime_chunk_block.json'],
    }


def entries(data):
    return [{
        'category': 'items', 'catalogue_entry': True, 'acquisition_verified': True,
        'display_title': 'Slime Chunk', 'local_page': ITEM_PAGE, 'registry_id': 'tensura:slime_chunk', 'asset': ITEM_ASSET,
        'status': 'Loot predicates and material conversions checked', 'notice_kind': 'info',
        'warning': 'The selected 1.21.1 artifact registers an ordinary material item, not a standard food. Crafting, cooking, loot predicates, and ingredient tags were inspected; live drops and server recipe overrides remain untested.',
        'summary': 'Keep ordinary slime material for compact storage, convert four chunks into one vanilla Slimeball, or make chilled material with eight Snowballs.',
        'stats': {'Rarity': 'Common', 'Stack limit': 64, 'Vanilla Slimeball recipe': '4 chunks → 1 Slimeball', 'Storage recipe': '9 chunks → 1 resource block', 'Standard food properties': 'None registered'},
        'obtainment': 'The packaged **Tensura Slime** and **Supermassive Slime** loot tables select Slime Chunk when the custom `SlimePredicate` matches `chilled: false`. Cold variants use the Chilled Slime branch instead. This describes the mod’s entities, not a guaranteed drop from every vanilla slime. Scale-dependent functions, Looting, spawn data, and server overrides affect actual loot.\n\nFor a crafting route, unpack **1 [Slime Chunk Block](../blocks/blocks-slime-chunk-block.md)** into **9 chunks**. You can also warm **1 [Chilled Slime](chilled-slime.md)** into **1 chunk**: Furnace **100**, Smoker **50**, or Campfire **300 recipe progress ticks**, each with **0.2 recipe XP**. Progress values are not measured wall-clock durations.',
        'use': '**Choose a material route:**\n\n- **Storage:** fill a Crafting Table with **9 chunks** to make **1 [Slime Chunk Block](../blocks/blocks-slime-chunk-block.md)**; the reverse recipe returns nine.\n- **Vanilla material:** place **4 chunks** in any crafting arrangement to make **1 Minecraft Slimeball**. The checked recipe set does not establish a reverse Slimeball-to-chunk conversion.\n- **Chilled ingredient:** surround **1 chunk** with **8 Snowballs** at a Crafting Table to make **1 [Chilled Slime](chilled-slime.md)**. Eight Snow Blocks are used for the separate block conversion, not this item recipe.',
        'effects': 'Slime Chunk is constructed as a plain `Item` with no standard food properties in this registration. Its membership in `#tensura:slime_food` is a custom ingredient classification, not proof that ordinary eating restores hunger or grants the Chilled Slime food behavior. Custom racial consumption still requires a separately checked ability or mechanic.\n\nThe packaged `#c:slime_balls` item tag also includes Slime Chunk. It can satisfy a recipe that explicitly accepts that tag; a recipe that requires the exact `minecraft:slime_ball` ID is different. Check the recipe browser rather than assuming universal substitution. Placed-block drag and collision are not effects granted by holding the item.',
        'legacy_anchors': {'Availability': ['Obtainment', 'Defeating', 'Crafting'], 'How to use': ['Usage']},
        'evidence_paths': ['TensuraMobDropItems SLIME_CHUNK registration', 'SlimePredicate', 'data/tensura/loot_table/entities/slime.json', 'data/tensura/loot_table/entities/supermassive_slime.json', 'data/minecraft/recipe/slime_ball_from_chunks.json', 'data/c/tags/item/slime_balls.json', 'data/tensura/tags/item/slime_food.json', 'data/slime_material_reference.json'],
    }]


def generate_block():
    data = manifest()
    packing = ''.join('<tr><td>Slime Chunk</td><td>Slime Chunk</td><td>Slime Chunk</td></tr>' for _ in range(3))
    chilling = '<tr><td>Snow Block</td><td>Snow Block</td><td>Snow Block</td></tr><tr><td>Snow Block</td><td>Slime Chunk Block</td><td>Snow Block</td></tr><tr><td>Snow Block</td><td>Snow Block</td><td>Snow Block</td></tr>'
    return '\n'.join([
        '---', 'title: Slime Chunk Block', 'description: Pack, unpack, chill, and place ordinary slime material with checked 1.21.1 recipes and movement limits.', '---', '', '# Slime Chunk Block', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{BLOCK_ASSET}" alt="Original translucent azure gel storage-block illustration" loading="eager" decoding="async"><figcaption>TSR material illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Slime materials · Minecraft 1.21.1</p><h2>Compact the supply. Know the surface.</h2><p>Store nine chunks in one resource block, unpack them when needed, or chill the block. Its custom movement rules make it a material block—not a drop-in replacement for ordinary flooring or vanilla Slime Block.</p><nav class="reference-quick-jumps" aria-label="Slime storage guide"><a href="#craft-and-convert">Craft &amp; convert</a><a href="#placed-block-behavior">Movement limits</a><a href="../../items/slime-chunk/">Slime Chunk item</a></nav></div></section>', '',
        '!!! note "Artifact rules checked · live behavior untested"',
        '    Registration, recipes, loot, tags, and the complete `SlimeChunkBlock` class were inspected in Tensura 2.0.1.2. Live movement, fall safety, piston compatibility, explosion recovery, and recipe overrides have not been tested.', '',
        '<span id="Obtainment"></span><span id="Crafting"></span><span id="Crafting_2"></span>', '', '## Craft and convert', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid">',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Pack the material</p><h3>9 chunks → 1 block</h3><p>Fill all nine Crafting Table slots with <a href="../../items/slime-chunk/">Slime Chunk</a>. This uses Tensura chunks, not nine vanilla Slimeballs.</p><details><summary>Packing arrangement</summary><table class="smithing-pattern" aria-label="Nine ordinary chunks into one resource block"><tbody>' + packing + '</tbody></table></details></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Add the chill</p><h3>8 Snow Blocks + 1 resource block</h3><p>Surround one Slime Chunk Block with eight Snow Blocks to make <a href="../blocks-chilled-slime-block/">1 Chilled Slime Block</a>.</p><details><summary>Chilling arrangement</summary><table class="smithing-pattern" aria-label="Ordinary resource block surrounded by Snow Blocks"><tbody>' + chilling + '</tbody></table></details></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Recover the supply</p><h3>1 block → 9 Slime Chunks</h3><p>The unpacking recipe is shapeless. It returns the nine stored chunks without requiring snow or fuel. For vanilla Slimeball crafting, unpack first: the separate recipe consumes four chunks per Slimeball.</p><a href="../../items/slime-chunk/">Compare item conversions →</a></article></div></div>', '',
        '### Warm chilled storage', '',
        'One **Chilled Slime Block** cooks into **1 ordinary Slime Chunk Block**. It does not turn directly into nine loose chunks; unpack the result separately.', '',
        '| Station | Block recipe progress ticks | Recipe XP |', '|---|---:|---:|', '| Furnace | 200 | 0.2 |', '| Smoker | 100 | 0.2 |', '| Campfire | 600 | 0.2 |', '',
        'These are packaged recipe requirements, not live wall-clock timings. Fuel, active chunks, server tick rate, and overrides affect completion.', '',
        '<span id="Usage"></span>', '', '## Placed-block behavior', '',
        '<div class="kiln-tier-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Drag</p><h3>Approximately 0.7 per axis</h3><p>The entity-inside method passes roughly <strong>X 0.7 · Y 0.7 · Z 0.7</strong> to the stuck-in-block operation. These method arguments are not measured walking-speed percentages. Entities in <code>#tensura:slime_walkable_mobs</code> return before this operation.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Collision</p><h3>Not an ordinary solid floor</h3><p>The collision shape is usually empty. An entity with <strong>fall distance greater than 2.5</strong> receives a special <strong>0.9-block-high collision shape</strong>. Test footing safely before building walkways.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Ordinary vs chilled</p><h3>No cold flag in this method</h3><p>The ordinary entity-inside method only applies drag. The chilled subclass adds the powder-snow flag and server-side extinguishing step, with a stronger horizontal stuck multiplier.</p><a href="../blocks-chilled-slime-block/">Compare chilled behavior →</a></article></div>', '',
        '??? warning "Sticky does not mean vanilla bouncing"', '',
        '    The class extends `HalfTransparentBlock`, not vanilla `SlimeBlock`. Its sticky-block check reads `#tensura:sticky_blocks`. `fallOn` plays a slime landing sound for falls of at least four blocks, but the inspected class does not implement a vanilla-style bounce method. Neither a tag nor a sound is proof of safe launchpads, universal fall protection, or identical piston behavior.', '',
        '??? info "Recovery and registry properties"', '',
        '    The packaged self-drop loot table returns one block subject to an explosion-survival condition; it does not include a Silk Touch condition. The registry specifies **0.8 friction**, Slime Block sounds, light-blue map color, and `noOcclusion`. Unknown hardness and resistance fields from the older article are not treated as checked values. Live mining, explosions, and rendered transparency remain untested.', '',
        '## Source and licensing', '',
        '[Slime Chunk Block source article, recorded revision 7897](https://tensura.wiki.gg/wiki/Blocks/Slime_Chunk_Block?oldid=7897) · [Slime Chunk source article](https://tensura.wiki.gg/wiki/Slime_Chunk). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [material evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/slime_material_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'Item and block use distinct original TSR material illustrations, not game textures. Both source inventory icons identify game-studio/licensor ownership; the other two reviewed image pages did not establish reusable permission. See the [media ledger](../../project/sources-and-attribution.md).', '',
        '??? info "Artifact evidence"', '',
        '    - `TensuraMobDropItems`, `TensuraBlocks`, `SlimeChunkBlock`, and `SlimePredicate`',
        '    - Eleven crafting/cooking definitions, three loot tables, and three relevant tag resources in the material register', '',
        '[Back to Blocks](index.md) · [Slime Chunk ingredient](../items/slime-chunk.md) · [Chilled Slime Block](blocks-chilled-slime-block.md)', '',
    ])
