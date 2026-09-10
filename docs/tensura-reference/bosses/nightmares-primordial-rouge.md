---
title: Primordial Rouge
---

# Primordial Rouge

The Nightmares Primordial Rouge / Gii Crimson boss encounter, distinct from the similarly named playable race.

!!! warning "1.21.1 reference — server build match pending"

    Verified against Nightmares **1.0.3.2.8-neoforge-1.21.1**. The server's exact Nightmares release has not been confirmed; availability and settings can differ.

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/bosses/primordial-rouge.webp" alt="Primordial Rouge encounter artwork" loading="eager" decoding="async">
<figcaption>Original TSR encounter artwork</figcaption>
</figure>

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Primordial Rouge</div>
<div class="druid-row"><div class="druid-label">Base health</div><div class="druid-data">850</div></div>
<div class="druid-row"><div class="druid-label">Base spiritual health</div><div class="druid-data">5,500</div></div>
<div class="druid-row"><div class="druid-label">Base armor</div><div class="druid-data">40</div></div>
<div class="druid-row"><div class="druid-label">Base attack damage</div><div class="druid-data">15</div></div>
<div class="druid-row"><div class="druid-label">Minimum EP</div><div class="druid-data">1,500,000</div></div>
<div class="druid-row"><div class="druid-label">Maximum EP</div><div class="druid-data">6,666,666</div></div>
<div class="druid-row"><div class="druid-label">Melee dodge attribute</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Projectile dodge attribute</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Dodge negation attribute</div><div class="druid-data">75%</div></div>
<div class="druid-row"><div class="druid-label">Presence sense attribute</div><div class="druid-data">155</div></div>
<div class="druid-row"><div class="druid-label">Movement speed attribute</div><div class="druid-data">0.28</div></div>
<div class="druid-row"><div class="druid-label">Follow range attribute</div><div class="druid-data">96</div></div>
</aside></div></div>

**Registry ID:** `trnightmare:sentient_boss_gii_crimson`

## Encounter identity

This page covers the boss registered as sentient_boss_gii_crimson. The reference release's friendship label identifies him as Primordial Rouge - Gii Crimson; the boss definition names him Primordial Rouge.

The similarly named race and boss are distinct registry entries. This encounter is not a race-evolution step.

The boss implementation includes Pride-related skill handling and summoned red Arch Daemons. Its combat mechanics can change the encounter beyond the base attributes shown above.

## Finding the boss

In the reference release, Primordial Rouge can replace a naturally spawning Tensura Lesser Daemon, Greater Daemon, or Arch Daemon in a biome tagged tensura:is_hell. This is a spawn-time replacement, not a drop or an evolution. Spawn eggs, spawners, and summoned daemons do not trigger this handler.

The default crimsonRarity setting is 25,000. With sky access OR at or above sea level, the individual Rouge roll is 1 in 6,250. Below sea level without sky access, it is 1 in 100,000. These are default per-eligible-event rolls, not a guaranteed waiting time or a live-server rate.

Pillager outposts are excluded. Nearby bosses of the same type and a local spawn cooldown can block replacement. The reviewed upstream article leaves spawning blank; this route comes from the release's spawn handler. Loaded biome tags and server settings determine eligible locations.

## Version differences

The upstream infobox lists 12,000 health, 24,000 spiritual health, 25 armor, 70 attack, and an EP range of 7,000,000–7,700,000. Those values differ from this reference release's entity definition and are not used in the stat card.

These are base definition values and initial attributes, not final phase statistics or a prediction of actual damage. The encounter has additional mechanics; this is a reference audit, not an in-game encounter test.

??? info "Sources and verification"

    [Reference release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382) · [Upstream article](https://tensuranightmares.wiki.gg/wiki/Primordial_Rouge) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid=2361)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.

    Evidence classes in `com.github.hvnbael.trnightmare`:

    - `registry.main.SentientBossEntityRegistration`
    - `main.entity.sentientboss.SentientBossDefinition`
    - `main.entity.sentientboss.TrSentientBossGiiCrimsonEntity`
    - `main.entity.sentientboss.AbstractTrNightmareSentientBossEntity`
    - `handler.SentientBossSpawnHandler`
    - `config.mechanic.nightmare.NightmareBossConfig`

    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Release-specific corrections and verification notes are identified above.

    Original TSR encounter artwork is used in place of the upstream article's placeholder image.

[Back to the collection](index.md)
