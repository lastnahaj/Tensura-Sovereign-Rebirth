---
title: Kamui Biome
description: The empty, cube-filled biome used by Mysticism's Kamui pocket dimension in the pinned 1.21.1 build.
---

# Kamui Biome

<span class="reference-badge">TR Mysticism reference</span> <span class="reference-category">Biomes</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/biomes/kamui-biome.webp" alt="Kamui Biome reference artwork" loading="eager" decoding="async">
<figcaption>Original TSR article artwork</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>The empty, cube-filled biome used by Mysticism&#x27;s Kamui pocket dimension in the pinned 1.21.1 build.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#what-is-here">What is here</a>
<a href="#how-to-reach-it">How to reach it</a>
<a href="#version-verification">Version verification</a>
</nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Verified against Mysticism **2.1.2** selected by the TSR pack manifest. This is an artifact and configuration check, not a live-server terrain test.

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Kamui Biome</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Mysticism 2.1.2</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">mysticism:kamui_biome</div></div>
<div class="druid-row"><div class="druid-label">Dimension</div><div class="druid-data">mysticism:kamui_dimension</div></div>
<div class="druid-row"><div class="druid-label">Precipitation</div><div class="druid-data">None</div></div>
<div class="druid-row"><div class="druid-label">Temperature</div><div class="druid-data">0.6</div></div>
<div class="druid-row"><div class="druid-label">Natural spawns</div><div class="druid-data">None</div></div>
<div class="druid-row"><div class="druid-label">Placed feature</div><div class="druid-data">mysticism:kamui_cube</div></div>
</aside></div></div>

## What is here

The pinned biome definition contains no natural creature, monster, ambient, or water spawns. Its only listed placed feature is `mysticism:kamui_cube`, while the matching dimension's noise settings use air as both the default block and default fluid.

The result is a sparse pocket realm built around isolated cube features rather than a normal surface biome. This describes the packaged 2.1.2 data; it is not an in-game terrain-generation benchmark.

## How to reach it

Mysticism's [Phaser](../skills/unique/phaser.md) skill documents the Kamui warp. Crouch while using Phaser to begin the transfer; releasing crouch cancels it. The exact delay and cost come from the server's Mysticism skill configuration.

The pinned TSR configuration sets the Kamui warp time to 60 ticks, the cooldown to 5 seconds, and the cost to 1,500. Server-side configuration can change those values.

## Version verification

`mysticism:kamui_biome` and `mysticism:kamui_dimension` are both present in the Mysticism 2.1.2 artifact selected by the pack manifest for Minecraft 1.21.1. This page is included because those registry resources exist in the pinned build, even though the upstream Mysticism wiki does not provide a dedicated Kamui biome article.

??? info "Sources and verification"

    [Mysticism 2.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-mysticism.pw.toml)

    Artifact SHA-1: `cca1bd878b46c21ddbbf507bd4489fbb217899c7`.

    Packaged registry evidence:

    - `data/mysticism/worldgen/biome/kamui_biome.json`
    - `data/mysticism/dimension/kamui_dimension.json`
    - `data/mysticism/worldgen/noise_settings/kamui_dimension_realm.json`
    - `io/github/Memoires/mysticism/world/biome/kamui_dimension/KamuiBiome.class`

    Original TSR environment artwork is used because the upstream wiki has no dedicated Kamui biome image.

[Back to the collection](index.md)
