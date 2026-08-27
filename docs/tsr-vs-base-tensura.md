# TSR vs Base Tensura

The wiki has two connected layers. The generated **Tensura: Reincarnated Reference** explains the upstream base mod; the handcrafted **Tensura: Sovereign Rebirth** guides explain the pack's installed systems, configuration, integrations, restrictions, and validation state.

| Question | Base Tensura reference | TSR layer |
|---|---|---|
| What does a race, skill, spell, item, mob, or mechanic do? | Upstream article data and version history | A TSR note only when the pack changes the context |
| Is it present in the beta? | Not sufficient evidence | Verified against Packwiz metadata, configuration, artifacts, and phase reports |
| What values does TSR use? | Upstream defaults may be historical | Tracked configuration wins when a value has been validated |
| How does another mod interact with it? | Outside the base article's scope | Compatibility matrix and subsystem guides |
| Is planned behavior working? | Not applicable | Status is explicitly Planned, Under Validation, Blocked, or Verified |

## Version boundary

TSR targets **Minecraft 1.21.1**, **NeoForge 21.1.248**, and **Java 21**. The upstream wiki preserves useful history from older releases. A historical page explains upstream behavior in its own context; it does not prove that the feature exists unchanged in TSR's frozen runtime.

## Status vocabulary

- **Implemented** — present in tracked pack source or documentation output.
- **Verified** — supported by a recorded build, startup, configuration, or targeted test.
- **Under Validation** — present or staged, but a required gameplay or integration gate remains.
- **Planned** — design target without a completed implementation.
- **Known Issue** — present with documented limitations.
- **Blocked** — cannot enter the active runtime until a specific failure is resolved.
- **Removed** — intentionally excluded from TSR.
- **Historical** — retained as technical or upstream version context.

## Start with the right layer

- Browse the [Tensura: Reincarnated Reference](tensura-reference/index.md) for base races, abilities, magic, mobs, equipment, structures, commands, and configuration.
- Use [Progression Overview](progression-overview.md) for the connected TSR journey.
- Use [Mod Manifest](mod-manifest.md) and [Compatibility Matrix](compatibility-matrix.md) for current pack decisions.
- Use [Ingestion Coverage](project/ingestion-coverage.md) for the exact upstream snapshot and exceptions.
