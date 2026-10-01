---
title: "High Magisteel Gear Schematic"
description: "Receive the blueprint through the High Magisteel inventory advancement, then use it to learn the crafting unlock. It supplies the material-tier requirement for a Medium Magic Staff."
---

# High Magisteel Gear Schematic

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/crafting-schematic.webp" alt="High Magisteel Gear Schematic illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Receive the blueprint through the High Magisteel inventory advancement, then use it to learn the crafting unlock. It supplies the material-tier requirement for a Medium Magic Staff.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Advancement reward and learning verified"
    Receiving the advancement reward and learning the schematic are separate steps. Medium Magic Staff crafting also requires the Magic Staff Schematic.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">High Magisteel Gear Schematic</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:high_magisteel_gear_schematic</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Advancement reward and learning verified</div></div>
</aside></div></div>

## Availability

Obtain a [High Magisteel Ingot](high-magisteel-ingot.md). The tensura:high_magisteel advancement checks for that item on inventory_changed and supplies its advancement-reward loot table, which contains this schematic. This is an advancement reward, not a repeatable drop from every ingot pickup. Replacement copies and reset interactions are unverified.

## How to use

Use the rewarded blueprint to learn it. The shared SmithingSchematicItem implementation consumes one copy only when unlocking an unknown schematic. Already learned copies are not consumed by that method. Check the recipe browser for the full set of learned requirements.

## Behavior and limits

The registered item is Uncommon and stacks to 16. The [Medium Magic Staff recipe](magic-staves.md) requires this High Magisteel Gear Schematic plus the Magic Staff Schematic: one Magic Stone, two High Magisteel Ingots, and three Sticks. Do not substitute the Low or Pure material-tier schematic. Server overrides and prestige retention have not been tested.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Items/Schematics/High Magisteel Gear Schematic](https://tensura.wiki.gg/wiki/Items/Schematics/High_Magisteel_Gear_Schematic) on the Tensura: Reincarnated Wiki, recorded revision `9439`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `data/tensura/advancement/high_magisteel.json`
    - `data/tensura/loot_table/advancement_reward/high_magisteel.json`
    - `data/tensura/recipe/smithing/medium_magic_staff.json`
    - `io/github/manasmods/tensura/registry/item/TensuraSmithingSchematicItems.class`
    - `io/github/manasmods/tensura/item/misc/SmithingSchematicItem.class`
    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`
