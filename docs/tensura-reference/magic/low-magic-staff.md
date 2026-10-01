---
title: "Low Magic Staff"
description: "A three-slot casting staff crafted with Magic Stone, Low Magisteel, and sticks. Both the Low Magisteel Gear and Magic Staff schematics must be learned."
---

# Low Magic Staff

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/low-magic-staff.webp" alt="Low Magic Staff illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A three-slot casting staff crafted with Magic Stone, Low Magisteel, and sticks. Both the Low Magisteel Gear and Magic Staff schematics must be learned.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Crafting unlocks and base capacity verified"
    Survival smithing checks require both listed schematics, not either one. The three-slot figure is the base capacity; Magic Capacity adds its enchantment level to that value.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Low Magic Staff</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:low_magic_staff</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Crafting unlocks and base capacity verified</div></div>
</aside></div></div>

## Availability

Learn the [Low Magisteel Gear Schematic](../items/items-schematics-low-magisteel-gear-schematic.md) and the [Magic Staff Schematic](magic-staff-schematic.md). At a [Smithing Bench](../blocks/blocks-smithing-bench.md), combine one [Magic Stone](magic-stone.md), two [Low Magisteel Ingots](../items/low-magisteel-ingot.md), and three Sticks to produce one Low Magic Staff. SmithingBenchRecipe.hasUnlocked checks that the learned schematic set contains all required schematics; Creative mode has a separate bypass.

## How to use

Bind a compatible spell through the [Spellbinding Table](../resistances/spellbinding-table.md), then use the staff with a selected bound spell. The staff's use method fails if its stored spell list is empty. Base capacity is three spells; getMagicSlots adds the item's Magic Capacity enchantment level. See the [staff comparison guide](../items/magic-staves.md) for Medium and High crafting requirements and base capacities.

## Behavior and limits

The registered Low staff has 100 base durability, a 20-tick base staff cooldown, and a +0.05 additive Chant Speed attribute modifier while held. The cooldown is not the spell's chant duration, and the attribute value is not stated here as a percentage reduction. Binding slots do not establish an acquisition route for every spell. Spell-specific costs, gear-evolution triggers, server overrides, and live casting behavior are outside this check.

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Low Magic Staff](https://tensura.wiki.gg/wiki/Low_Magic_Staff) on the Tensura: Reincarnated Wiki, recorded revision `12847`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraToolItems.class`
    - `io/github/manasmods/tensura/item/weapon/spell/SimpleSpellCastItem.class`
    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`
    - `data/tensura/recipe/smithing/low_magic_staff.json`
