---
title: "Vacuumed Magic Bottle of Water"
description: "Cook a Magic Bottle of Water to prepare the base for High and Full Potions. The filled item also restores a fixed 10 MP at full effect strength."
---

# Vacuumed Magic Bottle of Water

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/vacuumed-magic-bottle-of-water.webp" alt="Vacuumed Magic Bottle of Water illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Cook a Magic Bottle of Water to prepare the base for High and Full Potions. The filled item also restores a fixed 10 MP at full effect strength.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Cooking route verified"
    Vacuumed water uses fixed 10 MP recovery, not 10% of maximum MP. Its stack limit is 16. Recipe and code checks do not verify server-specific gameplay changes.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Vacuumed Magic Bottle of Water</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:vacuumed_magic_bottle_of_water</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Cooking route verified</div></div>
</aside></div></div>

## Availability

Cook one [Magic Bottle of Water](magic-bottle-of-water.md) in a furnace or smoker for 60 ticks, or on a campfire for 180 ticks. Each pinned recipe yields one vacuumed bottle and zero experience. At 20 TPS the processing times are 3 or 9 seconds, excluding setup and any fuel requirements.

## How to use

Brew this base with [Hipokute Grass](../items/hipokute-grass.md) for [High Potion](../items/high-potion.md) or [Hipokute Flower](../items/hipokute-flower.md) for [Full Potion](../items/full-potion.md). Drinking takes 16 ticks and returns an empty [Magic Bottle](magic-bottle.md) in survival. Sneak-use throws the bottle, and direct living-target interaction is also implemented.

## Behavior and limits

At full effect strength, ManaPotionItem adds a fixed 10 MP, capped at maximum MP. It does not heal health, raise permanent maximum MP, or revive dead targets. Thrown effect strength can be lower. The filled bottle stacks to 16.

[Compare recipes in the healing-potion guide](../items/healing-potions.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Vacuumed Magic Bottle of Water](https://tensura.wiki.gg/wiki/Vacuumed_Magic_Bottle_of_Water) on the Tensura: Reincarnated Wiki, recorded revision `10835`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `data/minecraft/recipe/vacuumed_magic_bottle_of_water_from_smelting.json`
    - `data/tensura/recipe/vacuumed_magic_bottle_of_water_from_smoking.json`
    - `data/tensura/recipe/vacuumed_magic_bottle_of_water_from_campfire_cooking.json`
