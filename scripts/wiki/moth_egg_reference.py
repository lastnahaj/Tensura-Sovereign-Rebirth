"""Render the pinned egg-laying, recovery, and hatching reference."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = 'tensura-reference/blocks/blocks-moth-egg.md'
ASSET = 'assets/images/blocks/moth-egg.webp'


def manifest():
    return json.loads((ROOT / 'data/moth_egg_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Moth Egg', 'source_key': 'tensura', 'local_page': PAGE,
        'asset': ASSET, 'artwork_kind': 'original-illustration',
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Moth_Egg', 'source_revision': 7517,
        'catalogue_entry': False, 'reclassify_import': True, 'registry_id': 'tensura:moth_egg',
        'role': 'Hell Moth egg laying and Hell Caterpillar hatching', 'visual': 'Original illustration; not the in-game texture',
        'access': 'Recover a placed egg with Silk Touch; no packaged crafting recipe found',
        'summary': 'Learn how moths lay eggs, recover them with Silk Touch, and provide wool or leaves for staged hatching into Hell Caterpillars.',
        'stats': {'Eggs per position': '1–4', 'Hatching substrate': 'Wool or leaves', 'Recovery': 'Silk Touch'},
        'details': ['', ''], 'evidence_paths': ['MothEggBlock', 'HellMothEntity', 'LayEggs', 'TensuraMobDropItems', 'SimpleBlockItem', 'data/tensura/loot_table/blocks/moth_egg.json'],
    }


def generate():
    data = manifest()
    return '\n'.join([
        '---', 'title: Moth Egg', 'description: Check egg laying, Silk Touch recovery, safe placement, and Hell Caterpillar hatching in Minecraft 1.21.1.', '---', '', '# Moth Egg', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original pale moth egg resting on a green leaf" loading="eager" decoding="async"><figcaption>TSR egg illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Creature lifecycle · Minecraft 1.21.1</p><h2>Protect the clutch. Prepare the nursery.</h2><p>Placed eggs can hatch into Hell Caterpillars. Choose a suitable substrate, keep traffic away, and decide whether to preserve an egg or harvest silk before breaking it.</p><nav class="reference-quick-jumps" aria-label="Moth Egg guide"><a href="#obtain-and-recover">Obtain &amp; recover</a><a href="#prepare-for-hatching">Hatching guide</a><a href="#protect-the-eggs">Protect the eggs</a></nav></div></section>', '',
        '!!! note "Artifact rules checked · live lifecycle untested"',
        '    Moth Egg registration, the full block class, moth breeding/laying callbacks, and block loot were inspected in Tensura 2.0.1.2. Live breeding access, AI navigation, egg recovery, incubation time, hatchling ownership, and server overrides remain untested.', '',
        '<span id="Obtainment"></span>', '', '## Obtain and recover', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid">',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Keep an egg</p><h3>Recover with Silk Touch</h3><p>The packaged block loot chooses <strong>Moth Egg</strong> when the tool has <strong>Silk Touch level 1 or higher</strong>. Otherwise it selects <a href="../../items/hell-moth-silk/">Hell Moth Silk</a>, with a base count of 1–3 and explosion decay. This loot branch is distinct from trampling.</p></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Laid by a moth</p><h3>1–4 eggs in a clutch</h3><p>The checked Hell Moth breeding callback sets a carried-egg flag. Its laying task searches for wool or leaves, checks two air blocks above the substrate, and places a clutch of <strong>1–4 eggs</strong> once the moth is close enough. Wool-tagged items are its checked food and taming-food class.</p></article>',
        '<article class="smithing-recipe"><p class="reference-eyebrow">Acquisition limits</p><h3>No packaged crafting recipe</h3><p>The inspected recipe resources contain no Moth Egg crafting recipe. Feeding wool is not a guarantee that a particular moth can breed or navigate to a laying site: inherited breeding conditions, the carried-egg flag, server settings, and AI still matter. Recover an existing placed egg rather than relying on an undocumented crafting conversion.</p><a href="../../mobs/mobs-hell-moth/">Open Hell Moth reference →</a></article></div></div>', '',
        '<span id="Usage"></span>', '', '## Prepare for hatching', '',
        '<ol class="hipokute-growth"><li><strong>Choose wool or leaves underneath.</strong><span>The hatching method checks the block directly below the egg against <code>#minecraft:wool</code> or <code>#minecraft:leaves</code>. A plain stone shelf does not satisfy that checked gate.</span></li><li><strong>Place and group the eggs.</strong><span>Placement rejects a target containing fluid. Using the same egg item on an existing clutch without secondary use can increase its count up to four; the current hatch state is preserved by that placement method.</span></li><li><strong>Allow eligible random updates.</strong><span>Hatch state advances from 0 to 1, then 2. The next qualifying update removes the egg block and attempts to create one baby Hell Caterpillar per stored egg—not an adult Hell Moth.</span></li></ol>', '',
        '??? info "Why there is no fixed incubation timer"', '',
        '    Each random tick first checks the level’s `getTimeOfDay(1)` result. The update gate always passes when **0.65 < value < 0.69**; outside that exclusive window it passes only when `nextInt(300) == 0`. The valid substrate gate must also pass. These are conditional code gates, not a measured real-time hatch duration or a universal dimension clock. Random-tick settings, active chunks, and server timing affect progress.', '',
        '??? info "Hatchling details and placement limits"', '',
        '    The checked hatching loop creates `tensura:hell_caterpillar`, assigns initial age **-24,000**, finalizes it with the breeding spawn type, and attempts to add it to the world. The loop does not assign a player owner here. Creation can fail; successful live spawning, maturation, ownership, and later evolution still need separate checks. The laying task requires two air blocks above its substrate; that AI condition is not the same as the item-placement method’s fluid rejection.', '',
        '[Meet the Hell Caterpillar](../mobs/mobs-hell-caterpillar.md)', '',
        '## Protect the eggs', '',
        '<div class="kiln-tier-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Foot traffic</p><h3>Keep paths away</h3><p>The step-on hook can decrement the clutch for living entities that are not stepping carefully. Its server-side random check cancels only one in 100 eligible attempts; it is not a one-percent break chance.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Exemptions</p><h3>Moths and caterpillars</h3><p>Hell Moths and Hell Caterpillars are excluded by the checked destruction gate. Creative players are excluded separately. Careful stepping bypasses the step-on call, but these checks do not establish protection against mining, explosions, or other damage.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Separate loot paths</p><h3>Trampling is not recovery</h3><p>The trampling method reduces the egg count and requests one Hell Moth Silk item. The mining loot table uses Silk Touch or a 1–3 silk branch. Do not treat stepping on eggs as a Silk Touch collection method.</p></article></div>', '',
        '??? info "Checked block and item properties"', '',
        '    - Registry strength argument: **0.5**; wool sounds, random ticks, and `noOcclusion` are set.',
        '    - The item uses `SimpleBlockItem` with default item properties, including a **64-item stack limit**; the older article’s non-stackable label is not used here.',
        '    - The block is in the packaged hoe-mineable tag. That classification does not by itself require a hoe for its Silk Touch loot condition.',
        '    - `#tensura:skill/unobtainable` includes Moth Egg. That tag is a special-system classification, not evidence that the Silk Touch loot branch is absent or that every acquisition route is disabled.', '',
        '## Source and licensing', '',
        '[Moth Egg source article, recorded revision 7517](https://tensura.wiki.gg/wiki/Blocks/Moth_Egg?oldid=7517) on the Tensura: Reincarnated Wiki. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The unfinished article is supplemented by artifact evidence rather than unknown hardness or acquisition fields.', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [Moth Egg evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/moth_egg_reference.json). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The original TSR egg illustration is conceptual artwork, not the game texture. Neither reviewed source File page established reusable image permission. See the [media ledger](../../project/sources-and-attribution.md).', '',
        '??? info "Artifact evidence"', '',
        '    - `MothEggBlock`: placement, hatching, collision shape, stepping, mining, and egg-count handling',
        '    - `HellMothEntity`: food, breeding callback, laying callback, and laying-site predicates; `LayEggs` behavior wiring',
        '    - `TensuraBlocks`, `TensuraMobDropItems`, and `SimpleBlockItem` registration',
        '    - Packaged block loot, hoe-mineable tag, and skill-unobtainable tag; relevant class/resource checksums are retained in the register', '',
        '[Back to Blocks](index.md) · [Hell Moth](../mobs/mobs-hell-moth.md) · [Hell Caterpillar](../mobs/mobs-hell-caterpillar.md) · [Hell Moth Silk](../items/hell-moth-silk.md)', '',
    ])
