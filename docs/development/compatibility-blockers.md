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
