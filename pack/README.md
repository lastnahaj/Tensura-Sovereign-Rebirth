# Pack source

This directory is the authoritative Packwiz source for Tensura: Sovereign Rebirth.
It contains metadata references and pack-owned overrides, not mirrored third-party
mod JARs.

- Minecraft: 1.21.1
- Loader: NeoForge 21.1.248
- Java: 21
- Pack version: 1.0.0-beta.1

Run `tools/packwiz.ps1` from the repository root to use the locally installed or
system Packwiz executable with repository-local cache and configuration paths.

Run `tools/export_client.ps1` to build and validate both launcher formats under
`dist/`. The CurseForge ZIP is reproducibly sourced from the pinned project/file
references. The Modrinth output is a local validation artifact until the
platform-availability audit in `docs/development/platform-availability.md` is
complete.

A public Modrinth release requires every active third-party artifact to have an
exact allowed-domain download URL and checksum, or explicit permission to
redistribute a hash-locked embedded JAR. CurseForge-only metadata is not treated
as dual-platform proof. Run with `-RequirePublishableModrinth` for the release
gate; it must remain blocked while any active entry is `MODRINTH-PENDING`.
