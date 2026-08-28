---
title: Config
description: In order to access the config, first go to your modpack/profile's directory (this is the one that contains folders for mods, logs, crash reports, the config, etc.) and then to the config folder. Then, go to the mysticism folder. From here, you can use the collapsible list below to navigate the config...
tags:
- Work_in_Progress
---

# Config

<span class="reference-badge">TR Mysticism reference</span> <span class="reference-category">Configuration</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/upstream/mysticism/races/mysticism-wip-6c2780ef0a.png" alt="Config source reference" loading="eager" decoding="async">
<figcaption><a href="https://trmysticism.wiki.gg/wiki/File:Mysticism_WIP.png">Mysticism WIP.png · CC BY-SA 4.0</a></figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>In order to access the config, first go to your modpack/profile&#x27;s directory (this is the one that contains folders for mods, logs, crash reports, the config, etc.) and then to the config folder. Then, go to the mysticism folder. From here, you can use the collapsible list below to navigate the config with summaries of what is in each file/folder. Some…</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#Accessing_and_Editing_the_Config">Accessing and Editing the Config</a>
<a href="#Config_Guide">Config Guide</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><div>
<table border="0" cellpadding="0">
<tbody><tr>
<td><a class="image reference-overview-duplicate" href="https://trmysticism.wiki.gg/wiki/File:Mysticism_WIP.png"><img alt="Work In Progress" data-file-height="128" data-file-width="128" decoding="async" height="102" loading="lazy" src="../../../assets/upstream/mysticism/races/mysticism-wip-6c2780ef0a.png" width="102"/></a>
</td>
<td><span> <b>Work In Progress.</b></span><br/> <i>This page is currently being worked on or has unfinished information.<br/>  Click <a class="text" href="./">here</a> in order to contribute to this article.</i>
</td></tr></tbody></table></div>
<h2><span class="mw-headline" id="Accessing_and_Editing_the_Config">Accessing and Editing the Config</span></h2>
<p>In order to access the config, first go to your modpack/profile's directory (this is the one that contains folders for mods, logs, crash reports, the config, etc.) and then to the config folder. Then, go to the mysticism folder. From here, you can use the collapsible list below to navigate the config with summaries of what is in each file/folder. Some advice for editing the config has also been provided below.
</p>
<ul><li>Make sure the game is closed while editing the config.</li>
<li>Before closing a file, save your changes with ctrl+s.</li>
<li>Lines in the config with a # at the beginning are comments. They describe what the config value below them does.</li></ul>
<p><br/>
</p>
<h2><span class="mw-headline" id="Config_Guide">Config Guide</span></h2>
<p>This section is meant to let you explore the config in a more user-friendly way than file explorer and dwindling hope. Sections that just have a name are folders which contain either more folders, files, or a combination of both, and ones with .toml at the end of the name are files, which actually have values that can be changed.
</p>
<div class="collapsible-header">ability</div>
<div class="collapsible-content">
<p>This includes config options related to abilities. It currently only has the skills folder, though could later contain other folders if/when non-skill abilities are added.
</p>
<div class="collapsible-header">skill</div>
<div class="collapsible-content">
<p>This includes config options related to skills. This includes costs, cooldowns, obtainment requirements, damage, etc. Contains three files separating skills by type
</p>
<div class="collapsible-header">extra_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to extra skills.
</p>
</div>
<div class="collapsible-header">intrinsic_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to intrinsic skills.
</p>
</div>
<div class="collapsible-header">unique_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to unique skills.
</p>
</div>
</div>
</div>
<div class="collapsible-header">effect</div>
<div class="collapsible-content">
<p>This includes config options related to effects. As of writing, this only has one file, with two values, both relating to brimstone flames.
</p>
<div class="collapsible-header">effects.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to effects. As of writing, this file has two values, both relating to brimstone flames.
</p>
</div>
</div>
<div class="collapsible-header">entity</div>
<div class="collapsible-content">
<p>This includes config options related to entities. As of writing, this only has one file, with one value determining how often the Memoires otherworlder spawns in the spirit world.
</p>
<div class="collapsible-header">spawn_rate_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to effects. As of writing, this file has one value determining how often the Memoires otherworlder spawns in the spirit world.
</p>
</div>
</div>
<div class="collapsible-header">race</div>
<div class="collapsible-content">
<p>This includes config options related to races. It currently has folders for the direwolf and insect related config files, and files for the rest of the races. Here you can configure evolution requirements and stats. Keep in mind that most of the stats inside files are modifiers applied to the player, so it's useful to know the base values of stats (See below).
HP=20, SHP=60, Size=1, Attack=1, Attack Speed=4, Knockback Resistance=0, Movement Speed=0.1, Swimming Speed = 0.1(?), Step Height=0.6
</p>
<div class="collapsible-header">direwolf</div>
<div class="collapsible-content">
<p>This includes config options related to the Direwolf race.
</p>
<div class="collapsible-header">direwolf_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Direwolf races: Direwolf, Black Fang, Blue Fang, Brown Fang, Green Fang, Purple Fang, Red Fang, their evolutions, and Divine Wolf.
</p>
</div>
<div class="collapsible-header">special_direwolf_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the "special" Direwolf races: Blaze Fang, Darkness Fang, Frost Fang, Guitar Wolf, Light Fang, Star Wolf, and their evolutions, excluding Divine Wolf.
</p>
</div>
</div>
<div class="collapsible-header">insect</div>
<div class="collapsible-content">
<p>This includes config options related to the Insect races.
</p>
<div class="collapsible-header">ant_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Ant race and its evolutions.
</p>
</div>
<div class="collapsible-header">beetle_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Beetle race and its evolutions.
</p>
</div>
<div class="collapsible-header">centipede_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Centipede race and its evolutions.
</p>
</div>
<div class="collapsible-header">mantis_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Mantis race and its evolutions.
</p>
</div>
<div class="collapsible-header">scorpion_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Scorpion race and its evolutions.
</p>
</div>
<div class="collapsible-header">wasp_config.toml</div>
<div class="collapsible-content">
<p>		  This file contains options related to the Wasp race and its evolutions.
</p>
</div>
</div>
<div class="collapsible-header">angel_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Angel race and its evolutions. Also includes the Fallen Angel, Fallen, and Tengu variants.
</p>
</div>
<div class="collapsible-header">daemon_doll_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Daemon Doll race and its evolutions. Also includes the Chaos Doll variant.
</p>
</div>
<div class="collapsible-header">dragonoid_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Dragonoid race and its evolutions. For this file, you change the minimum and maximum EP used for its scaling and what the highest boosts should be once you've reached the max EP. You can also change its starting MP/AP range and base stat modifiers if you wish.
</p>
</div>
<div class="collapsible-header">elemental_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Lesser Elemental race and its evolutions. Also includes the Majin Elemental Lord variant.
</p>
</div>
<div class="collapsible-header">forgotten_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Forgotten race and its evolutions. Includes both paths.
</p>
</div>
<div class="collapsible-header">phantom_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Phantom race and its evolutions.
</p>
</div>
<div class="collapsible-header">restricted_human_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Restricted Human race and its evolutions.
</p>
</div>
<div class="collapsible-header">wyrm_config.toml</div>
<div class="collapsible-content">
<p>	 This includes config options related to the Attuned Wyrm race and its evolutions. Includes both paths.
</p>
</div>
</div>
<div class="collapsible-header">general.toml</div>
<div class="collapsible-content">
<p>This file includes miscellaneous config options. As of writing, this file has two values determining if Mysticism's config changes should be reapplied and how fast the flying speed is for races.
</p>
</div>



</div>
</div>

---

## Source and licensing

TR Mysticism reference adapted from [Config](https://trmysticism.wiki.gg/wiki/Config) on the Tensura Reincarnated: Mysticism Wiki (revision `2889`, modified `2026-04-18T07:23:02Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

<details class="reference-media-credits">
<summary>Media credits (1 source files)</summary>
<ul>
<li><a href="https://trmysticism.wiki.gg/wiki/File:Mysticism_WIP.png">Mysticism WIP.png</a> — CC BY-SA 4.0; uploaded by Velo; revision 666</li>
</ul>
</details>
