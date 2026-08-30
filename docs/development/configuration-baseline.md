# Configuration Baseline

Configuration is promoted and tested with each subsystem. A phase does not pass solely because its mods construct successfully: its generated configuration must also be reviewed, added to the Packwiz source, reconstructed into a clean instance, and exercised by the same server and client gates.

## Phase 2A baseline

The initial Tensura progression runtime generated 109 mod configuration files;
107 remain active after the Unique Monsters defer. The
active pack includes the complete Tensura, Mysticism, SlimeThrone Extras,
Ascension, Origins, Better Subordinates, Modifications, and TerraBlender trees.
Unique Monsters' generated configuration is retained only as deferred
development evidence and is not an active runtime dependency.

TSR intentionally excludes NeoForge's machine-local `fml.toml`, `neoforge-common.toml`, and `neoforge-server.toml` defaults. It also excludes `stextras/internal/tensura_config_patcher_state.toml`, which records mutable first-run migration state rather than a pack policy.

The following design rule is enforced in the pack validator:

- `trorigins.general.refresh` is disabled after generation.
- No `trorigins:` race may appear in Tensura's ordinary `startingRaces` or `randomRaces` pools.
- SlimeThrone Extras' supported starter races and skill remain in the generated Tensura pools.
- The reviewed configuration tree must be present in the Packwiz index.

A clean reconstruction verified the 12 active Phase 2A runtime artifacts and all
107 active packaged configs before launch. The reconstructed server passed
new-world creation, a flushed save, clean shutdown, and warm restart. The only
files created outside the packaged tree were NeoForge's three machine defaults
and SlimeThrone Extras' expected internal patcher state; no packaged setting
changed semantically.

## Complete Phase 2 baseline

The remaining frozen Tensura layer expands the reviewed tree to 124 files. It adds Great Sage client/common settings, Guild and boss settings, the complete Skill Books generated pool and probability files, the TensuraMorph bridge, ReMorphed, Woodwalkers, CraftedCore, and the SlimeThrone client presentation default.

The following progression rules are locked in the packaged configuration:

- Skill Books natural loot tables contain no active entries. Authored quests and explicitly reviewed rewards remain the only planned distribution path.
- ReMorphed ordinary-kill unlocks require 100,000 kills and creative-mode automatic unlocks are disabled. TensuraMorph applies the same threshold so Predator and Gluttony remain the practical mimicry path.
- CraftedCore background version checking is disabled. Its generated supporter cache is runtime state and is not packaged.
- Great Sage voice input remains off by default. Its `needGreatSage` possession rule is a world gamerule rather than a TOML setting; automatic first-world enforcement remains a release gate for the pack-owned server policy layer.

The complete 24-artifact Phase 2 runtime passed five repeated clean-world dedicated-server starts after configuration, a warm restart, and an offline graphical client start through renderer, resource reload, and sound-engine initialization. NeoForge did not generate any world-scoped server config files for this layer, so no Phase 2 file belongs in `defaultconfigs`; that tree is populated when later server-scoped configuration owners enter the runtime.

Additional frozen settings are activated when their owning systems enter the runtime. These include automatic Great Sage gamerule enforcement, controlled Waystones travel, Quest Shop currency sources, Jade information limits, and conservative ServerCore behavior. Each setting receives a fresh-install regression test before its subsystem is accepted.

## Playable beta stability baseline

The playable beta profile adds conservative defaults without enabling gameplay-altering entity activation ranges or dynamic mob-cap scaling:

- ServerCore prevents players from moving into unloaded chunks while retaining its safe synchronous-load reduction and ticking-chunk cache.
- Dedicated-server defaults use view distance 8, simulation distance 6, synchronous chunk writes, and a 120-second watchdog ceiling for heavy modded generation.
- FTB Backups 3 runs hourly, retains eight archives within a 25 GB ceiling, uses moderate compression, creates a shutdown backup, and reports progress only to administrators.
- spark remains installed for on-demand diagnosis but its background profiler is disabled.
- FTB Quests uses a 20-tick detection interval and team-shared rewards. The first playable chapter contains 8 linear onboarding quests, a custom TSR background, and a clickable crest linked to the project wiki.
- First-launch client defaults use a 150 FPS cap, GUI scale 2, render and simulation distance 8, Bright brightness, disabled VSync, and disabled view bobbing. Tensura skill slots exclusively own Z/X/C. Core interfaces and abilities use unique defaults: Tensura mode on grave accent, backpack on O, forms on H, Iron's spell casting/wheel on J/K, Great Sage on G/comma/period, and the wireless terminal on apostrophe.
- TAB is reserved for the vanilla player list. FTB Quests keeps its TAB and Shift+TAB chapter navigation contextual to the quest screen, so it does not compete with the global player-list binding.
- Secondary gear abilities, redundant map and inventory shortcuts, pack-authoring controls, quest editor actions, cache/debug actions, and JEI cheat/edit actions are unbound. Players can opt into a secondary action later without inheriting a collision-heavy default profile.
- A versioned KubeJS client policy reapplies these mappings after NeoForge has registered every mod key and records a per-profile marker, avoiding the late-registration overwrite that affects a partial options file.
- Xaero's Minimap defaults to a circular map anchored in the top-right HUD corner through its packaged client profile and HUD layout policy.
- No optional resource pack is enabled in this checkpoint. Vanilla resources remain implicit, while TSR menu and quest visuals are supplied through FancyMenu and KubeJS assets.

