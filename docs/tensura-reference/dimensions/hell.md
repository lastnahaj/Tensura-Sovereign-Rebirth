---
title: Hell
description: "Tensura's Underworld dimension, reached through Hell Gate portals and generated from four verified 1.21.1 biomes."
---

# Hell

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Dimensions</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/encyclopedia/underworld-red-sands.webp" alt="Hell reference artwork" loading="eager" decoding="async">
<figcaption>Verified realm reference</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Tensura&#x27;s Underworld dimension, reached through Hell Gate portals and generated from four verified 1.21.1 biomes.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-enter-and-leave">How to enter and leave</a>
<a href="#what-is-inside">What is inside</a>
</nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Registered by **Tensura: Reincarnated 2.0.1.2**, the release selected by TSR. Registry and code paths were checked directly; claims that still require live gameplay are labeled.

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Hell</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:hell</div></div>
<div class="druid-row"><div class="druid-label">World type</div><div class="druid-data">Noise-generated</div></div>
<div class="druid-row"><div class="druid-label">Biomes</div><div class="druid-data">4 Underworld biomes</div></div>
<div class="druid-row"><div class="druid-label">Time</div><div class="druid-data">Fixed at 6000</div></div>
<div class="druid-row"><div class="druid-label">Beds</div><div class="druid-data">Disabled</div></div>
<div class="druid-row"><div class="druid-label">Portal</div><div class="druid-data">Hell Gate</div></div>
</aside></div></div>

## How to enter and leave

Find a Hell Gate in the Overworld and step into its portal surface. The pinned portal implementation sends entities from any non-Hell dimension into `tensura:hell` and sends entities in Hell back to the Overworld.

Master-level Dwarf cartographers can offer a Hell Gate Explorer Map according to the current upstream guide. Trades are generated gameplay content, so availability can vary with villager offers and server configuration.

## What is inside

The 1.21.1 generator selects Underworld Barrens, Underworld Red Sands, Underworld Sands, and Underworld Spikes. The Hell Gate can also generate within the Hell dimension, providing the portal surface used for the return trip.

Hell is not the vanilla Nether. It is a separate Tensura registry dimension with its own biome source and world-generation settings.

## Continue exploring

<div class="race-map-directory">
<a href="../../structures/structures-hell-gate/"><strong>Open the Hell Gate structure</strong><span>Open the connected reference.</span></a>
<a href="../../biomes/"><strong>Browse its biomes</strong><span>Open the connected reference.</span></a>
</div>

??? info "Sources and verification"

    [Tensura: Reincarnated 2.0.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml)

    Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

    Gameplay route cross-check: [Hell upstream reference](https://tensura.wiki.gg/wiki/Structures/Hell_Gate).

    Packaged evidence:

    - `data/tensura/dimension/hell.json`
    - `data/tensura/dimension_type/hell.json`
    - `data/tensura/worldgen/noise_settings/hell.json`
    - `io/github/manasmods/tensura/block/HellPortal.class`

[Back to Dimensions](index.md)
