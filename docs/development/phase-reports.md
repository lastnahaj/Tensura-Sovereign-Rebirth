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
