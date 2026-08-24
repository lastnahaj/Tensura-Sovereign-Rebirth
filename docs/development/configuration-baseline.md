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

Additional frozen settings are activated when their owning mods enter the runtime. These include Great Sage possession checks, controlled Waystones travel, Quest Shop currency sources, Jade information limits, and conservative ServerCore behavior. Each setting receives a fresh-install regression test before its subsystem is accepted.
