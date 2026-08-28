# Platform Availability Audit

## Scope

This audit covers the active `pack/mods/*.pw.toml` source on the
`build/version-1-beta` branch for Minecraft 1.21.1 and NeoForge 21.1.248.
Review date: 2026-08-28.
It records distribution-platform evidence separately from runtime
compatibility. A project page on both sites is not sufficient for release:
the exact loader-specific artifact, checksum, environment, and redistribution
terms must also agree.

## Current source coverage

The source contains 133 active mod metadata files:

- 132 record an exact CurseForge project/file reference.
- 1 (Ponder) uses the official Create Maven artifact with a SHA-256 pin.
- 4 (Beyond Adventures, Entity Culling, JEI, and ServerCore) use official
  Modrinth CDN URLs and checksum pins while retaining matching CurseForge
  project/file identities.

The CurseForge side is therefore reproducibly pinned. Most of the Modrinth side
is not yet release-certified. Packwiz can produce a local `.mrpack` by embedding files
that do not have an allowed-domain download source, but that is not a valid
public Modrinth distribution for the current third-party licensing mix.

The official Modrinth catalog does contain matching project pages for several
of the frozen Tensura entries, including [Tensura: Reincarnated](https://modrinth.com/mod/tensura-reincarnated), [Better
Subordinates](https://modrinth.com/mod/tensura-better-subordinates), [SlimeThrone
Extras](https://modrinth.com/mod/tensura-slimethrone-extras), [Mysticism](https://modrinth.com/mod/tensura-mysticism), and [Unique
Monsters](https://modrinth.com/mod/tensura-unique-monsters). Those pages confirm
1.21.1 NeoForge availability where applicable, but they do not by themselves
provide the exact hash-locked artifact selected by this branch.

The private beta `.mrpack` therefore contains four native Modrinth downloads
and embeds the remaining eligible client artifacts. That file is suitable for
local tester import, but the embedded third-party files keep it behind the
public Modrinth publication gate.

## Beyond Adventures

Beyond Adventures is a valid official project on both platforms and targets
Minecraft 1.21.1 with NeoForge support:

| Platform | Project | Selected artifact | Status |
|---|---|---|---|
| Modrinth | [`tensura_beyond_adventures`](https://modrinth.com/mod/tensura_beyond_adventures) | NeoForge 1.1.9 (`Ybm5N8pk`) | Pinned to the official CDN URL and SHA-512 checksum |
| CurseForge | [Beyond Adventures](https://www.curseforge.com/minecraft/mc-mods/beyond-adventures) | NeoForge 1.1.9 (file `8634809`) | Exact project/file identity is recorded for CurseForge export |

Both platforms now expose the selected 1.1.9 NeoForge release. The Packwiz
entry downloads the official Modrinth-hosted bytes, records SHA-512
`db5951096dceba302ae36cea58d140c462fbe91b92948c7e57266e63988afb9a5ac584f7d7cacc8e5c5f7bdf69a12d32c8d1abd71dd9ac988264d3fe5e95876b`,
and retains the CurseForge identity for native launcher export. The playable
server profile passed clean-world startup, authored quest loading, save,
shutdown, and warm restart with the artifact active.

## Known unresolved active entries

- The FTB stack (including FTB Chunks, FTB Teams, FTB Library, FTB Quests,
  FTB Essentials, and FTB XMod Compat) is currently represented by CurseForge
  metadata only. No matching loader-specific Modrinth artifact/checksum record
  is present in this branch; FTB Chunks is also described as CurseForge-only by
  [current Modrinth compatibility listing](https://modrinth.com/mod/claim-intrusion-alert).
- The pack-owned TSR compatibility JARs are project-local artifacts rather than
  published Modrinth projects. They require a publication/redistribution
  decision before a public `.mrpack` can be certified.
- Ponder is pinned to the official Create Maven URL. It is reproducible, but its
  source host is not in the current restricted Modrinth export allow-list, so it
  needs an approved Modrinth source record before submission.

## Release gate

The active pack is dual-platform release-ready only when every active entry has
one of these records:

1. an exact official Modrinth CDN URL and checksum plus its CurseForge project/
   file identity, or
2. documented redistribution permission for a hash-locked embedded artifact.

Entries that lack either record remain in the audit as `MODRINTH-PENDING`; they
are not silently replaced or removed from the frozen runtime. The
`tools/export_client.ps1 -RequirePublishableModrinth` path and
`tools/validate_exports.py --require-publishable-modrinth` are the final
mechanical gates once the source records are complete.
