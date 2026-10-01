---
title: Caster Tools Tutorial
description: Caster Tools include grimoires and staffs, storing spells and enabling their use through the tool. Caster tools can have spells applied to them through the use of the Spellbinding Table. These magics can then be used from the tool, even if the user does not have that magic unlocked(with some exceptions...
tags:
---

# Caster Tools Tutorial

<span class="reference-badge">Base Tensura reference</span> <span class="reference-category">Tools</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/items/low-magic-staff.webp" alt="Original casting staff illustration" loading="eager" decoding="async">
<figcaption>TSR illustration · casting staff example</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Caster Tools include grimoires and staffs, storing spells and enabling their use through the tool.</p>
<nav class="reference-quick-jumps" aria-label="Article sections">
<a href="#What_are_Caster_Tools.3F">What are Caster Tools?</a>
<a href="#How_do_Caster_Tools_work.3F">How do Caster Tools work?</a>
</nav>
<div class="reference-reading-controls" role="group" aria-label="Article reading mode">
<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>
<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>
</div>
</div>
</section>

<div class="tensura-reference-article">
<div class="mw-content-ltr mw-parser-output" dir="ltr" lang="en"><h1><span class="mw-headline" id="Caster_Tools">Caster Tools</span></h1>
<h2><span id="What_are_Caster_Tools.3F"></span><span class="mw-headline" id="What_are_Caster_Tools?">What are Caster Tools?</span></h2>
<p>Caster Tools include grimoires and staffs, storing spells and enabling their use through the tool.
</p>
<p>For checked staff capacities, ingredients, schematic obtainment, and learning behavior, see the <a href="../../items/magic-staves/">casting-staff guide</a>. The following adapted explanation preserves the upstream reference; spell-specific cost multipliers and reset retention have not been verified for the live server.</p>
<h2><span id="How_do_Caster_Tools_work.3F"></span><span class="mw-headline" id="How_do_Caster_Tools_work?">How do Caster Tools work?</span></h2>
<p>Caster tools store spells through the <a href="../../resistances/spellbinding-table/" title="Spellbinding Table">Spellbinding Table</a>. Eligible stored spells can be used without learning the spell, but the exclusions below still apply. Storing a spell does not teach it to your character. Reset-scroll and prestige retention have not been verified.</p>
<p>In the checked configuration, an unlearned cast multiplies both Aura and Magicule cost inputs by 5.0 and the normal chant input by 2.0 before further modifiers. These are not guarantees of final resource cost or elapsed cast time; attributes, spell behavior, and the instant-cast path can change the result.
</p>
<h3><span class="mw-headline" id="Magics_that_require_learning_to_use">Magics that require learning to use</span></h3>
<ul><li>All <a href="../../magic/abilities-magics/" title="Abilities/Magics"> Spiritual Magics</a></li>
<li><a href="../../magic/summon-medium-elemental/" title="Summon Medium Elemental"> Summon Medium Elemental</a></li>
<li><a href="../../magic/summon-greater-elemental/" title="Summon Greater Elemental"> Summon Greater Elemental</a></li>
<li><a href="../../magic/summon-otherworlder/" title="Summon Otherworlder"> Summon Otherworlder</a></li>
<li><a href="../../magic/spatial-storage/" title="Spatial Storage"> Spatial Storage</a></li>
<li><a href="../../magic/aspectual-possession/" title="Possession">Possession</a></li>
<li><a href="../../core-mechanics/reincarnation/" title="Reincarnation"> Reincarnation</a></li></ul>



</div>
</div>

<section class="reference-related">
<div class="reference-related-heading">
<h2>Continue exploring</h2>
<a href="../">Browse all Tools</a>
</div>
<div class="reference-related-grid">
<a class="reference-related-card" href="../adamantite-shovel/">
<img src="../../../assets/upstream/tensura/items/invicon-adamantite-shovel-3173ebb180.png" alt="" loading="lazy" decoding="async">
<span class="reference-related-copy">
<strong>Adamantite Shovel</strong>
<small>Obtainable through killing mobs while having Pure Magisteel Shovel in your offhand or equipped</small>
</span>
</a>
<a class="reference-related-card" href="../high-magisteel-axe/">
<img src="../../../assets/upstream/tensura/items/invicon-high-magisteel-axe-5d326d07af.png" alt="" loading="lazy" decoding="async">
<span class="reference-related-copy">
<strong>High Magisteel Axe</strong>
<small>Obtainable through killing mobs while having Low Magisteel Axe in your offhand or equipped</small>
</span>
</a>
<a class="reference-related-card" href="../adamantite-pickaxe/">
<img src="../../../assets/upstream/tensura/items/invicon-adamantite-pickaxe-30d9b4339b.png" alt="" loading="lazy" decoding="async">
<span class="reference-related-copy">
<strong>Adamantite Pickaxe</strong>
<small>Obtainable through killing mobs while having Pure Magisteel Pickaxe in your offhand or equipped</small>
</span>
</a>
<a class="reference-related-card" href="../high-magisteel-hoe/">
<img src="../../../assets/upstream/tensura/items/invicon-high-magisteel-hoe-f88f8f2d38.png" alt="" loading="lazy" decoding="async">
<span class="reference-related-copy">
<strong>High Magisteel Hoe</strong>
<small>Obtainable through killing mobs while having Low Magisteel Hoe in your offhand or equipped</small>
</span>
</a>
</div>
</section>

---

## Source and licensing

Base Tensura reference adapted from [Caster Tools Tutorial](https://tensura.wiki.gg/wiki/Caster_Tools_Tutorial) on the Tensura: Reincarnated Wiki (revision `12819`, modified `2026-05-07T07:49:02Z`). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Casting costs and exclusions were checked against the [selected Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599), `SimpleSpellCastItem.getMagicInstance`, `Magic.getCastingTime`, `Magic.isOutOfEnergy`, `data/tensura/tags/manascore_skill/skills/unlearnt_cast_excluded.json`, and TSR's [magic configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/ability/magic_config.toml). These are artifact and configuration checks, not live-server gameplay tests.
