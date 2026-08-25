# Mod Manifest

**Freeze:** v0.1<br>
**Minecraft:** 1.21.1<br>
**Loader:** NeoForge<br>
**Freeze date:** 2026-08-23

- Baseline frozen entries: **90**
- Test candidates: **12**
- Optional entries: **1**
- Rejected entries tracked: **20**

> This page reflects the v0.1 design freeze. Entries marked `DEPENDENCY` or `Resolve current...` are finalized into exact version locks during staged assembly.

## Tensura Core

| Mod | Version | Status | Notes |
|---|---|---|---|
| Tensura: Reincarnated | 2.0.1.2 | LOCK |  |
| Tensura: SlimeThrone Extras | 2.1.2.1 | LOCK |  |
| Tensura: Ascension | 2.1.2 | LOCK |  |
| Tensura: Mysticism | 2.1.2 | LOCK |  |
| Tensura: Reincarnated Addon (TR Addon) | 2.0.1 | DEFERRED-BLOCKED | Reproducible dedicated-server constructor race against ManasCore custom race/skill registries. The verified public artifact cannot complete NeoForge dedicated-server mod construction. Recheck upstream before the Version 1 (Beta) release candidate freeze. |
| Tensura: Origins | 2.0.5 | LOCK-GATED | Not available as an ordinary random starting race; high-tier race paths are late-game gated. |
| Tensura: Better Subordinates | 1.2.4 | LOCK |  |
| Tensura Modifications | 1.0.1.1 | LOCK |  |
| Tensura: Unique Monsters | 1.0.2 | LOCK | Required with TSR Unique Monsters Compat 1.0.0. Retain the exact official CurseForge artifact unmodified. |
| TSR Unique Monsters Compat | 1.0.0 | DEPENDENCY | Required while Tensura: Unique Monsters 1.0.2 is active; corrects its ManasCore skill-registry construction ordering without modifying the upstream artifact. |
| Great Sage | 0.0.5 | LOCK | Configure `needGreatSage=true`. |
| TenSura Guild | 1.0.1.2 | LOCK |  |
| Tensura Skill Books | 2.2.1 | LOCK | Primary controlled skill-reward system. |
| Tensura Utilities Manager | 1.0.1 | LOCK |  |
| Tensura: Not Enough Bosses | 2.0.0.3 | LOCK |  |
| TenSura Boss Structure | 1.0.3.3 | LOCK |  |
| TensuraMorph | 1.0.1 | LOCK |  |
| ReMorphed | 4.2 | DEPENDENCY | Required for TensuraMorph. |
| Woodwalkers | 5.8.12 | DEPENDENCY | Required by ReMorphed; client and server. |
| CraftedCore | 5.8.2 | DEPENDENCY | Required by ReMorphed, Woodwalkers, and TensuraMorph; client and server. |
| Tensura Gear Evolution | 1.2.5 | LOCK | Authoritative equipment progression system. |
| Tensura Backpack Expansion | 1.0.4 | LOCK |  |
| Tensura Metalworks | 1.0.4 | LOCK |  |
| Tensura x MineColonies | 0.2.2 | LOCK-CONFIGURED | Core citizen and reputation integration is active. Experimental faction, diplomacy, warfare, assassin, defense-swap, and reputation-raid systems are disabled for the beta baseline. |
| Nightmare Utils | 0.1.2 | LIBRARY-ONLY | Required API/library for Tensura x MineColonies. Its content systems are disabled and its test skills are excluded from Skill Books rewards. The official 0.1.2 file reports internal version 0.1.0. |
| Tensura Compat: FTB | 2.0.0.4 | LOCK |  |
| Tensura Compat: Iron's Spells | 2.0.0.0 | LOCK |  |
| Tensura Compat: Ice & Fire | 2.0.0.1 | LOCK |  |

## Civilization & Magic

| Mod | Version | Status | Notes |
|---|---|---|---|
| MineColonies | 1.1.1319 | PIN | Pinned because Tensura x MineColonies and MineColonies Mages explicitly target this line. |
| Structurize | 1.0.830 | DEPENDENCY | Exact Phase 3 lock. |
| Multi-Piston | 1.2.51 | DEPENDENCY | Exact Phase 3 lock. |
| BlockUI | 1.0.209 | DEPENDENCY | Exact Phase 3 lock. |
| Domum Ornamentum | 1.0.231 | DEPENDENCY | Exact Phase 3 lock. |
| MineColonies Mages (IronSpells integration) | 2.3 | LOCK-CONFIGURED | Uses native MineColonies flows where available and the tested barracks progression fallback when no native mage building is registered. |
| Iron's Spells 'n Spellbooks | 3.16.3 | LOCK |  |
| Iron's Lib | 2.1.0 | DEPENDENCY | Required by Iron's Spells. |
| Player Animator | 2.0.4 | DEPENDENCY | Required by Iron's Spells. |
| Curios API Continuation | 9.0.15 | DEPENDENCY | Required by Iron's Spells. |

