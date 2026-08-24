# Build Phase Reports

## Phase 0 — Baseline and build system

```text
PHASE: 0 — Inspect and establish baseline
STATUS: PASS
ADDED: Packwiz source, pack validation, server source skeleton, build environment record
REMOVED: None
VERSION CHANGES: NeoForge locked to 21.1.248; pack version set to 1.0.0-beta.1
DEPENDENCIES: None
CLIENT START: Not applicable; no content mods installed
SERVER START: Not applicable; no content mods installed
TESTS: Handoff checksum verification; manifest validation; Packwiz metadata and index validation
WARNINGS: Full graphical client validation depends on an authenticated Minecraft launcher profile
KNOWN ISSUES: None in the empty runtime source
COMMIT: Initialize Version 1 (Beta) modpack build system
NEXT PHASE: Minimal Tensura runtime bootstrap
```

## Phase 1 — Minimal Tensura runtime

```text
PHASE: 1 — Minimal Tensura runtime bootstrap
STATUS: PASS
ADDED: Tensura: Reincarnated 2.0.1.2, ManasCore 4.0.0.2, Architectury API 13.0.11, GeckoLib 4.9.2, SmartBrainLib 1.16.11, TerraBlender 4.1.0.8
REMOVED: None
VERSION CHANGES: None
DEPENDENCIES: All packaged Tensura requirements satisfied; ManasCore supplies its required race, skill, and storage modules as embedded artifacts
CLIENT START: Runtime and mods install successfully; graphical validation pending an authenticated launcher session and client assets
SERVER START: PASS — first world ready in 8.694 seconds; warm restart ready in 1.799 seconds; both exited cleanly
TESTS: Canonical artifact/hash verification; packaged dependency audit; Packwiz client/server install; new-world generation; warm restart; clean six-dimension save
WARNINGS: Packaged TerraBlender/GeckoLib refmap warnings; NeoForge union asset schema warnings; recovered GazelDwargoArena warm-load ordering warning
KNOWN ISSUES: Full graphical client menu and single-player world validation remains external to the isolated unauthenticated client
COMMIT: Add Tensura Reincarnated runtime foundation
NEXT PHASE: Add frozen Tensura ecosystem addons in tested sub-batches
```

## Phase 2A — Core Tensura progression addons

```text
PHASE: 2A — Core Tensura progression addons
STATUS: PASS
ADDED: SlimeThrone Extras 2.1.2.1, Ascension 2.1.2, Mysticism 2.1.2, Origins 2.0.5, Better Subordinates 1.2.4, Modifications 1.0.1.1, Unique Monsters 1.0.2, TSR Unique Monsters Compat 1.0.0
REMOVED: None
VERSION CHANGES: None
DEPENDENCIES: TSR Unique Monsters Compat 1.0.0 is required with the exact official Unique Monsters 1.0.2 artifact
CONFIGURATION: 109 generated mod configs promoted; mutable patcher state excluded; Origins starter-pool refresh disabled and no Origins race appears in ordinary starting/random pools
CLIENT START: Pack installation and metadata validation pass; authenticated graphical validation remains pending for the complete pack
SERVER START: PASS — isolated construction, 20/20 clean full-runtime cold starts, warm restart, existing Phase 2 world restart, and fresh packaged-config cold/warm reconstruction
TESTS: Exact artifact/hash verification; Packwiz/config validation; 109/109 packaged config reconstruction; new-world generation; flushed save; clean shutdown; restart; Unique Monsters Appraisal Eye registry verification on every clean cold start
WARNINGS: Better Subordinates is excluded from CurseForge's third-party API and requires the verified official file when using Packwiz Installer; CurseForge launcher metadata remains authoritative
KNOWN ISSUES: Remaining frozen Tensura addons have not yet entered this sub-batch
COMMIT: Add core Tensura progression addons
NEXT PHASE: Add the remaining frozen Tensura ecosystem addons in isolated sub-batches
```

## Phase 2B — Boss, reward, and mimicry systems

