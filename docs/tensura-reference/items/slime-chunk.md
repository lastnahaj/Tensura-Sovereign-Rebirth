---
title: "Slime Chunk"
description: "Keep ordinary slime material for compact storage, convert four chunks into one vanilla Slimeball, or make chilled material with eight Snowballs."
---

# Slime Chunk

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/slime-chunk.webp" alt="Slime Chunk illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Keep ordinary slime material for compact storage, convert four chunks into one vanilla Slimeball, or make chilled material with eight Snowballs.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Loot predicates and material conversions checked"
    The selected 1.21.1 artifact registers an ordinary material item, not a standard food. Crafting, cooking, loot predicates, and ingredient tags were inspected; live drops and server recipe overrides remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Slime Chunk</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:slime_chunk</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Loot predicates and material conversions checked</div></div>
<div class="druid-row"><div class="druid-label">Rarity</div><div class="druid-data">Common</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64</div></div>
<div class="druid-row"><div class="druid-label">Vanilla Slimeball recipe</div><div class="druid-data">4 chunks → 1 Slimeball</div></div>
<div class="druid-row"><div class="druid-label">Storage recipe</div><div class="druid-data">9 chunks → 1 resource block</div></div>
<div class="druid-row"><div class="druid-label">Standard food properties</div><div class="druid-data">None registered</div></div>
</aside></div></div>

<span id="Obtainment"></span><span id="Defeating"></span><span id="Crafting"></span>

## Availability

The packaged **Tensura Slime** and **Supermassive Slime** loot tables select Slime Chunk when the custom `SlimePredicate` matches `chilled: false`. Cold variants use the Chilled Slime branch instead. This describes the mod’s entities, not a guaranteed drop from every vanilla slime. Scale-dependent functions, Looting, spawn data, and server overrides affect actual loot.

For a crafting route, unpack **1 [Slime Chunk Block](../blocks/blocks-slime-chunk-block.md)** into **9 chunks**. You can also warm **1 [Chilled Slime](chilled-slime.md)** into **1 chunk**: Furnace **100**, Smoker **50**, or Campfire **300 recipe progress ticks**, each with **0.2 recipe XP**. Progress values are not measured wall-clock durations.

<span id="Usage"></span>

## How to use

**Choose a material route:**

- **Storage:** fill a Crafting Table with **9 chunks** to make **1 [Slime Chunk Block](../blocks/blocks-slime-chunk-block.md)**; the reverse recipe returns nine.
- **Vanilla material:** place **4 chunks** in any crafting arrangement to make **1 Minecraft Slimeball**. The checked recipe set does not establish a reverse Slimeball-to-chunk conversion.
- **Chilled ingredient:** surround **1 chunk** with **8 Snowballs** at a Crafting Table to make **1 [Chilled Slime](chilled-slime.md)**. Eight Snow Blocks are used for the separate block conversion, not this item recipe.

## Behavior and limits

Slime Chunk is constructed as a plain `Item` with no standard food properties in this registration. Its membership in `#tensura:slime_food` is a custom ingredient classification, not proof that ordinary eating restores hunger or grants the Chilled Slime food behavior. Custom racial consumption still requires a separately checked ability or mechanic.

The packaged `#c:slime_balls` item tag also includes Slime Chunk. It can satisfy a recipe that explicitly accepts that tag; a recipe that requires the exact `minecraft:slime_ball` ID is different. Check the recipe browser rather than assuming universal substitution. Placed-block drag and collision are not effects granted by holding the item.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Slime Chunk](https://tensura.wiki.gg/wiki/Slime_Chunk) on the Tensura: Reincarnated Wiki, recorded revision `9814`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `TensuraMobDropItems SLIME_CHUNK registration`
    - `SlimePredicate`
    - `data/tensura/loot_table/entities/slime.json`
    - `data/tensura/loot_table/entities/supermassive_slime.json`
    - `data/minecraft/recipe/slime_ball_from_chunks.json`
    - `data/c/tags/item/slime_balls.json`
    - `data/tensura/tags/item/slime_food.json`
    - `data/slime_material_reference.json`
