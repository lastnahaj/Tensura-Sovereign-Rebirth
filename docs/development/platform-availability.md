# Platform Availability Audit

## Scope

This audit covers the Version 1 Beta Packwiz source for Minecraft 1.21.1 and
NeoForge 21.1.248. Review date: 2026-08-30. Platform availability is tracked
separately from runtime compatibility: a private import can work even when an
artifact is not eligible for public redistribution on the other platform.

The exact 209-file launcher reference is recorded in
`data/client-runtime-inventory.json`. Its disposition and provider identities
are recorded in `data/client-runtime-reconciliation.json`.

## Current source coverage

The source contains 217 mod metadata files:

- 216 have a CurseForge project/file identity.
- 141 have both CurseForge and Modrinth project/version identities.
- Ponder uses the official Create Maven artifact with a SHA-256 pin.
- Two project-local TSR JARs are checksum-locked in repository validation.

The reconciled launcher reference contains 206 active files and three excluded
files. Of the active reference files, 131 have identities on both platforms,
73 currently resolve only through CurseForge, one is the Maven-hosted Ponder
dependency, and one is the project-local Silent Gear Metalworks bridge.

The CurseForge ZIP and Modrinth MRPACK are both valid private-beta imports. The
MRPACK embeds the artifacts that lack an allowed Modrinth download source, so
it is not certified for public Modrinth publication. The exact exception list
is machine-readable in the reconciliation report and is enforced by
`tools/export_client.ps1 -RequirePublishableModrinth` for a public candidate.

## Explicit non-shipping entries

| Mod | Disposition | Distribution rule |
|---|---|---|
| Tensura Skill Trainer 2.0.5 | `USER-OPTIONAL-NOT-SHIPPED` | Players may install it independently; no client or server profile includes it |
| C2ME 0.4.0-alpha.0.120 | `DEFERRED-BLOCKED` | Excluded after a clean dedicated-server shutdown hang |
| Tensura Compat: FancyMenu 0.1.1-beta | `DISABLED-NOT-SHIPPED` | The reference instance had the artifact disabled; base FancyMenu and Drippy remain active |
| TR Addon 2.0.1 | `DEFERRED-BLOCKED` | Excluded after the reproduced ManasCore construction race |
| Tensura: Unique Monsters 1.0.2 | `DEFERRED-BLOCKED` | Excluded after the reproduced ManasCore skill-registry race |

## Server administration additions

FTB Essentials 2101.1.10 is active on both profiles. TAB 5.5.0 is server-only
and is pinned to CurseForge project/file `1232967 / 7659430` and Modrinth
project/version `gG7VFbG0 / 7TrBCyBl`. Both passed the expanded dedicated-server
cold-start and warm-restart tests.

## Known public-Modrinth exceptions

The active private beta intentionally retains exact CurseForge artifacts when
no matching Modrinth release was verified. This includes parts of the FTB,
Tensura, MineColonies style/integration, and utility stacks. It also includes
the newly active JadeColonies, Minecolonies Questline, Stylecolonies, and the
selected Lunara Colonies 1.21.1.28 artifact. These are not silently removed or
substituted to satisfy a platform count.

Ponder is reproducibly pinned to the official Create Maven repository, but that
host is outside Modrinth's restricted public-download allow-list. Project-local
TSR compatibility JARs likewise require an explicit publication and licensing
decision before public Modrinth submission.

## Release gate

Public dual-platform release requires every active entry to have either:

1. exact official CurseForge and Modrinth provider identities with an allowed
   download source, or
2. documented redistribution permission for the checksum-locked artifact.

Until that gate passes, the generated MRPACK is for private tester import only.
