---
title: Belphegor, Lord of Sloth
description: "Store surplus Magicules through rest and weaken enemies with drowsiness."
tags:
- Ultimates
---

# Belphegor, Lord of Sloth

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Ultimate Skills</span>

<section class="reference-overview reference-theme-abilities">
<figure class="reference-overview-media reference-overview-media--theme"><img src="../../../../assets/illustrations/skills/belphegor.png" alt="Belphegor, Lord of Sloth illustration" width="96" height="96"><figcaption>TSR skill artwork</figcaption></figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Store surplus Magicules through rest and weaken enemies with drowsiness.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-obtain">How to obtain</a>
<a href="#Usage">Usage</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<!-- skill-catalogue:start -->
<nav class="skill-category-nav" aria-label="Skill directory"><a href="../">← Browse Ultimate Skills</a></nav>
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Ultimate Skills · 1.21.1 reference build</p><h2 id="how-to-obtain">How to obtain</h2><p class="skill-evidence-note"><strong>Server build match pending.</strong> Reference: <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Nightmares 1.0.3.2.8-neoforge-1.21.1</a>.</p><details class="skill-source-limits"><summary>Version and source limits</summary><p>This skill is registered in the reference release. The installed version and server configuration have not yet been matched. The acquisition review below checks reference-build conditions separately. Other usage details describe the cited wiki revision, not verified server behavior.</p><p class="skill-evidence-note">The upstream article is incomplete; missing effects or unlock conditions are not assumed.</p></details><div class="nightmares-acquisition-review"><p><strong>Reviewed reference-build evolution route:</strong> Sloth → Belphegor. Separate the skill’s stored reserve, your maximum Magicules, and the bed-progress counter.</p><div class="skill-reading-guide"><div><span>01</span><h3>Prepare Sloth’s reserve</h3><p>Fully master your own permanent <a href="../../unique/sloth/">Sloth</a>. Its <code>storedMagicule</code> tag must hold at least <strong>25,000 stored Magicules</strong> by default. Current player MP is not this reserve.</p></div><div><span>02</span><h3>Build bed progress</h3><p>The default is <strong>12,000 recorded ticks</strong> standing still on a bed. The condition also requires you to be on a bed when checked. Sleeping through a night is not the predicate inspected here.</p></div><div><span>03</span><h3>Meet the player thresholds</h3><p>Reference defaults: at least <strong>1,000 recorded mob kills</strong> and <strong>1,000,000 maximum Magicules</strong>. These are a player statistic and a capacity gate, not held items or current MP.</p></div></div><p><strong>Before evolving:</strong> the selected helper removes Sloth after successful learning. Gamerules, skill configuration, and the bed tracker must permit the route. Active server settings and successful evolution remain unverified.</p><details class="skill-source-limits"><summary>Bed progress: ticks, standing, and configuration</summary><p>The configured bed minutes are multiplied by 60 × 20. At the default of 10 minutes this is 12,000 ticks, nominally ten minutes at 20 ticks per second. No wall-clock timer or reliable live completion time has been verified.</p><p>The predicate checks a server player, horizontal movement squared no greater than 0.0001, and sampled bounding-box overlap with a block tagged <code>BEDS</code>. It then requires <code>designer_bed_still_ticks</code> to meet the threshold. Ordinary sleeping state is not checked.</p><p>The inspected tick helper increments the counter while this bed predicate is true. Leaving the bed does not reset the counter in that helper, but you must be on a bed when eligibility is evaluated. Other reset and persistence paths remain unverified.</p><p>The shared tracker uses Designer’s separate <code>slothBedMinutesRequired</code> setting, default 60, to enable tracking. A nonpositive value resets the counter to zero. That setting does not replace Belphegor’s default ten-minute threshold. The handler calls the tracker on its server-player tick path; effective runtime cadence remains untested.</p></details><details class="skill-source-limits"><summary>Evolution gates and exact counters</summary><p>The selected route requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Belphegor’s <code>enableUltimateEvolution</code>. The two gamerules default to false; the skill setting defaults to true. <a href="../../../gamerules/">Review the gamerules</a>. Already owning Belphegor blocks another evolution.</p><p>The reserve predicate reads Sloth’s skill-instance tag; the kill predicate reads <code>Stats.MOB_KILLS</code>. Both accept the configured minimum. The shared helper checks maximum Magicules with a 0.000001 tolerance; this does not prove the complete learning pipeline never charges resources.</p><p>The helper rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>, records predecessor mastery, and forgets Sloth after successful learning. Keeping both skills is not promised. Alternative routes and surrounding event ordering remain unverified.</p></details><p class="skill-evidence-note">Belphegor’s default mastery target is <strong>15,000</strong> from <code>ultMasteryConfig.masterySinUlt</code>, replacing the source’s 5,000 value. <a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/belphegor_acquisition_reference.json">Acquisition evidence</a> · <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Reviewed release</a>. Usage effects remain source-described, not a complete effect audit.</p></div></section>
<!-- skill-catalogue:end -->

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en">
<div class="druid-infobox druid-container noexcerpt druid-container-skill" id="druid-container-1"><div><div class="druid-title">「Belphegor, Lord of Sloth」</div></div><div class="druid-section-container"><div data-druid-section="Information"><div class="druid-section druid-section-Information">Information</div></div><div class="druid-row druid-row-Type" data-druid-section-row="Information"><div class="druid-label druid-label-Type">Type</div><div class="druid-data druid-data-Type druid-data-nonempty">Ultimate Skill</div></div><div class="druid-row druid-row-ObtainCost" data-druid-section-row="Information"><div class="druid-label druid-label-ObtainCost">Obtain Cost</div><div class="druid-data druid-data-ObtainCost druid-data-nonempty">
1,000,000 MP</div></div><div class="druid-row druid-row-PointstoMaster" data-druid-section-row="Information"><div class="druid-label druid-label-PointstoMaster">Points to Master</div><div class="druid-data druid-data-PointstoMaster druid-data-nonempty">15,000 (reference default)</div></div><div class="druid-row druid-row-Passive" data-druid-section-row="Information"><div class="druid-label druid-label-Passive">Passive</div><div class="druid-data druid-data-Passive druid-data-nonempty">
Toggle</div></div></div><div class="druid-section-container"><div data-druid-section="Evolution"><div class="druid-section druid-section-Evolution">Evolution</div></div><div class="druid-row druid-row-Previous" data-druid-section-row="Evolution"><div class="druid-label druid-label-Previous">Previous</div><div class="druid-data druid-data-Previous druid-data-nonempty">
<a class="external text" href="../../unique/sloth/">Sloth</a></div></div><div class="druid-row druid-row-Next" data-druid-section-row="Evolution"><div class="druid-label druid-label-Next">Next</div><div class="druid-data druid-data-Next druid-data-nonempty">
<a href="../nightmares-astaroth/" title="Astaroth">「Astaroth, King of Fallen」</a></div></div></div><div class="druid-section-container"><div data-druid-section="Obtaining"><div class="druid-section druid-section-Obtaining">Obtaining</div></div><div class="druid-row druid-row-Other" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other">Other</div><div class="druid-data druid-data-Other druid-data-nonempty"><a href="#how-to-obtain">Reviewed Sloth evolution conditions</a> · server build match pending</div></div><div class="druid-row druid-row-Other2" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other2"> </div><div class="druid-data druid-data-Other2 druid-data-nonempty">12,000 recorded standing-still-on-bed ticks; bed state required when checked</div></div><div class="druid-row druid-row-Other3" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other3"> </div><div class="druid-data druid-data-Other3 druid-data-nonempty">1,000 recorded mob kills (reference default)</div></div></div></div>
<h2><span class="mw-headline" id="Usage">Usage</span></h2>
<h3><span class="mw-headline" id="Passive">Passive</span></h3>
<ul><li>[Passive, True] Lord of Lethargy:
<ul><li>Whenever the user sleeps in a bed, they fully restore a large sum of magicules, and any amount that would bring them above 100% is stored as temp MP.</li></ul></li>
<li>[Passive, In-Slot] Phantasmal Style:
<ul><li>Applies an effect that deals 2.5% of the target's spiritual HP (5 when mastered) to the user's attacks. The user also has a chance of applying a level of Drowsiness to the target, (15% Chance, 30 when mastered), up to level 8.  The user increases the Spiritual Damage they do by 50 for every level of Drowsiness the target has.</li></ul></li></ul>
<p><br/>
</p>
<h3><span class="mw-headline" id="Active">Active</span></h3>
<ul><li>[Active, Press] Fallen Catastrophe:
<ul><li>The user can attacks a target, and instantly kills any target that doesn't check 2/3 of the conditions. If 2/3 conditions are met, it gives them drowsiness 4, if 3/3 are met, it gives them 3 instead.
<ul><li>Spiritual Attack Resistance or Nullification.</li>
<li>Greater than 30% of the user's EP.</li>
<li>Has an ultimate skill.</li></ul></li></ul></li>
<li>[Active, Press] Fallen Thanatos:
<ul><li>The target the user is looking at is given Drowsiness every 7 seconds. The target dies once the level of Drowsiness hits 10..</li></ul></li></ul>
<ul><li>[Active, Press]Fallen Strike:
<ul><li>The user's attacks deal 2.5% of the target's spiritual health damage (5% when mastered). This stacks with Phantasmal Style. Any target that doesn't possess an Ultimate Skill will be instantly killed upon their Spriitual HP reaching 30% of lower.</li></ul></li></ul>
<ul><li>[Active, Hold] True Sleep:
<ul><li>The user dozes into a sleeping state while it is held down, the player is unable to move, attack, or activate other abilities. Regen 100 (+10% of target’s max with Mastery) HP and Spiritual HP per sec and increases the players MP, and AP Regen by 100X. If MP is at max, it fills up a temporary MP storage at the same rate. If there is enough MP in the temporary storage (1000 x Y = X [Y = Number of Allies. X = Cost]), crouching will restore 2000 MP, 2000 AP, 100HP and 20 Spiritual HP to all allies within a 30x30 radius. Any nearby enemy instead has their SpiritualHP reduced by 20 and their MP and AP reduced by 100 every second per level of Drowsiness they have. When looking at no target and crouching, show the quantity of MP stored.</li></ul></li></ul>
</div>
</div>

---

## Source and licensing

Acquisition requirements reviewed against the [current source article](https://tensuranightmares.wiki.gg/wiki/Belphegor) on 29 September 2026. These source changes have not been confirmed against the installed server build.

Tensura Nightmares reference adapted from [Belphegor](https://tensuranightmares.wiki.gg/wiki/Belphegor) on the Tensura Reincarnated Nightmares Wiki (revision `2502`, modified `2026-07-26T17:26:51Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

<!-- skill-artwork-credit:start -->
Original TSR skill artwork; an illustrated interpretation, not an in-game icon.
<!-- skill-artwork-credit:end -->
