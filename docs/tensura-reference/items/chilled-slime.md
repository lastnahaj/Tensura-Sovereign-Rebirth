---
title: "Chilled Slime"
description: "Make chilled material with eight Snowballs and one Slime Chunk, unpack its storage block, or check the Tensura cold-variant loot route."
---

# Chilled Slime

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/chilled-slime.webp" alt="Chilled Slime illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Make chilled material with eight Snowballs and one Slime Chunk, unpack its storage block, or check the Tensura cold-variant loot route.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Crafting and cold-variant loot checked"
    Crafting, cooking, food properties, and cold-variant loot are checked in Tensura 2.0.1.2 for Minecraft 1.21.1. Live drops, refining access, and server overrides remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Chilled Slime</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:chilled_slime</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Crafting and cold-variant loot checked</div></div>
<div class="druid-row"><div class="druid-label">Rarity</div><div class="druid-data">Common</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64</div></div>
<div class="druid-row"><div class="druid-label">Food nutrition</div><div class="druid-data">1</div></div>
<div class="druid-row"><div class="druid-label">Saturation modifier</div><div class="druid-data">2.0</div></div>
<div class="druid-row"><div class="druid-label">Crafting output</div><div class="druid-data">1 / 9 when unpacking</div></div>
</aside></div></div>

<span id="Obtainment"></span><span id="Defeating"></span><span id="Crafting"></span>

## Availability

At a **Crafting Table**, surround **1 Slime Chunk** with **8 Snowballs** to craft **1 Chilled Slime**. Alternatively, one [Chilled Slime Block](../blocks/blocks-chilled-slime-block.md) unpacks into **9 Chilled Slime** using a shapeless recipe. These are two different quantities, not a one-snowball conversion.

The packaged Tensura Slime and Supermassive Slime loot tables select Chilled Slime when their cold-variant predicate does not select the ordinary Slime Chunk branch. `SlimePredicate` checks the mod’s `SlimeEntity.isChilled()`, not every vanilla slime. In the checked non-structure spawn path, a biome in `#minecraft:spawns_cold_variant_frogs` initializes the chilled flag. Structure spawns bypass that initialization; biome tags, spawn data, scale-dependent loot, and server overrides matter. This is not a guaranteed drop from every slime in every cold-looking biome.

<span id="Usage"></span>

## How to use

Craft **9 Chilled Slime** into one [storage block](../blocks/blocks-chilled-slime-block.md), or warm a single item into **1 Slime Chunk**. The packaged cooking times are **100 progress ticks in a Furnace**, **50 in a Smoker**, or **300 on a Campfire**, with **0.2 XP** in each definition. These are recipe times, not measured wall-clock completion.

The material is registered as a food with **1 nutrition**, a **2.0 saturation modifier**, and `alwaysEdible`. It can therefore be used while the hunger bar is full; this does not establish a healing, MP, or cold-resistance effect. Keep materials for crafting before consuming the supply.

## Behavior and limits

The pinned build also contains **36 refining potion definitions** that use Chilled Slime. Those are custom refining recipes, not proof of an ordinary Brewing Stand recipe or a verified player unlock path. The [chilled-material evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/chilled_reference.json) retains their exact input, potion components, and resource checksums. Refining access and live potion effects still require separate testing.

The block’s entity slowdown and powder-snow flag are **placed-block behavior**, not effects granted by eating this ingredient. [Compare the block guide](../blocks/blocks-chilled-slime-block.md) before using it in a base or movement system.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Chilled Slime](https://tensura.wiki.gg/wiki/Chilled_Slime) on the Tensura: Reincarnated Wiki, recorded revision `9202`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `TensuraConsumableItems`
    - `TensuraFoodProperties`
    - `SimpleFoodItem`
    - `SlimeEntity.finalizeSpawn`
    - `SlimePredicate`
    - `data/tensura/loot_table/entities/slime.json`
    - `data/tensura/loot_table/entities/supermassive_slime.json`
    - `data/minecraft/recipe/slime_chunk_from_snowball.json`
    - `data/tensura/recipe/chilled_slimefrom_chilled_slime_block.json`
    - `data/chilled_reference.json`
