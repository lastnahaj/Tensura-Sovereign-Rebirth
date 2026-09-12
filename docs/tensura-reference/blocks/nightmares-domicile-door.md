---
title: "Domicile Door"
description: "An ownership-aware doorway that connects a player with the private space created by Domicile."
---

# Domicile Door

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/icons/blocks/nightmares-domicile-door.svg" alt="Domicile Door reference symbol" loading="eager" decoding="async">
<figcaption>TSR reference symbol</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>An ownership-aware doorway that connects a player with the private space created by Domicile.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! warning "1.21.1 reference — server build match pending"

    Verified against **Tensura Nightmares 1.0.3.2.8** as a reference artifact. The server's exact Nightmares release has not been confirmed.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Domicile Door</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares 1.0.3.2.8</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">trnightmare:domicile_door</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Owned Domicile entrance</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Oak-door model</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Domicile-generated block</div></div>
</aside></div></div>

## What it does

The block stores owner and exterior-location data in its block entity. Its interaction and collision logic check the Domicile skill, apply a teleport cooldown, and move an eligible player between the exterior door and the owner's Domicile.

## Player access

The release uses vanilla oak-door textures. No conventional crafting recipe was verified; the block belongs to the Domicile system.

??? info "Sources and verification"

    [Tensura Nightmares 1.0.3.2.8 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Packaged implementation evidence:

    - `com/github/hvnbael/trnightmare/main/block/DomicileDoorBlock.class`
    - `com/github/hvnbael/trnightmare/main/block/DomicileDoorBlockEntity.class`
    - `com/github/hvnbael/trnightmare/world/DomicileDimensionService.class`
    - `assets/trnightmare/models/block/domicile_door_bottom_left.json`

    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.

[Back to Blocks](index.md)
