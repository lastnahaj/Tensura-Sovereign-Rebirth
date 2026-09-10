---
title: Quests & Reincarnation Essence
description: How SlimeThrone Extras quests and Reincarnation Essence support prestige in TSR 1.21.1.
---

# Quests & Reincarnation Essence

SlimeThrone Extras supplies TSR's repeatable progression objectives and its Reincarnation Essence (RE) system. RE is a prestige requirement: earning it is part of preparing a finished character for the next reincarnation rather than a replacement for EP or skill mastery.

<section class="quest-pool-stats" aria-label="Installed SlimeThrone Extras quest definitions">
  <article><strong>229</strong><span>Daily definitions</span></article>
  <article><strong>47</strong><span>Weekly definitions</span></article>
  <article><strong>688</strong><span>Required definitions</span></article>
  <article><strong>18</strong><span>Repeatable definitions</span></article>
  <article><strong>18</strong><span>Race-prestige definitions</span></article>
</section>

These are the **1,000 quest-definition files available to the installed system**, not 1,000 simultaneous assignments. The mod selects and tracks the objectives appropriate to the player and progression state.

## Quest types

<section class="progression-system-grid progression-system-grid--compact">
  <article><span class="progression-system-grid__icon">☀</span><h3>Daily</h3><p>Short-cycle objectives. The system can assign 1–3 daily quests from the installed pool.</p></article>
  <article><span class="progression-system-grid__icon">◫</span><h3>Weekly</h3><p>Longer objectives. The system can assign 3–5 weekly quests from its weekly pool.</p></article>
  <article><span class="progression-system-grid__icon">◆</span><h3>Required</h3><p>Progression conditions that must be completed for the relevant prestige route.</p></article>
  <article><span class="progression-system-grid__icon">↻</span><h3>Repeatable</h3><p>Reusable objectives that support the continuing progression loop.</p></article>
  <article><span class="progression-system-grid__icon">♜</span><h3>Race prestige</h3><p>One-time, race-specific challenges that award 3–5 Soul Grade when completed with a prestige.</p></article>
</section>

The installed pools cover actions such as defeating creatures or bosses, mastering skills, gathering or crafting items, mining resources, naming subordinates, and reaching progression states. Always follow the objective shown in the current interface; similar-sounding targets are not interchangeable.

## Preparing RE for prestige

1. Open the SlimeThrone Extras progression or quest interface and read the current assignments.
2. Complete daily, weekly, and relevant repeatable objectives while developing the character.
3. Track the RE total against the prestige requirement shown for the current route.
4. Finish required quests and boss objectives; RE alone does not complete the prestige checklist.
5. Confirm maximum evolution, awakening, skill locks, and the Character Reset Scroll before resetting.

!!! tip "Treat RE, EP, and Soul Grade as different resources"
    **RE** qualifies the character for reincarnation, **EP** tracks broad character power and is part of the skill-lock cost, and **Soul Grade** is permanent prestige progression that controls normal lock capacity.

## Race-prestige quest timing

TSR currently has `ImmediateRaceQuests = false`. Race-prestige objectives therefore wait until the race reaches maximum evolution and the relevant progression trigger. The configured reroll mode is `NONE`, so do not plan around freely replacing an unwanted race-prestige set.

## RE scaling in TSR

The current server configuration increases RE rewards by **5% per prestige** for daily and weekly quests. Required and repeatable quest RE rewards do not receive that prestige scaling. Duplicate-like assignments are skipped when possible, and matching daily, weekly, required, or race-prestige objectives take priority over repeatable tracking for the same progression event.

[Search the race-prestige objectives →](race-prestige-requirements.md){ .md-button .md-button--primary }
[Open the prestige checklist →](prestige-and-soul-grade.md){ .md-button }

## Verification

Quest counts and behavior were checked against TSR's exact `SlimeThroneExtras-neoforge-2.1.2.1.jar` and current configuration. The system overview is also documented by the [official SlimeThrone Quests & RE guide](https://slimethrone.net/help/articles/17/system-quests-and-re/) and [SlimeThrone Extras project page](https://modrinth.com/mod/tensura-slimethrone-extras).