## Gear, Crafting & Storage

| Mod | Version | Status | Notes |
|---|---|---|---|
| Silent Gear | 4.2.1.1 | LOCK |  |
| Silent Lib | 10.6.0 | DEPENDENCY | Required by Silent Gear. |
| Productive Metalworks | 1.15.1 | LOCK |  |
| Silent Gear Metalworks | 1.5.0 | LOCK |  |
| TSR Silent Gear Metalworks Compat | 1.0.0 | DEPENDENCY | Required while Silent Gear Metalworks is active without Silent Gems; replaces only the affected fluid unit map and verifies all installed mappings at data-map reload. |
| Ponder | 1.0.81+mc1.21.1 | DEPENDENCY | Exact official Create Maven artifact installed explicitly so its NeoForge platform service is discoverable during client setup. The artifact is on CurseForge's approved third-party list. |
| Flywheel | 1.0.4-30 | EMBEDDED-DEPENDENCY | Productive Metalworks supplies the exact official artifact through NeoForge JarJar; client discovery and rendering passed without a redistributed standalone copy. |
| Sophisticated Core | 1.4.89.2291 | DEPENDENCY | Exact shared dependency for the pinned Sophisticated Storage and Backpacks releases. |
| Sophisticated Backpacks | 3.25.78.2107 | LOCK |  |
| Sophisticated Storage | 1.5.91.2127 | LOCK |  |
| Tom's Simple Storage | 2.4.1 (1.21.x NeoForge) | LOCK-STRIPPED | Expose only Storage/Crafting Terminals, wireless terminals/items, and the minimum connector/link infrastructure required. Disable/hide the rest. |
| Almost Unified | 1.4.2 | LOCK |  |
| KubeJS | 2101.7.2-build.368 | LOCK | Pack scripting, recipe removal/hiding/gating, small integrations. |
| Rhino | 2101.2.7-build.81 | DEPENDENCY | Exact KubeJS JavaScript runtime. |
| Polymorph | 1.1.0+1.21.1 | LOCK |  |

## Adventure, Bosses & World

| Mod | Version | Status | Notes |
|---|---|---|---|
| L_Ender's Cataclysm | 3.33 | LOCK |  |
| Mowzie's Mobs | 1.8.2 | LOCK |  |
| IceAndFire Community Edition | 2.1.1 | LOCK |  |
| The Twilight Forest | 4.8.3345 | LOCK |  |
| The Aether | 1.5.10-neoforge | LOCK |  |
| Lootr | 1.11.38.124 | LOCK |  |
| Waystones | 21.1.41 | LOCK | Travel progression will be gated/configured; no free early cross-dimensional travel. |
| Nature's Compass | 3.4.0 | LOCK | Useful for finding Tensura/custom biomes without adding a biome overhaul. |
| Farmer's Delight | 1.3.3 | LOCK |  |

## Decoration

| Mod | Version | Status | Notes |
|---|---|---|---|
| Supplementaries | 3.9.1 | LOCK |  |
| Amendments | 2.1.7 | LOCK |  |
| FramedBlocks | 10.6.1 | LOCK |  |
| Macaw's Furniture | 3.4.1 | LOCK |  |
| Macaw's Doors | 1.1.5 | LOCK |  |
| Macaw's Windows | Resolve current 1.21.1 NeoForge release | LOCK |  |
| Macaw's Roofs | Resolve current 1.21.1 NeoForge release | LOCK |  |
| Macaw's Bridges | Resolve current 1.21.1 NeoForge release | LOCK |  |
| Macaw's Lights and Lamps | Resolve current 1.21.1 NeoForge release | LOCK |  |

## Quest, Economy & Server

| Mod | Version | Status | Notes |
|---|---|---|---|
| FTB Library | Match pinned FTB suite | DEPENDENCY |  |
| FTB Teams | 2101.1.10 | LOCK |  |
| FTB Chunks | 2101.1.21 | LOCK |  |
| FTB Quests | 2101.1.33 | LOCK |  |
| FTB XMod Compat | 21.1.11 | LOCK |  |
| FTB Essentials | 2101.1.10 | TEST-PERMISSIONS | Keep only if all desired commands honor the final LuckPerms permission model under non-OP accounts. |
| Quest Shop | 1.3.0 | LOCK | Disable ordinary mob coin drops; currency primarily comes from quests/guild/progression. |
| LuckPerms | 5.4.140 | LOCK-SERVER |  |
| GriefLogger | 1.2.7 | LOCK-SERVER |  |
| Tensura: Grief Logger | 1.2.1 | LOCK-SERVER |  |
| FTB Backups 3 | 21.1.5 | LOCK-SERVER |  |
| Chunky | 1.4.23 | LOCK-SERVER |  |
| spark | 1.10.124 | LOCK-SERVER |  |

## Client & QoL

