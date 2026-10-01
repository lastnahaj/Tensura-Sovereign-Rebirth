"""Render the artifact-backed casting-staff comparison guide."""


def generate(data):
    lines = ['---', 'title: Magic Staves', 'description: Compare staff capacities, cooldowns, durability, and smithing requirements for Minecraft 1.21.1.', '---', '',
             '<section class="reference-overview reference-theme-abilities staff-guide-hero">',
             '<figure class="reference-overview-media"><img src="../../../assets/images/items/low-magic-staff.webp" alt="Original wooden casting staff illustration with a cyan crystal" loading="eager" decoding="async"><figcaption>TSR illustration · not the in-game texture</figcaption></figure>',
             '<div class="reference-overview-copy"><p class="reference-eyebrow">Casting equipment · Minecraft 1.21.1</p><h1>Choose your casting staff</h1><p>Compare the three registered staff tiers. Prepare the materials and learned schematics, then account for base spell capacity and the Magic Capacity enchantment.</p>',
             '<nav class="reference-quick-jumps" aria-label="Staff guide"><a href="../">Browse Items</a><a href="../../magic/low-magic-staff/">Low Staff reference</a></nav></div></section>', '',
             '<section class="potion-guide"><div class="potion-guide-grid">']
    for staff in data['staff_tiers']:
        lines.extend(['<article class="potion-guide-card staff-tier-card">', '<p class="reference-eyebrow">' + staff['tier'] + ' tier</p>',
                      '<h2>' + staff['tier'] + ' Magic Staff</h2>', f'<p class="staff-capacity"><strong>{staff["base_slots"]}</strong><span>base spell slots</span></p>',
                      f'<dl><div><dt>Base cooldown</dt><dd>{staff["cooldown_ticks"]} <small>ticks · not chant duration</small></dd></div><div><dt>Durability</dt><dd>{staff["durability"]} <small>base maximum</small></dd></div></dl>',
                      '<details><summary>Crafting &amp; schematics</summary><p>At a <a href="../../blocks/blocks-smithing-bench/">Smithing Bench</a>: one <a href="../../magic/magic-stone/">Magic Stone</a>, two <a href="../' + staff['ingot_page'].removesuffix('.md') + '/">' + staff['ingot'] + ' Ingots</a>, and three Sticks produce one staff.</p>',
                      '<p>Learn <strong>both</strong>:</p><ul><li><a href="../' + staff['schematic_page'].removesuffix('.md') + '/">' + staff['schematic'] + ' Schematic</a></li><li><a href="../../magic/magic-staff-schematic/">Magic Staff Schematic</a></li></ul></details>', '</article>'])
    lines.extend(['</div></section>', '', '## Learn the schematics', '',
                  'Use a schematic to learn it; carrying the item alone does not unlock smithing. Learning an unknown schematic consumes one copy. Using a schematic already learned does not consume another copy in the checked method.', '',
                  'The [Magic Staff Schematic](../magic/magic-staff-schematic.md) appears in level-five Magic Trainer dwarf trades for a base cost of ten Gold Coins with TSR’s checked-in price multiplier of 1.0. The final trade price and the merchant’s selected offers can differ; check the in-game trading screen. Material-tier schematics remain separate requirements.', '',
                  'The [Low](items-schematics-low-magisteel-gear-schematic.md), [High](items-schematics-high-magisteel-gear-schematic.md), and [Pure](items-schematics-pure-magisteel-gear-schematic.md) Magisteel Gear schematics are rewards from the matching ingot inventory advancements. Receive the reward, then use the blueprint to learn it. The advancement reward is not granted anew for every ingot pickup; replacement copies and reset interactions remain unverified.', '', '## Prepare the staff', '',
                  'Use the [Spellbinding Table](../resistances/spellbinding-table.md) to bind compatible spells. An empty stored spell list causes the staff’s use method to fail. The [Low Staff reference](../magic/low-magic-staff.md) gives the starter recipe and implementation evidence.', '',
                  '## Read capacity correctly', '',
                  'Base capacities are **3 / 4 / 5** for Low / Medium / High. The slot calculation adds the item’s **Magic Capacity enchantment level**. These figures do not prove an acquisition route or binding compatibility for every spell.', '',
                  '## Separate cooldown from chant speed', '',
                  'The staff constructors specify **20 / 10 / 5 ticks** of base staff cooldown, separate from spell chant duration. Their additive Chant Speed attribute bonuses are **+0.05 / +0.10 / +0.20** while held; these raw attribute values are not described as percentage reductions.', '',
                  '!!! note "Verification scope"', '    Registration, ingredients, learned-schematic checks, base slots, cooldowns, and durability are checked against the selected artifact. Spell-specific costs, gear-evolution triggers, server overrides, and live casting tests remain outside this check.', '',
                  '## Sources and artwork', '', 'Implementation: [Tensura 2.0.1.2 release](' + data['reference_build']['source_url'] + ') · [TSR item evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json). The [Low Staff article](../magic/low-magic-staff.md) credits its imported upstream revision. The original illustration is not an in-game appearance guarantee.', '',
                  '??? info "Artifact evidence"', '', '    - `io/github/manasmods/tensura/registry/item/TensuraToolItems.class`', '    - `io/github/manasmods/tensura/item/weapon/spell/SimpleSpellCastItem.class`', '    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`'])
    lines.extend('    - `' + staff['recipe'] + '`' for staff in data['staff_tiers'])
    for material in ('low_magisteel', 'high_magisteel', 'pure_magisteel'):
        lines.extend(['    - `data/tensura/advancement/' + material + '.json`', '    - `data/tensura/loot_table/advancement_reward/' + material + '.json`'])
    lines.extend(['', '[Return to Items](index.md)', ''])
    return '\n'.join(lines)
