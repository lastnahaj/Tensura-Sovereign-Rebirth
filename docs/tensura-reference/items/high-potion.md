---
title: "High Potion"
description: "Brew flower with ordinary bottled water, or grass with vacuumed bottled water, for 66% maximum-health healing and 1,000 MP."
---

# High Potion

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/high-potion.webp" alt="High Potion illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Brew flower with ordinary bottled water, or grass with vacuumed bottled water, for 66% maximum-health healing and 1,000 MP.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Brewing route verified"
    The pinned 1.21.1 item stacks to 16. Ordinary brewing and Tensura Refining are different recipe systems; do not substitute their ingredients or results without checking the appropriate recipe.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">High Potion</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:high_potion</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Brewing route verified</div></div>
</aside></div></div>

## Availability

There are two registered brewing routes: Hipokute Flower with a Magic Bottle of Water, or Hipokute Grass with a Vacuumed Magic Bottle of Water. Separate Tensura Refining recipes also produce High Potion from grass and a Magic Bottle, but access to that recipe system has not been verified by this item pass.

## How to use

Use normally to drink for 16 ticks (0.8 seconds at 20 TPS), sneak-use to throw, or interact directly with a living target. Drinking in survival consumes one potion and returns a Magic Bottle. The item stack limit is 16.

## Behavior and limits

At full effect strength, heals 66% of maximum health and adds a fixed 1,000 MP, capped at maximum MP. It does not permanently increase either maximum. Thrown splash strength can be lower, and dead targets are not revived.

[Compare recipes in the healing-potion guide](healing-potions.md)

[Return to Items](index.md)

## Source and licensing

Upstream reference: [High Potion](https://tensura.wiki.gg/wiki/High_Potion) on the Tensura: Reincarnated Wiki, recorded revision `12029`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `io/github/manasmods/tensura/item/consumable/HealingPotionItem.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
    - `data/tensura/recipe/refining/high_potion_from_magic_bottle_using_hipokute_grass.json`
