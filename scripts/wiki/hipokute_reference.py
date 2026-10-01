"""Render the pinned Hipokute harvest reference and farming walkthrough."""
from __future__ import annotations

import html


def entries(data):
    evidence = data['hipokute']['evidence_paths']
    common = {
        'category': 'items', 'catalogue_entry': True, 'acquisition_verified': True,
        'status': 'Plant harvest and loot checked', 'notice_kind': 'info',
        'warning': 'Growth, harvest, and loot rules are checked against Tensura 2.0.1.2 for Minecraft 1.21.1. Live farm yields, server datapack overrides, and add-on interactions remain untested.',
        'stats': {'Rarity': 'Common', 'Stack limit': 64},
        'legacy_anchors': {'Availability': ['Obtainment'], 'How to use': ['Usage']},
        'evidence_paths': evidence,
    }
    pages = [
        ('seeds', 'Plant a renewable supply of potion ingredients. Area Magicules affect the first growth outcome; seeds are not guaranteed to remain Hipokute.',
         'Break a Hipokute plant to collect seeds. Ages 0 and 1 have a one-seed loot entry; age 2 uses a 1–3 seed count and age 3 uses 3–5, both with a Fortune bonus function. Explosion decay and loot overrides can change results. Picking a flower without breaking the plant does not use this seed-drop table.',
         'Use seeds to place the crop on **Grass Block, Dirt, or Farmland**. Irrigated farmland improves the checked growth-speed input; dense neighboring crops can reduce it. Follow the [Hipokute farming guide](../core-mechanics/mechanics-hipokute-farming.md) before expanding a plot.',
         'At the first successful growth attempt, the plant becomes a small Hipokute sprout or vanilla wheat at age 3. The Hipokute chance uses **current area Magicules**, not player MP or a biome’s nominal capacity. A surviving sprout later chooses grass or flower with equal probability. The base Hipokute class has no bonemeal growth interface; bee-assisted Hipokute growth is not verified.'),
        ('grass', 'Harvest the grass branch for brewing. Waiting longer does not turn a finished grass plant into a flower.',
         'Break the **age-2 grass branch** to collect one Hipokute Grass item and the separate seed loot entry. The checked crop does not randomly tick at age 2, so this branch will not become a flower by waiting. Natural generation includes Hipokute plants; a world-generation candidate is not a guaranteed find in a particular chunk.',
         'At a brewing stand, combine grass with [Magic Bottle of Water](../magic/magic-bottle-of-water.md) for [Low Potion](low-potion.md), or [Vacuumed Magic Bottle of Water](../magic/vacuumed-magic-bottle-of-water.md) for [High Potion](high-potion.md). [Compare brewing recipes](healing-potions.md); refining recipes are a separate system.',
         'The grass item is not the planting item: use [Hipokute Seeds](hipokute-seeds.md) to replant. Breaking a finished grass plant removes it. Keep seed reserves and see the [farming guide](../core-mechanics/mechanics-hipokute-farming.md) for the two growth decisions and seed-return limits.'),
        ('flower', 'Pick the flower branch for stronger brewing recipes, or inspect a level-three Alchemist’s offer before selling a surplus.',
         'Use an **empty hand** on a flowering **age-3 plant**. The checked server-side interaction drops one Hipokute Flower and resets the plant to age 1. Alternatively, breaking age 3 uses a one-flower loot entry plus its seed pool and removes the plant. Neither route means every grass plant can be picked for flowers.',
         'Brew a flower with [Magic Bottle of Water](../magic/magic-bottle-of-water.md) for [High Potion](high-potion.md), or [Vacuumed Magic Bottle of Water](../magic/vacuumed-magic-bottle-of-water.md) for [Full Potion](full-potion.md). One flower also crafts into one White Dye. A **level-three Alchemist Dwarf** trade candidate takes four flowers at the tracked `alchemistPriceMultiplier = 1.0` and defines a 20–50 Silver Coin output range. This does not guarantee every merchant offers it or fix a live offer’s price.',
         'Picking preserves an age-1 sprout, not a permanently flowering plant: the next successful growth decision is again **50% grass / 50% flower**. A grass result stops growing and must be broken and replanted. The [farming guide](../core-mechanics/mechanics-hipokute-farming.md) explains why a flower plot is renewable but not an endless guaranteed flower loop.'),
    ]
    return [{**common, 'local_page': f'tensura-reference/items/hipokute-{kind}.md',
             'display_title': f'Hipokute {kind.title()}', 'registry_id': 'tensura:hipokute_' + kind,
             'asset': f'assets/images/items/hipokute-{kind}.webp', 'summary': summary,
             'obtainment': obtain, 'use': use, 'effects': effects} for kind, summary, obtain, use, effects in pages]


