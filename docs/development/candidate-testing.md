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
