---
title: Prestige, Soul Grade & Skill Locking
description: Exact prestige requirements, Soul Grade tiers, and skill-lock rules for TSR's installed SlimeThrone Extras build.
---

<section class="progression-guide-hero progression-guide-hero--compact">
  <img src="../assets/images/guides/prestige-progression.webp" alt="A spirit approaching a radiant reincarnation gate" loading="eager" decoding="async">
  <div class="progression-guide-hero__shade"></div>
  <div class="progression-guide-hero__copy">
    <p class="reference-eyebrow">SlimeThrone Extras 2.1.2.1</p>
    <h1>Prestige without losing the plan</h1>
    <p>Prestige converts a completed character route into permanent Soul Grade. Skill locking lets you protect a limited number of eligible mastered skills before the reset.</p>
  </div>
</section>

## Prestige checklist

<ol class="prestige-steps">
  <li><b>1</b><div><strong>Reach maximum evolution</strong><span>Finish the evolution route for the character you are prestiging.</span></div></li>
  <li><b>2</b><div><strong>Awaken</strong><span>Become awakened or reach True Demon Lord status.</span></div></li>
  <li><b>3</b><div><strong>Meet the RE target</strong><span>Accumulate the required Reincarnation Essence shown by the prestige interface.</span></div></li>
  <li><b>4</b><div><strong>Complete required objectives</strong><span>Finish the required quests and required boss kills for the route.</span></div></li>
  <li><b>5</b><div><strong>Lock selected skills</strong><span>Spend the required EP and Soul Grade on eligible skills you want to retain.</span></div></li>
  <li><b>6</b><div><strong>Use a Character Reset Scroll</strong><span>Only reset after the interface confirms that every condition is complete.</span></div></li>
</ol>

Normal prestige grants **1 Soul Grade**. A race prestige can be completed once for each supported race and grants **3–5 Soul Grade**, but it still requires the normal prestige conditions.

## Soul Grade and lock capacity

Enter your current Soul Grade to see the maximum number of normal skill locks available at that tier.

<section class="soul-grade-calculator" data-soul-grade-calculator>
  <label for="soul-grade-input">Current Soul Grade</label>
  <div class="soul-grade-calculator__controls">
    <input id="soul-grade-input" type="number" min="0" step="1" value="0" inputmode="numeric" data-soul-grade-input>
    <output data-soul-grade-output aria-live="polite"><strong>0 locks</strong><span>Unranked · Soul Grade 0–10</span></output>
  </div>
  <div class="soul-grade-meter" aria-hidden="true"><span data-soul-grade-meter></span></div>
</section>

| Soul Grade | Rank | Maximum normal locks |
|---:|---|---:|
| 0–10 | Unranked | 0 |
| 11–20 | Low | 1 |
| 21–30 | Medium | 1 |
| 31–40 | High | 2 |
| 41–50 | Greater | 2 |
| 51–60 | Grand | 2 |
| 61+ | Supreme | 3 |

## How skill locking works

<section class="skill-lock-facts">
  <article><strong>10,000,000 EP</strong><span>Required by TSR to unlock one eligible skill lock.</span></article>
  <article><strong>3 Soul Grade</strong><span>Spent to unlock one eligible skill lock.</span></article>
  <article><strong>Up to 3</strong><span>Normal lock slots at Supreme rank.</span></article>
</section>

A locked skill is retained when the character resets. Locking is limited by your Soul Grade tier and by the mod's allowlist; it is not a way to preserve every skill. TSR currently sets `ignoreLockedSkillsOnReset = false`, so the reset flow honors properly locked skills.

!!! warning "Lock before resetting"
    A Character Reset Scroll starts the reset. Open the skill-lock interface first, verify that the intended skills show as locked, and only then perform the prestige.

<details>
<summary><strong>Eligible skill-lock list in TSR's current configuration</strong></summary>

Absolute Severance, Analyst, Berserk, Berserker, Bewilder, Chef, Chosen One, Commander, Cook, Creator, Degenerate, Engorger, Envy, Falsifier, Fighter, Fusionist, Gourmand, Gourmet, Great Sage, Greed, Guardian, Healer, Imitator, Infinity Prison, Lust, Martial Master, Mathematician, Merciless, Murderer, Musician, Observer, Oppressor, Predator, Pride, Reaper, Reflector, Researcher, Reverser, Royal Beast, Seeker, Seer, Severer, Shadow Striker, Sloth, Sniper, Spearhead, Suppressor, Survivor, Thrower, Traveler, Tuner, Unyielding, Usurper, Villain, and Wrath.

</details>

The configuration also names Predator, Gourmet, and Pride in its reset-skill-data compatibility list. That setting is currently disabled (`RestSkillData = false`), so it should not be mistaken for three additional guaranteed preservation slots.

## Race prestige

Race prestige quests do not appear immediately in TSR. The current pack sets `ImmediateRaceQuests = false`, so a race's questline begins after reaching maximum evolution and its progression trigger. No race-prestige races are disabled, and completed prestige boss kills may be counted again where the system permits it.

<details>
<summary><strong>Bosses currently accepted for normal prestige objectives</strong></summary>

Charybdis, Elemental Colossus, Hinata Sakaguchi, Orc Disaster, Shizu, Supermassive Slime, Carrion, Luminous Valentine, and Rimuru's Ogre Fight encounter. TSR allows repeated kills of an accepted boss to count toward prestige boss requirements.

</details>

[Search all 18 race-prestige requirements →](race-prestige-requirements.md){ .md-button .md-button--primary }
[Read about quests and Reincarnation Essence →](quests-and-reincarnation-essence.md){ .md-button }

## Verification

The values on this page were checked against TSR's exact `SlimeThroneExtras-neoforge-2.1.2.1.jar` and shipped `stextras` configuration. The public system explanations are available in the [SlimeThrone Prestige & Soul Grade guide](https://slimethrone.net/help/articles/18/system-prestiging-and-soul-grade/), [Race Prestige guide](https://slimethrone.net/help/articles/19/extra-race-prestige-requirements/), and [Quests & RE guide](https://slimethrone.net/help/articles/17/system-quests-and-re/).
