# Modrinth Upload Copy

## Project fields

**Project type:** Modpack

**Title:** Tensura: Sovereign Rebirth

**Slug:** `tensura-sovereign-rebirth`

**Summary:** Reincarnate, evolve, forge legendary gear, build a nation, and
conquer a quest-driven Tensura RPG world.

**Featured categories:** Adventure, Magic, Quests

**Additional categories:** Exploration, Multiplayer, Combat, Optimization

**Environment:** Client and server

**License:** All Rights Reserved is the conservative choice for the pack's
original configuration, quest, compatibility, and branding work. The project
owner must confirm this selection before submission.

**Body:** Paste the complete contents of `STOREFRONT_DESCRIPTION.md`.

**Wiki URL:** https://lastnahaj.github.io/Tensura-Sovereign-Rebirth/

**Issues URL:** https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/issues/new/choose

Leave the source URL empty while the repository remains private.

## Version fields

**Primary file:** `Tensura-Sovereign-Rebirth-1.0.0-beta.1-Playable-Modrinth.mrpack`

**Version name:** Tensura: Sovereign Rebirth 1.0.0 Beta 1

**Version number:** `1.0.0-beta.1`

**Version type:** Beta

**Game version:** 1.21.1

**Loader:** NeoForge

**Environment:** Client and server

**Featured:** No, until beta feedback confirms the release candidate.

**Changelog:** Paste `RELEASE_NOTES_1.0.0-beta.1.md`.

## Public publication gate

Do **not** upload the current `.mrpack` as a public Modrinth version. It is a
valid private tester import, but it embeds files whose public Modrinth
redistribution status is not complete.

The reconciled launcher reference currently records:

- 131 active exact artifacts pinned on both CurseForge and Modrinth;
- 73 active exact artifacts currently pinned only on CurseForge;
- Ponder from the official Create Maven repository;
- two TSR-owned runtime modules that need their own Modrinth projects.

For each non-Modrinth artifact, complete one of these before submission:

1. reference the same exact official file uploaded to Modrinth;
2. document a license that permits redistribution;
3. document an explicit project statement allowing Modrinth modpack use; or
4. obtain author permission and attach the evidence in the project's
   moderation area.

All Rights Reserved artifacts without explicit permission must not be embedded
in a public `.mrpack`. The exact audit is stored in
`data/client-runtime-reconciliation.json` and summarized in
`docs/development/platform-availability.md`.

After the gate is resolved, regenerate with:

```powershell
.\tools\export_client.ps1 -OutputDirectory dist -PlayableProfile -RequirePublishableModrinth
```

Only submit an archive produced by that strict export.

## Moderator note

Use this note only after the strict export passes:

> Tensura: Sovereign Rebirth is a Minecraft 1.21.1 NeoForge modpack. Every
> referenced file is either the exact Modrinth-hosted version or has documented
> redistribution permission recorded in the project moderation materials. The
> two TSR compatibility modules are original pack components published as
> separate Modrinth projects. The pack includes client and server overrides and
> has been import-tested through a clean launcher profile.