| Mod | Version | Status | Notes |
|---|---|---|---|
| Tensura Skill Wiki | 1.0.2.4 | LOCK-CLIENT |  |
| TenSura Evolution UI | 1.0.0.3 | LOCK-CLIENT |  |
| JEI | 19.27.0.336 baseline | LOCK-CLIENT | Use stable baseline first; only advance after compatibility smoke test. |
| Jade | 15.10.6 | LOCK-CLIENT | Configure so it does not spoil Great Sage/Appraisal mechanics. |
| Xaero's Minimap | 26.4.2 | LOCK-CLIENT |  |
| Xaero's World Map | 1.45.0 | LOCK-CLIENT |  |
| Mouse Tweaks | 2.26.1 | LOCK-CLIENT |  |
| Inventory Essentials | 21.1.17 | LOCK-CLIENT |  |
| Controlling | 19.0.4 | LOCK-CLIENT |  |
| AppleSkin | Resolve current 1.21.1 NeoForge release | LOCK-CLIENT |  |

## Optimization

| Mod | Version | Status | Notes |
|---|---|---|---|
| ModernFix | 5.27.20+mc1.21.1 | LOCK |  |
| FerriteCore | 7.0.3-neoforge | LOCK |  |
| ServerCore | 1.5.19+1.21.1 | LOCK-SERVER-CONSERVATIVE | Begin with conservative optimizations only; do not aggressively alter AI/entity activation until MineColonies and Tensura testing passes. |
| ImmediatelyFast | 1.6.12 | LOCK-CLIENT |  |
| Entity Culling | 1.10.5 | LOCK-CLIENT |  |
| Embeddium | 1.0.15 | TEST-CLIENT | Keep only after rendering tests with Tensura entities, MineColonies previews, boss effects and UI. |
| Dynamic FPS | 3.11.3 | LOCK-CLIENT |  |
| Clumps | 19.0.0.1 | LOCK |  |

## Initial Test Candidates

| Mod | Version | Status | Notes |
|---|---|---|---|
| When Dungeons Arise | 2.1.68 | TEST | Strong thematic fit and present in the Tempest Protocol reference quest structure; must pass worldgen density/performance tests. |
| You're in Grave Danger (YIGD) | 2.0.13 | TEST | Verify death/restoration preserves all Tensura, Gear Evolution and accessory/component state. |
| Tensura: Virtuoso | 2.0.0.1 | TEST | Good skill diversity; audit incomplete/nonfunctional item content and balance first. |
| Tensura: Ancient Artifacts | Resolve current 1.21.1 release | TEST | Keep only if artifacts complement rather than replace Gear Evolution. |
| Tensura Plundering | Resolve current 1.21.1 release | TEST | Audit skill-farm exploits with named mobs, citizens and subordinates. |
| Tensura Naturesaura + Nature's Aura | Resolve current 1.21.1 releases | TEST | Include only if it adds world flavor without creating a competing mandatory magic progression. |
| TNO / Neo Otherworld Compatibility Fix | Resolve current 1.21.1 release | TEST-COMPAT-ONLY | Use only if compatibility fixes are needed and overlapping backpack/progression content can be disabled. |
| Bosses' Rise + Tensura compat | Resolve current 1.21.1 releases | TEST |  |
| Legendary Monsters + Tensura compat | Resolve current 1.21.1 releases | TEST |  |
| Block Factory's Bosses | Resolve current 1.21.1 release | TEST |  |
| Simple Voice Chat | Resolve current 1.21.1 NeoForge release | OPTIONAL |  |

## Rejected

| Mod | Reason |
|---|---|
| Apotheosis | Gear Evolution is authoritative. |
| Tensura Reincarnated Nightmares | Explicitly excluded. |
| Nightmare's Apothic Tensura | Nightmare content branch excluded. |
| BTRUltima | 1.19.2 only; ideas can be represented with modern 1.21.1 content. |
| Ars Nouveau Tensura compatibility | Useful compat found was for the wrong Minecraft version. |
| Tensura: KumoDesu | Crossover and WIP. |
| Tensura: Skill Obtain | Redundant with controlled Skill Books/quest reward design. |
| Tensura: Arcane | Experimental/non-lore races and explicitly not PvP-balanced. |
| Simply Tensura Additions | High-tier/crossover-style progression conflicts with the curated race balance. |
| Tensura: Authorities | Additional competing high-tier power system. |
| Tensura Horizons Expanded | Very new beta; reconsider after v0.1 stabilizes. |
| Applied Energistics 2 | Wrong technology/aesthetic direction for storage. |
| Refined Storage | Wrong technology/aesthetic direction for storage. |
| Simple Storage Network | Tom's terminal-only approach won. |
| Chipped | Decorative block/menu/recipe bloat. |
| Handcrafted | Overlaps frozen decoration stack. |
| Beautify | Overlaps frozen decoration stack. |
| MCA Reborn | MineColonies owns civilization/NPC gameplay. |
| Open Parties and Claims | FTB Teams/Chunks owns team/claim gameplay. |
| FTB Ranks | LuckPerms is the permission/rank authority. |
