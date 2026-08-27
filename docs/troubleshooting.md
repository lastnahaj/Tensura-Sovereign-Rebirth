# Troubleshooting

## General rule

Always report:
- TSR version
- Minecraft version
- NeoForge version
- client or dedicated server
- relevant crash/log section
- whether the problem occurs on a fresh world
- whether the issue reproduces without test/optional mods

## Player problems

### Wrong Java or loader
Confirm Java 21, Minecraft 1.21.1, and NeoForge 21.1.248 before changing mods or deleting configuration.

### Quest or menu presentation
The handcrafted campaign and FancyMenu/Drippy presentation are not complete in the current tracked beta. Missing planned presentation is not equivalent to a runtime corruption.

## Server problems

### MineColonies/Tensura behavior
Confirm the pinned MineColonies compatibility branch and required libraries have not been auto-updated independently.

### Missing recipes/items
Check whether TSR intentionally disables redundant Tom's Storage or overlapping content through KubeJS.

### Gear loses data after evolution
This is a release blocker. Record the original item, evolution step, components/upgrades, and resulting item.

### Claim protection failure
Record the exact Tensura skill/action, claim ownership/team relationship, and whether PvP is enabled.

### Performance regression
Capture a spark profile before changing random optimization settings.

### Quest does not detect progress
Do not force-complete it as a permanent fix. The detector/registry/API condition must be verified in the assembled pack.

## Developer problems

Registry construction failures, compatibility patches, and version-specific stack traces belong in [Compatibility Blockers](development/compatibility-blockers.md) and the subsystem phase reports, not in player-facing reference pages.
