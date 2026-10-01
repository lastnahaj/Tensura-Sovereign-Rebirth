---
title: "Hipokute Flower"
description: "Pick the flower branch for stronger brewing recipes, or inspect a level-three Alchemist\u2019s offer before selling a surplus."
---

# Hipokute Flower

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/hipokute-flower.webp" alt="Hipokute Flower illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Pick the flower branch for stronger brewing recipes, or inspect a level-three Alchemist’s offer before selling a surplus.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Plant harvest and loot checked"
    Growth, harvest, and loot rules are checked against Tensura 2.0.1.2 for Minecraft 1.21.1. Live farm yields, server datapack overrides, and add-on interactions remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Hipokute Flower</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:hipokute_flower</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Plant harvest and loot checked</div></div>
<div class="druid-row"><div class="druid-label">Rarity</div><div class="druid-data">Common</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64</div></div>
</aside></div></div>

<span id="Obtainment"></span>

## Availability

Use an **empty hand** on a flowering **age-3 plant**. The checked server-side interaction drops one Hipokute Flower and resets the plant to age 1. Alternatively, breaking age 3 uses a one-flower loot entry plus its seed pool and removes the plant. Neither route means every grass plant can be picked for flowers.

<span id="Usage"></span>

## How to use

Brew a flower with [Magic Bottle of Water](../magic/magic-bottle-of-water.md) for [High Potion](high-potion.md), or [Vacuumed Magic Bottle of Water](../magic/vacuumed-magic-bottle-of-water.md) for [Full Potion](full-potion.md). One flower also crafts into one White Dye. A **level-three Alchemist Dwarf** trade candidate takes four flowers at the tracked `alchemistPriceMultiplier = 1.0` and defines a 20–50 Silver Coin output range. This does not guarantee every merchant offers it or fix a live offer’s price.

## Behavior and limits

Picking preserves an age-1 sprout, not a permanently flowering plant: the next successful growth decision is again **50% grass / 50% flower**. A grass result stops growing and must be broken and replanted. The [farming guide](../core-mechanics/mechanics-hipokute-farming.md) explains why a flower plot is renewable but not an endless guaranteed flower loop.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Hipokute Flower](https://tensura.wiki.gg/wiki/Hipokute_Flower) on the Tensura: Reincarnated Wiki, recorded revision `13311`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/block/HipokuteGrass.class`
    - `io/github/manasmods/tensura/registry/item/TensuraMaterialItems.class`
    - `io/github/manasmods/tensura/item/misc/HipokuteFlowerItem.class`
    - `io/github/manasmods/tensura/entity/merchant/profession/DwarfProfession.class`
    - `io/github/manasmods/tensura/entity/merchant/trade/OneForOneTrade.class`
    - `data/tensura/loot_table/blocks/hipokute_grass.json`
    - `data/tensura/neoforge/biome_modifier/hipokute_grass.json`
    - `data/tensura/worldgen/configured_feature/hipokute_grass.json`
    - `data/tensura/worldgen/placed_feature/hipokute_grass.json`
    - `data/minecraft/recipe/white_dye_from_hipokute_flower.json`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
