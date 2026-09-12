---
title: "Cadence Acceleration Glass"
description: "A replaceable glass field block tracked by the Nightmares Cadence time-acceleration handler."
---

# Cadence Acceleration Glass

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/icons/blocks/nightmares-cadence-acceleration-glass.svg" alt="Cadence Acceleration Glass reference symbol" loading="eager" decoding="async">
<figcaption>TSR reference symbol</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A replaceable glass field block tracked by the Nightmares Cadence time-acceleration handler.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! warning "1.21.1 reference — server build match pending"

    Verified against **Tensura Nightmares 1.0.3.2.8** as a reference artifact. The server's exact Nightmares release has not been confirmed.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Cadence Acceleration Glass</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares 1.0.3.2.8</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">trnightmare:cadence_accel_glass</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Cadence time-field helper</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Glass-textured field block</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Skill-created/internal block</div></div>
</aside></div></div>

## What it does

Placement and removal notify the Cadence time-tick handler, identifying this as implementation support for Cadence's accelerated-time field rather than an ordinary building block.

## Player access

The reference build gives it a vanilla glass model, no occlusion, and replaceable behavior. No conventional crafting recipe or survival acquisition path was verified.

??? info "Sources and verification"

    [Tensura Nightmares 1.0.3.2.8 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Packaged implementation evidence:

    - `com/github/hvnbael/trnightmare/registry/main/NightmareBlocks.class`
    - `com/github/hvnbael/trnightmare/main/block/CadenceAccelGlassBlock.class`
    - `com/github/hvnbael/trnightmare/handler/CadenceTimeTickHandler.class`
    - `assets/trnightmare/models/block/cadence_accel_glass.json`

    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.

[Back to Blocks](index.md)
