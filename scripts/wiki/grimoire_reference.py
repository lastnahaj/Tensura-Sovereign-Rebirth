"""Render artifact-backed grimoire references and a tier comparison."""
from __future__ import annotations

import html


def entries(data):
    result = []
    for tier in data['grimoire_tiers']:
        special = tier['tier'] == 'Special A'
        status = 'Base evolution route checked' if special else 'Wizard Tower chest loot checked'
        acquisition = (
            'The pinned base gear data maps [Grimoire A](grimoire-a.md) to this item at **80,000 gear EP**, not the 100,000 stated in the older upstream article. No direct Special A entry was found in the five reviewed Wizard Tower chest definitions.'
            if special else
            'This tier appears in the **Buried, Burnt, Frozen, Rotted, and Ruined Wizard Tower** chest loot definitions. It is a weighted candidate, not a guaranteed chest result. These definitions do not verify world placement or prove that every generated tower supplies a grimoire.'
        )
        if tier['tier'] == 'D':
            acquisition += ' The Magic Trainer dwarf chest definition also includes D; that is chest loot, not evidence of a merchant trade.'
        acquisition += ' No ordinary packaged crafting recipe mentioning these grimoire IDs was found. Server datapacks, trades, and add-on overrides remain separate checks.'
        evolution = (
            f'The base gear definition points to [Grimoire {tier["next_tier"]}]({tier["next_slug"]}.md) at **{tier["max_ep"]:,} gear EP**. The checked death-handler evolution path requires initialized EP components and is blocked by the Stagnation enchantment.'
            if tier['next_slug'] else
            'The Special A gear JSON contains no successor or explicit maximum EP. The checked GearExistenceData codec supplies a **2,000,000 maximum EP** default. Its minimum is **80,000 EP** when the base initializer applies; it is not an unlimited EP item or a further evolution route.'
        )
        result.append({
            'local_page': f'tensura-reference/items/{tier["slug"]}.md',
            'display_title': f'Grimoire {tier["tier"]}', 'category': 'items',
            'asset': 'assets/images/items/grimoire.webp', 'catalogue_entry': True,
            'registry_id': tier['registry_id'], 'status': status, 'acquisition_verified': True,
            'notice_kind': 'info',
            'warning': 'Item constructors, base gear data, and the stated supply route are checked against Tensura 2.0.1.2. TSR also uses Gear Evolution; its overrides, current stack components, and live casting/evolution behavior are not verified by this base-artifact check.',
            'summary': f'A {tier["base_slots"]}-slot caster book with a {tier["cooldown_ticks"]}-tick base item cooldown. Compare its loot route, spell controls, and base gear progression.',
            'stats': {'Rarity': tier['rarity'], 'Stack limit': 1, 'Base spell slots': tier['base_slots'], 'Base item cooldown': f'{tier["cooldown_ticks"]} ticks', 'Base durability': tier['durability'], 'Chant Speed attribute': f'+{tier["chant_bonus"]:.2f}'},
            'legacy_anchors': {'Availability': ['Obtainment'], 'How to use': ['Usage'], 'Behavior and limits': ['Description']},
            'obtainment': acquisition,
            'use': 'Put the book in the [Spellbinding Table](../resistances/spellbinding-table.md) and bind eligible learned magic. Ordinary binding needs nonnegative mastery, capacity, and equip checks—not full mastery. Hold the book and use it to cast the selected stored spell; an empty spell list cannot cast. Use your assigned **Next Ability Mode** modifier plus scroll to select a spell, or modifier plus item use to change its mode. See the [casting walkthrough](../tools/caster-tools-tutorial.md) for exclusions and resource checks. Binding and casting do not automatically teach the stored spell.',
            'effects': f'The fresh item constructor has **{tier["base_slots"]} base spell slots**, **{tier["cooldown_ticks"]} ticks** of item cooldown, **{tier["durability"]} durability**, and **{tier["rarity"]}** rarity. Magic Capacity adds its enchantment level to the slot calculation. The held Chant Speed attribute adds **+{tier["chant_bonus"]:.2f}**; this is not a percentage reduction or a promised final casting time.\n\n{evolution}\n\nProgression EP and `EP_DURABILITY` are distinct from ordinary item durability. The checked Magic resource method can draw MP contribution from stored gear EP when its conditions are met; it does not bypass Aura costs or make casting free. [Compare all five tiers](grimoires.md) for base thresholds and the server-override limits. The shared illustration represents grimoire equipment, not the exact appearance of this tier.',
            'evidence_paths': [
                'io/github/manasmods/tensura/registry/item/TensuraToolItems.class',
                'io/github/manasmods/tensura/item/weapon/spell/SimpleSpellCastItem.class',
                'io/github/manasmods/tensura/handler/GearHandler.class',
                'io/github/manasmods/tensura/handler/DeathHandler.class',
                'io/github/manasmods/tensura/data/existence/gear/GearExistenceData.class',
                'io/github/manasmods/tensura/ability/Magic.class',
                f'data/tensura/gear_existence/{tier["registry_id"].split(":")[1]}.json',
                'data/tensura/tags/item/magic_grimoires.json',
                *[f'data/tensura/loot_table/chests/{kind}_wizard_tower.json' for kind in data['grimoire_verification']['wizard_tower_loot']],
            ],
        })
    return result


