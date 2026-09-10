---
title: Soul Essence
---

# Soul Essence

A Nightmares evolution material awarded by completed Direwolf and Daemon raids in the reviewed 1.21.1 release.

!!! warning "1.21.1 reference — server build match pending"

    Verified against Nightmares **1.0.3.2.8-neoforge-1.21.1**. The server's exact Nightmares release has not been confirmed; availability and settings can differ.

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../../../assets/images/items/nightmares-soul-essence.webp" alt="Soul Essence item artwork" loading="eager" decoding="async">
<figcaption>Original TSR item artwork</figcaption>
</figure>

<div class="tensura-reference-article">
<div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Soul Essence</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura Nightmares</div></div>
<div class="druid-row"><div class="druid-label">Direwolf raid reward</div><div class="druid-data">100%</div></div>
<div class="druid-row"><div class="druid-label">Direwolf raid amount</div><div class="druid-data">1–3</div></div>
<div class="druid-row"><div class="druid-label">Daemon raid reward</div><div class="druid-data">50%</div></div>
<div class="druid-row"><div class="druid-label">Daemon raid amount</div><div class="druid-data">1–2</div></div>
<div class="druid-row"><div class="druid-label">Rewarded to</div><div class="druid-data">Nearby players</div></div>
<div class="druid-row"><div class="druid-label">Nutrition when eaten</div><div class="druid-data">4</div></div>
<div class="druid-row"><div class="druid-label">Saturation modifier</div><div class="druid-data">0.3</div></div>
</aside></div></div>

**Registry ID:** `trnightmare:soul_essence`

## How to obtain

Complete a Nightmares Direwolf raid while inside its reward area. Each nearby player receives an independent 100% Soul Essence roll for 1–3 items when the final wave is cleared.

A completed Nightmares Daemon raid gives each nearby player an independent 50% roll for 1–2 Soul Essence. Missing that roll does not mean the raid reward system failed.

In the reference data, Direwolf raids use Tensura Goblin Village structures and require a Goblin resident; Daemon raids use the Tensura Dwarf Village and require a Dwarf resident. Entering the structure alone is not enough: the player must also have a valid raid-trigger effect, and the handler consumes that trigger when the raid begins.

## How it is used

Soul Essence is consumed by multiple Nightmares race-evolution requirement helpers. The required count is configuration-driven, so individual race pages should be used for the relevant branch rather than assuming one universal amount.

The item is also always edible in the reference release, restoring 4 nutrition with a 0.3 saturation modifier. Eating it is not shown as a substitute for satisfying a race evolution's explicit item-consumption requirement.

## Source clarification

The upstream article lists Vindicator, Illusioner, Evoker, Witch, Villager, and Pillager drops and labels the item non-renewable. Packaged files for those drops use the pre-1.21 loot_tables directory, while Minecraft 1.21 uses loot_table; those routes are not presented here as working without an in-game confirmation.

The raid rewards are assembled and granted directly by the reference release's Java handlers, so they do not depend on the legacy loot folder. The repeatable raid routes also conflict with the article's non-renewable label.

??? info "Sources and verification"

    [Reference release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382) · [Upstream article](https://tensuranightmares.wiki.gg/wiki/Soul_Essence) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid=1041)

    Artifact SHA-256: `94b37573cb247ed060c81a0c90a37a7258ab3517d6ad64c0e85902cd7da64127`.

    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.

    Evidence classes in `com.github.hvnbael.trnightmare`:

    - `registry.main.NightmareMobDrops`
    - `handler.RaidRewardTables`
    - `handler.DirewolfRaidHandler`
    - `handler.DaemonRaidHandler`
    - `main.races.NightmareEvolutionHelper`
    - `main.food.NightmareFoodProperties`

    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Release-specific corrections and verification notes are identified above.

    The page uses original TSR article artwork and does not present it as the in-game item texture.

[Back to the collection](index.md)
