---
title: "High Quality Magic Crystal"
description: "Recover 5,000 base MP through Absorb & Dissolve, craft nine Magic Bottles, or split into two Medium crystals at the Smithing Bench."
---

# High Quality Magic Crystal

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/high-quality-magic-crystal.webp" alt="High Quality Magic Crystal illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Recover 5,000 base MP through Absorb &amp; Dissolve, craft nine Magic Bottles, or split into two Medium crystals at the Smithing Bench.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Loot and crafting routes verified"
    The shared loot rule tests adjusted maximum EP of at least 9,000, the crystal-drop tag, spawn exclusions, and named-evolution eligibility. Boss names alone are not proof of a guaranteed drop.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">High Quality Magic Crystal</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:high_quality_magic_crystal</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Loot and crafting routes verified</div></div>
</aside></div></div>

## Availability

The pinned shared loot rule selects High for eligible tensura:drop_crystal entities at adjusted maximum EP of 9,000 or more. MOB_SUMMONED and TRIGGERED spawn types are excluded, and named-evolution entities must allow crystal drops. One High Quality Magic Crystal Block also unpacks into nine High crystals. The checked downgrade recipes only reduce quality; they do not upgrade Low or Medium crystals into High.

## How to use

Hold one in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md). One High crystal and three Glass craft nine [Magic Bottles](magic-bottle.md). With the [Low Magisteel Gear Schematic](../items/items-schematics-low-magisteel-gear-schematic.md), downgrade one High crystal into two [Medium crystals](medium-quality-magic-crystal.md) at a Smithing Bench. Nine High crystals craft one same-quality storage block, which unpacks back into nine.

## Behavior and limits

The pinned dissolving definition supplies 5,000 base MP; TSR's checked-in Absorb & Dissolve magiculeMultiplier is 1.0. Recovery replenishes current MP rather than increasing permanent maximum MP. The shared loot rule's 9,000 boundary is inclusive and uses the namespace EP multiplier. Source trading claims have not been reverified in this pass; live-server loot and add-on changes remain untested.

[Compare Magic Crystal tiers](../items/magic-crystals.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [High Quality Magic Crystal](https://tensura.wiki.gg/wiki/High_Quality_Magic_Crystal) on the Tensura: Reincarnated Wiki, recorded revision `12990`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMobDropItems.class`
    - `io/github/manasmods/tensura/handler/MobHandler.class`
    - `io/github/manasmods/tensura/data/template/critereon/ExistencePointPredicate.class`
    - `data/tensura/tags/entity_type/drop_crystal.json`
    - `data/tensura/item_dissolving/high_quality_magic_crystal.json`
    - `io/github/manasmods/tensura/ability/skill/intrinsic/AbsorbDissolveSkill.class`
    - `io/github/manasmods/tensura/util/EnergyHelper.class`
    - `pack/config/tensura/ability/skill/intrinsic_config.toml`
    - `data/minecraft/recipe/bottles_of_high_crystal.json`
    - `data/tensura/recipe/high_quality_magic_crystal_blockfrom_high_quality_magic_crystal.json`
    - `data/tensura/recipe/high_quality_magic_crystalfrom_high_quality_magic_crystal_block.json`
    - `data/tensura/recipe/smithing/medium_quality_magic_crystal.json`
