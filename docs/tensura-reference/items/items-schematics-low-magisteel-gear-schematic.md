---
title: "Low Magisteel Gear Schematic"
description: "Receive the blueprint through the Low Magisteel inventory advancement, then use it to learn the crafting unlock. Receiving and learning are separate steps."
---

# Low Magisteel Gear Schematic

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/crafting-schematic.webp" alt="Low Magisteel Gear Schematic illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Receive the blueprint through the Low Magisteel inventory advancement, then use it to learn the crafting unlock. Receiving and learning are separate steps.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Advancement reward and learning verified"
    Getting an ingot rewards the schematic through an advancement; it does not directly teach every recipe. Use the rewarded schematic to learn it before smithing.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Low Magisteel Gear Schematic</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:low_magisteel_gear_schematic</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Advancement reward and learning verified</div></div>
</aside></div></div>

## Availability

Obtain a [Low Magisteel Ingot](low-magisteel-ingot.md). The tensura:low_magisteel advancement uses an inventory_changed criterion matching that item and calls the low_magisteel advancement-reward loot table, which contains this schematic. The documented supply is an advancement reward, not a repeatable reward for every ingot pickup. Replacement copies after loss, advancement resets, or prestige have not been verified.

## How to use

Hold the rewarded schematic and use it. SmithingSchematicItem.use records the unlock and consumes one copy only if this schematic is not already learned. Carrying an unused blueprint is not sufficient for the Smithing Bench's learned-schematic check.

## Behavior and limits

This registered schematic is Uncommon and stacks to 16. It is required for the [Magic Stone](../magic/magic-stone.md) recipe and [Magic Crystal downgrades](magic-crystals.md). A [Low Magic Staff](../magic/low-magic-staff.md) also requires the separate Magic Staff Schematic. Recipes can demand multiple learned schematics; this item does not unlock every Low Magisteel recipe on its own. Live-server overrides and prestige retention remain untested.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Items/Schematics/Low Magisteel Gear Schematic](https://tensura.wiki.gg/wiki/Items/Schematics/Low_Magisteel_Gear_Schematic) on the Tensura: Reincarnated Wiki, recorded revision `13088`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `data/tensura/advancement/low_magisteel.json`
    - `data/tensura/loot_table/advancement_reward/low_magisteel.json`
    - `io/github/manasmods/tensura/registry/item/TensuraSmithingSchematicItems.class`
    - `io/github/manasmods/tensura/item/misc/SmithingSchematicItem.class`
    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`
