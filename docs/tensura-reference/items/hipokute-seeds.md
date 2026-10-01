---
title: "Hipokute Seeds"
description: "Plant a renewable supply of potion ingredients. Area Magicules affect the first growth outcome; seeds are not guaranteed to remain Hipokute."
---

# Hipokute Seeds

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/hipokute-seeds.webp" alt="Hipokute Seeds illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Plant a renewable supply of potion ingredients. Area Magicules affect the first growth outcome; seeds are not guaranteed to remain Hipokute.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Plant harvest and loot checked"
    Growth, harvest, and loot rules are checked against Tensura 2.0.1.2 for Minecraft 1.21.1. Live farm yields, server datapack overrides, and add-on interactions remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Hipokute Seeds</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:hipokute_seeds</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Plant harvest and loot checked</div></div>
<div class="druid-row"><div class="druid-label">Rarity</div><div class="druid-data">Common</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64</div></div>
</aside></div></div>

<span id="Obtainment"></span>

## Availability

Break a Hipokute plant to collect seeds. Ages 0 and 1 have a one-seed loot entry; age 2 uses a 1–3 seed count and age 3 uses 3–5, both with a Fortune bonus function. Explosion decay and loot overrides can change results. Picking a flower without breaking the plant does not use this seed-drop table.

<span id="Usage"></span>

## How to use

Use seeds to place the crop on **Grass Block, Dirt, or Farmland**. Irrigated farmland improves the checked growth-speed input; dense neighboring crops can reduce it. Follow the [Hipokute farming guide](../core-mechanics/mechanics-hipokute-farming.md) before expanding a plot.

## Behavior and limits

At the first successful growth attempt, the plant becomes a small Hipokute sprout or vanilla wheat at age 3. The Hipokute chance uses **current area Magicules**, not player MP or a biome’s nominal capacity. A surviving sprout later chooses grass or flower with equal probability. The base Hipokute class has no bonemeal growth interface; bee-assisted Hipokute growth is not verified.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Hipokute Seeds](https://tensura.wiki.gg/wiki/Hipokute_Seeds) on the Tensura: Reincarnated Wiki, recorded revision `13310`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

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
