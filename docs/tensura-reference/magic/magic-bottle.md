---
title: "Magic Bottle"
description: "Craft empty bottles from Glass and a Magic Crystal, then fill them at a water source to begin brewing."
---

# Magic Bottle

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-bottle.webp" alt="Magic Bottle illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Craft empty bottles from Glass and a Magic Crystal, then fill them at a water source to begin brewing.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Crafting route verified"
    This is a crafting and brewing container, not a spell. Its existing article address remains available, but the item is listed under Items.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Bottle</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_bottle</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Crafting route verified</div></div>
</aside></div></div>

## Availability

Craft three Glass around one Magic Crystal: Glass–Crystal–Glass across one row, then Glass beneath the crystal. The pinned recipes produce 3 bottles with Low Quality, 6 with Medium Quality, or 9 with High Quality Magic Crystal.

## How to use

Use the empty bottle while aiming at a water source. MagicBottleItem uses source-only fluid targeting, checks interaction permission, and returns a [Magic Bottle of Water](magic-bottle-of-water.md). Flowing-water targeting is not the documented filling route.

## Behavior and limits

The empty container does not restore health or MP. It is distinct from the drinkable filled bottles. Its implementation also supports collecting vanilla Dragon's Breath from a live Ender Dragon-owned area-effect cloud; this code path is not a live encounter test.

[Compare recipes in the healing-potion guide](../items/healing-potions.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Bottle](https://tensura.wiki.gg/wiki/Magic_Bottle) on the Tensura: Reincarnated Wiki, recorded revision `10834`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/item/consumable/MagicBottleItem.class`
    - `data/minecraft/recipe/bottles_of_low_crystal.json`
    - `data/minecraft/recipe/bottles_of_medium_crystal.json`
    - `data/minecraft/recipe/bottles_of_high_crystal.json`
