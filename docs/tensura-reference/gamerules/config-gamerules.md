---
title: Gamerules
description: Base Tensura reference for Gamerules.
tags: []
---

# Gamerules

<span class="reference-badge">Base Tensura reference</span> <span class="reference-category">Gamerules</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/reference-world-equipment.png" alt="" loading="eager" decoding="async">
<figcaption>Original TSR section artwork</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Upstream reference information for Gamerules.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#Tutorial_Video">Tutorial Video</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en">
<h2><span class="mw-headline" id="Tutorial_Video">Tutorial Video</span></h2>
<figure class="embedvideo" data-mw-iframeconfig='{"src":"https://www.youtube-nocookie.com/embed/uGrdaj56NJw?autoplay=1"}' data-service="youtube">
<div class="embedvideo-wrapper">
<div class="embedvideo-consent" data-show-privacy-notice="1">
<div class="embedvideo-overlay">
<div class="embedvideo-loader" role="button">
<div class="embedvideo-loader__fakeButton">Load video</div>
<div class="embedvideo-loader__footer">
<div class="embedvideo-loader__service">YouTube</div>
</div>
</div>
<div class="embedvideo-privacyNotice hidden">
<div class="embedvideo-privacyNotice__content">YouTube might collect personal data. <a class="embedvideo-privacyNotice__link" href="https://www.youtube.com/howyoutubeworks/user-settings/privacy/" rel="nofollow,noopener" target="_blank">Privacy Policy</a></div>
<div class="embedvideo-privacyNotice__buttons">
<button class="embedvideo-privacyNotice__continue">Continue</button>
<button class="embedvideo-privacyNotice__dismiss">Dismiss</button>
</div>
</div>
</div>
</div>
</div>
</figure>

