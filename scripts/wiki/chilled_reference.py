"""Render the selected build's chilled-material recipes and movement limits."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOCK_PAGE = 'tensura-reference/blocks/blocks-chilled-slime-block.md'
BLOCK_ASSET = 'assets/images/blocks/chilled-slime-block.webp'
ITEM_PAGE = 'tensura-reference/items/chilled-slime.md'
ITEM_ASSET = 'assets/images/items/chilled-slime.webp'


def manifest():
    return json.loads((ROOT / 'data/chilled_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Chilled Slime Block', 'source_key': 'tensura', 'local_page': BLOCK_PAGE,
        'asset': BLOCK_ASSET, 'artwork_kind': 'original-illustration',
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Chilled_Slime_Block', 'source_revision': 7894,
        'catalogue_entry': False, 'reclassify_import': True, 'registry_id': 'tensura:chilled_slime_block',
        'role': 'Chilled-material storage and entity slowdown', 'visual': 'Original illustration; not the in-game texture',
        'access': 'Craft nine Chilled Slime, or surround a Slime Chunk Block with eight Snow Blocks',
        'summary': 'Compare two crafting routes, unpack or warm the stored material, and understand the block’s movement and cold-exposure limits.',
        'stats': {'Crafting routes': '2', 'Unpacking return': '9 Chilled Slime', 'Horizontal stuck multiplier': '0.5'},
        'details': ['', ''], 'evidence_paths': ['ChilledSlimeBlock', 'SlimeChunkBlock', 'TensuraBlocks', 'data/tensura/loot_table/blocks/chilled_slime_block.json'],
    }


def entries(data):
    return [{
        'category': 'items', 'catalogue_entry': True, 'acquisition_verified': True,
        'display_title': 'Chilled Slime', 'local_page': ITEM_PAGE, 'registry_id': 'tensura:chilled_slime', 'asset': ITEM_ASSET,
        'status': 'Crafting and cold-variant loot checked', 'notice_kind': 'info',
        'warning': 'Crafting, cooking, food properties, and cold-variant loot are checked in Tensura 2.0.1.2 for Minecraft 1.21.1. Live drops, refining access, and server overrides remain untested.',
        'summary': 'Make chilled material with eight Snowballs and one Slime Chunk, unpack its storage block, or check the Tensura cold-variant loot route.',
        'stats': {'Rarity': 'Common', 'Stack limit': 64, 'Food nutrition': 1, 'Saturation modifier': '2.0', 'Crafting output': '1 / 9 when unpacking'},
        'obtainment': 'At a **Crafting Table**, surround **1 Slime Chunk** with **8 Snowballs** to craft **1 Chilled Slime**. Alternatively, one [Chilled Slime Block](../blocks/blocks-chilled-slime-block.md) unpacks into **9 Chilled Slime** using a shapeless recipe. These are two different quantities, not a one-snowball conversion.\n\nThe packaged Tensura Slime and Supermassive Slime loot tables select Chilled Slime when their cold-variant predicate does not select the ordinary Slime Chunk branch. `SlimePredicate` checks the mod’s `SlimeEntity.isChilled()`, not every vanilla slime. In the checked non-structure spawn path, a biome in `#minecraft:spawns_cold_variant_frogs` initializes the chilled flag. Structure spawns bypass that initialization; biome tags, spawn data, scale-dependent loot, and server overrides matter. This is not a guaranteed drop from every slime in every cold-looking biome.',
        'use': 'Craft **9 Chilled Slime** into one [storage block](../blocks/blocks-chilled-slime-block.md), or warm a single item into **1 Slime Chunk**. The packaged cooking times are **100 progress ticks in a Furnace**, **50 in a Smoker**, or **300 on a Campfire**, with **0.2 XP** in each definition. These are recipe times, not measured wall-clock completion.\n\nThe material is registered as a food with **1 nutrition**, a **2.0 saturation modifier**, and `alwaysEdible`. It can therefore be used while the hunger bar is full; this does not establish a healing, MP, or cold-resistance effect. Keep materials for crafting before consuming the supply.',
        'effects': 'The pinned build also contains **36 refining potion definitions** that use Chilled Slime. Those are custom refining recipes, not proof of an ordinary Brewing Stand recipe or a verified player unlock path. The [chilled-material evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/chilled_reference.json) retains their exact input, potion components, and resource checksums. Refining access and live potion effects still require separate testing.\n\nThe block’s entity slowdown and powder-snow flag are **placed-block behavior**, not effects granted by eating this ingredient. [Compare the block guide](../blocks/blocks-chilled-slime-block.md) before using it in a base or movement system.',
        'legacy_anchors': {'Availability': ['Obtainment', 'Defeating', 'Crafting'], 'How to use': ['Usage']},
        'evidence_paths': ['TensuraConsumableItems', 'TensuraFoodProperties', 'SimpleFoodItem', 'SlimeEntity.finalizeSpawn', 'SlimePredicate', 'data/tensura/loot_table/entities/slime.json', 'data/tensura/loot_table/entities/supermassive_slime.json', 'data/minecraft/recipe/slime_chunk_from_snowball.json', 'data/tensura/recipe/chilled_slimefrom_chilled_slime_block.json', 'data/chilled_reference.json'],
    }]


def generate_block():
    data = manifest()
    lines = [
        '---', 'title: Chilled Slime Block', 'description: Compare crafting, storage, warming, and cold-exposure behavior for the chilled resource block.', '---', '', '# Chilled Slime Block', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{BLOCK_ASSET}" alt="Original pearl-blue chilled-gel resource block illustration" loading="eager" decoding="async"><figcaption>TSR material illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Cold materials · Minecraft 1.21.1</p><h2>Store the chill. Plan the footing.</h2><p>Use two crafting routes to build a chilled resource block. Unpack it later, warm it into ordinary material, or inspect its movement limits before placing it underfoot.</p><nav class="reference-quick-jumps" aria-label="Chilled block guide"><a href="#craft-and-convert">Craft &amp; convert</a><a href="#placed-block-behavior">Movement limits</a><a href="../../items/chilled-slime/">Chilled Slime item</a></nav></div></section>', '',
        '!!! note "Artifact rules checked · live behavior untested"',
        '    Crafting and cooking definitions, the entity-inside method, inherited collision behavior, and loot data were inspected in Tensura 2.0.1.2. Live freezing damage, player immunity, piston interactions, automation, and server recipe overrides have not been tested.', '',
        '<span id="Obtainment"></span><span id="Crafting"></span><span id="Crafting_2"></span>', '', '## Craft and convert', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid">',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Compact the item</p><h3>9 chilled items → 1 block</h3><p>Fill all nine Crafting Table slots with <a href="../../items/chilled-slime/">Chilled Slime</a>.</p><details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="Nine chilled items into one block"><tbody>' + ''.join('<tr><td>Chilled Slime</td><td>Chilled Slime</td><td>Chilled Slime</td></tr>' for _ in range(3)) + '</tbody></table></details></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Chill ordinary storage</p><h3>8 Snow Blocks + 1 resource block</h3><p>Surround one <a href="../blocks-slime-chunk-block/">Slime Chunk Block</a> with eight Snow Blocks. The result is one Chilled Slime Block.</p><details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="Snow-block chilling recipe"><tbody><tr><td>Snow Block</td><td>Snow Block</td><td>Snow Block</td></tr><tr><td>Snow Block</td><td>Slime Chunk Block</td><td>Snow Block</td></tr><tr><td>Snow Block</td><td>Snow Block</td><td>Snow Block</td></tr></tbody></table></details></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Recover the ingredient</p><h3>1 block → 9 chilled items</h3><p>Use the shapeless unpacking recipe. No snow or fuel is required for this direction. Packing and unpacking preserve the nine-item quantity in the checked definitions.</p><a href="../../items/chilled-slime/">Open Chilled Slime →</a></article>',
        '</div></div>', '',
        '### Warm it into ordinary material', '',
        'One Chilled Slime Block cooks into **1 Slime Chunk Block**. The single-item route cooks one Chilled Slime into one Slime Chunk. The block route does not produce nine loose items unless you unpack it separately.', '',
        '| Station | Block recipe progress ticks | Single-item recipe progress ticks | Recipe XP |', '|---|---:|---:|---:|',
        '| Furnace | 200 | 100 | 0.2 |', '| Smoker | 100 | 50 | 0.2 |', '| Campfire | 600 | 300 | 0.2 |', '',
        'Cooking times are required recipe progress, not verified wall-clock durations. Appropriate fuel, active chunks, server tick rate, and overrides affect completion.', '',
        '<span id="Usage"></span>', '', '## Placed-block behavior', '',
        '<div class="kiln-tier-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Movement</p><h3>Stronger horizontal drag</h3><p>The entity-inside method applies a stuck multiplier of <strong>X 0.5 · Y 0.7 · Z 0.5</strong>. Ordinary Slime Chunk Block uses approximately 0.7 horizontally. These are method arguments, not a measured walking-speed percentage.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Cold &amp; fire</p><h3>Powder-snow exposure flag</h3><p>It sets the entity’s powder-snow flag and clears an existing fire flag on the server. Actual freezing damage and immunity depend on the entity and other mechanics; extinguishing is not a verified fire-proof shelter.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Exceptions</p><h3>Walkable entity tag</h3><p>Entities in <code>#tensura:slime_walkable_mobs</code> return before the slowdown, powder-snow flag, and extinguishing steps. Check the current tag rather than assuming every creature or player shares an exemption.</p></article></div>', '',
        '??? warning "Not an ordinary floor or a verified launchpad"', '',
        '    The inherited collision method usually returns an empty shape for entity collision. An entity with **fall distance greater than 2.5** gets the special **0.9-block-high collision shape**. The class derives from Tensura’s Slime Chunk Block, not vanilla Slime Block; a sticky-block tag does not establish identical bouncing or piston behavior. Test movement safely before using it as flooring, a fall system, or a multiplayer trap.', '',
        '??? info "Recovery and block properties"', '',
        '    The packaged self-drop loot table returns the block with an explosion-survival condition and no Silk Touch condition. The registry copies Slime Chunk Block properties, including its 0.8 friction value. The old article’s unknown hardness and resistance fields are not promoted to verified numerical values here. Live mining and explosion recovery have not been tested.', '',
        '## Source and licensing', '',
        '[Chilled Slime Block source article, recorded revision 7894](https://tensura.wiki.gg/wiki/Blocks/Chilled_Slime_Block?oldid=7894) · [Chilled Slime item article](https://tensura.wiki.gg/wiki/Chilled_Slime). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [recipe evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/chilled_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The block and ingredient have separate original TSR illustrations. They are conceptual material art, not verified game textures. The reviewed source images lacked reusable image permission, including a game-studio/licensor ownership notice on the inventory block icon. See the [media ledger](../../project/sources-and-attribution.md).', '',
        '??? info "Artifact evidence"', '',
        '    - `ChilledSlimeBlock`, `SlimeChunkBlock`, and `TensuraBlocks` registration',
        '    - Ten crafting and cooking definitions, 36 separate refining definitions, and three loot tables in the chilled-material register',
        '    - `SlimeEntity.finalizeSpawn`, `SlimePredicate`, `TensuraFoodProperties`, `TensuraConsumableItems`, and `SimpleFoodItem`',
        '    - `data/tensura/tags/entity_type/slime_walkable_mobs.json` and `data/tensura/tags/block/sticky_blocks.json`', '',
        '[Back to Blocks](index.md) · [Chilled Slime ingredient](../items/chilled-slime.md) · [Ordinary Slime Chunk Block](blocks-slime-chunk-block.md)', '',
    ]
    return '\n'.join(lines)
