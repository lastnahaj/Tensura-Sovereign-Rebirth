---
title: "Pure Magisteel Gear Schematic"
description: "Receive the blueprint through the Pure Magisteel inventory advancement, then use it to learn the crafting unlock. It supplies the material-tier requirement for a High Magic Staff."
---

# Pure Magisteel Gear Schematic

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/crafting-schematic.webp" alt="Pure Magisteel Gear Schematic illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Receive the blueprint through the Pure Magisteel inventory advancement, then use it to learn the crafting unlock. It supplies the material-tier requirement for a High Magic Staff.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Advancement reward and learning verified"
    Receiving the advancement reward does not replace learning the schematic. High Magic Staff crafting requires this blueprint's unlock and the separate Magic Staff Schematic.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Pure Magisteel Gear Schematic</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:pure_magisteel_gear_schematic</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Advancement reward and learning verified</div></div>
</aside></div></div>

## Availability

Obtain a [Pure Magisteel Ingot](pure-magisteel-ingot.md). The tensura:pure_magisteel advancement checks for that item on inventory_changed and calls its advancement-reward loot table, which contains this schematic. The route is an advancement reward, not a repeatable reward for every ingot pickup. Replacement copies after loss or resets are unverified.

## How to use

Hold and use the rewarded schematic. The shared item method records its unlock and consumes one copy only if it is not already learned. A blueprint left unused in your inventory does not satisfy the learned-schematic gate.

## Behavior and limits

The registered schematic is Uncommon and stacks to 16. The [High Magic Staff recipe](magic-staves.md) requires this Pure Magisteel Gear Schematic plus the Magic Staff Schematic: one Magic Stone, two Pure Magisteel Ingots, and three Sticks. Do not confuse High staff tier with High Magisteel material tier. Live-server recipe overrides and prestige retention remain untested.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Items/Schematics/Pure Magisteel Gear Schematic](https://tensura.wiki.gg/wiki/Items/Schematics/Pure_Magisteel_Gear_Schematic) on the Tensura: Reincarnated Wiki, recorded revision `9440`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `data/tensura/advancement/pure_magisteel.json`
    - `data/tensura/loot_table/advancement_reward/pure_magisteel.json`
    - `data/tensura/recipe/smithing/high_magic_staff.json`
    - `io/github/manasmods/tensura/registry/item/TensuraSmithingSchematicItems.class`
    - `io/github/manasmods/tensura/item/misc/SmithingSchematicItem.class`
    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`
