# Configuration Baseline

Configuration is promoted and tested with each subsystem. A phase does not pass solely because its mods construct successfully: its generated configuration must also be reviewed, added to the Packwiz source, reconstructed into a clean instance, and exercised by the same server and client gates.

## Phase 2A baseline

The initial Tensura progression runtime generated 109 mod configuration files. The pack includes the complete Tensura, Mysticism, SlimeThrone Extras, Ascension, Origins, Better Subordinates, Modifications, Unique Monsters, and TerraBlender trees.

TSR intentionally excludes NeoForge's machine-local `fml.toml`, `neoforge-common.toml`, and `neoforge-server.toml` defaults. It also excludes `stextras/internal/tensura_config_patcher_state.toml`, which records mutable first-run migration state rather than a pack policy.

The following design rule is enforced in the pack validator:

- `trorigins.general.refresh` is disabled after generation.
- No `trorigins:` race may appear in Tensura's ordinary `startingRaces` or `randomRaces` pools.
- SlimeThrone Extras' supported starter races and skill remain in the generated Tensura pools.
- The reviewed configuration tree must be present in the Packwiz index.

A clean reconstruction verified all 14 Phase 2A runtime artifacts and all 109 packaged configs before launch. The reconstructed server passed new-world creation, a flushed save, clean shutdown, and warm restart. The only files created outside the packaged tree were NeoForge's three machine defaults and SlimeThrone Extras' expected internal patcher state; no packaged setting changed semantically.

## Complete Phase 2 baseline

The remaining frozen Tensura layer expands the reviewed tree to 124 files. It adds Great Sage client/common settings, Guild and boss settings, the complete Skill Books generated pool and probability files, the TensuraMorph bridge, ReMorphed, Woodwalkers, CraftedCore, and the SlimeThrone client presentation default.

The following progression rules are locked in the packaged configuration:

- Skill Books natural loot tables contain no active entries. Authored quests and explicitly reviewed rewards remain the only planned distribution path.
- ReMorphed ordinary-kill unlocks require 100,000 kills and creative-mode automatic unlocks are disabled. TensuraMorph applies the same threshold so Predator and Gluttony remain the practical mimicry path.
- CraftedCore background version checking is disabled. Its generated supporter cache is runtime state and is not packaged.
- Great Sage voice input remains off by default. Its `needGreatSage` possession rule is a world gamerule rather than a TOML setting; automatic first-world enforcement remains a release gate for the pack-owned server policy layer.

The complete 24-artifact Phase 2 runtime passed five repeated clean-world dedicated-server starts after configuration, a warm restart, and an offline graphical client start through renderer, resource reload, and sound-engine initialization. NeoForge did not generate any world-scoped server config files for this layer, so no Phase 2 file belongs in `defaultconfigs`; that tree is populated when later server-scoped configuration owners enter the runtime.

Additional frozen settings are activated when their owning systems enter the runtime. These include automatic Great Sage gamerule enforcement, controlled Waystones travel, Quest Shop currency sources, Jade information limits, and conservative ServerCore behavior. Each setting receives a fresh-install regression test before its subsystem is accepted.

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
