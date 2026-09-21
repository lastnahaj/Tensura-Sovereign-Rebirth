---
title: Elemental Realm
description: "Mysticism's seven-biome elemental world, called the Spirit Realm by the upstream guide and Elemental Realm by the 1.21.1 registry."
---

# Elemental Realm

<span class="reference-badge">Tensura: Mysticism</span> <span class="reference-category">Dimensions</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/upstream/mysticism/biomes/fire-biome-ead4504af1.png" alt="Elemental Realm reference artwork" loading="eager" decoding="async">
<figcaption>Verified realm reference</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Mysticism&#x27;s seven-biome elemental world, called the Spirit Realm by the upstream guide and Elemental Realm by the 1.21.1 registry.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-enter">How to enter</a>
<a href="#how-to-leave">How to leave</a>
<a href="#what-is-inside">What is inside</a>
</nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Registered by **Tensura: Mysticism 2.1.2**, the release selected by TSR. Registry and code paths were checked directly; claims that still require live gameplay are labeled.

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Elemental Realm</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">mysticism:elemental_realm</div></div>
<div class="druid-row"><div class="druid-label">World type</div><div class="druid-data">Noise-generated</div></div>
<div class="druid-row"><div class="druid-label">Biomes</div><div class="druid-data">7 elemental biomes</div></div>
<div class="druid-row"><div class="druid-label">Time</div><div class="druid-data">Fixed at 6000</div></div>
<div class="druid-row"><div class="druid-label">Beds</div><div class="druid-data">Disabled</div></div>
<div class="druid-row"><div class="druid-label">Return route</div><div class="druid-data">Fall into the void</div></div>
</aside></div></div>

## How to enter

The current upstream Mysticism guide directs players to fly to the roof above the praying platform in the Labyrinth. It recommends roughly 20,000–30,000 EP to survive the realm's Magicule Poisoning.

Those EP figures are upstream gameplay guidance rather than a fixed value found in the packaged dimension JSON. Approach the first trip as a survival check and confirm any server-tuned requirements in play.

## How to leave

For the 1.21.1 build, the upstream guide says to fall into the void to return. The older route through large biome portal structures applies to the 1.19 line and is not presented here as the current exit method.

## What is inside

The pinned generator explicitly selects Dark, Earth, Fire, Light, Space, Water, and Wind biomes. Each biome has its own terrain palette and reference page in the combined Biomes directory.

Only Dark, Earth, and Wind portal structures are registered by the reviewed 2.1.2 worldgen data. Fire, Space, and Water structure files exist in the jar, but their worldgen registrations are incomplete, so they are not promoted as working structures.

## Continue exploring

<div class="race-map-directory">
<a href="../../biomes/"><strong>Browse elemental biomes</strong><span>Open the connected reference.</span></a>
<a href="../../structures/structures-labyrinth-tree/"><strong>Find the praying platform</strong><span>Open the connected reference.</span></a>
</div>

??? info "Sources and verification"

    [Tensura: Mysticism 2.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-mysticism.pw.toml)

    Artifact SHA-1: `cca1bd878b46c21ddbbf507bd4489fbb217899c7`.

    Gameplay route cross-check: [Elemental Realm upstream reference](https://trmysticism.wiki.gg/wiki/Spirit_Realm).

    Packaged evidence:

    - `data/mysticism/dimension/elemental_realm.json`
    - `data/mysticism/dimension_type/elemental_realm.json`
    - `data/mysticism/worldgen/noise_settings/elemental_realm.json`
    - `io/github/Memoires/mysticism/handler/ElementalRealmHandler.class`
    - `io/github/Memoires/mysticism/mixin/block/MixinPrayingPathBlockEntity.class`

[Back to Dimensions](index.md)
