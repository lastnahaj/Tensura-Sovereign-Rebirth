---
title: "Low Potion"
description: "Brew Hipokute Grass with a Magic Bottle of Water to restore 33% of maximum health and 100 MP at full strength."
---

# Low Potion

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/low-potion.webp" alt="Low Potion illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Brew Hipokute Grass with a Magic Bottle of Water to restore 33% of maximum health and 100 MP at full strength.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Brewing route verified"
    The pinned 1.21.1 item stacks to 16, unlike the older source page's non-stackable label. Recipe and effect values are artifact checks, not a live-server gameplay test.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Low Potion</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:low_potion</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Brewing route verified</div></div>
</aside></div></div>

## Availability

Brew Hipokute Grass with a Magic Bottle of Water. This input combination is registered by SpecialRecipeRegister in the pinned artifact. Use the healing-potion guide below to compare all four ordinary brewing combinations.

## How to use

Use normally to drink for 16 ticks (0.8 seconds at 20 TPS), sneak-use to throw, or interact directly with a living target. Drinking in survival consumes one potion and returns a Magic Bottle. The item stack limit is 16.

## Behavior and limits

At full effect strength, heals 33% of the target's maximum health and adds a fixed 100 MP, capped at maximum MP. It does not increase maximum health or MP. Thrown splash strength can be lower. The healing implementation ignores targets that are not alive.

[Compare recipes in the healing-potion guide](healing-potions.md)

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Low Potion](https://tensura.wiki.gg/wiki/Low_Potion) on the Tensura: Reincarnated Wiki, recorded revision `12028`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `io/github/manasmods/tensura/item/consumable/HealingPotionItem.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
