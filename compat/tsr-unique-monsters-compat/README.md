# TSR Unique Monsters Compat

This NeoForge compatibility mod retains the official Tensura: Unique Monsters 1.0.2 artifact while correcting its ManasCore Skill registration lifecycle.

One required Mixin redirects only the premature `ExtraSkills.init()` call inside `TRUniqueMobsRegistry.injectInit()`. A second required Mixin invokes the original method at the tail of ManasCore `SkillRegistry` class initialization, after the custom registry and key have been assigned. A third, exact-key bridge supplies that captured registrar only to the Unique Monsters Architectury provider while parallel construction is active. Architectury can then queue the original skill entry for the normal `RegisterEvent`. The common setup check fails closed unless both lifecycle hooks ran exactly once and `tr_unique_monsters:appraisal_eye` is present.

The build accepts the directory containing the verified TSR runtime JARs through `-PruntimeModsDir=<path>` or `TSR_RUNTIME_MODS_DIR`. It validates the exact Unique Monsters, ManasCore, Tensura, and Architectury SHA-256 hashes before compiling.

Build on Java 21:

```text
gradlew.bat clean build -PruntimeModsDir=<verified-runtime-mods-directory>
```

The upstream Unique Monsters JAR is neither modified nor included in this project.