def generate(data):
    lines = ['---', 'title: Grimoires', 'description: Compare grimoire slots, cooldowns, loot routes, and the pinned base equipment evolution chain.', '---', '',
             '<section data-reference-section="items" class="reference-overview reference-theme-abilities staff-guide-hero">',
             '<figure class="reference-overview-media"><img src="../../../assets/images/items/grimoire.webp" alt="Original open grimoire illustration with a cyan spell diagram" loading="eager" decoding="async"><figcaption>TSR illustration · equipment class, not a tier texture</figcaption></figure>',
             '<div class="reference-overview-copy"><p class="reference-eyebrow">Caster equipment · Minecraft 1.21.1</p><h1>Choose your grimoire</h1><p>Five tiers. More room for spells, shorter base item cooldowns, and a linked equipment progression. Start with a book you can obtain, then distinguish its spell loadout, gear EP, and casting fuel.</p>',
             '<nav class="reference-quick-jumps" aria-label="Grimoire guide"><a href="#compare-the-tiers">Compare tiers</a><a href="#follow-the-base-evolution-chain">Evolution chain</a><a href="../../tools/caster-tools-tutorial/">Casting walkthrough</a></nav></div></section>', '',
             '!!! note "Base artifact values, not a live-server guarantee"',
             '    These values come from Tensura 2.0.1.2. TSR also selects Gear Evolution 1.2.5 and allows datapack chain extensions. The table is a base reference; current stack components, add-on thresholds, and live equipment retention remain unverified.', '',
             '## Compare the tiers', '', '<section class="potion-guide"><div class="potion-guide-grid">']
    for tier in data['grimoire_tiers']:
        supply = 'A-tier evolution; no direct Tower drop verified' if tier['tier'] == 'Special A' else 'Candidate in five Tower chest definitions'
        next_step = f'<a href="../{tier["next_slug"]}/">{html.escape(tier["next_tier"])} at {tier["max_ep"]:,} base gear EP →</a>' if tier['next_slug'] else 'No successor in the base definition'
        lines.extend(['<article class="potion-guide-card staff-tier-card">', f'<p class="reference-eyebrow">{tier["rarity"]} · caster book</p>',
                      f'<h2><a href="../{tier["slug"]}/">Grimoire {html.escape(tier["tier"])}</a></h2>',
                      f'<p class="staff-capacity"><strong>{tier["base_slots"]}</strong><span>base spell slots</span></p>',
                      f'<dl><div><dt>Item cooldown</dt><dd>{tier["cooldown_ticks"]}<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+{tier["chant_bonus"]:.2f}<small>additive, not a percentage</small></dd></div></dl>',
                      '<details><summary>Supply &amp; progression</summary>', f'<p>{supply}. Read the <a href="../{tier["slug"]}/#availability">item supply notes</a> before planning a trip.</p>',
                      f'<p><strong>Base durability:</strong> {tier["durability"]}; <strong>stack limit:</strong> 1.</p><p>{next_step}</p></details>', '</article>'])
    lines.extend(['</div></section>', '', '## Follow the base evolution chain', '',
                  'These are **equipment EP** thresholds, not player EP requirements or a count of spell casts. The pinned finite-tier definitions and checked evolution method give:', '',
                  '| Current book | Base initialized EP | Base evolution threshold | Successor |', '|---|---:|---:|---|'])
    for tier in data['grimoire_tiers']:
        if tier['next_slug']:
            lines.append(f'| [{tier["tier"]}]({tier["slug"]}.md) | {tier["min_ep"]:,} | {tier["max_ep"]:,} | [{tier["next_tier"]}]({tier["next_slug"]}.md) |')
    lines.extend(['', 'A evolves toward Special A at **80,000 EP** in the base artifact; the older upstream article says 100,000. The death-handler path requires initialized gear components, checks the threshold, and refuses the ordinary tier transition when **Stagnation** is present. Existing gear component patches are carried to the replacement stack before the next tier is initialized; this is not a promise that every add-on component survives.', '',
                  'Special A has no successor and omits maxEP in its JSON, but the checked **GearExistenceData codec defaults that field to 2,000,000**. The base initializer uses its **80,000 minimum EP** when initializing a fresh eligible stack. Existing components and add-on overrides can differ; this is not infinite EP or proof of another tier.', '',
                  'Gear EP gain depends on the death-handler input, game rules, item EP_GAIN, and enchantments including Lethargy, Vigor, and Growth. It is rounded in the checked base helper. A fixed number of kills or casts is not verified. Use [Gear Evolution](../../gear-evolution.md) for TSR’s wider equipment system; current add-on threshold and retention behavior still needs gameplay checks.', '',
                  '## Find a book, then bind a loadout', '',
                  'D, C, B, and A are candidates in Buried, Burnt, Frozen, Rotted, and Ruined Wizard Tower chest definitions. Relative loot weights are not guaranteed drops or per-tower percentages. No Special A direct entry or ordinary grimoire crafting recipe was found in those packaged resources.', '',
                  'Bind compatible learned spells at the [Spellbinding Table](../resistances/spellbinding-table.md). Magic Capacity adds its enchantment level to base slots. Binding does not teach spells. The [casting walkthrough](../tools/caster-tools-tutorial.md) covers modifier-and-scroll selection, mode changes, unlearned-casting exclusions, and costs.', '',
                  '## Separate three resource concepts', '',
                  '- **Gear EP:** the equipment progression value used for base tier thresholds.',
                  '- **EP_DURABILITY:** the stored gear resource checked for a contribution toward MP casting costs when the required conditions apply.',
                  '- **Ordinary durability:** the item’s separate damageable durability; the base maxima are 100 / 200 / 300 / 400 / 500.', '',
                  'An initialized book is not unlimited fuel, and gear EP support does not waive Aura costs. Raw Chant Speed bonuses are not percentage discounts or final wall-clock casting times.', '',
                  '## Sources and artwork', '',
                  'Implementation: [Tensura 2.0.1.2 release](' + data['reference_build']['source_url'] + ') · [item and tier evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json). Individual tier articles credit their upstream revisions under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '',
                  '[Gear Evolution selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-gear-evolution.pw.toml) · [tracked configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/gearevolution-common.toml). Configuration inspection is not a live-server evolution or prestige-retention test.', '',
                  'The open-book illustration is original TSR artwork shared by the five tier references. It represents the equipment class, not five different verified textures. The upstream inventory images have no verified reusable image license and are not reproduced.', '', '[Return to Items](index.md)', ''])
    return '\n'.join(lines)
