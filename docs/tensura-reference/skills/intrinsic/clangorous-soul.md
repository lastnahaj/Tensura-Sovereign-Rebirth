---
title: Clangorous Soul
description: An area taunt granted by the Hardshell Ant evolution line.
---

<section class="skill-detail-hero"><img src="../../../../assets/icons/skills/mysticism-clangorous_soul.svg" alt="Clangorous Soul emblem"><div><p class="reference-eyebrow">Intrinsic Skills</p><h1>Clangorous Soul</h1><p>An area taunt granted by the Hardshell Ant evolution line.</p></div></section>

[Browse Intrinsic Skills](index.md)

<!-- skill-catalogue:start -->
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Intrinsic Skills · Pinned pack inventory</p><h2 id="how-to-obtain">How to obtain</h2><p><strong>Obtainment:</strong> Granted starting at <strong>Hardshell Ant Insectar</strong>. The pinned Ant race configuration also grants it to <strong>Hardshell Ant Savant</strong>, <strong>Earth Soul Insect</strong>, and <strong>Divine Hardshell Ant</strong>.</p></section>
<!-- skill-catalogue:end -->

<div class="maintained-skill-article" markdown="1">

**Obtainment:** Granted starting at **Hardshell Ant Insectar**. The pinned Ant race configuration also grants it to **Hardshell Ant Savant**, **Earth Soul Insect**, and **Divine Hardshell Ant**.

## Use

Press the skill to draw nearby eligible mobs' attention. It changes their attack target to you and activates aggression; it does not control other players. Allied, dead, and non-attackable entities are excluded.

| Setting | Unmastered | Mastered |
| --- | --- | --- |
| Configured taunt range | 10 blocks | 15 blocks |
| Cooldown | 60 seconds | 45 seconds |

The implementation searches an expanded bounding box, rather than measuring a spherical radius. It awards mastery progress and applies the cooldown when eligible entities are found.

</div>

## Evidence

Documented from `ClangorousSoulSkill` in [Mysticism 2.1.2 for NeoForge 1.21.1](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529), the [skill configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/mysticism/ability/skill/intrinsic_config.toml), and the [Ant race configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/mysticism/race/insect/ant_config.toml). These are implementation and configuration checks, not a live-server playtest. Artwork: TSR skill emblem.
