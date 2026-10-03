---
title: Asmodeus, Lord of Lust
description: Dominate life force, heal allies, drain enemies, and revive fallen subordinates.
tags:
- Ultimates
---

# Asmodeus, Lord of Lust

<span class="reference-badge">Tensura Nightmares reference</span> <span class="reference-category">Ultimate Skills</span>

<section class="reference-overview reference-theme-abilities">
<figure class="reference-overview-media reference-overview-media--source"><img src="../../../../assets/upstream/nightmares/skills/asmodeus.jpeg" alt="Asmodeus, Lord of Lust source icon" loading="eager" decoding="async"><figcaption><a href="https://tensuranightmares.wiki.gg/wiki/File:Asmodeus.jpeg">Tensura Reincarnated Nightmares Wiki · CC BY-SA 4.0</a></figcaption></figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Dominate life force, heal allies, drain enemies, and revive fallen subordinates.</p>
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
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Ultimate Skills · 1.21.1 reference build</p><h2 id="how-to-obtain">How to obtain</h2><p class="skill-evidence-note"><strong>Server build match pending.</strong> Reference: <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Nightmares 1.0.3.2.8-neoforge-1.21.1</a>.</p><details class="skill-source-limits"><summary>Version and source limits</summary><p>This skill is registered in the reference release. The installed version and server configuration have not yet been matched. The acquisition review below checks reference-build conditions separately. Other usage details describe the cited wiki revision, not verified server behavior.</p><p class="skill-evidence-note">The upstream article is incomplete; missing effects or unlock conditions are not assumed.</p></details><div class="nightmares-acquisition-review"><p><strong>Reviewed reference-build evolution route:</strong> Lust → Asmodeus. These conditions replace the source’s vague resource wording; they do not confirm live-server availability.</p><div class="skill-reading-guide"><div><span>01</span><h3>Master Lust</h3><p>Fully master your own <a href="../../unique/lust/">Lust</a> skill. Already owning Asmodeus blocks another evolution.</p></div><div><span>02</span><h3>Meet the recorded counters</h3><p>Reference defaults: at least <strong>25 entities named</strong> and <strong>100 animals bred</strong>. The player route checks statistics, not a headcount of currently living followers.</p></div><div><span>03</span><h3>Reach maximum Magicules</h3><p>The default capacity requirement is <strong>1,200,000 maximum Magicules</strong>, not current MP or total EP. Configuration can change this threshold.</p></div></div><p><strong>Before evolving:</strong> the inspected helper removes Lust after successful learning. Keeping both skills is not promised.</p><details class="skill-source-limits"><summary>Evolution gates and resource details</summary><p>The checked automatic route requires <code>nightmare_ultimates</code> and <code>auto_evolve</code> to be true, plus Asmodeus’s <code>enableUltimateEvolution</code> setting. The two gamerules default to <strong>false</strong> in this reference artifact; the skill setting defaults to true. <a href="../../../gamerules/">Review the gamerule reference</a>; active server values have not been checked.</p><p>The helper compares <code>EnergyHelper.getMaxMagicule(player) + 0.000001</code> with the skill’s configured acquiring cost. Exactly 1,200,000 meets the default comparison. This is a capacity gate; it does not prove that the final learning pipeline never charges resources.</p><p>The subordinate condition’s player branch reads <code>TensuraStats.ENTITY_NAMED</code>. The breeding condition reads <code>Stats.ANIMALS_BRED</code>. Both accept counts equal to the configured minimum. Pet ownership, nearby mobs, and putting an animal into love mode are not the counters inspected here; statistic-update behavior has not been tested live.</p><p>A predecessor marked <code>trnightmare_directive_ego</code> or <code>AkashicStarOrderImprint</code> is rejected by the shared helper. After successful learning, that helper records predecessor mastery and forgets Lust. This specific path does not consult <code>lose_unique_on_upgrade</code> before forgetting it; retaining both skills is not promised.</p><p>Prerequisites do not establish the event cadence or guarantee a successful grant through the surrounding learning system. Other acquisition routes have not been established by this review.</p></details><p class="skill-evidence-note">Acquisition handlers and defaults checked in <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Nightmares 1.0.3.2.8 for 1.21.1</a>. <a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_acquisition_review.json">Review the class checksums and conditions</a>. Usage values below remain source-described and are not a complete effect audit.</p><details class="skill-source-limits"><summary>Client inventory versus running server</summary><p>The September 20 client inventory names the same release file as this reference. The inventory supplies no artifact digest, so a filename match does not verify installed bytes, deployment, effective configuration, or gameplay.</p></details></div><aside class="skill-evidence-note skill-mastery-note"><strong>Mastery target:</strong> 15,000 points in the reviewed reference default, from <code>ultMasteryConfig.masterySinUlt</code>. This is the skill’s own mastery target, not a predecessor unlock condition or a verified server setting. <a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_mastery_reference.json">Mastery evidence</a>.</aside></section>
<!-- skill-catalogue:end -->

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><p>Dominate life force, heal allies, drain enemies, and revive fallen subordinates.</p><div class="druid-infobox druid-container noexcerpt druid-container-skill" id="druid-container-1"><div><div class="druid-title">「Asmodeus, Lord of Lust」</div></div><div class="druid-section-container"></div><div class="druid-section-container"><div data-druid-section="Information"><div class="druid-section druid-section-Information">Information</div></div><div class="druid-row druid-row-Type" data-druid-section-row="Information"><div class="druid-label druid-label-Type">Type</div><div class="druid-data druid-data-Type druid-data-nonempty">Ultimate Skill</div></div><div class="druid-row druid-row-ObtainCost" data-druid-section-row="Information"><div class="druid-label druid-label-ObtainCost">Obtain Cost</div><div class="druid-data druid-data-ObtainCost druid-data-nonempty">
1.2M</div></div><div class="druid-row druid-row-PointstoMaster" data-druid-section-row="Information"><div class="druid-label druid-label-PointstoMaster">Points to Master</div><div class="druid-data druid-data-PointstoMaster druid-data-nonempty">15,000 (reference default)</div></div><div class="druid-row druid-row-Passive" data-druid-section-row="Information"><div class="druid-label druid-label-Passive">Passive</div><div class="druid-data druid-data-Passive druid-data-nonempty">
Toggle</div></div></div><div class="druid-section-container"><div data-druid-section="Evolution"><div class="druid-section druid-section-Evolution">Evolution</div></div><div class="druid-row druid-row-Previous" data-druid-section-row="Evolution"><div class="druid-label druid-label-Previous">Previous</div><div class="druid-data druid-data-Previous druid-data-nonempty">
<a class="external text" href="../../unique/lust/">Lust</a></div></div></div><div class="druid-section-container"><div data-druid-section="Obtaining"><div class="druid-section druid-section-Obtaining">Obtaining</div></div><div class="druid-row druid-row-Other" data-druid-section-row="Obtaining"><div class="druid-label druid-label-Other">Other</div><div class="druid-data druid-data-Other druid-data-nonempty"><a href="#how-to-obtain">Reviewed Lust evolution conditions</a> · server build match pending</div></div></div></div>
<h2><span class="mw-headline" id="Usage">Usage</span></h2>
<h3><span class="mw-headline" id="Passive">Passive</span></h3>
<ul><li>[Passive, Toggle] Life Domination: Consumption - The user is able to heal themselves for a percentage of physical damage they deal.</li></ul>
<ul><li>[Passive, In-Slot] Life Domination: Pain Amplification - The user is able to bypass resistances and degrades nullifications to resistances.</li></ul>
<ul><li>[Passive, True] Life Domination: Superior Life Force - The user cannot have their Energy drained by an attack from a player that has less than 75% of their EP.  Any draining effects on the user are cut in half. (75% when mastered)</li></ul>
<p><br/>
</p>
<h3><span class="mw-headline" id="Actives">Actives</span></h3>
<ul><li>[Active, In-Slot] Re-Birth - When this mode is in-slot, the user's subordinates, when killed, will leave behind their Soul. You can use this ability while looking at the target to revive them.</li></ul>
<ul><li>[Active, Hold] Life Domination: Seduction - When held the user begins to deal 1% of the target's SHP every second, if Seduction is used to reduce their SHP to 30% or lower, they become Charmed.</li></ul>
<ul><li>[Active, Press} Life Domination: Embracing Drain - Requires the player to be looking at a mob and be within 3 blocks. Locks the player and the mob in place and drains 500 (2.5% with Mastery) MP and AP per second. Lasts for a total of 5 seconds. Causes pain effects even with resistance/nullification. Cost 1,000 MP.</li></ul>
<ul><li>[Active, Press] Life Domination: Arousal - When used while not looking at a mob or when sneaking, fully heals the player and removes all status effects. When looking at a mob while sneaking, fully heals them and removes all status effects [Cost 40 MP (20 with Mastery) per HP and 20 MP per effect level]. If used on a mob that can breed while its at full hp, will cause them to enter hearts mode. This ability when mastered can be used to reset a mob's breeding timer.</li></ul>
<ul><li>[Active, Hold] Death Blessing - When holding down, a pair of divine hands reaching from the sky toward the position/target that the user is looking at (in 14 block range), while being casted, every entities in 6x6 block radius around the targeted position are slowed down by 80%. Once reaching 4s casted, all of the affected entities are instantly killed if their EP is lower than 65% of the player's and restores the player's expended MP and AP by the target mobs EP (75/25). If the target is between 65% and 95% Drains 25% EP and deals half their HP in damage. If above 95% drains 5% and deals half their HP in damage. Cost 170,500 MP - 5s cooldown.</li></ul>
<ul><li>[Active, In-Slot] Memory End Requiem - While this mode is in slot, the user drains the life force of anyone they strike, to various degrees based off several factors. This art does have a 7 Second Cooldown.
<ul><li>If the target has less than 30% of your EP, this skill will drain 80% of their Magicules and Aura in a single strike.</li>
<li>The the target has less than 50% of your EP, this skill will drain 60% of their Magicules and Aura in a single strike.</li>
<li>The the target has less than 70% of your EP, this skill will drain 40% of their Magicules and Aura in a single strike.</li>
<li>The the target has less than 50% of your EP and has no Ultimate Skill, this will drain 99% of their Magicules and Aura in a single strike.</li></ul></li></ul>
</div>
</div>

---

## Source and licensing

Tensura Nightmares reference adapted from [Asmodeus](https://tensuranightmares.wiki.gg/wiki/Asmodeus) on the Tensura Reincarnated Nightmares Wiki (revision `2569`, modified `2026-07-31T20:41:19Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

<!-- skill-artwork-credit:start -->
Icon: [Asmodeus, Lord of Lust](https://tensuranightmares.wiki.gg/wiki/File:Asmodeus.jpeg), Tensura Reincarnated Nightmares Wiki; uploaded by UnluckyWarl0ck (2025-05-31T19:55Z). [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Unmodified wiki-hosted image.
<!-- skill-artwork-credit:end -->
