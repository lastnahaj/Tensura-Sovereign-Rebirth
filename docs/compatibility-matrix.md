# Compatibility Matrix

| System A | System B | TSR decision |
|---|---|---|
| Tensura | MineColonies | Dedicated Tensura x MineColonies bridge; core |
| Tensura | FTB Teams/Chunks/Quests | Dedicated Tensura Compat: FTB; core |
| LuckPerms | FTB | FTB XMod Compat where supported; test all actions under non-OP |
| Tensura | Iron's Spells | Dedicated compatibility; core |
| Tensura | Ice & Fire | Dedicated compatibility; core |
| TR Addon 2.0.1 | ManasCore race/skill registries | DEFERRED-BLOCKED; excluded from the active runtime after reproducible dedicated-server construction failures; recheck official releases before release candidate freeze |
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
