"""Render the checked cave variants and encounter preparation guide."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = 'tensura-reference/structures/structures-charybdis-cave.md'
ASSET = 'assets/images/structures/charybdis-cave.webp'
SUMMARY = 'Find the four cave variants, inspect the core phase, and prepare for a deliberate Charybdis encounter.'


def manifest():
    return json.loads((ROOT / 'data/charybdis_cave_reference.json').read_text(encoding='utf-8'))


def apply(records):
    for record in records:
        if record['local_page'] == PAGE:
            record['_summary_override'] = SUMMARY
            record['_primary_media'] = {'local_path': ASSET, 'kind': 'original'}
            record['_card_stats'] = {'Variants': 'Plains, desert, ice, mesa', 'Placement spacing': '90 chunks', 'Separation': '20 chunks'}
            record['_stat_source_note'] = 'Pinned 1.21.1 resources; live generation untested.'


def generate():
    data = manifest()
    lines = [
        '---', 'title: Charybdis Cave', f'description: {SUMMARY}', '---', '', '# Charybdis Cave', '',
        '<section data-reference-section="structures" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original moss-covered underground core chamber illustration" loading="eager" decoding="async"><figcaption>TSR environment illustration · not a structure map</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Exploration · Minecraft 1.21.1</p><h2>Find the chamber. Check the core before you use it.</h2><p>Four packaged cave variants share a room pool. This is a place to find a boss core, not proof that Charybdis is already roaming inside.</p><nav class="reference-quick-jumps" aria-label="Cave guide"><a href="#where-to-look">Where to look</a><a href="#inside-the-cave">Inside the cave</a><a href="#prepare-before-activation">Prepare first</a></nav></div></section>', '',
        '!!! warning "A room can contain an already-active core"',
        '    The packaged `charybdis_room_2` template contains an **ACTIVE core with 100,000 stored EP**. Do not assume every discovered core needs charging. Non-sneaking empty-hand use of an active core starts the primed encounter, including a **200-tick fuse and strength-10 explosion**. Read the [activation guide](../blocks/blocks-charybdis-core.md#activate-the-encounter) before interacting.', '',
        '!!! note "Resources checked · live generation untested"',
        '    Structure definitions, placement, biome tags, template pools, and all 25 packaged cave templates were inspected in Tensura 2.0.1.2. Actual server locations, room assembly, discovery rates, merchant map offers, and encounters remain untested.', '',
        '## Where to look', '',
        'The structure set uses **random-spread placement**, **90-chunk spacing**, and **20-chunk separation**, with equal selection weights of **1** for its four variants. These are placement settings, not a guarantee of one cave every 90 chunks, a distance from spawn, or a 25% discovery chance in each biome.', '',
        '| Variant | Packaged biome eligibility |', '|---|---|',
        '| Plains | Biomes in the Plains, Savanna, and Taiga village tags; Ancient Forest |',
        '| Desert | Biomes in the Desert village tag; Barren Land; Desert of Death |',
        '| Ice | Biomes in Tensura’s cold tag; see its exact contents below |',
        '| Mesa | Biomes in Minecraft’s Badlands tag |', '',
        '??? info "Exact biome IDs and entrance pools"', '',
        '    - Plains: `#minecraft:has_structure/village_plains`, `#minecraft:has_structure/village_savanna`, `#minecraft:has_structure/village_taiga`, and `tensura:ancient_forest`; pool `tensura:charybdis_cave/start`.',
        '    - Desert: `#minecraft:has_structure/village_desert`, `tensura:barren_land`, and `tensura:desert_of_death`; pool `tensura:charybdis_cave/start_desert`.',
        '    - Ice: `#tensura:is_cold`; pool `tensura:charybdis_cave/start_ice`.',
        '    - Mesa: `#minecraft:is_badlands`; pool `tensura:charybdis_cave/start_mesa`.', '',
        '??? info "What the cold tag actually contains"', '',
        '    The packaged `tensura:is_cold` tag includes `#minecraft:has_structure/village_snowy`, `minecraft:ice_spikes`, and an optional biome ID `c:is_cold` with `required: false`. That optional entry is a biome ID in this definition, not a `#c:is_cold` tag expansion. Datapack additions can alter the resolved eligibility; this is not a claim that every cold biome qualifies.', '',
        'Each variant is a Jigsaw structure projected to `WORLD_SURFACE_WG` with start height absolute 0. The heightmap projection means this is **not a fixed Y=0 location instruction**. The recorded size parameter is 7; it is not a guaranteed room count. The plains variant has max distance from center 116; the other three use 80. Existing terrain, world borders, server overrides, and failed assembly can affect discovery.', '',
        '## Inside the cave', '',
        'The four entrance pools each select their matching entrance template. The shared stairs pool has four entries with weight 1 each; the shared rooms pool has 17 entries with weight 5 each. This does not establish that a themed entrance uses only rooms of its own theme, or that every assembled cave contains every listed room.', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Template evidence</p><h3>Inspect the phase</h3><p>Core-bearing room templates contain inactive, zero-EP cores except charybdis_room_2, which stores an active 100,000-EP core. The entrance and stair templates contain no core blocks in the checked summaries.</p><a href="../../blocks/blocks-charybdis-core/">Core phases &amp; interactions →</a></article><article class="smithing-recipe"><p class="reference-eyebrow">Spawn distinction</p><h3>Finding is not summoning</h3><p>The structure definitions have an empty monster spawn override within the full bounding box. The checked templates have zero embedded entities. Neither establishes a universal no-mob safety guarantee; Charybdis is attempted through core activation.</p><a href="../../bosses/mobs-charybdis/">Charybdis reference →</a></article><article class="smithing-recipe"><p class="reference-eyebrow">Explorer-map scope</p><h3>A target tag, not an offer</h3><p>The on_charybdis_explorer_maps tag lists all four structure IDs. A target tag alone does not prove a merchant sells a map, its price, or that an offer is available on the current server.</p></article></div></div>', '',
        '## Prepare before activation', '',
        '<ol class="hipokute-growth"><li><strong>Inspect before using.</strong><span>Check the phase and stored EP. Do not activate simply to identify the block; an active core enters the summoning branch.</span></li><li><strong>Recover deliberately.</strong><span>Sneak-use follows the pickup branch before phase actions. Keep inventory space free; the checked method does not handle a failed insertion with a fallback drop.</span></li><li><strong>Choose an encounter site.</strong><span>Move away from homes and storage before deliberate activation. No safe radius, build-protection behavior, or live encounter outcome is certified by this guide.</span></li></ol>', '',
        '[Core item reference](../items/charybdis-core.md) · [Inert reward reference](../items/inert-charybdis-core.md)', '',
        '??? info "Template checks and limitations"', '',
    ]
    for path, item in data['template_summaries'].items():
        if not item['core_blocks']:
            continue
        state = item['core_palette_entries'][0]['Properties']['sculk_sensor_phase']
        ep = item['core_blocks'][0]['nbt']['EP']
        lines.append(f'    - `{Path(path).stem}`: **{state}**, **{ep:,.0f} EP** in its recorded core block.')
    lines.extend([
        '', '    Template presence is not a live guarantee that the room assembles, its blocks remain unchanged, or its core survives other world systems. No cave coordinates or drop probability are inferred from these definitions.', '',
        '## Source and licensing', '',
        '[Structures/Charybdis Cave](https://tensura.wiki.gg/wiki/Structures/Charybdis_Cave?oldid=9628), recorded revision `9628`, on the Tensura: Reincarnated Wiki. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Packaged biome tags and template states replace the unfinished article’s broader biome list.', '',
        f'Implementation resources: [Tensura {data["version"]}]({data["source_url"]}) · [cave evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/charybdis_cave_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The environment illustration is original TSR concept artwork, not an in-game screenshot, floor plan, or verified appearance. The two source structure-image File pages did not establish reusable image permission. The editorial WIP portrait is omitted. See [Sources and attribution](../../project/sources-and-attribution.md).', '',
        '[Back to Structures](index.md) · [Core lifecycle](../blocks/blocks-charybdis-core.md)', '',
    ])
    return '\n'.join(lines)
