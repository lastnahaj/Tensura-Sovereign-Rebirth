# Server Administration

TSR dedicated servers require **Java 21** and the pack's locked **NeoForge 21.1.248** runtime. Do not substitute a different loader build without rerunning the recorded startup, world, configuration, and restart gates.

## Baseline administration stack

- LuckPerms
- FTB Teams / Chunks / Quests
- FTB XMod Compat
- Tensura Compat: FTB
- Tensura Utilities Manager
- GriefLogger
- Tensura: Grief Logger
- FTB Backups 3
- Chunky
- spark

## Administration philosophy

- Do not rely on OP as the normal staff permission model.
- Use LuckPerms groups for staff/admin access.
- Keep gameplay progression inside gameplay systems rather than permission groups.
- Log destructive and Tensura-specific actions.
- Maintain scheduled backups before enabling experimental nation warfare features.
- Profile actual performance before changing AI/ticking behavior.

## Safe operating cycle

1. Announce the restart and stop new progression activity.
2. Allow the server to flush every loaded dimension and shut down cleanly.
3. Back up the complete world and mod-specific saved data before changing mods, configs, scripts, or quests.
4. Apply one reviewed pack update as a unit; do not auto-update individual frozen mods.
5. Start against a copy or staging world first when registries, world generation, dimensions, colonies, or progression data changed.
6. Confirm mod construction, datapack load, world load, player join, configuration persistence, and a second clean restart.

## Back up more than region files

TSR persistence includes player data, teams, claims, quests, configuration, default configuration, mod capabilities, colonies, dimensions, and other mod-specific saved data. See [Backups & Recovery](backups-and-recovery.md) for the required scope.

## Profiling

Use spark and repeatable scenarios before changing ticking, pathfinding, entity activation, storage scanning, or structure generation. TSR does not publish a universal RAM figure because actual requirements depend on player count, world activity, colonies, and the final retained content stack.

See [Permissions](permissions.md), [Backups & Recovery](backups-and-recovery.md), and [Performance & Optimization](performance-and-optimization.md).

Base administration references: [Commands](tensura-reference/commands/index.md) · [Configuration](tensura-reference/configuration/index.md) · [Gamerules](tensura-reference/gamerules/index.md)
