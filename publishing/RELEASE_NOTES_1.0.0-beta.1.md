# Tensura: Sovereign Rebirth 1.0.0 Beta 1

The first playable Version 1 Beta assembles the complete client and dedicated
server profiles for Minecraft 1.21.1 and NeoForge 21.1.248.

## Highlights

- Built a 209-JAR client profile and a separately filtered 175-JAR dedicated
  server profile.
- Added eight TSR-authored quest chapters alongside the active MineColonies
  integration chapter, for 140 loaded FTB Quests entries in the tested runtime.
- Added custom quest backgrounds and direct project-wiki links.
- Added the custom TSR main menu and Drippy loading presentation with native
  widescreen artwork.
- Added Beyond Adventures, Artifacts, Supplementaries Squared, Tensura:
  Ancient Artifacts, the expanded colony and structure stack, and the current
  client quality-of-life profile.
- Added FTB Essentials and server-only TAB to the server administration stack.
- Added conservative default configuration for server stability, generation,
  networking, storage, backups, and client performance.
- Set first-launch defaults to a 150 FPS cap, GUI scale 2, render distance 8,
  simulation distance 8, Bright brightness, VSync off, and view bobbing off.
- Set the default Xaero minimap to circular and top-right.
- Assigned Tensura skill activation slots to Z, X, and C while clearing
  conflicting nonessential defaults.
- Fixed client keybind changes being overwritten during startup. Changed and
  unbound controls persisted through two complete restart tests.
- Kept optional resource-pack selection empty for the initial beta.

## Validation completed

- Clean dedicated-server world creation, save, and shutdown.
- Warm dedicated-server restart from the saved world.
- Clean-world startup from the extracted delivery server ZIP.
- All nine active chapters and 140 FTB Quests entries loaded.
- Full graphical client startup, resource loading, and branded main menu.
- Changed keybinding persistence across two full client restarts.
- CurseForge manifest and Modrinth archive structure validation.
- Final archive scan for intentionally excluded and diagnostic JARs.

## Deliberately excluded

- Tensura Skill Trainer 2.0.5 is player-managed and not distributed.
- TR Addon 2.0.1 remains deferred after a reproducible ManasCore registry
  construction race on dedicated servers.
- Tensura: Unique Monsters 1.0.2 remains deferred after a reproducible
  ManasCore skill-registry startup race.
- C2ME 0.4.0-alpha.0.120 remains deferred after a clean-shutdown hang.
- The diagnostic Unique Monsters bridge, disabled Tensura FancyMenu bridge,
  blocked GriefLogger pair, and blocked Ice & Fire compatibility pair are not
  included.

## Beta notice

Back up worlds before updating. Extended progression balance, non-OP
permissions, claim protection, long-duration world generation, high-concurrency
multiplayer, and late-game boss scaling remain active beta-test targets.
