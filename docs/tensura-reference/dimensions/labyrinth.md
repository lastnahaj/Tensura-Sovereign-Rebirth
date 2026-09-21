---
title: Labyrinth
description: "Tensura's generated challenge maze, entered through a Labyrinth Tree and built around the Elemental Colossus route."
---

# Labyrinth

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Dimensions</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/upstream/tensura/structures/labyrinth-hallway-10fc0a387d.png" alt="Labyrinth reference artwork" loading="eager" decoding="async">
<figcaption>Verified realm reference</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Tensura&#x27;s generated challenge maze, entered through a Labyrinth Tree and built around the Elemental Colossus route.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-enter-and-leave">How to enter and leave</a>
<a href="#progress-through-the-maze">Progress through the maze</a>
<a href="#mysticism-connection">Mysticism connection</a>
</nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Registered by **Tensura: Reincarnated 2.0.1.2**, the release selected by TSR. Registry and code paths were checked directly; claims that still require live gameplay are labeled.

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Labyrinth</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:labyrinth</div></div>
<div class="druid-row"><div class="druid-label">World type</div><div class="druid-data">Generated maze in a void world</div></div>
<div class="druid-row"><div class="druid-label">Entry</div><div class="druid-data">Labyrinth Tree portal</div></div>
<div class="druid-row"><div class="druid-label">Suggested minimum</div><div class="druid-data">8,000 EP</div></div>
<div class="druid-row"><div class="druid-label">Beds</div><div class="druid-data">Disabled</div></div>
<div class="druid-row"><div class="druid-label">Key encounter</div><div class="druid-data">Elemental Colossus</div></div>
</aside></div></div>

## How to enter and leave

Find a Labyrinth Tree and step through its portal. The upstream 1.21.1 guide recommends at least 8,000 EP because underprepared players are rejected by Magicule Poisoning; that figure is guidance, not a value stored in the dimension JSON.

The portal implementation returns players from the Labyrinth to their Overworld respawn route when possible. A master-level Dwarf cartographer can offer a Labyrinth Explorer Map, but individual villager trades vary.

## Progress through the maze

The dimension file itself is an empty flat world. Tensura's Labyrinth storage and generation systems build the playable maze into that space, so the route is not represented by normal biome terrain.

The entrance destination changes after the Elemental Colossus milestone: the portal code checks whether the entity has passed the Colossus and uses the post-encounter entrance when appropriate.

## Mysticism connection

Mysticism uses the praying platform near the Labyrinth route as the current upstream entrance point for its Elemental Realm. That is a separate dimension and should not be confused with the unrelated Tensura: Dungeon mod, which is not installed in TSR.

## Continue exploring

<div class="race-map-directory">
<a href="../../structures/structures-labyrinth-tree/"><strong>Open the Labyrinth Tree</strong><span>Open the connected reference.</span></a>
<a href="../elemental-realm/"><strong>Continue to the Elemental Realm</strong><span>Open the connected reference.</span></a>
</div>

??? info "Sources and verification"

    [Tensura: Reincarnated 2.0.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml)

    Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

    Gameplay route cross-check: [Labyrinth upstream reference](https://tensura.wiki.gg/wiki/Structures/Labyrinth_Tree).

    Packaged evidence:

    - `data/tensura/dimension/labyrinth.json`
    - `data/tensura/dimension_type/labyrinth.json`
    - `io/github/manasmods/tensura/block/LabyrinthPortal.class`
    - `io/github/manasmods/tensura/handler/LabyrinthHandler.class`
    - `io/github/manasmods/tensura/storage/labyrinth/LabyrinthStorage.class`

[Back to Dimensions](index.md)
