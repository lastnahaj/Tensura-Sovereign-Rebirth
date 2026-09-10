---
title: Elder Essence
---

# Elder Essence

A Nightmares boss reward that can attempt to awaken an ego in each compatible learned skill when consumed.

!!! warning "1.21.1 reference — server build match pending"

    Verified against Nightmares **1.0.3.2.8-neoforge-1.21.1**. The server's exact Nightmares release has not been confirmed; availability and settings can differ.

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/items/nightmares-elder-essence.webp" alt="Elder Essence item artwork" loading="eager" decoding="async">
<figcaption>Original TSR item artwork</figcaption>
</figure>

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Elder Essence</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares</div></div>
<div class="druid-row"><div class="druid-label">Primordial Rouge</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Primordial Daemon</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Milim Wrath</div><div class="druid-data">45%</div></div>
<div class="druid-row"><div class="druid-label">Veldora / Velzard / Velgrynd</div><div class="druid-data">80% each</div></div>
<div class="druid-row"><div class="druid-label">Agera</div><div class="druid-data">5%</div></div>
<div class="druid-row"><div class="druid-label">Quantity per successful roll</div><div class="druid-data">1</div></div>
<div class="druid-row"><div class="druid-label">Ego attempt per compatible skill</div><div class="druid-data">25%</div></div>
</aside></div></div>

**Registry ID:** `trnightmare:elder_essence`

## How to obtain

In the reference release, Elder Essence is a programmatic boss reward. Primordial Rouge and Primordial Daemon each roll at 50%; Milim Wrath rolls at 45%; Veldora, Velzard, and Velgrynd each roll at 80%; and Agera rolls at 5%.

Each successful listed roll awards one Elder Essence. The percentages are independent drop chances in the reference code, not guaranteed live-server rates; datapacks, configuration, or a different installed build can change the result.

Packaged mob loot files also mention Elder Essence, but they are stored under the pre-1.21 loot_tables path. Minecraft 1.21 renamed that data-pack folder to loot_table, so those file-based mob drops are not presented as working acquisition routes without an in-game confirmation.

## How it works

When a server player consumes Elder Essence, the reference handler checks every learned skill that is capable of developing an ego. Each compatible skill independently has a 25% chance to receive its assigned ego.

This is not a 25% chance to select exactly one skill. A single use can succeed for none, one, or multiple compatible learned skills because the handler rolls each eligible skill separately.

## Source clarification

The upstream article describes the ego chance as 75%. In the reviewed reference handler, rolls below 0.75 are skipped, leaving a 25% success interval. This page follows the executable condition rather than repeating the article's percentage.

The upstream article's mob-drop claims are not used as verified 1.21.1 routes because the packaged loot files use the legacy directory name. The boss rewards above are registered directly by Java code and do not depend on that folder.

??? info "Sources and verification"

    [Reference release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382) · [Upstream article](https://tensuranightmares.wiki.gg/wiki/Elder_Essence) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid=2365)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.

    Evidence classes in `com.github.hvnbael.trnightmare`:

    - `registry.main.NightmareMobDrops`
    - `handler.BossRewards`
    - `handler.EventBusHandler`

    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Release-specific corrections and verification notes are identified above.

    The page uses original TSR article artwork and does not present it as the in-game item texture.

[Back to the collection](index.md)