<h1><span class="mw-headline" id="Player">Player</span></h1>
<table class="wikitable">
<tbody><tr>
<th>Name</th>
<th>Description</th>
<th>Default Value</th>
<th>Valid Values
</th></tr>
<tr>
<td>epDeathPenalty</td>
<td>The percentage of EP that the player will lose when respawning</td>
<td>5</td>
<td>0 - 100
</td></tr>
<tr>
<td>epSteal</td>
<td>Enables certain skills to steal EP from Players</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>labyrinthDeath</td>
<td>Allows players to die in the Labyrinth Dimension instead of getting teleport out at 1HP</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>labyrinthPvp</td>
<td>Allows players to pvp in the Labyrinth Dimension</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td>maxAP</td>
<td>Maximum Aura Possible</td>
<td>1000000000</td>
<td>0 - 2147483647
</td></tr>
<tr>
<td>maxMP</td>
<td>Maxiumum Magicule Possible</td>
<td>1000000000</td>
<td>0 - 2147483647
</td></tr>
<tr>
<td>minEP</td>
<td>Minimum EP a Player can reach while playing</td>
<td>100</td>
<td>
</td></tr>
<tr>
<td>mpSkillCost</td>
<td>The percentage of MP that the player will lose when gaining a new skill</td>
<td>100</td>
<td>0 - 100
</td></tr>
<tr>
<td>playerMindControl</td>
<td>Enables certain skills to mind control Players</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td>playerNaming</td>
<td>Allows players to be named by others</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td>skillGriefing</td>
<td>Determines if Skills/Magic/Battlewill can grief blocks</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td>skillSteal</td>
<td>Enables certain skills to steal Skills from Players instead of copying</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td>disableSpiritualLimit</td>
<td>Disables the limit of EP for daemons outside hell without a name or awakening</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>disableDaemonAutoMagic</td>
<td>Disables automatic obtainment of aspectual magic upon evolution for daemons</td>
<td>false</td>
<td>true - false
</td></tr></tbody></table>
<h1><span class="mw-headline" id="Spawning">Spawning</span></h1>
<table class="wikitable">
<tbody><tr>
<th>Name</th>
<th>Description</th>
<th>Default Value</th>
<th>Valid Values
</th></tr>
<tr>
<td>colossusRespawn</td>
<td>Respawns the Elemental Colossus when a player who hasn't won against a colossus before reaches the arena in the Labyrinth</td>
<td>false</td>
<td>true - false
</td></tr></tbody></table>
<h1><span class="mw-headline" id="Drops">Drops</span></h1>
<table class="wikitable">
<tbody><tr>
<th>Name</th>
<th>Description</th>
<th>Default Value</th>
<th>Valid Values
</th></tr>
<tr>
<td>epGain</td>
<td>How much percentage of EP that mobs can give when killed</td>
<td>3</td>
<td>0 - 100
</td></tr>
<tr>
<td>maxApGain</td>
<td>Maximum amount of Aura an entity can gain at once from killing a target</td>
<td>1000000000</td>
<td>0 - 2147483647
</td></tr>
<tr>
<td>maxMpGain</td>
<td>Maximum amount of Magicule an entity can gain at once from killing a target</td>
<td>1000000000</td>
<td>0 - 2147483647
</td></tr>
<tr>
<td>playerEP</td>
<td>How much percentage of default EP value that fallen players can be used for EP gain calculation</td>
<td>100</td>
<td>0-100
</td></tr>
<tr>
<td>spawnerEP</td>
<td>How much percentage of default EP value that mobs spawned from Spawners can be used for EP gain calculation</td>
<td>10</td>
<td>0 - 100
</td></tr>
<tr>
<td>vanillaEP</td>
<td>How much percentage of default EP value that vanilla mobs can be used for EP gain calculation</td>
<td>100</td>
<td>0 - 100
</td></tr></tbody></table>
<h1><span class="mw-headline" id="Chat">Chat</span></h1>
<table class="wikitable">
<tbody><tr>
<th>Name</th>
<th>Description</th>
<th>Default Value</th>
<th>Valid Values
</th></tr>
<tr>
<td>tensuraDisplayName</td>
<td>Display the tensura name if the player is named</td>
<td>false</td>
<td>true - false
</td></tr></tbody></table>
<h1><span class="mw-headline" id="Miscellaneous">Miscellaneous</span></h1>
<table class="wikitable">
<tbody><tr>
<th>Name</th>
<th>Description</th>
<th>Default Value</th>
<th>Valid Values
</th></tr>
<tr>
<td>demonLordAwaken</td>
<td>The amount of Soul Points needed to be a True Demon Lord</td>
<td>10000</td>
<td>0 - ?
</td></tr>
<tr>
<td>demonLordSeed</td>
<td>The amount of EP needed to be a Demon Lord Seed</td>
<td>200000</td>
<td>0 - ?
</td></tr>
<tr>
<td>forceHarvestFestival</td>
<td>The souls required to force a harvest festival</td>
<td>20000</td>
<td>0 - 2147483
</td></tr>
<tr>
<td>experimentalFeature</td>
<td>Allow experimental features from Tensura:Reincarnated to be used</td>
<td>true</td>
<td>true - false
</td></tr>
<tr>
<td><a href="../../core-mechanics/mechanics-hardcore-race/" title="Mechanics/Hardcore Race">hardcoreRace</a></td>
<td>Makes some Races harder to play as</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>noUniqueStart</td>
<td>Starts with a buff in MP/AP but no Unique Skills</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td><a href="../../core-mechanics/mechanics-reset-counter/" title="Mechanics/Reset Counter">resetCounterBonusUnique</a></td>
<td>Gains more Unique skills on resetting based on how many Reset Counters per skill. Maximum skills dictated by <a class="new" href="https://tensura.wiki.gg/wiki/Config/Common?action=edit&amp;redlink=1" rel="nofollow" title="Config/Common (page does not exist)">maxCounterBonus</a></td>
<td>0</td>
<td>0 - ?
</td></tr>
<tr>
<td><a href="../../core-mechanics/mechanics-reset-counter/" title="Mechanics/Reset Counter">resetIncompletePenalty</a></td>
<td>Number of points gets removed from the Reset Counter when a player uses any reset scroll while not meeting the requirement</td>
<td>0</td>
<td>0 - ?
</td></tr>
<tr>
<td><a href="../../core-mechanics/mechanics-rimuru-mode/" title="Mechanics/Rimuru Mode">rimuruMode</a></td>
<td>Starts as Rimuru</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>skillBeforeRace</td>
<td>GainsUnique Skills before choosing race</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>trulyUnique</td>
<td>Removes owned Unique Skills from reincarnation skill list</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>DisableNullification</td>
<td>Disables nullification skills from being used</td>
<td>false</td>
<td>true - false
</td></tr>
<tr>
<td>NpcGrief</td>
<td>Enables humanoid NPCs to interact with the environment regardless of mobGriefing</td>
<td>true</td>
<td>true - false
</td></tr></tbody></table>



</div>
</div>

## In Tensura: Sovereign Rebirth

<span class="tsr-status">Under Validation</span>

World-scoped gamerules are treated separately from tracked TOML files. In particular, automatic enforcement of Great Sage's possession rule remains a documented release gate until the pack-owned first-world policy layer is complete.

**TSR guides:** [Great Sage](../../great-sage.md) · [Configuration Baseline](../../development/configuration-baseline.md)

---

## Source and licensing

Base Tensura reference adapted from [Config/Gamerules](https://tensura.wiki.gg/wiki/Config/Gamerules) on the Tensura: Reincarnated Wiki (revision `11489`, modified `2026-04-01T12:30:54Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
