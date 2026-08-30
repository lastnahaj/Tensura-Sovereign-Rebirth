# Candidate Testing

Candidate mods do not enter the active manifest as a group. Each candidate is added to the last passing runtime, verified by exact artifact hash, and tested through the subsystem gates that match its risk.

## Required gates

1. Isolated dependency and construction check.
2. Complete-runtime clean dedicated-server start.
3. New-world or new-chunk generation when content affects worldgen.
4. Flushed save, clean shutdown, and warm restart.
5. Graphical client resource and rendering start when the mod has client content.
6. Targeted gameplay checks for recipes, loot, structures, entities, permissions, or persistent components.
7. Removal test when the candidate is optional, confirming that no pack-owned data retains a hard dependency.

Warm or repeated starts do not replace a clean/cold construction test. A candidate that fails a required gate is removed from the active test runtime and documented with its exact artifact, failure, and re-entry criteria.

## World-generation order

Terrain is established before structures. The required Terralith and Tectonic pair must pass as the baseline. Structure candidates are then added one at a time in this order: YUNG's Better Dungeons, Better Mineshafts, Better Strongholds, Better Nether Fortresses, Repurposed Structures, Sparse Structures, and finally When Dungeons Arise if its density and performance remain acceptable.

Each structure step requires clean generation, representative `/locate` checks, new-chunk exploration, density review, and restart. Boss content that adds structures or entities is tested as its approved content-plus-Tensura-compatibility pair.

## Release-candidate review

Before release candidate freeze, all retained candidates must have a recorded pass in the phase reports and compatibility matrix. Deferred blockers are rechecked only against newer official artifacts, beginning with isolated construction before full-runtime restoration.

## FTB Chunks x Xaero's Map Compat

- Artifact: 1.1.4, CurseForge project `1357724`, file `8103626`, NeoForge 1.21.1.
- Purpose: expose FTB Chunks claims and claim-edit controls on Xaero's Minimap and World Map.
- Dependency metadata: Architectury API 13.0.8 or newer (already present in the TSR runtime); FTB Chunks and both Xaero map mods are already pinned.
- Current disposition: `PENDING-VERIFICATION`.
- Remaining gates: verify the official JAR hash, run client construction/resource reload, connect to a dedicated server, confirm claim visibility and map-side claim editing, then confirm the server payload remains unchanged.
- Distribution note: the project is listed on CurseForge but no Modrinth project was found, so it remains outside the dual-platform release gate unless an explicit CurseForge-only client exception is approved.

## Artifact and decoration additions

- Artifacts 13.2.3, Supplementaries Squared 1.21-1.2.18, and Tensura: Ancient Artifacts 1.0.3 are active in the beta runtime.
- Exact official NeoForge 1.21.1 releases are pinned on both CurseForge and Modrinth.
- Complete-runtime clean-world construction, 64 authored quest loading, flushed save, clean shutdown, saved-world restart, and graphical client resource loading pass.
- Artifacts campsite attempts are capped at 16 per chunk in the pack baseline. Targeted loot frequency, Curios equipment behavior, refinement persistence, and Gear Evolution progression overlap remain release-candidate gameplay checks.