The configured server loaded the saved world, reported all 8 quests, created a shutdown backup, saved all dimensions, and exited cleanly.

## Phase 3 baseline

The civilization and magic layer expands the reviewed tree to 141 files. It adds MineColonies, Structurize, Tensura x MineColonies, MineColonies Mages, Iron's Spells, Curios, and Nightmare Utils configuration.

The following server-stability rules are locked in validation:

- MineColonies is capped at 150 citizens per colony, colony force-loading is disabled, delayed colony loading is set to five minutes with strictness six, maximum tree scans are 300 blocks, maximum raid size is 60, and pathfinding remains single-threaded.
- Structurize is limited to 500 world operations per tick, 25 cached undo changes, 64 cached schematics, and 500 blocks checked per worker operation.
- Tensura x MineColonies keeps assassins, extra citizen aggression, natural rival settlement generation, factions/diplomacy/warfare, defense transformation, and reputation raids disabled. Colony protection against Tensura mob and skill griefing remains enabled.
- Iron's Spells terrain griefing is disabled.
- Nightmare Utils is present only as a required library. Autocast, mob trading, skill rewards, and spawn profiles are disabled, and every `nightmareutils:` test skill is blacklisted from Skill Books random rewards.
- MineColonies Mages uses the native flow when exposed and requires its combat research and progression anchor. With no native mage building ID in the tested build, its registered barracks fallback is the accepted baseline.

The complete 37-artifact runtime passed five configured clean-world starts, a warm restart, clean saves and shutdowns, 141/141 semantic config reconstruction, and a graphical client start. Representative client interaction also verified the MineColonies Build Tool browser, Town Hall schematic preview, placement dispatch, and colony-start advancement. Persistent colony state and long-running citizen AI remain later integrated gameplay checks because automated focus changes pause the integrated server.

## Phase 4A baseline

The gear and storage layer expands the reviewed tree to 159 files. It adds Gear Evolution, Tensura Metalworks, Silent Gear, Productive Metalworks, Silent Gear Metalworks, the Sophisticated storage family, Tensura Backpack Expansion, Tom's Simple Storage, Almost Unified, KubeJS, Rhino, and Polymorph configuration.

The following stability and progression rules are locked in validation:

- Productive Metalworks foundries are limited to 256 blocks of volume, 96 blocks of circumference, and 12 blocks of height. Foundry inventory rendering is disabled.
- Silent Gear does not grant starter blueprints or its material book automatically.
- Tom's inventory connectors scan no farther than 12 blocks and no more than 256 positions. Basic wireless access is limited to 12 blocks, advanced access to 64 blocks, link range to 128 blocks, beacon-based unlimited or cross-dimensional access is disabled, and multithreaded scanning remains off.
- Eighteen non-terminal Tom's recipes are removed. The seven core terminal, wireless, connector, and link recipes remain available.
- Eleven pack-owned recipe overrides gate optional integrations that are not installed. Almost Unified owns duplicate-material normalization.
- TSR Silent Gear Metalworks Compat replaces only the affected Productive Metalworks fluid-unit map. It preserves the full upstream baseline, retains seven installed Silent Gear molten-fluid mappings, conditionally excludes 21 Silent Gems mappings, and verifies the effective map after reload.
- Ponder 1.0.81 is an explicit, hash-locked upstream dependency because a nested-only client does not discover its NeoForge platform service reliably. Productive Metalworks' embedded Ponder is byte-identical. Its embedded Flywheel 1.0.4-30 is also byte-identical to the official upstream artifact and passes client discovery without a standalone copy.

The complete Phase 4A runtime passed a clean dedicated-server world creation, flushed save, clean shutdown, saved-world restart, 159/159 semantic config reconstruction, and a graphical client launch with fatal-state log rejection. The only recurring error is CraftedCore's obsolete supporter-list URL, which does not affect construction or gameplay.
