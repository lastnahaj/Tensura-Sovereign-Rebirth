---
title: Mod Guide Directory
description: Player-facing routes through every major content system in the TSR beta.
---

# Mod Guide Directory

The playable profile contains far more than the two upstream article collections. This directory gives every major player-facing mod family a wiki home while keeping libraries, rendering helpers, and server tooling out of the gameplay guides.

<div class="reference-path-grid">

<article class="reference-path-card reference-theme-evolution">
<img src="../assets/images/reference-races-evolution.png" alt="A reincarnated adventurer facing branching paths" loading="lazy" decoding="async">
<div class="reference-path-copy">
<h2>Character systems</h2>
<p>Races, evolution, skills, Great Sage, mimicry, gear growth, and external magic.</p>
<div class="reference-path-links">
<a href="../race-and-evolution/">Race & evolution</a>
<a href="../mimicry-and-forms/">Mimicry & forms</a>
<a href="../gear-evolution/">Gear evolution</a>
</div>
</div>
</article>

<article class="reference-path-card reference-theme-bestiary">
<img src="../assets/images/reference-bestiary.png" alt="An adventurer confronting a powerful creature" loading="lazy" decoding="async">
<div class="reference-path-copy">
<h2>Adventure & bosses</h2>
<p>Missions, contracts, external encounters, dimensions, travel, and shared loot.</p>
<div class="reference-path-links">
<a href="../adventure-travel-and-loot/">Adventure & travel</a>
<a href="../bosses-and-dimensions/">Bosses & dimensions</a>
</div>
</div>
</article>

<article class="reference-path-card reference-theme-world">
<img src="../assets/images/reference-world-equipment.png" alt="A wide fantasy landscape with equipment in the foreground" loading="lazy" decoding="async">
<div class="reference-path-copy">
<h2>World & structures</h2>
<p>Terrain, curated dungeons, structure density, settlements, and biome discovery.</p>
<div class="reference-path-links">
<a href="../world-generation/">World generation</a>
<a href="../structures/">Structure index</a>
<a href="../minecolonies-and-nations/">Nations</a>
</div>
</div>
</article>

<article class="reference-path-card reference-theme-abilities">
<img src="../assets/images/reference-skills-magic.png" alt="Arcane energy and magical symbols" loading="lazy" decoding="async">
<div class="reference-path-copy">
<h2>Kingdom systems</h2>
<p>Magic, colonies, crafting, storage, building, quests, teams, and claims.</p>
<div class="reference-path-links">
<a href="../magic/">Magic</a>
<a href="../storage-and-logistics/">Storage</a>
<a href="../quests-and-shop/">Quests & shop</a>
<a href="../current-modlist/">Search all 249 mods</a>
</div>
</div>
</article>

</div>

## Coverage map

Each row names the player-facing additions covered by that route. **Startup verified** means the assembled runtime reached its recorded client or server gate; it does not mean every encounter or long-session interaction has passed.

| Route | Included systems | Current evidence |
|---|---|---|
| [Character progression](../progression-overview.md) | Tensura core and extensions, Great Sage, Origins, Ascension, SlimeThrone Extras, Skill Books, Gear Evolution | Core startup and configuration verified; extended progression under validation |
| [Mimicry & forms](../mimicry-and-forms/index.md) | TensuraMorph, ReMorphed, Woodwalkers, CraftedCore | Startup verified; unlock-bypass policy verified |
| [Magic](../magic.md) | Iron's Spells 'n Spellbooks, Tensura compatibility, MineColonies Mages | Client/server startup and configuration verified |
| [Adventure, travel & loot](../adventure-travel-and-loot/index.md) | Beyond Adventures, Lootr, Waystones, Nature's Compass | Assembled-profile startup verified; extended gameplay under validation |
| [Bosses & dimensions](../bosses-and-dimensions.md) | Native boss layer, Bosses' Rise, Legendary Monsters, Cataclysm, Mowzie's Mobs, Twilight Forest, The Aether | Present in the profile; individual balance and progression checks remain |
| [World generation](../world-generation.md) | Terralith, Tectonic, YUNG's structure suite, Repurposed Structures, Sparse Structures, When Dungeons Arise | Playable startup verified; density and long-range exploration remain |
| [Nations](../minecolonies-and-nations.md) | MineColonies, Structurize, MineColonies Mages, Tensura x MineColonies | Construction/startup verified; long-running colony play remains |
| [Forging](../forging-and-metalworks.md) | Silent Gear, Productive Metalworks, Silent Gear Metalworks, Almost Unified, Polymorph | Startup and configured integration verified |
| [Storage](../storage-and-logistics.md) | Sophisticated Backpacks, Backpack Expansion, Sophisticated Storage, Tom's Simple Storage | Startup and recipe policy verified; multiplayer contention remains |
| [Building](../decoration-and-building.md) | Supplementaries, Amendments, FramedBlocks, Macaw's building suite, Farmer's Delight | Playable startup verified; broad recipe and multiplayer use remains |
| [Quests & multiplayer](../quests-and-shop.md) | FTB Quests, Teams, Chunks, XMod Compat, Essentials, Quest Shop, LuckPerms | Onboarding load verified; permissions and claim behavior remain |
| [Interface & discovery](../getting-started.md) | Skill Wiki, Evolution UI, JEI, Jade, Xaero's maps, Controlling, AppleSkin, inventory helpers | Graphical main-menu and resource-load smoke verified |

??? warning "Not active in the playable beta"
    Tensura: Unique Monsters, TR Addon, Ice & Fire with its Tensura bridge, and GriefLogger with its Tensura bridge are retained only as compatibility or design records. They are not presented as playable features. See [Unique Monsters](../unique-monsters.md) and the [Compatibility Matrix](../compatibility-matrix.md).

??? info "Technical-only additions"
    API libraries, shared dependencies, renderers, memory optimizers, backup tools, pregeneration tools, and profilers do not need player encyclopedia pages. Their versions and roles remain documented in the [Mod Manifest](../mod-manifest.md), [Performance & Optimization](../performance-and-optimization.md), and [Server Administration](../server-administration.md).

## What is still intentionally incomplete?

The directory now covers the installed gameplay families, but it does not invent mechanics that have not been verified. Exact boss reward tables, structure frequency, Waystones costs, long-duration colony behavior, and the full authored campaign will be expanded from runtime evidence as those beta gates close.
