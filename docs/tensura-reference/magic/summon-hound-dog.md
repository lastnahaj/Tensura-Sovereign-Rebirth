---
title: Summon Hound Dog
description: Summon a tamed, snake-tailed Hound Dog that obeys the caster.
---

# Summon Hound Dog

<section class="skill-detail-hero"><img src="../../../assets/illustrations/skills/summon-hound-dog.webp" alt="Summon Hound Dog illustration"><div><p class="reference-eyebrow">Magic</p><h2>A companion called from the dark.</h2><p>Summon a tamed Hound Dog that obeys its caster. The illustration represents the spell, not the in-game icon or model.</p></div></section>

<!-- skill-catalogue:start -->
<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">Magic · Pinned pack inventory</p><h2 id="how-to-obtain">How to obtain</h2><p><strong>Obtainment:</strong> The upstream <a href="../../mobs/mobs-hound-dog/">Hound Dog article</a> identifies naming a <strong>snake-tailed variant</strong> as the unlock route. Naming an ordinary Hound Dog is not described as granting this spell.</p></section>
<!-- skill-catalogue:end -->

<div class="maintained-skill-article" markdown="1">

## Acquisition evidence

- **Obtainment:** The upstream [Hound Dog article](../mobs/mobs-hound-dog.md) identifies naming a **snake-tailed variant** as the unlock route. Naming an ordinary Hound Dog is not described as granting this spell.
- **Learning limits:** This is Summoning magic, not an outcome from the unbound random aspectual-tome pool. Generic tome support does not verify a separate spell-specific tome supply route.

The pinned **post-tame event** handler checks the evolved Hound Dog variant and calls the normal skill-learning system for this spell. This confirms a taming-related learning attempt, not a promise that a failed naming event or unmet learning condition will grant it.

## Casting and upkeep

| Setting | Tracked value |
|---|---|
| Cast time | 100 ticks; 60 when mastered |
| Initial cost | 50 MP |
| Upkeep | 10 MP per second |
| Summon duration | 600 seconds |
| Cooldown | 600 seconds; 300 when mastered |

These values come from the tracked `SummonHoundDog` configuration for Minecraft 1.21.1. At the normal 20 ticks per second, the cast takes 5 seconds, or 3 when mastered. Server overrides and lag can change observed behavior.

## What it summons

The pinned implementation creates a Hound Dog with the evolved variant, tames it to a player caster, records the summoner and spell, and applies the configured duration. It suppresses experience drops from the summoned creature. A summoned companion is not evidence of a wild-mob drop or farming route.

The upstream spell article also reports that mastery reduces, but does not remove, the movement-speed penalty. That penalty's exact value is not verified here.

## Source and licensing

Spell behavior is adapted from [Summon Hound Dog](https://tensura.wiki.gg/wiki/Abilities/Magics/Summon_Hound_Dog?oldid=13734), Tensura: Reincarnated Wiki revision `13734`, reviewed September 30, 2026. Naming acquisition is described in [Hound Dog](https://tensura.wiki.gg/wiki/Mobs/Hound_Dog). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Implementation checks use Tensura 2.0.1.2: `SummonHoundDogMagic`, the `POST_TAME_EVENT` callback in `BehaviourHandler`, and the [tracked summoning configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/ability/magic/summoning_config.toml). These are source, artifact, and configuration checks, not a live-server acquisition test.

[Browse Magic](index.md) · [Magic learning guide](../../magic-learning.md)

</div>

<!-- skill-artwork-credit:start -->
Original TSR skill artwork; an illustrated interpretation, not an in-game icon.
<!-- skill-artwork-credit:end -->
