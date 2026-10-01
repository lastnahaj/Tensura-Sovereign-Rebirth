---
title: "Full Potion"
description: "Brew Hipokute Flower with vacuumed bottled water to restore 99% of maximum health and 10,000 MP at full strength."
---

# Full Potion

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/full-potion.webp" alt="Full Potion illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Brew Hipokute Flower with vacuumed bottled water to restore 99% of maximum health and 10,000 MP at full strength.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Brewing route verified"
    Full Potion uses 99% maximum-health healing, not the 100% value used by Revival Elixir. Its MP restoration is a fixed 10,000, not a percentage of maximum MP.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Full Potion</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:full_potion</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Brewing route verified</div></div>
</aside></div></div>

## Availability

Brew Hipokute Flower with a Vacuumed Magic Bottle of Water. Separate Tensura Refining recipes produce Full Potion from flower and a Magic Bottle, including ordinary or vacuumed filled bottles, but this item pass does not verify access to that skill-driven recipe system.

## How to use

Use normally to drink for 16 ticks (0.8 seconds at 20 TPS), sneak-use to throw, or interact directly with a living target. Drinking in survival consumes one potion and returns a Magic Bottle. The pinned item stack limit is 16, not the source page's older non-stackable value.

## Behavior and limits

At full effect strength, heals 99% of maximum health and adds a fixed 10,000 MP, capped at maximum MP. It does not increase maximum health or MP. Thrown splash strength can be lower, and the item does not resurrect a dead player.

[Compare recipes in the healing-potion guide](healing-potions.md)

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Full Potion](https://tensura.wiki.gg/wiki/Full_Potion) on the Tensura: Reincarnated Wiki, recorded revision `12025`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `io/github/manasmods/tensura/item/consumable/HealingPotionItem.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
    - `data/tensura/recipe/refining/full_potion_from_magic_bottle_using_hipokute_flower.json`
