# World Generation

TSR separates the base mod's world content from the pack's broader terrain and structure policy.

## Base Tensura world

The local reference includes every maintained upstream article currently documented for [biomes](tensura-reference/biomes/index.md), [structures](tensura-reference/structures/index.md), [mobs](tensura-reference/mobs/index.md), and [bosses](tensura-reference/bosses/index.md). Those pages retain upstream version context and do not imply that every historical entry has been runtime-verified in TSR.

## Terratonic foundation

<span class="tsr-status">Under Validation</span>

The required Version 1 Beta terrain target combines **Terralith** and **Tectonic**, with **Lithostitched** where required by their exact artifacts. TSR refers to this pairing as its **Terratonic** foundation.

The terrain stack is selected, but the repository does not yet contain a completed phase report for clean world creation, saved-world restart, representative biome coverage, or the complete structure stack on that terrain. Until those gates pass, Terratonic remains **Under Validation**, not Verified.

## Structure policy

TSR intentionally limits structure density. Additions are evaluated for:

1. clean generation on Terralith and Tectonic terrain,
2. clipping and collision behavior,
3. distinct gameplay purpose,
4. exploration pacing,
5. chunk-generation cost,
6. multiplayer reliability,
7. restart and persistence behavior.

General structure content may enter the candidate process without a Tensura bridge, but boss or progression integrations must be explicit before they are described as Tensura-aware.

## Validation gates

- new-world creation and clean shutdown,
- saved-world restart,
- representative `/locate` and biome checks,
- new-chunk exploration,
- Tensura structure and Labyrinth generation,
- portal and return-path behavior for retained dimensions,
- collision and density review,
- server generation profiling before pregeneration.

Chunky pregeneration begins only after the terrain and retained structure set are frozen.
