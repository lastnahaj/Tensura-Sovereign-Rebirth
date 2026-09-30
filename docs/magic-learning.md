---
title: Magic Learning & Spell Schools
description: Choose a spell school, understand tome learning, and check the difference between acquisition, mastery, and casting costs.
hide:
  - navigation
---

<div class="battlewill-guide magic-learning-guide" markdown="1">
<header class="skill-directory-heading"><p class="reference-eyebrow">Spellcraft · Minecraft 1.21.1</p><h1>Find your spell.<br>Understand its conditions.</h1><p>A spell's casting cost is not its acquisition requirement. Start with the correct school, check its obtainment evidence, then learn how it behaves before investing in mastery.</p><a class="reference-directory-overview-link" href="../tensura-reference/magic/">Browse the spell directory →</a></header>

## Choose your school

<div class="skill-reading-guide">
<div><span>01</span><h3>Aspectual</h3><p>Elemental, healing, movement, and utility spells. A Magic Tome with no stored spell chooses from the aspectual-magic tag; that is not a roll across every school.</p></div>
<div><span>02</span><h3>Spiritual</h3><p>Spells grouped by their spiritual level and element. Check the spell's own entry for its tier, requirements, controls, and cost. Do not assume an aspectual random tome can teach it.</p></div>
<div><span>03</span><h3>Summoning</h3><p>Spells that summon creatures or other entities. Read the individual reference for the summon, resource cost, and behavior; registration alone does not establish a reward or racial unlock.</p></div>
</div>

## How Magic Tomes work

| Tome state | Checked behavior | What it does not prove |
|---|---|---|
| Stored spell | Uses the recorded ability ID and attempts learning through the normal skill-learning system | Where a tome for that specific spell can be obtained, or whether all learning conditions are met |
| No stored spell | Randomly selects from the aspectual-magic tag | A random result from Spiritual or Summoning magic, or the separate Skill Study Book pool |
| Duplicate or failed learning | Can still consume the tome and apply its survival cooldown | A guaranteed new spell from every use |

The pinned item implementation requires at least **10 ticks of use before release** and applies a **200-tick survival cooldown** after a resolved attempt. At the normal 20 ticks per second these are 0.5 seconds and 10 seconds; server lag changes real elapsed time. Infinite-material players do not consume the item or receive this cooldown.

The [upstream Magic Tome article](tensura-reference/magic/magic-tome.md) lists Wizard Towers as a supply source. That is a general item reference, **not a verified drop table for every spell**, and loot settings can change availability.

## Copying mastered magic

The [Unbound Tome reference](tensura-reference/items/unbound-tome.md) describes placing mastered magic into a tome for another player to learn. The source article is unfinished. Copy exclusions, spell-specific eligibility, and a complete supply route have not been verified in this guide; do not assume every mastered spell can be copied.

## Read an entry before committing resources

1. **How to obtain:** distinguish a source-described racial, tome, or other route from an explicitly unverified route.
2. **Cast time and resource cost:** these control using a spell, not obtaining it. MP cost is not an EP learning threshold.
3. **Effect and controls:** check range, targeting, charge behavior, and damage type.
4. **Mastery bonus:** an improved effect is not automatically an unlock for another spell. Follow a successor only when that connection is documented.

!!! warning "Similar names are different abilities"
    The **Possession spell** and **Possession skill** have different registry IDs. The same applies to the **Strength spell** and **Strength skill**, and to Aspectual versus Spiritual Fire and Water. Their requirements and effects must not be merged.

## Scope and sources

The spell directory follows the tracked 1.21.1 registry inventory and spell infoboxes. Items, bottles, crystals, masks, staffs, and schematics remain item references; they are not spell cards. Magic Resistance belongs in Resistances. Command-only Magic Nullification and unmatched Spatial Void remain reference-only.

[Tome implementation review](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/magic_reference.json) · [Tracked ability inventory](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura_skill_books/tensura_skill_books-random-skills.txt) · [Magic Tome source](https://tensura.wiki.gg/wiki/Magic_Tome) · [Unbound Tome source](https://tensura.wiki.gg/wiki/Unbound_tome) · [All sources and media attribution](project/sources-and-attribution.md).

These are artifact, configuration, and cited-source checks—not a live-server acquisition test. Iron's Spells integration is described separately in the [TSR magic overview](magic.md).

</div>
