---
title: "Medium Quality Magic Crystal"
description: "Recover 2,500 base MP through Absorb & Dissolve, make six Magic Bottles, or downgrade into two Low crystals with the required schematic."
---

# Medium Quality Magic Crystal

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/medium-quality-magic-crystal.webp" alt="Medium Quality Magic Crystal illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Recover 2,500 base MP through Absorb &amp; Dissolve, make six Magic Bottles, or downgrade into two Low crystals with the required schematic.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Loot and crafting routes verified"
    The shared loot rule requires adjusted maximum EP from 3,000 through 8,999 inclusive, plus the crystal tag and spawn checks. It does not mean every member of a species always drops this tier.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Medium Quality Magic Crystal</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:medium_quality_magic_crystal</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Loot and crafting routes verified</div></div>
</aside></div></div>

## Availability

The pinned shared loot rule selects Medium for eligible tensura:drop_crystal entities with adjusted maximum EP from 3,000 to 8,999 inclusive. MOB_SUMMONED and TRIGGERED spawn types are excluded, and named-evolution entities must allow crystal drops. Unpack one Medium Quality Magic Crystal Block into nine crystals, or downgrade one [High Quality Magic Crystal](high-quality-magic-crystal.md) into two Medium crystals at a Smithing Bench with the [Low Magisteel Gear Schematic](../items/items-schematics-low-magisteel-gear-schematic.md).

## How to use

Hold one in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md). One Medium crystal and three Glass craft six [Magic Bottles](magic-bottle.md). At a Smithing Bench with the Low Magisteel Gear Schematic, one Medium crystal becomes two [Low crystals](low-quality-magic-crystal.md). Nine crystals craft one same-quality storage block, which unpacks into nine again.

## Behavior and limits

The pinned dissolving definition supplies 2,500 base MP; TSR's checked-in Absorb & Dissolve magiculeMultiplier is 1.0. Recovery replenishes current MP, not permanent maximum MP. The shared drop rule tests namespace-adjusted maximum EP. The Smithing Bench downgrade needs its schematic; it is not an unrestricted crafting-grid recipe. Live-server changes are not tested.

[Compare Magic Crystal tiers](../items/magic-crystals.md)

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Medium Quality Magic Crystal](https://tensura.wiki.gg/wiki/Medium_Quality_Magic_Crystal) on the Tensura: Reincarnated Wiki, recorded revision `12988`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMobDropItems.class`
    - `io/github/manasmods/tensura/handler/MobHandler.class`
    - `io/github/manasmods/tensura/data/template/critereon/ExistencePointPredicate.class`
    - `data/tensura/tags/entity_type/drop_crystal.json`
    - `data/tensura/item_dissolving/medium_quality_magic_crystal.json`
    - `io/github/manasmods/tensura/ability/skill/intrinsic/AbsorbDissolveSkill.class`
    - `io/github/manasmods/tensura/util/EnergyHelper.class`
    - `pack/config/tensura/ability/skill/intrinsic_config.toml`
    - `data/minecraft/recipe/bottles_of_medium_crystal.json`
    - `data/tensura/recipe/medium_quality_magic_crystal_blockfrom_medium_quality_magic_crystal.json`
    - `data/tensura/recipe/medium_quality_magic_crystalfrom_medium_quality_magic_crystal_block.json`
    - `data/tensura/recipe/smithing/medium_quality_magic_crystal.json`
    - `data/tensura/recipe/smithing/low_quality_magic_crystal.json`
