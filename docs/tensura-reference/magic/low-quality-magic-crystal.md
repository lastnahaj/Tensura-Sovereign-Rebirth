---
title: "Low Quality Magic Crystal"
description: "A crafting resource with 1,000 base MP recovery through Absorb & Dissolve. One crystal makes three Magic Bottles with three Glass."
---

# Low Quality Magic Crystal

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/low-quality-magic-crystal.webp" alt="Low Quality Magic Crystal illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A crafting resource with 1,000 base MP recovery through Absorb &amp; Dissolve. One crystal makes three Magic Bottles with three Glass.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Loot and crafting routes verified"
    Crystal drops require an eligible tagged entity and a passing EP/spawn predicate. This is not a guaranteed drop from every mob, and source species lists do not override the pinned loot rules.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Low Quality Magic Crystal</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:low_quality_magic_crystal</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Loot and crafting routes verified</div></div>
</aside></div></div>

## Availability

The shared crystal loot rule uses Low as its fallback after the Medium and High checks, requiring adjusted maximum EP of at least 1. For whole-number EP, the usual Low band is 1–2,999. Eligible entities must be in tensura:drop_crystal; MOB_SUMMONED and TRIGGERED spawn types are excluded, and named-evolution entities must allow crystal drops. Alternatively, unpack one Low Quality Magic Crystal Block into nine crystals, or downgrade one [Medium Quality Magic Crystal](medium-quality-magic-crystal.md) into two Low crystals at a Smithing Bench with the [Low Magisteel Gear Schematic](../items/items-schematics-low-magisteel-gear-schematic.md).

## How to use

Hold the crystal in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md) to consume one and recover its configured Magicules. With three Glass, one Low crystal crafts three [Magic Bottles](magic-bottle.md). Nine crystals in a full 3×3 crafting grid produce one same-quality storage block, which unpacks back into nine.

## Behavior and limits

The pinned dissolving definition supplies 1,000 base MP. Absorb & Dissolve multiplies this by magiculeMultiplier; TSR's checked-in value is 1.0. This restores current MP rather than increasing permanent maximum MP. The loot predicate uses the namespace EP multiplier and entity eligibility, not just an unadjusted wiki stat. Live-server overrides and other add-on loot are not tested.

[Compare Magic Crystal tiers](../items/magic-crystals.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Low Quality Magic Crystal](https://tensura.wiki.gg/wiki/Low_Quality_Magic_Crystal) on the Tensura: Reincarnated Wiki, recorded revision `12989`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMobDropItems.class`
    - `io/github/manasmods/tensura/handler/MobHandler.class`
    - `io/github/manasmods/tensura/data/template/critereon/ExistencePointPredicate.class`
    - `data/tensura/tags/entity_type/drop_crystal.json`
    - `data/tensura/item_dissolving/low_quality_magic_crystal.json`
    - `io/github/manasmods/tensura/ability/skill/intrinsic/AbsorbDissolveSkill.class`
    - `io/github/manasmods/tensura/util/EnergyHelper.class`
    - `pack/config/tensura/ability/skill/intrinsic_config.toml`
    - `data/minecraft/recipe/bottles_of_low_crystal.json`
    - `data/tensura/recipe/low_quality_magic_crystal_blockfrom_low_quality_magic_crystal.json`
    - `data/tensura/recipe/low_quality_magic_crystalfrom_low_quality_magic_crystal_block.json`
    - `data/tensura/recipe/smithing/low_quality_magic_crystal.json`
