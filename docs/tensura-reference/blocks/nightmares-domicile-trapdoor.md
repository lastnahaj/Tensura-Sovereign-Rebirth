---
title: "Domicile Trapdoor"
description: "The trapdoor form of the Domicile entrance, with the same ownership and return-travel checks."
---

# Domicile Trapdoor

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Blocks</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/icons/blocks/nightmares-domicile-trapdoor.svg" alt="Domicile Trapdoor reference symbol" loading="eager" decoding="async">
<figcaption>TSR reference symbol</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>The trapdoor form of the Domicile entrance, with the same ownership and return-travel checks.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! warning "1.21.1 reference — server build match pending"

    Verified against **Tensura Nightmares 1.0.3.2.8** as a reference artifact. The server's exact Nightmares release has not been confirmed.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Domicile Trapdoor</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares 1.0.3.2.8</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">trnightmare:domicile_trapdoor</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Owned Domicile entrance</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Oak-trapdoor model</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Domicile-generated block</div></div>
</aside></div></div>

## What it does

The block uses Domicile ownership data and a teleport cooldown to connect an eligible player with the correct private space or exterior return point.

## Player access

The release uses vanilla oak-trapdoor textures. No conventional crafting recipe was verified; it is registered as part of the Domicile system.

??? info "Sources and verification"

    [Tensura Nightmares 1.0.3.2.8 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Packaged implementation evidence:

    - `com/github/hvnbael/trnightmare/main/block/DomicileTrapDoorBlock.class`
    - `com/github/hvnbael/trnightmare/main/block/DomicileDoorBlockEntity.class`
    - `com/github/hvnbael/trnightmare/world/DomicileDimensionService.class`
    - `assets/trnightmare/models/block/domicile_trapdoor_bottom.json`

    The symbol on this page is original TSR interface art; it is not presented as an in-game texture.

[Back to Blocks](index.md)
