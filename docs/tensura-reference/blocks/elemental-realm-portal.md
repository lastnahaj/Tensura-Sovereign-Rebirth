---
title: "Elemental Realm Portal"
description: "The invisible, collisionless portal surface used by Mysticism's registered Elemental Realm portals."
---

# Elemental Realm Portal

<span class="reference-badge">TR Mysticism reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/icons/blocks/mysticism-elemental-realm-portal.svg" alt="Elemental Realm Portal reference symbol" loading="eager" decoding="async">
<figcaption>TSR reference symbol</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>The invisible, collisionless portal surface used by Mysticism&#x27;s registered Elemental Realm portals.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Verified against **TR Mysticism 2.1.2** selected by the TSR pack manifest.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Elemental Realm Portal</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">TR Mysticism 2.1.2</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">mysticism:elemental_realm_portal</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Dimension portal surface</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Invisible in-world render</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Structure/internal block</div></div>
</aside></div></div>

## What it does

Entities touching the portal surface are handed to Mysticism's dimension-transition logic. The reviewed class routes travel from the Overworld into the Elemental Realm and handles the return path through its configured destination logic.

## Player access

The block is waterloggable, has no collision, uses no loot table, and reports an invisible render shape. It should be understood as portal infrastructure rather than a normal decorative or survival-harvested block.

??? info "Sources and verification"

    [TR Mysticism 2.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-mysticism.pw.toml)

    Artifact SHA-1: `cca1bd878b46c21ddbbf507bd4489fbb217899c7`.

    Packaged implementation evidence:

    - `io/github/Memoires/mysticism/registry/MysticismBlocks.class`
    - `io/github/Memoires/mysticism/block/ElementalRealmPortal.class`
    - `assets/mysticism/blockstates/elemental_realm_portal.json`
    - `assets/mysticism/models/block/elemental_realm_portal.json`

    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.

[Back to Blocks](index.md)
