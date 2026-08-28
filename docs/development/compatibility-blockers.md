# Compatibility Blockers

## TR Addon 2.0.1

- **Status:** `DEFERRED-BLOCKED`
- **Runtime disposition:** Excluded from the active Version 1 (Beta) pack
- **Review gate:** Check for a newer official release before release candidate freeze

TR Addon remains part of the design record and is not permanently rejected. The verified 2.0.1 public artifact cannot complete dedicated-server mod construction because its constructor races the creation of ManasCore's custom race and skill registries.

### Verified artifact

| Field | Value |
|---|---|
| CurseForge project | `1132105` |
| CurseForge file | `7899584` |
| Version | `2.0.1` |
| Filename | `traddon-neoforge-2.0.1.jar` |
| SHA-1 | `0cbb72baaf6a7c7008043b99b299326417a53bce` |
| SHA-256 | `38def0f47748e11a5d153a9dde57892c53f396a78dff97c9aaebf3ba631ece83` |

### Exact failure

The failure alternates between the ManasCore race and skill registries, consistent with parallel mod construction:

```text
Failed to create mod instance. ModID: traddon
java.lang.IllegalArgumentException:
Registry ResourceKey[minecraft:root / manascore_race:races] does not exist!
    at TrAddonRaces.init(TrAddonRaces.java:21)
    at TrAddonRegistry.init(TrAddonRegistry.java:18)
    at TrAddon.init(TrAddon.java:16)
    at TrAddonNeoForge.<init>(TrAddonNeoForge.java:11)
```

An equivalent run failed against the skill registry:

```text
java.lang.IllegalArgumentException:
Registry ResourceKey[minecraft:root / manascore_skill:skills] does not exist!
    at TrAddonUniqueSkills.init(TrAddonUniqueSkills.java:29)
```

### Compatibility matrix tested

| Test | Result |
|---|---|
| Phase 2 addon batch, NeoForge 21.1.248 and ManasCore 4.0.0.2 | Failed during TR Addon construction |
| TR Addon isolated with the Phase 1 foundation | Failed with the same missing registry |
| SlimeThrone Extras, Ascension, and Mysticism without TR Addon | Passed dedicated-server startup and clean shutdown |
| Diagnostic dependency-order metadata change | Failed; constructor dispatch remained parallel |
| Historical ManasCore 4.0.0.1 | Failed; missing registry varied between race and skill |
| Contemporaneous NeoForge 21.1.224 / FML 4.0.42 | Failed during TR Addon construction |

### Root cause assessment

TR Addon immediately registers content into ManasCore custom registries from its mod constructor. Its published descriptor does not declare direct dependencies on the embedded `manascore_race` or `manascore_skill` modules. FML performs mod construction in parallel, so ordinary dependency metadata does not serialize these constructor bodies. The alternating missing registry confirms a timing-sensitive constructor race rather than a regression limited to one current dependency version.

### Resolution policy

- Do not publish the diagnostic metadata-patched JAR.
- Do not create or distribute a fork while the upstream project is All Rights Reserved unless explicit author permission is obtained.
- Do not substitute another addon merely to preserve the mod count.
- Before release candidate freeze, check for a newer official release.
- Test any newer official artifact first against the Phase 1 foundation in isolation.
- Restore it only after both the isolated dedicated-server test and the complete Phase 2 startup pass.

Until those gates pass, TR Addon remains `DEFERRED-BLOCKED` and absent from the active client and server runtime.

## Tensura: Unique Monsters 1.0.2

- **Status:** `DEFERRED-BLOCKED`
- **Runtime disposition:** Removed from the active Phase 2 client and server runtime
- **Replacement:** None
- **CurseForge project/file:** `1489273 / 7844220`
- **SHA-1:** `0cbb72baaf6a7c7008043b99b299326417a53bce`
- **SHA-256:** `38def0f47748e11a5d153a9dde57892c53f396a78dff97c9aaebf3ba631ece83`

The official artifact can invoke `ExtraSkills.init()` during parallel mod
construction before ManasCore has created the `manascore_skill:skills` registry.
The resulting registry-order exception is reproducible; successful warm or
repeated starts are not considered a resolution. The previously tested
TSR lifecycle bridge was diagnostic only and is neither indexed nor distributed.

Re-entry requires a newer official artifact that corrects the registration
lifecycle/dependency ordering and passes isolated construction, repeated clean
cold Phase 2 starts, new-world creation, clean shutdown/restart, and a scan with
no registry-order exceptions. The full report is preserved in
`development/unique-monsters-compatibility.md`.

## Version 1 Beta playable profile

The playable beta test profile is a diagnostic export of the frozen design manifest. It does not amend the locked source manifest. Two additional frozen subsystem pairs are omitted from this profile because the exact pinned artifacts prevent startup:

| Pair | Runtime result | Playable-profile disposition |
|---|---|---|
| GriefLogger 1.2.7 + Tensura: Grief Logger 1.2.1 | GriefLogger's `MixinBucketItem` fails its required `onLiquidPlaced` injection during bootstrap. | Both server-side files are omitted together. FTB Backups 3 remains active; no replacement logger was added. |
| IceAndFire Community Edition 2.1.1 + Tensura Compat: Ice & Fire 2.0.0.1 | The compatibility mixin references the removed `com.iafenvoy.iceandfire.registry.IafStatusEffects` class and its former Architectury registry descriptor. | Both files are omitted together. No patch or substitute was distributed. |

The exact pinned artifacts remain in the Packwiz source and retain their frozen status. Restoring either pair requires project-owner direction after a compatible official artifact is identified and passes isolated construction, the complete server startup gate, world creation, client join, save, and restart.

### Playable-profile validation

With only those two blocker pairs omitted, the assembled server reached `Done` on a new world, generated the Tensura dimensions, saved every dimension, stopped cleanly, reloaded the saved world, and stopped cleanly again. A later restart loaded the reviewed stability defaults and the FTB Quests onboarding chapter with 8 quests.
