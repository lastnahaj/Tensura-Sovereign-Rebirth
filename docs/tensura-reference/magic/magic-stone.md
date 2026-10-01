---
title: "Magic Stone"
description: "Craft one stone from a Low Magisteel Ingot and eight Low Quality Magic Crystals at a Smithing Bench with the required schematic."
---

# Magic Stone

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-stone.webp" alt="Magic Stone illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Craft one stone from a Low Magisteel Ingot and eight Low Quality Magic Crystals at a Smithing Bench with the required schematic.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Smithing recipe verified"
    The pinned recipe produces one Magic Stone, not eight. It requires the Low Magisteel Gear Schematic and cannot be made in an ordinary crafting grid.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Stone</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_stone</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Smithing recipe verified</div></div>
</aside></div></div>

## Availability

At a [Smithing Bench](../blocks/blocks-smithing-bench.md), combine one [Low Magisteel Ingot](../items/low-magisteel-ingot.md) with eight [Low Quality Magic Crystals](low-quality-magic-crystal.md). The recipe requires the [Low Magisteel Gear Schematic](../items/items-schematics-low-magisteel-gear-schematic.md) and outputs one Magic Stone.

## How to use

Magic Stone is a component for equipment, cores, and reset scrolls. For example, one stone plus eight [Medium Quality Magic Crystals](medium-quality-magic-crystal.md) produces one [Empty Element Core](../items/element-core-empty.md) at a Smithing Bench with the Low Magisteel Gear Schematic. Alternatively, hold a stone in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md) to consume it for MP recovery.

## Behavior and limits

The dissolving definition supplies 1,000 base MP. TSR's checked-in Absorb & Dissolve multiplier is 1.0; this replenishes current MP rather than raising permanent maximum MP. Other recipes can require different schematics. Artifact and configuration checks do not confirm live-server recipe overrides or gameplay.

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Stone](https://tensura.wiki.gg/wiki/Magic_Stone) on the Tensura: Reincarnated Wiki, recorded revision `9515`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMaterialItems.class`
    - `data/tensura/recipe/smithing/magic_stone.json`
    - `data/tensura/recipe/smithing/element_core_empty.json`
    - `data/tensura/item_dissolving/magic_stone.json`
    - `io/github/manasmods/tensura/ability/skill/intrinsic/AbsorbDissolveSkill.class`
    - `io/github/manasmods/tensura/util/EnergyHelper.class`
    - `pack/config/tensura/ability/skill/intrinsic_config.toml`
