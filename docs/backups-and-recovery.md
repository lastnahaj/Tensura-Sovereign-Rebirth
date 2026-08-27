# Backups & Recovery

FTB Backups 3 is included as the baseline in-pack backup solution.

A recoverable TSR backup includes:

- every world dimension and level metadata,
- player data and mod capabilities,
- FTB teams, claims, and quest progress,
- MineColonies colony and citizen state,
- `config/` and `defaultconfigs/`,
- mod-specific saved data, scripts, datapacks, and quest source,
- the exact pack version or lock metadata needed to reconstruct the runtime.

Backups are especially important before:
- enabling experimental MineColonies warfare/diplomacy,
- large config migrations,
- worldgen/content upgrades,
- Tensura addon updates,
- quest/script changes that touch progression data.

GriefLogger and Tensura Grief Logger are forensic/audit tools; they are not treated as a substitute for backups.

The production server should also maintain host-level/off-server backup retention independently of the Minecraft process.

Test restoration in a separate directory. A backup is not verified merely because an archive file exists; the restored server must load the world, allow a player join, retain progression/teams/colonies, and survive a second clean restart.
