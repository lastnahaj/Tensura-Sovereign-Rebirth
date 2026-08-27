---
title: Damage Types
description: 'Energy Drain damage is applied when a damage source meets any of the following conditions: damage type: ENERGY_DRAIN damage type: ENERGY_SOURCE_LOST Magic damage is applied when a damage source meets any of the following conditions: has non-SPIRITUAL MagicType set msgId contains "magic" note: MAGICULE_POISON...'
tags: []
---

# Damage Types

<span class="reference-badge">Base Tensura reference</span> <span class="reference-category">Core Mechanics</span>

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en">
<h2><span class="mw-headline" id="Energy_Drain">Energy Drain</span></h2>
<p><a class="mw-selflink-fragment" href="#Energy_Drain"><span>Energy Drain</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>damage type: ENERGY_DRAIN</li>
<li>damage type: ENERGY_SOURCE_LOST</li></ul>
<h2><span class="mw-headline" id="Magic">Magic</span></h2>
<p><a class="mw-selflink-fragment" href="#Magic"><span>Magic</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>has non-SPIRITUAL MagicType set</li>
<li>msgId contains "magic"</li>
<li>note: MAGICULE_POISON is excluded</li></ul>
<h2><span class="mw-headline" id="Holy">Holy</span></h2>
<p><a class="mw-selflink-fragment" href="#Holy"><span>Holy</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == HOLY</li>
<li>msgId contains "holy"</li>
<li>msgId contains "divine"</li>
<li>damage type: HOLY_DAMAGE</li></ul>
<h2><span class="mw-headline" id="Darkness">Darkness</span></h2>
<p><a class="mw-selflink-fragment" href="#Darkness"><span>Darkness</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == DARKNESS</li>
<li>msgId contains "dark"</li>
<li>msgId contains "hell"</li>
<li>msgId contains "abyss"</li>
<li>msgId contains "ray_of_siphoning"</li>
<li>msgId contains "void"</li></ul>
<h2><span class="mw-headline" id="Earth">Earth</span></h2>
<p><a class="mw-selflink-fragment" href="#Earth"><span>Earth</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == EARTH</li>
<li>msgId contains "earth"</li>
<li>msgId contains "stone"</li>
<li>msgId contains "rock"</li>
<li>msgId contains "dirt"</li>
<li>msgId contains "magma"</li>
<li>damage type: IN_WALL</li></ul>
<h2><span class="mw-headline" id="Flame">Flame</span></h2>
<p><a class="mw-selflink-fragment" href="#Flame"><span>Flame</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == FLAME</li>
<li>damage effect == BURNING</li>
<li>msgId contains "flame"</li>
<li>msgId contains "flaming"</li>
<li>msgId contains "scorch"</li>
<li>msgId contains "burn"</li>
<li>msgId contains "blaze"</li>
<li>msgId contains "fire" (case-insensitive)</li>
<li>tag: IS_FIRE</li></ul>
<h2><span class="mw-headline" id="Light">Light</span></h2>
<p><a class="mw-selflink-fragment" href="#Light"><span>Light</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == LIGHT</li>
<li>msgId contains "light" (not "lightning")</li>
<li>msgId contains "heaven"</li>
<li>msgId contains "sun"</li>
<li>msgId contains "wisp"</li>
<li>msgId contains "paradise"</li></ul>
<h2><span class="mw-headline" id="Space">Space</span></h2>
<p><a class="mw-selflink-fragment" href="#Space"><span>Space</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == SPACE</li>
<li>msgId contains "sever"</li>
<li>msgId contains "dimension"</li>
<li>msgId contains "space"</li>
<li>msgId contains "ender"</li>
<li>msgId contains "dragon_breath"</li>
<li>msgId contains "spatial"</li></ul>
<h2><span class="mw-headline" id="Water">Water</span></h2>
<p><a class="mw-selflink-fragment" href="#Water"><span>Water</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == WATER</li>
<li>msgId contains "water"</li>
<li>msgId contains "icicle"</li>
<li>msgId contains "ice"</li>
<li>msgId contains "aqua"</li></ul>
<p><b>Note:</b> "ice" also triggers Cold.
</p>
<h2><span class="mw-headline" id="Wind">Wind</span></h2>
<p><a class="mw-selflink-fragment" href="#Wind"><span>Wind</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>element == WIND</li>
<li>msgId contains "wind"</li>
<li>msgId contains "gust"</li>
<li>msgId contains "tornado"</li></ul>
<h2><span class="mw-headline" id="Lightning">Lightning</span></h2>
<p><a class="mw-selflink-fragment" href="#Lightning"><span>Lightning</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>msgId contains "lightning"</li>
<li>msgId contains "thunder"</li>
<li>msgId contains "electric"</li>
<li>msgId contains "electrocute"</li>
<li>msgId contains "bolt" (not containing "fire")</li>
<li>tag: IS_LIGHTNING</li></ul>
<h2><span class="mw-headline" id="Gravity">Gravity</span></h2>
<p><a class="mw-selflink-fragment" href="#Gravity"><span>Gravity</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>msgId contains "blackHole"</li>
<li>msgId contains "black_hole"</li>
<li>msgId contains "oppress"</li>
<li>msgId contains "star"</li>
<li>msgId contains "gravity"</li></ul>
<h2><span class="mw-headline" id="Heat">Heat</span></h2>
<p><a class="mw-selflink-fragment" href="#Heat"><span>Heat</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>tag: IS_EXPLOSION</li>
<li>any Flame damage (superset)</li>
<li>msgId contains "hot"</li>
<li>msgId contains "warm"</li>
<li>msgId contains "heat"</li>
<li>msgId contains "hyperthermia"</li>
<li>msgId contains "megiddo"</li>
<li>damage type: LAVA</li></ul>
<p><b>Note:</b> Heat is a superset of Flame. All Flame damage is also Heat.
</p>
<h2><span class="mw-headline" id="Cold">Cold</span></h2>
<p><a class="mw-selflink-fragment" href="#Cold"><span>Cold</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>damage effect == FREEZING</li>
<li>msgId contains "cold"</li>
<li>msgId contains "ice"</li>
<li>msgId contains "frost"</li>
<li>msgId contains "freeze"</li>
<li>msgId contains "snow"</li>
<li>damage type: FREEZE</li></ul>
<h2><span class="mw-headline" id="Temperature">Temperature</span></h2>
<p><a class="mw-selflink-fragment" href="#Temperature"><span>Temperature</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>any Cold damage (superset)</li>
<li>any Heat damage (superset)</li>
<li>msgId contains "thermal"</li>
<li>msgId contains "thermia"</li>
<li>msgId contains "temperature"</li></ul>
<p><b>Note:</b> Temperature is a superset of both Heat and Cold.
</p>
<h2><span class="mw-headline" id="Poison">Poison</span></h2>
<p><a class="mw-selflink-fragment" href="#Poison"><span>Poison</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>msgId contains "poison"</li>
<li>msgId contains "venom"</li>
<li>msgId contains "toxic"</li>
<li>msgId contains "toxin"</li>
<li>note: MAGICULE_POISON is excluded</li></ul>
<h2><span class="mw-headline" id="Corrosion">Corrosion</span></h2>
<p><a class="mw-selflink-fragment" href="#Corrosion"><span>Corrosion</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>msgId contains "corrosion"</li>
<li>msgId contains "wither"</li>
<li>damage type: WITHER</li></ul>
<h2><span class="mw-headline" id="Spiritual">Spiritual</span></h2>
<p><a class="mw-selflink-fragment" href="#Spiritual"><span>Spiritual</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>tag: IS_SPIRITUAL</li>
<li>tag: IS_MENTAL</li>
<li>source marked as spiritual</li>
<li>msgId contains "soul"</li>
<li>msgId contains "spirit"</li></ul>
<h2><span class="mw-headline" id="Battlewill">Battlewill</span></h2>
<p><a class="mw-selflink-fragment" href="#Battlewill"><span>Battlewill</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>ability instance is a Battlewill skill</li>
<li>physical attack from entity with AURA_SWORD effect</li>
<li>physical attack from entity with OGRE_GUILLOTINE effect</li></ul>
<p><b>Note:</b> Same colour as <span>Holy</span>
</p>
<h2><span class="mw-headline" id="Pierce">Pierce</span></h2>
<p><a class="mw-selflink-fragment" href="#Pierce"><span>Pierce</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>projectile: arrow, spear, kunai, trident, horn</li>
<li>melee weapon item id contains "spear" or "trident"</li></ul>
<h2><span class="mw-headline" id="Physical">Physical</span></h2>
<p><a class="mw-selflink-fragment" href="#Physical"><span>Physical</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>not bypasses-invulnerability</li>
<li>not magic type set</li>
<li>not element set</li>
<li>tag: IS_PHYSICAL</li>
<li>not BYPASSES_ARMOR / IS_FIRE / IS_EXPLOSION / IS_LIGHTNING / IS_DROWNING / IS_FREEZING / THORNS</li></ul>
<h2><span class="mw-headline" id="Sound">Sound</span></h2>
<p><a class="mw-selflink-fragment" href="#Sound"><span>Sound</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>damage type: MIND_REQUIEM</li>
<li>msgId contains "music"</li>
<li>msgId contains "sound"</li>
<li>msgId contains "shockwave"</li>
<li>msgId contains "echo"</li>
<li>msgId contains "voice"</li>
<li>msgId contains "sonic"</li></ul>
<p><b>Note:</b> No dedicated colour in getDamageColor — uses <span>default</span>.
</p>
<h2><span class="mw-headline" id="Abnormal">Abnormal</span></h2>
<p><a class="mw-selflink-fragment" href="#Abnormal"><span>Abnormal</span></a> damage is applied when a damage source meets any of the following conditions:
</p>
<ul><li>msgId contains "petrification"</li>
<li>msgId contains "petrificate"</li>
<li>msgId contains "insane"</li>
<li>msgId contains "insanity"</li>
<li>msgId contains "virus"</li>
<li>msgId contains "infection"</li>
<li>msgId contains "fear"</li>
<li>msgId contains "scare"</li></ul>
<p><b>Note:</b> No dedicated colour in getDamageColor — uses <span>default</span>.
</p>



</div>
</div>

---

## Source and licensing

Base Tensura reference adapted from [Damage Types](https://tensura.wiki.gg/wiki/Damage_Types) on the Tensura: Reincarnated Wiki (revision `12882`, modified `2026-05-12T17:08:41Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
