---
title: Yuuki of Desire
---

# Yuuki of Desire

Nightmares' Yuuki encounter, named Grandmaster - Yuuki in the reference release, with Creator and Greed.

!!! warning "1.21.1 reference — server build match pending"

    Verified against Nightmares **1.0.3.2.8-neoforge-1.21.1**. The server's exact Nightmares release has not been confirmed; availability and settings can differ.

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/bosses/yuuki-of-desire.webp" alt="Yuuki of Desire encounter artwork" loading="eager" decoding="async">
<figcaption>Original TSR encounter artwork</figcaption>
</figure>

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Yuuki of Desire</div>
<div class="druid-row"><div class="druid-label">Base health</div><div class="druid-data">4,000</div></div>
<div class="druid-row"><div class="druid-label">Base spiritual health</div><div class="druid-data">6,000</div></div>
<div class="druid-row"><div class="druid-label">Base armor</div><div class="druid-data">0</div></div>
<div class="druid-row"><div class="druid-label">Base attack damage</div><div class="druid-data">45</div></div>
<div class="druid-row"><div class="druid-label">Minimum EP</div><div class="druid-data">3,500,000</div></div>
<div class="druid-row"><div class="druid-label">Maximum EP</div><div class="druid-data">4,500,000</div></div>
<div class="druid-row"><div class="druid-label">Melee dodge attribute</div><div class="druid-data">10%</div></div>
<div class="druid-row"><div class="druid-label">Projectile dodge attribute</div><div class="druid-data">10%</div></div>
<div class="druid-row"><div class="druid-label">Dodge negation attribute</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Presence sense attribute</div><div class="druid-data">155</div></div>
<div class="druid-row"><div class="druid-label">Movement speed attribute</div><div class="druid-data">0.26</div></div>
<div class="druid-row"><div class="druid-label">Follow range attribute</div><div class="druid-data">64</div></div>
</aside></div></div>

**Registry ID:** `trnightmare:sentient_boss_yuuki_desire`

## Encounter identity

This is the Nightmares entity registered as sentient_boss_yuuki_desire, not every mob named Yuuki. Its definition uses the display name Grandmaster - Yuuki and the neutral behavior profile.

The starting skill list in the definition contains Creator, Greed, Multilayer Barrier, and Ultraspeed Regeneration. Skills and encounter logic can change combat performance beyond the base attributes shown above.

## Finding the boss

In the reference release, Yuuki can replace a naturally spawning human-like mob in a biome tagged tensura:otherworlder_spawn. This is a spawn-time replacement, not a reward for killing an Otherworlder. Spawn eggs, spawners, and summoned mobs do not trigger this handler.

The default yuukiRarity setting is 50, but the handler adjusts that denominator. With sky access OR at or above sea level, the individual Yuuki roll is 1 in 12. Below sea level without sky access, it is 1 in 200. These examples assume the default setting and that the event reaches Yuuki's rule; they are not an overall encounter probability.

Pillager outposts are excluded. Nearby bosses of the same type and a local spawn cooldown can block replacement, and an earlier successful boss rule ends processing. Loaded biome tags and server settings determine eligible locations; no exact TSR biome list has been confirmed.

## Version differences

The upstream infobox lists 4,500 health, 9,000 spiritual health, 150 armor, and 190 attack. Those values differ from this reference release's entity definition and are not used in the stat card.

The numbers above describe base definition values and initial attributes, not a guarantee of final damage, difficulty, or live-server settings. This is a reference audit, not an in-game encounter test.

??? info "Sources and verification"

    [Reference release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382) · [Upstream article](https://tensuranightmares.wiki.gg/wiki/Yuuki_Of_Desire) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid=2360)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.

    Evidence classes in `com.github.hvnbael.trnightmare`:

    - `registry.main.SentientBossEntityRegistration`
    - `main.entity.sentientboss.SentientBossDefinition`
    - `main.entity.sentientboss.TrSentientBossYuukiDesireEntity`
    - `main.entity.sentientboss.AbstractTrNightmareSentientBossEntity`
    - `handler.SentientBossSpawnHandler`
    - `config.mechanic.nightmare.NightmareBossConfig`

    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Release-specific corrections and verification notes are identified above.

    Original TSR encounter artwork is used in place of the upstream article's placeholder image.

[Back to the collection](index.md)
