---
title: Magicule Poison
description: Magicule Poison is an effect which applies a nausea-like screen effect to the player as well as reddens the border of the screen.
tags: []
---

# Magicule Poison

<span class="reference-badge">Base Tensura reference</span> <span class="reference-category">Core Mechanics</span>

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><div class="druid-infobox druid-container" id="druid-container-1"><div><div class="druid-title">Magicule Poison</div></div><div class="druid-section-container"><div class="druid-main-image"><div><a class="image" href="https://tensura.wiki.gg/wiki/File:Magicule_poison.png"><img alt="Magicule poison.png" data-file-height="32" data-file-width="32" decoding="async" height="512" src="../../../assets/upstream/tensura/misc/magicule-poison-43e95651fa.png" width="512"/></a></div></div></div><div class="druid-section-container"><div class="druid-row druid-row-source" data-druid-section-row="main"><div class="druid-label druid-label-source">Sources</div><div class="druid-data druid-data-source druid-data-nonempty">
See <a class="mw-selflink-fragment" href="#Causes">Causes</a></div></div><div class="druid-row druid-row-particle" data-druid-section-row="main"><div class="druid-label druid-label-particle">Particle</div><div class="druid-data druid-data-particle druid-data-nonempty">
#EF054D (Red)</div></div><div class="druid-row druid-row-type" data-druid-section-row="main"><div class="druid-label druid-label-type">Type</div><div class="druid-data druid-data-type druid-data-nonempty">
Neutral</div></div></div></div>
<p>Magicule Poison is an effect which applies a nausea-like screen effect to the player as well as reddens the border of the screen.
</p>

<h2><span class="mw-headline" id="Effect">Effect</span></h2>
<ul><li>Per level, magicule poisoning does 2 damage to the player, applies a screen swirl effect like <a class="external text" href="https://minecraft.wiki/w/Nausea" rel="nofollow">Nausea</a>, and reddens the border of the screen.</li></ul>
<h2><span class="mw-headline" id="Causes">Causes</span></h2>
<ul><li>Having more than 1.25x your maximum magicules, for every 0.25x greater than that amount, the level of the effect is increased by 1.</li>
<li>Being in a high magicule area. Each player has a tolerance value, if the magicules in the area is greater than the player's EP * 4 * (tolerance + 1), then they get 1 level of magicule poisoning for every 4x the surrounding magicules is above their tolerance point.
<ul><li>The player cannot get magicule poisoning from this source if they are in the dimension that they respawn in naturally.</li></ul></li>
<li>When meeting either of the above conditions, the effect is applied for 5 seconds, refreshing every half second.</li></ul>
<h2><span class="mw-headline" id="Chunk_Magicule_Tolerance">Chunk Magicule Tolerance</span></h2>
<p>Tolerance is based on the following factors:
</p>
<ul><li>Base of 0</li>
<li>If the player is a Majin, +1</li>
<li>If the player has magic resistance, and it's active, +2</li></ul>
<p>The formula can be broken down as "T = (R + 1) • 4X", where "T" is chunk magicule tolerance, "R" is the player's current resistance (the +1 functionally represents a baseline resistance of zero), and "X" representing the player's current EP.
</p><p>For example: A slime player with an EP of 400 can tolerate a chunk magicule level of up to 3200 (or, 3200 = (1 + 1) • (4 • 400)).
</p>
<h2><span class="mw-headline" id="TIPS">TIPS</span></h2>
<p>You can check the current area's magicule level through this command.
</p>
<ul><li>/tensura worldData areaMagicule get current</li>
<li>Avoid biomes such as the Ancient Forest (Big Trees), until you have at least 5000 EP.</li></ul>



</div>
</div>

---

## Source and licensing

Base Tensura reference adapted from [Effects/Magicule Poison](https://tensura.wiki.gg/wiki/Effects/Magicule_Poison) on the Tensura: Reincarnated Wiki (revision `13046`, modified `2026-06-10T23:46:47Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
