---
title: Life Essence
---

# Life Essence

A Nightmares material obtained by tending crops: bone meal on growing crops or harvesting mature crops.

!!! warning "1.21.1 reference — server build match pending"

    Verified against Nightmares **1.0.3.2.8-neoforge-1.21.1**. The server's exact Nightmares release has not been confirmed; availability and settings can differ.

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/items/nightmares-life-essence.webp" alt="Life Essence item artwork" loading="eager" decoding="async">
<figcaption>Original TSR item artwork</figcaption>
</figure>

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Life Essence</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares</div></div>
<div class="druid-row"><div class="druid-label">Bone meal on growing crops</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Breaking mature crops</div><div class="druid-data">10%</div></div>
</aside></div></div>

**Registry ID:** `trnightmare:life_essence`

## How to obtain

Use bone meal on an immature crop to trigger a 50% chance of one Life Essence. The block must be a CropBlock and must not have reached its maximum age; this does not apply to every plant that accepts bone meal.

Break a fully grown crop to trigger a 10% chance of one Life Essence. Breaking an immature crop does not meet this condition.

These are two separate server-side event checks in the reference release. A chance is not a guarantee, and other server rules can affect farming.

## Source clarification

The upstream article gives the same percentages but omits the crop-age conditions. The reference release explicitly checks crop type and maturity. Its repeatable farming routes also mean the article's non-renewable label is not used here.

??? info "Sources and verification"

    [Reference release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382) · [Upstream article](https://tensuranightmares.wiki.gg/wiki/Life_Essence) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid=1409)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.

    Evidence classes in `com.github.hvnbael.trnightmare`:

    - `registry.main.NightmareMobDrops`
    - `handler.MobDropHandler`

    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Release-specific corrections and verification notes are identified above.

    The page uses original TSR article artwork and does not present it as the in-game item texture.

[Back to the collection](index.md)
