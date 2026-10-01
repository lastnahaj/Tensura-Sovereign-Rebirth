---
title: "Magic Staff Schematic"
description: "Learn the casting-staff blueprint by using one schematic. A level-five Magic Trainer dwarf offers it for a base cost of ten Gold Coins before trade adjustments."
---

# Magic Staff Schematic

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/crafting-schematic.webp" alt="Magic Staff Schematic illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Learn the casting-staff blueprint by using one schematic. A level-five Magic Trainer dwarf offers it for a base cost of ten Gold Coins before trade adjustments.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Trade and learning behavior verified"
    A schematic must be learned, not merely carried. Learning consumes one copy only when this schematic is not already unlocked. Staff recipes also require the matching material-tier gear schematic.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Staff Schematic</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_staff_schematic</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Trade and learning behavior verified</div></div>
</aside></div></div>

## Availability

Reach the level-five (Master) trades of a [Magic Trainer dwarf](../mobs/mobs-dwarf.md). The pinned trade list includes one Magic Staff Schematic for a base cost of ten Gold Coins multiplied by magicTrainerPriceMultiplier. TSR's checked-in multiplier is 1.0. This is the base offer, not a guarantee of the final displayed price or of every merchant's selected offers. Confirm the actual trade in game; live-server trades have not been tested.

## How to use

Hold the schematic and use the item. On the server, SmithingSchematicItem.use checks whether the player already knows it. If not, it unlocks the schematic, marks the player data dirty, sends the unlock message, and consumes one copy. Reusing an already learned schematic does not consume another copy in this method.

## Behavior and limits

The registered item is Uncommon and stacks to 16. The [casting-staff guide](../items/magic-staves.md) documents Low, Medium, and High recipes that require this learned schematic plus their Low, High, or Pure Magisteel Gear schematic respectively. Smithing requires the complete learned set; the physical blueprint is not a recipe ingredient. This check does not establish schematic retention across prestige resets, merchant restocking, or add-on overrides.

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Staff Schematic](https://tensura.wiki.gg/wiki/Magic_Staff_Schematic) on the Tensura: Reincarnated Wiki, recorded revision `13424`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraSmithingSchematicItems.class`
    - `io/github/manasmods/tensura/item/misc/SmithingSchematicItem.class`
    - `io/github/manasmods/tensura/entity/merchant/profession/DwarfProfession.class`
    - `io/github/manasmods/tensura/entity/merchant/trade/OneForOneTrade.class`
    - `io/github/manasmods/tensura/recipe/SmithingBenchRecipe.class`
    - `pack/config/tensura/entity/entity_config.toml`
