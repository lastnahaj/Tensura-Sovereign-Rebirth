# TSR Silent Gear Metalworks Compat

This pack-owned NeoForge mod corrects Productive Metalworks fluid-unit data when Silent Gear Metalworks is installed without Silent Gems.

The compatibility artifact registers a required, top-priority built-in datapack. Its narrowly scoped resource filter blocks only the lower-priority fluid-unit map before validation, then supplies the corrected effective map. The map preserves Productive Metalworks defaults and the seven Silent Gear fluids present in the Version 1 Beta runtime while conditionally excluding the 21 optional Silent Gems fluids.

After each data-map update, the mod verifies the installed Metalworks mappings and fails fast if the required entries disappear or optional Silent Gems entries load without their owning mod.

Build from the repository root with:

```powershell
compat\tsr-unique-monsters-compat\gradlew.bat -p compat\tsr-sgear-metalworks-compat build
```

The build verifies the tested upstream JAR hashes before creating a reproducible artifact.
