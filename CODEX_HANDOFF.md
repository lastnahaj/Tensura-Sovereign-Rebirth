# Tensura: Sovereign Rebirth — Build Handoff

This file is the machine-readable starting point for the next maintainer or
Codex task. It describes the repository state on `build/version-1-beta`, the
tested artifacts, and the remaining release gates.

## Project target

- Minecraft `1.21.1`
- NeoForge `21.1.248`
- Java `21`
- Pack format: Packwiz source with separate client and dedicated-server exports
- Branch: `build/version-1-beta`

## Verified and present

- Core Tensura progression, ManasCore, MineColonies, Iron's Spells, Gear
  Evolution, storage, claims, permissions, and server administration layers
  are represented in `data/mod-manifest.json` and `pack/mods/`.
- Artifacts `13.2.3`, Supplementaries Squared `1.21-1.2.18`, and Tensura:
  Ancient Artifacts `1.0.3` are active with exact Modrinth checksum pins and
  matching CurseForge project/file identities.
- The client profile contains 156 JARs; the server profile contains 129 JARs.
- `pack/config/` contains reviewed defaults, including client video/input
  settings, Xaero map defaults, Tensura skill controls, server stability
  baselines, artifact configs, and the authored FTB Quests files.
- The quest content currently loads 8 chapters and 64 quests. Custom quest
  backgrounds are under `pack/kubejs/assets/tsr/textures/gui/quests/`.
- FancyMenu/Drippy presentation assets and the widescreen TSR menu are in the
  client profile. The graphical smoke test passes.
- The keybinding persistence fix is the active
  `compat/tsr-client-stability/` JAR. The old KubeJS keybinding workaround is
  not active. Two full client restarts have preserved changed and unbound keys.
- Dedicated-server cold and warm runs with the three artifact additions pass
  clean-world construction, quest loading, save, shutdown, and restart. Logs:
  `.build/test-logs/three-artifacts-server-cold.log` and
  `.build/test-logs/three-artifacts-server-warm.log`.
- The active client graphical smoke log is
  `.build/client-playable-beta-rc/client-smoke-console.log`.

## Deferred or excluded from the active runtime

- TR Addon `2.0.1` is `DEFERRED-BLOCKED` because its public artifact has a
  reproducible dedicated-server constructor race with ManasCore registries.
- Tensura: Unique Monsters `1.0.2` is `DEFERRED-BLOCKED` because parallel
  construction can call `ExtraSkills.init()` before the ManasCore skill
  registry exists. No diagnostic bridge or patched JAR is distributed.
- The C2ME alpha artifact is deferred after a clean-shutdown hang.
- Frozen Ice & Fire and GriefLogger compatibility pairs remain documented but
  are omitted from the playable profile after reproducible startup failures.
- No unofficial fork or patched upstream artifact is part of the pack.

The full reports are in `docs/development/compatibility-blockers.md` and the
compatibility matrix. Re-entry requires an official artifact and the staged
tests described there.

## Platform audit

`docs/development/platform-availability.md` records platform identity and
redistribution status separately from runtime compatibility. The active source
has 165 Packwiz mod metadata files, 164 CurseForge identities, and 36 exact
Modrinth project/version identities. The private beta Modrinth export remains
for local tester import until every active entry has a public Modrinth source
or documented redistribution permission.

The latest colony audit found:

- Lunara Colonies has matching 1.21.1 NeoForge listings on both platforms, but
  its artifact still needs to be downloaded, checksum-pinned, and tested.
- JadeColonies, Minecolonies Questline, and Stylecolonies have verified
  CurseForge 1.21.1 NeoForge files but no located official Modrinth artifact;
  they are not active in the dual-platform pack.

## Remaining work before release candidate freeze

1. Stage and hash-lock any approved dual-platform additions, then run
   `packwiz refresh` from `pack/`.
2. Re-run `tools/validate_pack.py` and
   `tools/validate_config_reconstruction.py`.
3. Repeat dedicated-server cold, warm, new-world, save, clean shutdown, and
   restart tests after the final metadata set is frozen.
4. Repeat the graphical client smoke test and verify keybindings persist after
   a second clean restart.
5. Complete gameplay validation for Gear Evolution component persistence,
   Ascension boss scaling, LuckPerms non-OP permissions, claim protection,
   YIGD, Embeddium, worldgen density, multiplayer profiling, and ServerCore.
6. Expand the authored campaign beyond the current onboarding set only with
   registry-backed task and reward types.
7. Recheck upstream TR Addon and Unique Monsters releases before the release
   candidate freeze. Test a newer official artifact in isolation, then in the
   full Phase 2 runtime, before restoring either addon.
8. Run the final CurseForge and Modrinth export validators and retain the
   resulting checksums with the release notes.

## Useful commands

```powershell
Set-Location pack
..\.build\tools\packwiz\packwiz.exe refresh
Set-Location ..
$py = 'C:\Users\LastN\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py tools\validate_pack.py
& $py tools\validate_config_reconstruction.py
```

Do not remove or substitute a frozen core mod to resolve a conflict. Record a
blocker and stop the affected phase when a frozen subsystem cannot pass its
required construction or gameplay tests.
