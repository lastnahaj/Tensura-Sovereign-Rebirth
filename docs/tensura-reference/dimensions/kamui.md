---
title: Kamui
description: "A sparse Mysticism pocket dimension tied to Phaser, with isolated Kamui cubes and no natural mob spawns in its fixed biome."
---

# Kamui

<span class="reference-badge">Tensura: Mysticism</span> <span class="reference-category">Dimensions</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/biomes/kamui-biome.webp" alt="Kamui reference artwork" loading="eager" decoding="async">
<figcaption>Verified realm reference</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A sparse Mysticism pocket dimension tied to Phaser, with isolated Kamui cubes and no natural mob spawns in its fixed biome.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-enter-and-leave">How to enter and leave</a>
<a href="#what-is-inside">What is inside</a>
</nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Registered by **Tensura: Mysticism 2.1.2**, the release selected by TSR. Registry and code paths were checked directly; claims that still require live gameplay are labeled.

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Kamui</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">mysticism:kamui_dimension</div></div>
<div class="druid-row"><div class="druid-label">World type</div><div class="druid-data">Sparse pocket realm</div></div>
<div class="druid-row"><div class="druid-label">Biome</div><div class="druid-data">mysticism:kamui_biome</div></div>
<div class="druid-row"><div class="druid-label">Natural spawns</div><div class="druid-data">None</div></div>
<div class="druid-row"><div class="druid-label">Entry skill</div><div class="druid-data">Phaser</div></div>
<div class="druid-row"><div class="druid-label">TSR warp time</div><div class="druid-data">60 ticks</div></div>
</aside></div></div>

## How to enter and leave

Equip Phaser, crouch, and hold the skill long enough to complete its Kamui transfer. Releasing crouch cancels the process. Using the transfer again from inside Kamui returns the user to the recorded source dimension when it is still available, with an Overworld fallback.

Mastering Phaser halves the configured transfer time. TSR's pinned Mysticism configuration sets the normal Kamui warp to 60 ticks, a 5-second cooldown, and a cost of 1,500; server-side settings can change those values.

## What is inside

The dimension uses one fixed biome, `mysticism:kamui_biome`. Its packaged biome definition has no natural creature, monster, ambient, or water spawns and lists Kamui cubes as its placed feature.

The noise settings use air as both the default block and default fluid, so this is not a conventional terrain world. Plan around isolated generated features and the Phaser route home.

## Continue exploring

<div class="race-map-directory">
<a href="../../../mysticism-reference/skills/unique/phaser/"><strong>Read the Phaser skill</strong><span>Open the connected reference.</span></a>
<a href="../../../mysticism-reference/biomes/kamui-biome/"><strong>Open the Kamui biome</strong><span>Open the connected reference.</span></a>
</div>

??? info "Sources and verification"

    [Tensura: Mysticism 2.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-mysticism.pw.toml)

    Artifact SHA-1: `cca1bd878b46c21ddbbf507bd4489fbb217899c7`.

    Packaged evidence:

    - `data/mysticism/dimension/kamui_dimension.json`
    - `data/mysticism/dimension_type/kamui_dimension.json`
    - `data/mysticism/worldgen/biome/kamui_biome.json`
    - `data/mysticism/worldgen/noise_settings/kamui_dimension_realm.json`
    - `io/github/Memoires/mysticism/ability/skill/unique/PhaserSkill.class`

[Back to Dimensions](index.md)
