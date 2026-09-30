---
title: Reincarnation
description: "Re-select a race through a rebirth spell that changes player state and reduces maximum MP and AP."
tags:
- Aspectual_Magic
---

# Reincarnation

<span class="reference-badge">Base Tensura reference</span> <span class="reference-category">Magic</span>

<section class="reference-overview reference-theme-evolution">
<figure class="reference-overview-media reference-overview-media--source"><img src="../../../assets/illustrations/skills/reincarnation.webp" alt="Reincarnation illustration" width="96" height="96"><figcaption>TSR skill artwork</figcaption></figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Re-select a race through a rebirth spell that changes player state and reduces maximum MP and AP.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-obtain">How to obtain</a>
<a href="#Effect">Effect</a>
<a href="#Mastery_Bonus">Mastery Bonus</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<!-- skill-catalogue:start -->
<nav class="skill-category-nav" aria-label="Skill directory"><a href="../../magic/">← Browse Magic</a></nav>
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Magic · Pinned pack inventory</p><h2 id="how-to-obtain">How to obtain</h2><p>Source-described obtainment methods:</p><ul><li><strong>Other:</strong>
Learning it from a tome</li></ul><p class="skill-evidence-note">An obtainment method is separate from a skill’s MP cost. Check all conditions; a listed route is not a guaranteed starting roll.</p></section>
<!-- skill-catalogue:end -->

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><div class="druid-infobox druid-container druid-container-magic" id="druid-container-1"><div><div class="druid-title">Reincarnation</div></div><div class="druid-section-container"><div class="druid-main-image"><img alt="Reincarnation illustration" decoding="async" height="256" loading="lazy" src="../../../assets/illustrations/skills/reincarnation.webp" width="256"/></div></div><div class="druid-section-container"><div data-druid-section="Information"><div class="druid-section druid-section-Information">Information</div></div><div class="druid-row druid-row-Type" data-druid-section-row="Information"><div class="druid-label druid-label-Type">Type</div><div class="druid-data druid-data-Type druid-data-nonempty">
Aspectual</div></div><div class="druid-row druid-row-Cost" data-druid-section-row="Information"><div class="druid-label druid-label-Cost">Cost</div><div class="druid-data druid-data-Cost druid-data-nonempty">
10,000 MP to cast initially, then 25% Max MP and AP</div></div><div class="druid-row druid-row-CastTime" data-druid-section-row="Information"><div class="druid-label druid-label-CastTime">Cast Time</div><div class="druid-data druid-data-CastTime druid-data-nonempty">
200 Ticks</div></div><div class="druid-row druid-row-PointstoMaster" data-druid-section-row="Information"><div class="druid-label druid-label-PointstoMaster">Points to Master</div><div class="druid-data druid-data-PointstoMaster druid-data-nonempty">
100</div></div></div><div class="druid-section-container"><div data-druid-section="Obtaining"><div class="druid-section druid-section-Obtaining">Obtaining</div></div><div class="druid-row druid-row-Other" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other">Other</div><div class="druid-data druid-data-Other druid-data-nonempty">
Learning it from a tome</div></div></div></div>
<p>Re-select a race through a rebirth spell that changes player state and reduces maximum MP and AP.</p>
<h2><span class="mw-headline" id="Effect">Effect</span></h2>
<p><br/>
</p>
<ul><li>Allows the player to re-select their race and be reborn (resets alignment with race). The player maintains all of their non-intrinsic skills/magics/arts (even resistances), contracted spirits, awakening status (DL, Hero) and 75% of their max MP/AP. Chant Annulment does not work on this spell, and each use will grant 20 mastery points.</li></ul>
<h2><span class="mw-headline" id="Mastery_Bonus">Mastery Bonus</span></h2>
<p><br/>
</p>
<ul><li>Allows non-standard races to be selected.</li></ul>
<table class="wikitable pixel-image" data-description="History"><tbody><tr class="collapsible collapsible-rows"><th colspan="8">1.21.1</th></tr><tr><th colspan="4" rowspan="1"><a class="new" href="https://tensura.wiki.gg/wiki/1.21.1_2.0.0.0?action=edit&amp;redlink=1" rel="nofollow" title="1.21.1 2.0.0.0 (page does not exist)">2.0.0.0</a></th><td>Added</td></tr></tbody></table>
<p><br/>
</p>




</div>
</div>

## Spell safety in TSR

!!! warning "Reincarnation is not prestige"
    This is the **Reincarnation spell**, not the opening character-selection process or SlimeThrone Extras' prestige system. It resets player state and applies configured reductions to maximum MP and AP. Do not cast it expecting a prestige reward or a harmless race preview.

The pinned `ReincarnationMagic` implementation removes temporary skills and skills recorded as granted intrinsics of the old race, with removal-event checks. It also resets effects, flight state, warp points, and the respawn point before opening race selection. These implementation details qualify the upstream retention summary; other add-ons can affect the final outcome.

The tracked configuration sets a **200-tick cast**, **10,000 MP minimum casting cost**, and **25% reductions** to maximum Aura and Magicules. Its instant-cast override always returns false. Mastery expands the race-selection mode; it does not make this a SlimeThrone Extras prestige action. Artifact/configuration checks are not a live-server reset test.

**TSR guides:** [Getting Started](../../getting-started.md) · [Race & Evolution](../../race-and-evolution.md) · [Prestige & Soul Grade](../../prestige-and-soul-grade.md)



---

## Source and licensing

Base Tensura reference adapted from [Reincarnation](https://tensura.wiki.gg/wiki/Reincarnation) on the Tensura: Reincarnated Wiki (revision `13419`, modified `2026-09-04T14:08:52Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

<!-- skill-artwork-credit:start -->
Original TSR skill artwork; an illustrated interpretation, not an in-game icon.
<!-- skill-artwork-credit:end -->
