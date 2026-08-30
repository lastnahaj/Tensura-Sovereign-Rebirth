# Publishing Kit

This directory contains the copy and release metadata for publishing **Tensura:
Sovereign Rebirth 1.0.0-beta.1**. The copy is written for Minecraft 1.21.1,
NeoForge 21.1.248, and Java 21.

## Paste-ready files

- `STOREFRONT_DESCRIPTION.md` — shared long description for CurseForge and
  Modrinth.
- `CURSEFORGE_UPLOAD.md` — CurseForge project fields, file metadata, and
  moderator notes.
- `MODRINTH_UPLOAD.md` — Modrinth project/version fields and publication gate.
- `RELEASE_NOTES_1.0.0-beta.1.md` — public beta changelog.
- `QUEST_STATUS.md` — exact playable-beta quest scope and remaining campaign
  work.
- `SERVER_FILE.md` — server additional-file description and installation copy.
- `SUPPORT.md` — player support, installation, updating, and bug-report copy.
- `GALLERY_AND_BRANDING.md` — existing artwork, alt text, and screenshot
  captions.
- `COMPAT_PROJECTS.md` — project-page copy for the two TSR-owned runtime
  modules.
- `OWNER_CHECKLIST.md` — decisions and permission work that cannot be inferred
  from the build.

## Current artifact disposition

| Artifact | Current use | Public upload status |
|---|---|---|
| CurseForge client ZIP | CurseForge/Prism custom-profile import | Structurally valid; publish the two TSR-owned modules as platform projects and regenerate before submission |
| Modrinth MRPACK | Private tester import | Do not submit publicly until the Modrinth permission/source gate passes |
| Dedicated-server ZIP | Private server deployment | Attach to the approved CurseForge beta as its server additional file |

The current Modrinth archive is intentionally a private-import artifact. The
active launcher reference includes 131 exact artifacts pinned on both
platforms, 73 exact artifacts currently pinned only on CurseForge, Ponder from
the official Create Maven repository, and TSR-owned runtime modules. Public
Modrinth publication requires permission for every embedded artifact or the
same exact file hosted on Modrinth.

## Submission order

1. Confirm the public project license, support URL, wiki availability, and
   rights to the selected project artwork.
2. Create project pages for **TSR Client Stability** and **TSR Silent Gear
   Metalworks Compat** on both platforms using `COMPAT_PROJECTS.md`.
3. Replace the two embedded TSR JARs with platform project/version references
   and regenerate both client exports.
4. Verify that Ponder remains accepted under CurseForge's approved
   non-CurseForge content rules.
5. Upload the CurseForge client ZIP as a **Beta** file. Add the server ZIP as
   the main file's **Additional File**.
6. Resolve every item in the Modrinth permission/source audit, regenerate with
   `tools/export_client.ps1 -RequirePublishableModrinth`, and submit the
   resulting `.mrpack` as a **Beta** version.
7. Import both final downloads through their target launchers before marking
   either file public.

## Official platform references

- [CurseForge modpack export and submission](https://support.curseforge.com/support/solutions/articles/9000197908-exporting-a-modpack-for-curseforge-project-submission)
- [CurseForge project submission fields](https://support.curseforge.com/support/solutions/articles/9000197241-creating-and-submitting-a-project)
- [CurseForge moderation policies](https://support.curseforge.com/support/solutions/articles/9000197279-project-and-modpack-moderation-policies)
- [Modrinth modpack permissions](https://support.modrinth.com/en/articles/8797527-obtaining-modpack-permissions)
- [Modrinth modpack sharing](https://support.modrinth.com/en/articles/8797522-sharing-modpacks)
- [Modrinth `.mrpack` format](https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack)