def generate(data):
    lines = ['---', 'title: Hipokute Farming', 'description: Plant, grow, harvest, and brew Hipokute using the checked Minecraft 1.21.1 rules.', '---', '',
             '<section data-reference-section="items" class="reference-overview reference-theme-world staff-guide-hero">',
             '<figure class="reference-overview-media"><img src="../../../assets/images/items/hipokute-flower.webp" alt="Original ivory Hipokute flower illustration with green leaves" loading="eager" decoding="async"><figcaption>TSR botanical illustration · not an in-game model</figcaption></figure>',
             '<div class="reference-overview-copy"><p class="reference-eyebrow">Alchemy supply · Minecraft 1.21.1</p><h1>Grow your healing supply</h1><p>Collect seeds. Give the crop time to grow. Harvest the branch you actually have—not the one you hoped for. Hipokute links a small garden to your potion kit.</p>',
             '<nav class="reference-quick-jumps" aria-label="Hipokute guide"><a href="#plan-the-growth-decisions">Growth decisions</a><a href="#choose-your-harvest">Harvest guide</a><a href="../../items/healing-potions/">Brewing planner</a></nav></div></section>', '',
             '!!! note "Pinned 1.21.1 rules · live farm yields untested"',
             '    This guide checks Tensura 2.0.1.2’s crop class, loot table, generation resources, item constructors, and Alchemist trade definitions. It does not measure TSR’s live farm output or promise a crop timer.', '',
             '## Start a small plot', '',
             '1. Find a Hipokute plant and break it for [seeds](../items/hipokute-seeds.md). The packaged Overworld generation definition includes small, grass, and flowering states; it does not guarantee a find in every chunk.',
             '2. Plant on **Grass Block, Dirt, or Farmland**. The checked placement and survival methods accept these three blocks, not arbitrary stone.',
             '3. Prefer irrigated farmland for its growth-speed contribution. Crowding same-crop neighbors in both directions or diagonally can halve that contribution. Keep the plot in a ticking area; no fixed real-time completion is verified.',
             '4. Wait for a successful growth attempt, then identify the result. Do not spend your whole seed supply before learning how your plot behaves.', '',
             '<span id="1.21.1"></span>', '', '## Plan the growth decisions', '',
             '<div class="tensura-reference-article"><ol class="hipokute-growth" aria-label="Hipokute growth decisions"><li><strong>Seed · age 0</strong><span>After the growth-speed gate, current area Magicules determine Hipokute sprout versus wheat.</span></li><li><strong>Sprout · age 1</strong><span>A later successful growth attempt chooses grass or flower with equal probability.</span></li><li><strong>Grass · age 2 / Flower · age 3</strong><span>Both stop random growth. Break grass; pick a flower to return it to age 1.</span></li></ol></div>', '',
             'The first-decision probability is `1 / max(1, 10 − trunc(trunc(M) / 500))`, where **M is current area Magicules**. For nonnegative values this matches the upstream floor formula. It is **conditional on passing the earlier growth-speed gate**, not a chance per tick, flower yield, or guarantee of reaching flowers.', '',
             '<section class="potion-planner hipokute-calculator" data-hipokute-calculator aria-label="First growth outcome calculator"><h3>Compare an area’s current Magicules</h3><div class="potion-planner-controls"><label>Example current area Magicules<select data-hipokute-magicules><option value="0">0</option><option value="1000" selected>1,000</option><option value="2000">2,000</option><option value="3000">3,000</option><option value="4000">4,000</option><option value="4500">4,500 or more</option></select></label></div><p class="potion-planner-status" data-hipokute-result role="status" aria-live="polite">At 1,000 current area Magicules: 12.5% Hipokute sprout / 87.5% wheat at the first decision.</p><p class="potion-guide-footnote">Calculated base-rule examples, not measured yields. The separate sprout-to-harvest decision remains 50% grass / 50% flower.</p></section>', '',
             '<details><summary>Probability examples without the calculator</summary>', '<table><thead><tr><th>Current area Magicules</th><th>Hipokute sprout</th><th>Wheat</th></tr></thead><tbody>',
             '<tr><td>0</td><td>10%</td><td>90%</td></tr><tr><td>1,000</td><td>12.5%</td><td>87.5%</td></tr><tr><td>2,000</td><td>16.67%</td><td>83.33%</td></tr><tr><td>3,000</td><td>25%</td><td>75%</td></tr><tr><td>4,000</td><td>50%</td><td>50%</td></tr><tr><td>4,500 or more</td><td>100%</td><td>0%</td></tr>',
             '</tbody></table><p>Examples round to two decimal places. A 100% sprout outcome still does not guarantee a flower or bypass the growth-speed gate. A dimension’s name alone is not proof of its current Magicules.</p></details>', '',
             '## Choose your harvest', '', '<section class="potion-guide"><div class="potion-guide-grid">']
    harvests = [
        ('seeds', 'Replant', 'Break the plant', 'Ages 0–1 have a one-seed entry; grass uses 1–3 seeds and flower uses 3–5, with a Fortune bonus function on the mature pools.', 'Loot counts are not a guaranteed final stack: Fortune, explosion decay, and overrides matter. Picking a flower does not run the seed loot table.'),
        ('grass', 'Brew or restart', 'Break age 2', 'Collect the grass item and seed loot. Finished grass cannot grow into a flower simply by waiting.', 'Plant a new seed if you want another first-stage attempt. Grass + water bottle makes Low Potion; grass + vacuumed water bottle makes High Potion.'),
        ('flower', 'Pick and regrow', 'Empty-hand use at age 3', 'Collect one flower and reset the standing plant to age 1. Breaking it instead also gives the flower and seed loot, but removes the plant.', 'The next branch is again 50/50. Flower + water bottle makes High Potion; flower + vacuumed water bottle makes Full Potion.'),
    ]
    for kind, action, interaction, summary, detail in harvests:
        lines.extend(['<article class="potion-guide-card hipokute-harvest-card">',
                      f'<a href="../../items/hipokute-{kind}/"><img src="../../../assets/images/items/hipokute-{kind}.webp" alt="Hipokute {kind} botanical illustration" loading="lazy" decoding="async"><h2>Hipokute {kind.title()}</h2></a>',
                      f'<p class="reference-eyebrow">{action}</p><p><strong>{interaction}</strong><br>{html.escape(summary)}</p>',
                      f'<details><summary>Harvest limits &amp; next step</summary><p>{html.escape(detail)}</p></details>', '</article>'])
    lines.extend(['</div></section>', '', '## Use the harvest', '',
                  'Reserve seeds to restart grass outcomes. Save some flowers for your [healing-potion kit](../items/healing-potions.md) before selling the surplus. A level-three Alchemist Dwarf has a four-flower → 20–50 Silver Coin trade candidate at the tracked `alchemistPriceMultiplier = 1.0`. The definition is checked, but a particular merchant’s availability and live offer remain untested. One flower also crafts into one White Dye.', '',
                  '??? info "Why waiting or bonemeal may not solve the plot"', '',
                  '    Age-2 grass and age-3 flowers do not randomly tick in the base crop. Flowers need empty-hand picking to return to the sprout stage; grass needs breaking and replanting. The checked class has no bonemeal growth interface. Bee-assisted Hipokute growth is not verified, and neither mechanism is a substitute for the two growth decisions.', '',
                  '<span id="1.19.2"></span>', '', '## Version scope', '',
                  'The older 1.19.2 dimension-specific seed percentages are not the farming rules used here. The 1.21.1 check uses current area Magicules and does not treat Hell or a biome label as an automatic flower guarantee.', '',
                  '## Source and licensing', '',
                  'Upstream adaptation: [Hipokute Farming](https://tensura.wiki.gg/wiki/Mechanics/Hipokute_Farming), recorded revision `12190`; [Grass](https://tensura.wiki.gg/wiki/Hipokute_Grass), [Flower](https://tensura.wiki.gg/wiki/Hipokute_Flower), and [Seeds](https://tensura.wiki.gg/wiki/Hipokute_Seeds). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
                  'Implementation: [Tensura 2.0.1.2](' + data['reference_build']['source_url'] + ') · [plant evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json) · [tracked Alchemist configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/entity/entity_config.toml). These are artifact and configuration checks, not live-server trials.', '',
                  'Original TSR botanical illustrations replace source images without verified reusable image permission. They are conceptual references, not crop-stage textures or in-game models. See the [source and media ledger](../../project/sources-and-attribution.md).', '',
                  '??? info "Artifact evidence"', ''])
    lines.extend('    - `' + path + '`' for path in data['hipokute']['evidence_paths'])
    lines.extend(['', '[Compare healing recipes](../items/healing-potions.md) · [Return to Items](../items/index.md)', ''])
    return '\n'.join(lines)
