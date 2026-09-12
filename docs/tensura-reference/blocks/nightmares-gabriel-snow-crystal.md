---
title: "Gabriel Snow Crystal"
description: "A non-occluding ice-textured support block registered for Gabriel's frost mechanics."
---

# Gabriel Snow Crystal

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/icons/blocks/nightmares-gabriel-snow-crystal.svg" alt="Gabriel Snow Crystal reference symbol" loading="eager" decoding="async">
<figcaption>TSR reference symbol</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A non-occluding ice-textured support block registered for Gabriel&#x27;s frost mechanics.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! warning "1.21.1 reference — server build match pending"

    Verified against **Tensura Nightmares 1.0.3.2.8** as a reference artifact. The server's exact Nightmares release has not been confirmed.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Gabriel Snow Crystal</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares 1.0.3.2.8</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">trnightmare:gabriel_snow_crystal</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Gabriel frost-field helper</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Ice-textured crystal block</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Skill-created/internal block</div></div>
</aside></div></div>

## What it does

The reviewed implementation provides custom player-destruction behavior and glass-like sound and visibility properties. Its naming and registration tie it to Gabriel, Lord of Patience.

## Player access

No conventional crafting recipe or survival acquisition path was verified in the reference artifact, so this entry does not present it as a player-crafted block.

??? info "Sources and verification"

    [Tensura Nightmares 1.0.3.2.8 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Packaged implementation evidence:

    - `com/github/hvnbael/trnightmare/registry/main/NightmareBlocks.class`
    - `com/github/hvnbael/trnightmare/main/block/GabrielSnowCrystalBlock.class`
    - `com/github/hvnbael/trnightmare/main/ultimates/GabrielSkill.class`
    - `assets/trnightmare/models/block/gabriel_snow_crystal.json`

    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.

[Back to Blocks](index.md)
