---
title: "Inert Charybdis Core"
description: "The spent COOLDOWN phase of Charybdis Core, produced by the boss death callback and used for configured skill-learning attempts."
---

# Inert Charybdis Core

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/inert-charybdis-core.webp" alt="Inert Charybdis Core illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>The spent COOLDOWN phase of Charybdis Core, produced by the boss death callback and used for configured skill-learning attempts.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Boss death callback checked · live recovery untested"
    Block interactions and registration were checked in Tensura 2.0.1.2. Cave acquisition, live recovery, combat, skill grants, and synthesis remain untested.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Inert Charybdis Core</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:charybdis_core</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Boss death callback checked · live recovery untested</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">64, subject to matching components</div></div>
<div class="druid-row"><div class="druid-label">Item property</div><div class="druid-data">Fire resistant</div></div>
</aside></div></div>

<span id="Obtaining"></span><span id="Mob_Drop"></span>

## Availability

The checked `CharybdisEntity.tickDeath` callback creates a falling Charybdis Core in **COOLDOWN** phase when its death counter reaches **40 ticks**, with the falling entity’s indestructible flag set. This is a death-callback path, not an ordinary core entry in the boss loot JSON. Landing, collection, and successful server recovery remain untested. It uses the same `tensura:charybdis_core` item ID as the other phases.

<span id="Usage"></span>

## How to use

Use a placed inert core without sneaking to attempt the configured [Gravity Manipulation](../skills/extra/gravity-manipulation.md) and [Magic Jamming](../magic/magic-jamming.md) skill-learning calls. This is not a guarantee that an already-owned, blocked, or otherwise ineligible skill can be learned. See the [core lifecycle guide](../blocks/blocks-charybdis-core.md#inert-core-rewards) before using or recovering it.

## Behavior and limits

With a nonempty resolved skill list, the checked branch removes the core if at least one `SkillHelper.learnSkill` call succeeds. If none succeeds it returns without removing the block. An empty resolved list also reaches the removal branch. The tracked synthesis configuration separately specifies **200,000 EP** and four inert-core skills, including [Magic Sense](../magic/magic-sense.md) and [Ultraspeed Regeneration](../skills/extra/ultraspeed-regeneration.md). These synthesis settings are configuration evidence only here; implementation eligibility and live rewards were not tested. Do not treat ordinary inert-core use as proof of those extra rewards.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Inert Charybdis Core](https://tensura.wiki.gg/wiki/Inert_Charybdis_Core) on the Tensura: Reincarnated Wiki, recorded revision `13037`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `TensuraMobDropItems`
    - `SimpleBlockItem`
    - `CharybdisCoreBlock`
    - `CharybdisCoreBlockEntity`
    - `data/tensura/loot_table/blocks/charybdis_core.json`
