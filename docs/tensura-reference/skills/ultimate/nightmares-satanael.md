---
title: Satanael, Lord of Wrath
description: Generate Magicules, build Rampage, and regulate a powerful energy reactor.
tags:
- Ultimates
---

# Satanael, Lord of Wrath

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Ultimate Skills</span>

<section class="reference-overview reference-theme-abilities">
<figure class="reference-overview-media reference-overview-media--source"><img src="../../../../assets/upstream/nightmares/skills/satanael.png" alt="Satanael, Lord of Wrath source icon" loading="eager" decoding="async"><figcaption><a href="https://tensuranightmares.wiki.gg/wiki/File:Satanael.png">Tensura Reincarnated Nightmares Wiki · CC BY-SA 4.0</a></figcaption></figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Generate Magicules, build Rampage, and regulate a powerful energy reactor.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#how-to-obtain">How to obtain</a>
<a href="#Usage">Usage</a>
<a href="#Breeder_Reacter_Effect">Breeder Reacter Effect</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<!-- skill-catalogue:start -->
<nav class="skill-category-nav" aria-label="Skill directory"><a href="../">← Browse Ultimate Skills</a></nav>
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Ultimate Skills · 1.21.1 reference build</p><h2 id="how-to-obtain">How to obtain</h2><p class="skill-evidence-note"><strong>Server build match pending.</strong> Reference: <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Nightmares 1.0.3.2.8-neoforge-1.21.1</a>.</p><details class="skill-source-limits"><summary>Version and source limits</summary><p>This skill is registered in the reference release. The installed version and server configuration have not yet been matched. The acquisition review below checks reference-build conditions separately. Other usage details describe the cited wiki revision, not verified server behavior.</p><p class="skill-evidence-note">The upstream article is incomplete; missing effects or unlock conditions are not assumed.</p></details><div class="nightmares-acquisition-review"><p><strong>Reviewed reference-build evolution route:</strong> Wrath → Satanael. The selected checks use recorded victories and current health, not a Rampage effect level.</p><div class="skill-reading-guide"><div><span>01</span><h3>Master Wrath and record victories</h3><p>Fully learn and master your own non-temporary <a href="../../unique/wrath/">Wrath</a>. Reference defaults: at least <strong>500 recorded mob kills</strong> and <strong>20 recorded raid wins</strong>.</p></div><div><span>02</span><h3>Reach the capacity gate</h3><p>The reference default is <strong>1,500,000 maximum Magicules</strong>, not current MP or total EP. Automatic-evolution gamerules and Satanael’s configuration must allow the route.</p></div><div><span>03</span><h3>Meet the current-health check</h3><p>Default: health at or below <strong>40% of maximum health</strong> when eligibility is checked. This is a ratio, not 40 HP. Deliberately taking damage does not guarantee evolution or protection from death.</p></div></div><p><strong>Before evolving:</strong> the inspected helper removes Wrath after successful learning. Live eligibility, exact trigger timing, and effective server settings remain unverified.</p><details class="skill-source-limits"><summary>Health, victory counters, and source corrections</summary><p>The health predicate requires positive maximum health and accepts <code>getHealth() / getMaxHealth() &lt;= satanaelHP / 100.0</code>. The reviewed default is 40. The source says “under 40%”; this selected implementation uses an inclusive comparison.</p><p>Victories are checked through <code>Stats.MOB_KILLS</code> and <code>Stats.RAID_WIN</code>, accepting their configured minimums. A Hero of the Village effect or nearby monsters does not replace these counters. The raid condition’s identifier mentions Rampage, but its class reads raid wins; no Rampage-effect condition appears in this four-condition list.</p></details><details class="skill-source-limits"><summary>Evolution settings and predecessor replacement</summary><p>The selected path requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Satanael’s <code>enableUltimateEvolution</code>. The gamerules default to false; the skill setting defaults to true. <a href="../../../gamerules/">Review the gamerules</a>. Already owning Satanael prevents another evolution.</p><p>The shared helper checks maximum Magicules with a 0.000001 tolerance, rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>, and forgets Wrath after successful learning. This capacity check does not establish every learning charge, alternate route, or live event cadence.</p></details><p class="skill-evidence-note"><a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/satanael_acquisition_reference.json">Acquisition evidence and class checksums</a> · <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Reviewed release</a>. Usage effects retain their source attribution and are not a complete effect audit.</p></div><aside class="skill-evidence-note skill-mastery-note"><strong>Mastery target:</strong> 15,000 points in the reviewed reference default, from <code>ultMasteryConfig.masterySinUlt</code>. This is the skill’s own mastery target, not a predecessor unlock condition or a verified server setting. <a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_mastery_reference.json">Mastery evidence</a>.</aside></section>
<!-- skill-catalogue:end -->

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"> <div class="druid-infobox druid-container noexcerpt druid-container-skill" id="druid-container-1"><div><div class="druid-title">「Satanael, Lord of Wrath」</div></div><div class="druid-section-container"></div><div class="druid-section-container"><div data-druid-section="Information"><div class="druid-section druid-section-Information">Information</div></div><div class="druid-row druid-row-Type" data-druid-section-row="Information"><div class="druid-label druid-label-Type">Type</div><div class="druid-data druid-data-Type druid-data-nonempty">Ultimate Skill</div></div><div class="druid-row druid-row-ObtainCost" data-druid-section-row="Information"><div class="druid-label druid-label-ObtainCost">Obtain Cost</div><div class="druid-data druid-data-ObtainCost druid-data-nonempty">
1.5M</div></div><div class="druid-row druid-row-PointstoMaster" data-druid-section-row="Information"><div class="druid-label druid-label-PointstoMaster">Points to Master</div><div class="druid-data druid-data-PointstoMaster druid-data-nonempty">15,000 (reference default)</div></div><div class="druid-row druid-row-Passive" data-druid-section-row="Information"><div class="druid-label druid-label-Passive">Passive</div><div class="druid-data druid-data-Passive druid-data-nonempty">
Toggle</div></div></div><div class="druid-section-container"><div data-druid-section="Evolution"><div class="druid-section druid-section-Evolution">Evolution</div></div><div class="druid-row druid-row-Previous" data-druid-section-row="Evolution"><div class="druid-label druid-label-Previous">Previous</div><div class="druid-data druid-data-Previous druid-data-nonempty">
<a class="external text" href="../../unique/wrath/">Wrath</a></div></div></div><div class="druid-section-container"><div data-druid-section="Obtaining"><div class="druid-section druid-section-Obtaining">Obtaining</div></div><div class="druid-row druid-row-Other" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other">Other</div><div class="druid-data druid-data-Other druid-data-nonempty"><a href="#how-to-obtain">Reviewed Wrath evolution conditions</a> · health at or below 40% (reference default)</div></div></div></div>
<h2><span class="mw-headline" id="Usage">Usage</span></h2>
<h3><span class="mw-headline" id="Passive">Passive</span></h3>
<ul><li>[Passive, In-Slot] Breaking Point - While you have the Rampage Effect, the durability damage you cause from attacking armor will increase based off the Rampage Level.</li></ul>
<ul><li>[Passive, True (Mastery Required)] Law Breaker - While you have this skill mastered, you become immune to the conditions and laws of skills while your Rampaging. This means you are immune to the effects of Infinity Prison, Uriel, Law Manipulation, Magicule Poisoning and even Anti-Skill.</li></ul>
<ul><li>[Passive, True] Stampede - While you have Rampage above level 15, if you were to die, you instead are not killed, surviving even past instant kill skills. This reduces your level of Rampage by 15, and there is a chance that you're taken over by your own Wrath. (This can be change in the config, default is a 25% Chance. While taken over, the player is unable to control themselves as the Satanael Skill takes over and begins to attack and destroy everything.</li></ul>
<h3><span class="mw-headline" id="Actives">Actives</span></h3>
<ul><li>[Active, In-Slot] Anger Point - When taking damage, there is a chance of increasing your level of Rampage each time you take damage. (This cannot raise your Rampage above level 10. - Can be changed in configs)</li></ul>
<ul><li>[Active, Hold] Magicule Breeder Reactor - While held down, gives the player MP equal to 4% (6% at Mastery) of their maximum every 100 ticks. Each usage has a 5% (10% at mastery) chance to add 1 level of Rampage and 1 (2 at mastery) minute of duration which rises to 10% if the player's MP is past their natural maximum. With Mastery, becomes a toggle ability instead of hold.</li></ul>
<ul><li>[Active, Hold] Output Control - While held, the user can scroll and modify Satanael's output by 10% at a time, when Satanael is below 90%, Rampage is replaced with the Magicule Reactor effect.</li></ul>
<h2><span class="mw-headline" id="Breeder_Reacter_Effect">Breeder Reacter Effect</span></h2>
<p>Per level
</p>
<ul><li>+3 Armor</li>
<li>+15 Atk</li>
<li>+0.01 Atk Speed</li>
<li>+0.005 Speed</li>
<li>+0.005 Swim Speed</li>
<li>+ 0.05 Knockback Resist</li></ul>
</div>
</div>

---

## Source and licensing

Acquisition requirements reviewed against the [current source article](https://tensuranightmares.wiki.gg/wiki/Satanael) on 29 September 2026. These source changes have not been confirmed against the installed server build.

Tensura Nightmares reference adapted from [Satanael](https://tensuranightmares.wiki.gg/wiki/Satanael) on the Tensura Reincarnated Nightmares Wiki (revision `2535`, modified `2026-07-26T17:44:34Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

<!-- skill-artwork-credit:start -->
Icon: [Satanael, Lord of Wrath](https://tensuranightmares.wiki.gg/wiki/File:Satanael.png), Tensura Reincarnated Nightmares Wiki; uploaded by Maske (2026-05-28T15:33Z). [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unmodified wiki-hosted image.
<!-- skill-artwork-credit:end -->
