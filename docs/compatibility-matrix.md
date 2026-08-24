# Compatibility Matrix

| System A | System B | TSR decision |
|---|---|---|
| Tensura | MineColonies | Dedicated Tensura x MineColonies bridge; core |
| Tensura | FTB Teams/Chunks/Quests | Dedicated Tensura Compat: FTB; core |
| LuckPerms | FTB | FTB XMod Compat where supported; test all actions under non-OP |
| Tensura | Iron's Spells | Dedicated compatibility; core |
| Tensura | Ice & Fire | Dedicated compatibility; core |
| TR Addon 2.0.1 | ManasCore race/skill registries | DEFERRED-BLOCKED; excluded from the active runtime after reproducible dedicated-server construction failures; recheck official releases before release candidate freeze |
| Unique Monsters 1.0.2 | ManasCore Skill 4.0.0.2 / Architectury 13.0.11 | REQUIRED with TSR Unique Monsters Compat 1.0.0; exact official JAR retained unmodified; 20/20 Phase 2A and 5/5 complete Phase 2 clean cold starts passed |
| TensuraMorph 1.0.1 | ReMorphed 4.2 / Woodwalkers 5.8.12 / CraftedCore 5.8.2 | REQUIRED stack; ordinary-kill and creative morph unlock bypasses disabled by pack configuration |
| Tensura Skill Books 2.2.1 | FTB Quests | Skill Books supplies controlled rewards; natural loot injection remains empty until authored reward placement is validated |
| Tensura | Sophisticated Backpacks | Gear Evolution + Backpack Expansion; core |
| Gear Evolution | Apotheosis | Not used; Apotheosis excluded |
| Sophisticated Storage | Tom's | Sophisticated = storage, Tom's = terminal/wireless only |
| Great Sage | Jade | Jade configured not to spoil Tensura analysis |
| SlimeThrone | FTB Quests | SlimeThrone = repeatable/prestige, FTB = handcrafted campaign |
| Ascension | External bosses | Ascension scaling used where supported |
| MineColonies | Iron's Spells | MineColonies Mages; core |
| FTB Ranks | LuckPerms | FTB Ranks excluded; LuckPerms authoritative |
| OPAC | FTB Chunks | OPAC excluded; FTB owns claims |
| AE2 / Refined Storage | TSR storage | Excluded for theme and redundancy |

## Pending validation

- TR Addon upstream release recheck before Version 1 (Beta) release candidate freeze; test any newer official artifact in isolation and then with the full Phase 2 runtime
- YIGD with Tensura/Gear Evolution/component state
- Embeddium rendering compatibility
- TNO compatibility-only deployment
- Ancient Artifacts vs Gear Evolution
- Plundering exploit behavior
- Bosses' Rise / Legendary Monsters / Block Factory's Bosses
- When Dungeons Arise worldgen density/performance
