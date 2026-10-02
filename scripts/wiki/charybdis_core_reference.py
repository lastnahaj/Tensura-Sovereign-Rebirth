"""Render the core lifecycle, activation hazard, and checked recovery routes."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOCK_PAGE = 'tensura-reference/blocks/blocks-charybdis-core.md'
ASSET = 'assets/images/blocks/charybdis-core.webp'
INERT_ASSET = 'assets/images/items/inert-charybdis-core.webp'


def manifest():
    return json.loads((ROOT / 'data/charybdis_core_reference.json').read_text(encoding='utf-8'))


def entry():
    return {
        'display_title': 'Charybdis Core', 'source_key': 'tensura', 'local_page': BLOCK_PAGE,
        'asset': ASSET, 'artwork_kind': 'original-illustration', 'reclassify_import': True,
        'source_article_url': 'https://tensura.wiki.gg/wiki/Blocks/Charybdis_Core', 'source_revision': 9626,
        'catalogue_entry': False, 'registry_id': 'tensura:charybdis_core',
        'role': 'Charge and prime a Charybdis encounter', 'visual': 'Original illustration; not the game texture',
        'access': 'Source-described cave core; checked block recovery and charging methods',
        'summary': 'Charge nearby death-event EP, use an active core to prime Charybdis, and distinguish the inert reward from the summoning state.',
        'stats': {'Charge threshold': '100,000 EP', 'Listener radius': '16 blocks', 'Primed fuse': '200 ticks'},
        'details': ['', ''], 'evidence_paths': ['CharybdisCoreBlock', 'CharybdisCoreBlockEntity$CoreListener', 'PrimedCharybdisCoreEntity'],
    }


def entries(_data):
    common = {
        'category': 'items', 'registry_id': 'tensura:charybdis_core', 'catalogue_entry': True,
        'acquisition_verified': True, 'notice_kind': 'info',
        'warning': 'Block interactions and registration were checked in Tensura 2.0.1.2. Cave acquisition, live recovery, combat, skill grants, and synthesis remain untested.',
        'stats': {'Stack limit': '64, subject to matching components', 'Item property': 'Fire resistant'},
        'evidence_paths': ['TensuraMobDropItems', 'SimpleBlockItem', 'CharybdisCoreBlock', 'CharybdisCoreBlockEntity', 'data/tensura/loot_table/blocks/charybdis_core.json'],
    }
    return [
        {
            **common, 'local_page': 'tensura-reference/items/charybdis-core.md', 'display_title': 'Charybdis Core', 'asset': ASSET,
            'status': 'Block recovery checked · live acquisition untested',
            'summary': 'A stateful boss core: recover it as an item, place it to collect EP, and use the active placed core to prime a Charybdis encounter.',
            'obtainment': 'The source locates inactive cores in [Charybdis Cave](../structures/structures-charybdis-cave.md). The checked block loot returns one `tensura:charybdis_core` and copies its stored EP component and phase. Sneak-use of a placed core also requests its block drops, adds them to the player inventory, then destroys the block without further drops. Keep inventory space free: that method does not provide a fallback for a failed inventory insertion. No packaged crafting recipe referencing the core was found.',
            'use': 'Place the core and follow the [charging and activation guide](../blocks/blocks-charybdis-core.md). Only an **active placed core** enters the priming branch when used without sneaking; the checked action is **use/right-click with an empty hand**, not a left-click strike or an air-use of the inventory item. Sneak-use is the pickup branch.',
            'effects': 'The item factory uses `SimpleBlockItem` with default stack properties and fire resistance. The **64-item limit** does not prove cores with different phase or EP components will merge. The active branch removes the placed block and creates a primed entity with a **200-tick fuse** and **strength-10 MOB explosion** before attempting to spawn Charybdis. Do not activate near a settlement. Actual explosion damage, protection-plugin behavior, and successful server spawning are untested.',
            'legacy_anchors': {'Availability': ['Obtainment', 'Location'], 'How to use': ['Usage']},
        },
        {
            **common, 'local_page': 'tensura-reference/items/inert-charybdis-core.md', 'display_title': 'Inert Charybdis Core', 'asset': INERT_ASSET,
            'status': 'Boss death callback checked · live recovery untested',
            'summary': 'The spent COOLDOWN phase of Charybdis Core, produced by the boss death callback and used for configured skill-learning attempts.',
            'obtainment': 'The checked `CharybdisEntity.tickDeath` callback creates a falling Charybdis Core in **COOLDOWN** phase when its death counter reaches **40 ticks**, with the falling entity’s indestructible flag set. This is a death-callback path, not an ordinary core entry in the boss loot JSON. Landing, collection, and successful server recovery remain untested. It uses the same `tensura:charybdis_core` item ID as the other phases.',
            'use': 'Use a placed inert core without sneaking to attempt the configured [Gravity Manipulation](../skills/extra/gravity-manipulation.md) and [Magic Jamming](../magic/magic-jamming.md) skill-learning calls. This is not a guarantee that an already-owned, blocked, or otherwise ineligible skill can be learned. See the [core lifecycle guide](../blocks/blocks-charybdis-core.md#inert-core-rewards) before using or recovering it.',
            'effects': 'With a nonempty resolved skill list, the checked branch removes the core if at least one `SkillHelper.learnSkill` call succeeds. If none succeeds it returns without removing the block. An empty resolved list also reaches the removal branch. The tracked synthesis configuration separately specifies **200,000 EP** and four inert-core skills, including [Magic Sense](../magic/magic-sense.md) and [Ultraspeed Regeneration](../skills/extra/ultraspeed-regeneration.md). These synthesis settings are configuration evidence only here; implementation eligibility and live rewards were not tested. Do not treat ordinary inert-core use as proof of those extra rewards.',
            'legacy_anchors': {'Availability': ['Obtaining', 'Mob_Drop'], 'How to use': ['Usage']},
        },
    ]


def generate():
    data = manifest()
    config = data['configuration']['CharybdisCore']
    return '\n'.join([
        '---', 'title: Charybdis Core', 'description: Check core charging, active summoning hazards, inert rewards, and safe recovery in Minecraft 1.21.1.', '---', '', '# Charybdis Core', '',
        '<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original crimson organic Charybdis Core illustration" loading="eager" decoding="async"><figcaption>TSR core illustration · not the in-game texture</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Boss encounter · Minecraft 1.21.1</p><h2>Charge deliberately. Activate away from home.</h2><p>The inactive, active, and inert core are different phases of one registered block. Charging prepares an encounter; the spent core has a separate skill-learning use.</p><nav class="reference-quick-jumps" aria-label="Core guide"><a href="#charge-the-core">Charging</a><a href="#activate-the-encounter">Activation &amp; hazards</a><a href="#inert-core-rewards">Inert rewards</a></nav></div></section>', '',
        '!!! warning "Activation includes an explosion"',
        '    The checked active-core path primes a **200-tick fuse**, then calls a **strength-10 MOB explosion** before attempting to spawn Charybdis. Strength is a code parameter, not a safe-distance recommendation. Do not activate near players’ homes, storage, or protected builds. No live damage or protection-plugin test was performed.', '',
        '!!! note "Artifact and configuration checked · live encounter untested"',
        '    Charging, block interactions, priming, the boss death callback, item registration, and loot were inspected in Tensura 2.0.1.2. Cave acquisition, successful server summoning, combat, recovery, skill eligibility, and synthesis rewards remain untested.', '',
        '<span id="Description"></span>', '', '## Obtain or recover', '',
        'The [source article](https://tensura.wiki.gg/wiki/Blocks/Charybdis_Core) locates the core in the core room of [Charybdis Cave](../structures/structures-charybdis-cave.md). That location is source-described, not a live server find. No packaged crafting recipe referencing the core was found.', '',
        'The checked block loot returns one core item, copying `tensura:existence_durability` and the `sculk_sensor_phase` property. **Sneak-use picks up before other phase actions**: it obtains block drops, tries to add them to the player inventory, and removes the placed block without further drops. Keep spare inventory slots; this branch ignores a failed insertion result.', '',
        '[Core inventory reference](../items/charybdis-core.md)', '',
        '## Charge the core', '',
        '<ol class="hipokute-growth"><li><strong>Place an inactive core.</strong><span>The listener only accepts charging in the INACTIVE phase. An active or inert core does not follow this charging branch.</span></li><li><strong>Keep eligible deaths nearby.</strong><span>The listener radius is 16 blocks. It handles ENTITY_DIE events from living entities whose EP-drop suppression flag is not already set.</span></li><li><strong>Reach the configured threshold.</strong><span>Positive EnergyHelper.getEPGain contributions are added to stored core EP, capped at the tracked 100,000-EP threshold. Reaching it switches the core to ACTIVE.</span></li></ol>', '',
        '!!! info "Charging redirects the death reward"',
        '    When a positive contribution is accepted, the listener marks the entity to skip its EP drop and calls `skipDropExperience`. That death does not also supply the usual player EP and experience through those paths. This is not a claim that its ordinary item-loot table is cleared, or that every nearby death is eligible.', '',
        '## Activate the encounter', '',
        'Use the **active placed core** with an empty hand, without sneaking. The checked `useWithoutItem` branch creates a primed core and removes the original block. It is the use/right-click action, not left-click mining.', '',
        'The primed entity starts with **200 ticks** of fuse time, moves under gravity, and makes unstable jumps when on the ground. At 20 TPS the fuse is nominally **10 seconds**, not a measured wall-clock delay. After expiration the server-side method calls an explosion with strength **10** and `ExplosionInteraction.MOB`, then creates and finalizes Charybdis as an event spawn. The entity-add result is not used to guarantee success.', '',
        '[Charybdis boss reference](../bosses/mobs-charybdis.md)', '',
        '## Inert core rewards', '',
        f'<div class="tensura-reference-article"><div class="chilled-crafting-grid"><article class="smithing-recipe"><p class="reference-eyebrow">After the boss dies</p><h3>A spent core phase</h3><p>The checked death callback produces a falling core in COOLDOWN phase at death counter 40 ticks. The source calls this the inert core. The ordinary boss loot JSON does not contain a separate inert-core item entry.</p><a href="../../items/inert-charybdis-core/">Open the inert reference →</a></article><article class="smithing-recipe"><p class="reference-eyebrow">Ordinary block use</p><h3>Two configured skill calls</h3><p>The tracked list contains <a href="../../skills/extra/gravity-manipulation/">Gravity Manipulation</a> and <a href="../../magic/magic-jamming/">Magic Jamming</a>. Non-sneaking use resolves the configured IDs and calls SkillHelper.learnSkill for each valid entry. Eligibility and success are not guaranteed.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Separate synthesis settings</p><h3>{config["charybdisCoreFusingEP"]:,.0f} EP configuration</h3><p>The inert synthesis list additionally names Magic Sense and Ultraspeed Regeneration. These are tracked configuration values, not verified synthesis eligibility or live grants. Ordinary core use does not establish the extra EP or two extra skills.</p><a href="../../skills/unique/degenerate/">Read Degenerate →</a></article></div></div>', '',
        '??? info "When ordinary inert-core use consumes it"', '',
        '    With a nonempty resolved skill list, at least one successful learning call reaches the removal branch. If all calls fail, the method plays a failure cue and returns without removing the block. An empty resolved list also reaches removal. Successful use removes the core; this is not a reusable training station. Sneak-use instead follows the pickup branch before checking phase.', '',
        '??? info "Checked properties and preservation limits"', '',
        '    - Item: default **64-item stack limit** and fire resistance. Differing phase or EP components are not assumed to merge.',
        '    - Block constructor: strength **0.5**, Shroomlight sounds, `noOcclusion`, and blocked piston reaction.',
        '    - State-dependent light: **2 inactive**, **12 active**, **8 inert**; the older non-luminous label is not used.',
        '    - Placement tracks the clicked face and supports waterlogging. This does not establish that water neutralizes its explosion.',
        '    - Block-entity and loot methods preserve EP and phase components. Server pickup behavior and component retention were not tested live.', '',
        '## Source and licensing', '',
        '[Blocks/Charybdis Core](https://tensura.wiki.gg/wiki/Blocks/Charybdis_Core?oldid=9626), recorded revision `9626`, on the Tensura: Reincarnated Wiki. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The checked interaction and light rules supersede the unfinished block article’s conflicting fields.', '',
        f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [core evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/charybdis_core_reference.json) · [tracked core configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{data["configuration"]["path"]}). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
        'The core illustrations are original TSR conceptual artwork, not game textures. Reviewed source File pages did not establish reusable image permission; neither their images nor the embedded player-chat screenshot is reproduced. See [Sources and attribution](../../project/sources-and-attribution.md).', '',
        '[Back to Blocks](index.md) · [Core item](../items/charybdis-core.md) · [Inert core](../items/inert-charybdis-core.md) · [Charybdis Cave](../structures/structures-charybdis-cave.md)', '',
    ])