```text
PHASE: 2B — Complete frozen Tensura ecosystem
STATUS: PASS WITH RELEASE POLICY GATE
ADDED: Great Sage 0.0.5, TenSura Guild 1.0.1.2, Tensura Skill Books 2.2.1, Tensura Utilities Manager 1.0.1, Not Enough Bosses 2.0.0.3, TenSura Boss Structure 1.0.3.3, TensuraMorph 1.0.1, ReMorphed 4.2, Woodwalkers 5.8.12, CraftedCore 5.8.2
REMOVED: None
VERSION CHANGES: ReMorphed and its required libraries resolved to exact 1.21.1 NeoForge artifacts
DEPENDENCIES: ReMorphed requires Woodwalkers and CraftedCore; TensuraMorph requires the complete stack
CONFIGURATION: 124 generated client/common configs promoted; Skill Books natural loot disabled; mimicry unlock bypasses disabled; generated cache and machine-local NeoForge configs excluded
CLIENT START: PASS — offline graphical client reached renderer, complete resource reload, sound engine, and main menu, then closed normally with exit code 0
SERVER START: PASS — isolated sub-batches, complete clean-world start, warm restart, and 5/5 repeated configured cold starts with flushed saves and clean shutdowns
TESTS: Exact artifact/hash and dependency verification; new-world Labyrinth generation; boss quest target resolution; config generation and review; mimicry policy persistence; complete client mod construction and resource reload
WARNINGS: Upstream resource-model warnings from Tensura, Mysticism, and Origins; optional compatibility class probes; CraftedCore's obsolete supporter-list URL returns 404 without affecting startup
KNOWN ISSUES: Great Sage `needGreatSage` is a world gamerule and must be set automatically by the later pack-owned first-world policy layer; final integrated gameplay validation remains required
COMMIT: Add Tensura boss and mimicry systems
NEXT PHASE: Civilization and magic compatibility branch
```

## Phase 3 — Civilization and magic

```text
PHASE: 3 — Nation building and mage integration
STATUS: PASS
ADDED: MineColonies 1.1.1319, Structurize 1.0.830, Multi-Piston 1.2.51, BlockUI 1.0.209, Domum Ornamentum 1.0.231, Tensura x MineColonies 0.2.2, Nightmare Utils 0.1.2, MineColonies Mages 2.3, Iron's Spells 'n Spellbooks 3.16.3, Tensura Compat: Iron's Spells 2.0.0.0, Iron's Lib 2.1.0, Player Animator 2.0.4, Curios API Continuation 9.0.15
REMOVED: None
VERSION CHANGES: Civilization and magic dependency floors resolved to exact tested 1.21.1 NeoForge artifacts
DEPENDENCIES: Complete MineColonies and Iron's Spells runtime stacks installed; Nightmare Utils retained only as the required Tensura x MineColonies library
CONFIGURATION: 141 reviewed files; colony force-loading disabled; citizen, raid, pathfinding, schematic-operation, griefing, experimental warfare, and Nightmare library-content limits locked by validation
CLIENT START: PASS — full renderer/resource/sound initialization, MineColonies and BlockUI atlases, mage model registration, Build Tool browser, Town Hall preview, placement dispatch, and colony-start advancement
SERVER START: PASS — isolated MineColonies and bridge sub-batches, complete 37-artifact clean world, five repeated configured cold starts, warm restart, flushed saves, and clean shutdowns
TESTS: Exact artifact/hash verification; dependency audit; 141/141 config reconstruction; Tensura bridge setup; mage recruitment hook registration; graphical client smoke; representative Build Tool and schematic placement flow
WARNINGS: The official Nightmare Utils 0.1.2 file reports internal version 0.1.0; MineColonies Mages uses its building-level fallback and logs missing optional mage citizen sound events; Structurize emits a first-run main-folder warning before registering style packs
KNOWN ISSUES: Automated client focus control pauses integrated-server time, so persistent colony state and long-running citizen AI remain later integrated gameplay gates rather than Phase 3 acceptance gates
COMMIT: Add Tensura nation building and mage integration
NEXT PHASE: Gear, storage, adventure, world, performance, and client-quality subsystems
```
