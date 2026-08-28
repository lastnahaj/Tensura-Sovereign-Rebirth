# Compatibility Matrix

| System A | System B | Integration | Type | Version | Status | Notes |
|---|---|---|---|---|---|---|
| Tensura | MineColonies | Tensura x MineColonies | Explicit Integration | 0.2.2 | Verified startup; gameplay Under Validation | Core citizen/reputation bridge active; experimental faction, warfare, assassin, defense-swap, and raid systems disabled |
| Beyond Adventures | Tensura: Reincarnated / Better Subordinates | Mission, contract, and currency integration | External addon | 1.1.9 | Verified startup; gameplay Under Validation | The same official NeoForge artifact is pinned on Modrinth and CurseForge; clean-world construction, authored quest loading, save, shutdown, and warm restart pass |
| Tensura | FTB Teams/Chunks/Quests | Tensura Compat: FTB | Explicit Integration | 2.0.0.4 | Verified startup; gameplay Under Validation | Active in the playable profile; onboarding quest loading and team-shared configuration pass |
| LuckPerms | FTB | FTB XMod Compat where supported | Explicit Integration | Frozen targets | Planned | Non-OP permission matrix required |
| Tensura | Iron's Spells | Tensura Compat: Iron's Spells | Explicit Integration | 2.0.0.0 | Verified startup | Client/server construction and configuration baseline passed |
| Tensura | Ice & Fire | Tensura Compat: Ice & Fire | Explicit Integration | 2.0.0.1 target | PLAYABLE-PROFILE-BLOCKED | Frozen source entries are retained, but the pair is jointly omitted from beta staging because the compatibility mixin targets removed upstream registry classes |
| TR Addon | ManasCore race/skill registries | Constructor ordering | Native dependency | 2.0.1 / 4.0.0.2 | Blocked | Reproducible dedicated-server registry race; excluded from active runtime |
| Unique Monsters | ManasCore Skill / Architectury | Registration lifecycle | Native dependency | 1.0.2 | DEFERRED-BLOCKED | Reproducible parallel-construction race can reach `ExtraSkills.init()` before `manascore_skill:skills`; no replacement is active and the diagnostic bridge is not distributed |
| TensuraMorph | ReMorphed / Woodwalkers / CraftedCore | Required mimicry stack | Native dependency | 1.0.1 / 4.2 / 5.8.12 / 5.8.2 | Verified startup | Ordinary-kill and creative unlock bypasses disabled |
| Tensura Skill Books | FTB Quests | Controlled skill rewards | Authored quest integration | 2.2.1 | Under Validation | Natural loot injection is empty; the 8-quest onboarding chapter is active, while the full campaign reward design remains unfinished |
| Gear Evolution | Sophisticated Backpacks | Tensura Backpack Expansion | Explicit Integration | 1.2.5 / 1.0.4 | Verified startup; gameplay Under Validation | Component-retention and long-duration evolution gates remain |
| Gear Evolution | Apotheosis | Competing equipment progression | Not Required | — | Removed | Apotheosis excluded; Gear Evolution is authoritative |
| Sophisticated Storage | Tom's Simple Storage | Physical storage plus access terminals | Configured architecture | 1.5.91.2127 / 2.4.1 | Verified startup | 18 recipes removed, seven access recipes retained, wireless and scan ranges bounded |
| Silent Gear Metalworks | Productive Metalworks without Silent Gems | TSR Silent Gear Metalworks Compat | Datapack Integration | 1.5.0 / 1.15.1 / 1.0.0 | Verified | Seven installed fluids retained; unavailable Silent Gems mappings conditionally excluded |
| Productive Metalworks | Ponder / Flywheel | Client dependency discovery | Native and embedded dependencies | 1.0.81 / 1.0.4-30 | Verified | Ponder explicit; Flywheel byte-verified embedded dependency |
| Great Sage | Jade | Information-progression boundary | Configuration | 0.0.5 / 15.10.6 | Startup verified; gameplay Under Validation | Both are active in the playable client; spoiler-boundary gameplay review remains |
| SlimeThrone | FTB Quests | Repeatable prestige versus authored campaign | Separated ownership | 2.1.2.1 / 2101.1.33 | Onboarding implemented | Branded 8-quest first-steps chapter is active; the complete handcrafted campaign remains planned |
| Ascension | External bosses | Supported boss scaling | Explicit Integration | 2.1.2 | Under Validation | No unsupported registry IDs or invented values are added |
| MineColonies | Iron's Spells | MineColonies Mages | Explicit Integration | 1.1.1319 / 3.16.3 / 2.3 | Verified startup | Tested barracks fallback used when no native mage building ID exists |
| Nightmare Utils | Tensura x MineColonies | Required API/library | Native dependency | 0.1.2 | Verified configuration | Autocast, trading, spawn profiles, rewards, and test skills disabled |
| Iron's Spells | Terrain griefing | Stability baseline | Configuration | 3.16.3 | Verified configuration | Spell terrain griefing disabled |
| FTB Ranks | LuckPerms | Permission authority | Not Required | — | Removed | LuckPerms is authoritative |
| OPAC | FTB Chunks | Claim authority | Not Required | — | Removed | FTB owns teams and claims |
| AE2 / Refined Storage | TSR storage | Competing storage architecture | Not Required | — | Removed | Excluded for theme and redundancy |

## Pending validation

- Dual-platform artifact audit for all active entries; every mod must have an exact official Modrinth source/checksum or documented redistribution permission in addition to its CurseForge pin
- TR Addon upstream release recheck before Version 1 (Beta) release candidate freeze; test any newer official artifact in isolation and then with the full Phase 2 runtime
- YIGD with Tensura/Gear Evolution/component state
- Embeddium rendering compatibility
- TNO compatibility-only deployment
- Ancient Artifacts vs Gear Evolution
- Plundering exploit behavior
- Bosses' Rise / Legendary Monsters / Block Factory's Bosses
- When Dungeons Arise worldgen density/performance
