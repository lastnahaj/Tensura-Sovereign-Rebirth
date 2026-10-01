---
title: "Magic Bottle of Water"
description: "Fill an empty Magic Bottle at a water source. Brew grass into Low Potion or flower into High Potion, or cook the bottle into a vacuumed base."
---

# Magic Bottle of Water

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-bottle-of-water.webp" alt="Magic Bottle of Water illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Fill an empty Magic Bottle at a water source. Brew grass into Low Potion or flower into High Potion, or cook the bottle into a vacuumed base.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Filling route verified"
    The pinned filled-bottle implementation stacks to 16, not the source page's older value of 64. Ordinary bottled water is registered with zero MP recovery.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Bottle of Water</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_bottle_of_water</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Filling route verified</div></div>
</aside></div></div>

## Availability

Use an empty [Magic Bottle](magic-bottle.md) on a permitted water source. The filled item is registered as tensura:magic_bottle_of_water; it is not a vanilla Water Bottle.

## How to use

At a brewing stand, combine this base with [Hipokute Grass](../items/hipokute-grass.md) for [Low Potion](../items/low-potion.md) or [Hipokute Flower](../items/hipokute-flower.md) for [High Potion](../items/high-potion.md). Cook it in a furnace or smoker for 60 ticks, or on a campfire for 180 ticks, to obtain [Vacuumed Magic Bottle of Water](vacuumed-magic-bottle-of-water.md). Consult the healing-potion guide for the complete recipe comparison.

## Behavior and limits

The item uses ManaPotionItem with zero food, saturation, and MP recovery. Drinking takes 16 ticks and returns an empty Magic Bottle in survival. Sneak-use throws the bottle; direct living-target interaction is also implemented. Filled bottles stack to 16.

[Compare recipes in the healing-potion guide](../items/healing-potions.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Bottle of Water](https://tensura.wiki.gg/wiki/Magic_Bottle_of_Water) on the Tensura: Reincarnated Wiki, recorded revision `9554`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/item/consumable/MagicBottleItem.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `data/minecraft/recipe/vacuumed_magic_bottle_of_water_from_smelting.json`
