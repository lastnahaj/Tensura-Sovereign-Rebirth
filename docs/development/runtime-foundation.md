# Runtime Foundation

The first playable subsystem locks Tensura: Reincarnated and every dependency
declared by its artifact metadata. Packwiz downloads each artifact from its
canonical project; no third-party JAR is stored in the repository.

## Locked artifacts

| Mod | Version | Provider identity | Artifact hash |
|---|---:|---|---|
| Tensura: Reincarnated | 2.0.1.2 | CurseForge `643695 / 8665599` | SHA-1 `f6f0c8ce46b77a1996c5986d029411878142112f` |
| ManasCore | 4.0.0.2 | CurseForge `619025 / 8022425` | SHA-1 `f11a0062d7829e26a8705183762a5e0f2d022dd3` |
| Architectury API | 13.0.11 | CurseForge `419699 / 8492726` | SHA-1 `008656a0702801174b8ec245ed7aad1921d6e9f1` |
| GeckoLib | 4.9.2 | CurseForge `388172 / 8350073` | SHA-1 `14c64013cadee7d28f3685f94350f9a4d2ec6d86` |
| SmartBrainLib | 1.16.11 | CurseForge `661293 / 7055149` | SHA-1 `0310135a01eeceefbc7f1ab017498a65f3ad6836` |
| TerraBlender | 4.1.0.8 | CurseForge `940057 / 6054947` | SHA-1 `744394d979b422be560babf9df7a6800ede9ac5b` |

TerraBlender is pinned explicitly because Tensura's packaged NeoForge metadata
requires version 4.1.0.0 or newer, although the CurseForge relationship list did
not expose it as a dependency.

## Dependency audit

Tensura requires NeoForge 21.1 or newer, Minecraft 1.21.1 or newer,
ManasCore race, skill, and storage modules 3.0.2.9 or newer, Architectury
13.0.8 or newer, GeckoLib 4.7.5 or newer, SmartBrainLib 1.16.7 or newer,
and TerraBlender 4.1.0.0 or newer. NeoForge 21.1.248 satisfies the loader
ranges. ManasCore 4.0.0.2 embeds the required race, skill, and storage modules
at the same version.

## Runtime verification

An isolated NeoForge server installed the six pinned artifacts through Packwiz.
The first world boot loaded 3,826 recipes and 2,345 advancements, generated the
Tensura labyrinth, and reached ready in 8.694 seconds. A warm restart reached
ready in 1.799 seconds. Both runs stopped normally and saved the Overworld,
Nether, End, boss area, labyrinth, and hell dimensions.

The official NeoForge client runtime and all six Packwiz artifacts also install
successfully in an isolated client instance. A graphical menu/world test remains
pending because that disposable instance has no authenticated launcher session
or downloaded asset set.

The server generated 47 common configuration files, including the full Tensura
ability, energy, entity, race, reincarnation, and client-default trees. Phase
2A promoted these files into the Packwiz source together with the reviewed
addon configuration baseline.

## Observed warnings

TerraBlender and GeckoLib emit missing development-refmap warnings from their
packaged mixin declarations. NeoForge also reports its expected union asset URL
schema warnings on the dedicated server. On warm world load, Tensura briefly
skips the saved `GazelDwargoArena` state before loading and reloading the matching
boss configuration. The server then reaches ready with no missing dependency,
class, or mixin failure.
