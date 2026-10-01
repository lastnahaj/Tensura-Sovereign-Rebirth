---
title: "Magic Ore Shard"
description: "Mine Magic Ore with a Netherite-tier pickaxe, refine shards into Pure Magisteel Nuggets, or consume them toward the Metal Slime evolution gate."
---

# Magic Ore Shard

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-ore-shard.webp" alt="Magic Ore Shard illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Mine Magic Ore with a Netherite-tier pickaxe, refine shards into Pure Magisteel Nuggets, or consume them toward the Metal Slime evolution gate.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Mining, refining, and consumption rules verified"
    Silk Touch drops the ore block instead of shards. The Metal Slime evolution gate counts consumed item uses, not the number of shards carried in your inventory.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Ore Shard</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_ore_shard</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Mining, refining, and consumption rules verified</div></div>
</aside></div></div>

## Availability

Mine [Magic Ore](../blocks/blocks-magic-ore.md) or its Deepslate variant using a Netherite-tier pickaxe. Without Silk Touch, the loot table drops shards and applies Fortune's ore-drop rule; Silk Touch returns the block. The [Metal Slime mob](../mobs/mobs-metal-slime.md) also has a base drop of 5–8 shards, with Looting able to increase it. These are pinned loot definitions, not guaranteed live-server yields.

## How to use

With [Great Sage](../skills/unique/great-sage.md), select its Refine mode and hold Sneak while activating the ability to open Refining. The pinned refining recipe converts one shard into two [Pure Magisteel Nuggets](../items/pure-magisteel-nugget.md); a normal activation of that mode opens Repeat Crafting instead. Nine shards in a full crafting grid make one [Block of Magic Ore](../blocks/blocks-block-of-magic-ore.md), which unpacks into nine shards. The [Kiln](../blocks/blocks-kiln.md) also has a Magisteel melting recipe for this material.

## Behavior and limits

One shard supplies 5,000 base MP through [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md), replenishing current MP at TSR's checked-in multiplier of 1.0. For [Slime → Metal Slime](../races/families/slime.md#races-metal-slime), the checked-in configuration requires 100 ore-shard uses. The evolution requirement reads the item's use statistic, and Absorb & Dissolve records one use per shard consumed. Carrying 100 shards is not sufficient; other evolution conditions still apply. Refining costs, timings, world-generation heights, and live-server overrides are not confirmed here.

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Ore Shard](https://tensura.wiki.gg/wiki/Magic_Ore_Shard) on the Tensura: Reincarnated Wiki, recorded revision `9238`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMaterialItems.class`
    - `data/neoforge/tags/block/needs_netherite_tool.json`
    - `data/minecraft/tags/block/mineable/pickaxe.json`
    - `data/tensura/loot_table/blocks/magic_ore.json`
    - `data/tensura/loot_table/blocks/deepslate_magic_ore.json`
    - `data/tensura/loot_table/entities/metal_slime.json`
    - `data/tensura/recipe/refining/pure_magisteel_nugget_from_magic_ore_shard.json`
    - `io/github/manasmods/tensura/ability/skill/unique/GreatSageSkill.class`
    - `io/github/manasmods/tensura/ability/subclass/IRefining.class`
    - `data/tensura/recipe/magic_ore_blockfrom_magic_ore_shard.json`
    - `data/tensura/recipe/magic_ore_shardfrom_magic_ore_block.json`
    - `data/tensura/recipe/melting/magic_ore_shard.json`
    - `data/tensura/item_dissolving/magic_ore_shard.json`
    - `io/github/manasmods/tensura/race/slime/MetalSlimeRace.class`
    - `io/github/manasmods/tensura/race/template/EvolutionRequirement$ItemConsumeRequirement.class`
    - `io/github/manasmods/tensura/ability/skill/intrinsic/AbsorbDissolveSkill.class`
    - `pack/config/tensura/race/slime_config.toml`
    - `pack/config/tensura/ability/skill/intrinsic_config.toml`
