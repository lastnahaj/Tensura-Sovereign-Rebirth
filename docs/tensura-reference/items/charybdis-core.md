---
title: "Charybdis Core"
description: "A stateful boss core: recover it as an item, place it to collect EP, and use the active placed core to prime a Charybdis encounter."
---

# Charybdis Core

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/blocks/charybdis-core.webp" alt="Charybdis Core illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A stateful boss core: recover it as an item, place it to collect EP, and use the active placed core to prime a Charybdis encounter.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Block recovery checked · live acquisition untested"
    Block interactions and registration were checked in Tensura 2.0.1.2. Cave acquisition, live recovery, combat, skill grants, and synthesis remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Charybdis Core</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:charybdis_core</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Block recovery checked · live acquisition untested</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64, subject to matching components</div></div>
<div class="druid-row"><div class="druid-label">Item property</div><div class="druid-data">Fire resistant</div></div>
</aside></div></div>

<span id="Obtainment"></span><span id="Location"></span>

## Availability

The source locates inactive cores in [Charybdis Cave](../structures/structures-charybdis-cave.md). The checked block loot returns one `tensura:charybdis_core` and copies its stored EP component and phase. Sneak-use of a placed core also requests its block drops, adds them to the player inventory, then destroys the block without further drops. Keep inventory space free: that method does not provide a fallback for a failed inventory insertion. No packaged crafting recipe referencing the core was found.

<span id="Usage"></span>

## How to use

Place the core and follow the [charging and activation guide](../blocks/blocks-charybdis-core.md). Only an **active placed core** enters the priming branch when used without sneaking; the checked action is **use/right-click with an empty hand**, not a left-click strike or an air-use of the inventory item. Sneak-use is the pickup branch.

## Behavior and limits

The item factory uses `SimpleBlockItem` with default stack properties and fire resistance. The **64-item limit** does not prove cores with different phase or EP components will merge. The active branch removes the placed block and creates a primed entity with a **200-tick fuse** and **strength-10 MOB explosion** before attempting to spawn Charybdis. Do not activate near a settlement. Actual explosion damage, protection-plugin behavior, and successful server spawning are untested.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Charybdis Core](https://tensura.wiki.gg/wiki/Charybdis_Core) on the Tensura: Reincarnated Wiki, recorded revision `13039`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `TensuraMobDropItems`
    - `SimpleBlockItem`
    - `CharybdisCoreBlock`
    - `CharybdisCoreBlockEntity`
    - `data/tensura/loot_table/blocks/charybdis_core.json`
