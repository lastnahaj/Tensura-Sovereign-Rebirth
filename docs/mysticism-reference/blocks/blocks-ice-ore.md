---
title: "Ice Ore"
description: "Mysticism's Ice Essence ore, verified for cold-biome generation in the pinned 1.21.1 build."
---

# Ice Ore

<span class="reference-badge">TR Mysticism reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/blocks/ice-ore.webp" alt="Ice Ore illustration" loading="eager" decoding="async">
<figcaption>TSR block illustration</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Mysticism&#x27;s Ice Essence ore, verified for cold-biome generation in the pinned 1.21.1 build.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Verified against **TR Mysticism 2.1.2** selected by the TSR pack manifest.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Ice Ore</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">TR Mysticism 2.1.2</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">mysticism:ice_ore</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Ice Essence ore</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Original illustration; not the in-game texture</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Diamond-tier pickaxe or better</div></div>
</aside></div></div>

## What it does

The pinned build places veins of up to three Ice Ore blocks inside ice between Y 55 and 100. It makes 75 placement attempts per chunk in biomes carrying Mysticism's ice-spikes biome tag. In this artifact, that tag contains only Minecraft's Ice Spikes biome. The current upstream article also mentions the Spirit Realm; broader realm generation is not confirmed by this check.

## Player access

Ice Ore is tagged for pickaxe mining and requires a diamond-tier tool. Silk Touch drops the ore block; otherwise it drops Ice Essence, with the standard ore Fortune bonus and explosion decay applied.

## Source and licensing

??? info "Sources and verification"

    [TR Mysticism 2.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-mysticism.pw.toml)

    Artifact SHA-1: `cca1bd878b46c21ddbbf507bd4489fbb217899c7`.

    Upstream article: [TR Mysticism Wiki revision 3499](https://trmysticism.wiki.gg/wiki/Blocks/Ice_Ore?oldid=3499). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

    Packaged implementation evidence:

    - `data/minecraft/tags/block/mineable/pickaxe.json`
    - `data/minecraft/tags/block/needs_diamond_tool.json`
    - `data/mysticism/loot_table/blocks/ice_ore.json`
    - `data/mysticism/neoforge/biome_modifier/ice_ore.json`
    - `data/mysticism/tags/worldgen/biome/ice_spikes.json`
    - `data/mysticism/worldgen/configured_feature/ice_ore.json`
    - `data/mysticism/worldgen/placed_feature/ice_ore.json`

    The illustration on this page is original TSR artwork; it is not the in-game texture.

[Back to Blocks](../../tensura-reference/blocks/index.md)
