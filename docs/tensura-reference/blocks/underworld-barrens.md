---
title: Underworld Barrens
description: "An Underworld biome with Hound Dogs, Daemons, and a configured 104,000-Magicule baseline before other modifiers."
---

# Underworld Barrens

<span class="reference-badge">Tensura · Minecraft 1.21.1</span> <span class="reference-category">Biomes</span>

<section data-reference-section="biomes" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--theme"><img src="../../../assets/images/encyclopedia/underworld-barrens.webp" alt="Underworld Barrens conceptual landscape" loading="eager" decoding="async"><figcaption>Original TSR landscape · not an in-game screenshot</figcaption></figure>
<div class="reference-overview-copy"><p class="reference-eyebrow">Underworld field reference</p><h2>Daemon territory. Open your route carefully.</h2><p>An Underworld biome with Hound Dogs, Daemons, and a configured 104,000-Magicule baseline before other modifiers.</p><nav class="reference-quick-jumps" aria-label="Biome guide"><a href="#spawns">Spawn entries</a><a href="#magicules">Magicules</a><a href="#terrain-and-structures">Terrain &amp; structures</a></nav></div></section>

!!! note "Artifact and configuration checked · live world untested"
    This is a biome, not a collectible terrain block. The guide checks Tensura 2.0.1.2 resources and the tracked TSR configuration. Actual spawning, generated terrain, structure locations, and chunk Magicules have not been measured on the server.

<div class="tensura-reference-article" markdown="1">

<span id="Description"></span>

## Spawns

The base biome list and the tagged NeoForge additions are shown separately. **Arch Daemon is added through a biome modifier**, rather than appearing in the base biome JSON. Greater and Lesser Daemons also have Hell-tag additions; those entries are not collapsed into invented percentage chances.

| Mob | Weight | Group range | Resource route |
| --- | ---: | --- | --- |
| [Hound Dog](../mobs/mobs-hound-dog.md) | 70 | 1–1 | Biome definition |
| [Lesser Daemon](../mobs/mobs-lesser-daemon.md) | 40 | 1–1 | Biome definition |
| [Greater Daemon](../mobs/mobs-greater-daemon.md) | 5 | 1–1 | Biome definition |
| [Arch Daemon](../mobs/mobs-arch-daemon.md) | 1 | 1–1 | Hell-tag spawn addition |
| [Greater Daemon](../mobs/mobs-greater-daemon.md) | 30 | 1–1 | Hell-tag spawn addition |
| [Lesser Daemon](../mobs/mobs-lesser-daemon.md) | 60 | 1–1 | Hell-tag spawn addition |

Weights are relative selection inputs, not spawn percentages or measured encounter rates. Group bounds, spawn costs, placement rules, area Magicules, other add-ons, and server data packs can affect the final result. The checked Hound Dog biome modifier targets Overworld tags; its presence in Barrens and Spikes instead comes from their own base biome lists.

## Magicules

<div class="kiln-tier-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Tracked base</p><h3>500</h3><p>Base chunk Magicules in the tracked area configuration.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Hell level modifier</p><h3>+100,000</h3><p>Packaged ADD modifier for <code>tensura:hell</code>.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Biome modifier</p><h3>+3,500</h3><p>Packaged ADD modifier for this biome.</p></article></div>

These three additive inputs give a **104,000 reference baseline** before other modifiers. It is not a guaranteed current chunk reading or a personal MP grant. Generation, regeneration, magic engines, and server overrides can change the area value.

??? info "Regeneration inputs"

    The tracked base regeneration is **10**; the Hell resource has a **MULTIPLY 2** regeneration modifier, and this biome has an **ADD 50** regeneration modifier. No final rate or modifier-order result is asserted without checking the applying implementation and live server.

<span id="Notes"></span>

## Terrain and structures

The packaged biome feature list includes `tensura:hell_block_blob`. Precipitation is disabled in its definition. Landscape artwork is atmospheric illustration, not evidence of a particular castle, landmark, or terrain shape in game.

No dedicated ruin association is asserted here. The upstream article does not establish one, and the checked sand-ruin tags select the two sand biomes instead. Use the [Structures directory](../structures/index.md) for separately verified locations.

</div>

<section class="reference-related"><div class="reference-related-heading"><h2>Compare Underworld biomes</h2><a href="../../biomes/">Browse all Biomes</a></div><div class="reference-related-grid">
<a class="reference-related-card" href="../underworld-red-sands/"><img src="../../../assets/images/encyclopedia/underworld-red-sands.webp" alt="" loading="lazy" decoding="async"><span class="reference-related-copy"><strong>Underworld Red Sands</strong><small>A red-sand Underworld biome eligible for Big Ruins, with Megalodons, Daemons, and a configured 102,000-Magicule baseline.</small></span></a>
<a class="reference-related-card" href="../underworld-sands/"><img src="../../../assets/images/encyclopedia/underworld-sands.webp" alt="" loading="lazy" decoding="async"><span class="reference-related-copy"><strong>Underworld Sands</strong><small>An Underworld biome eligible for Ruins, with Megalodons, Daemons, and a configured 101,000-Magicule baseline.</small></span></a>
<a class="reference-related-card" href="../underworld-spikes/"><img src="../../../assets/images/encyclopedia/underworld-spikes.webp" alt="" loading="lazy" decoding="async"><span class="reference-related-copy"><strong>Underworld Spikes</strong><small>A rock-spike Underworld biome with Hound Dogs, Daemons, and a configured 103,000-Magicule baseline before other modifiers.</small></span></a>
</div></section>

## Source and licensing

Adapted from [Underworld Barrens](https://tensura.wiki.gg/wiki/Underworld_Barrens?oldid=11826) on the Tensura: Reincarnated Wiki, recorded revision `11826`. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The upstream spawn list is supplemented by the checked base biome and tagged additions.

Implementation: [Tensura 2.0.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [Underworld evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/underworld_biome_reference.json) · [tracked area configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/area_magicule_config.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

The original TSR landscape is conceptual artwork. The source articles show missing image-file links; those upload links are not usable media and are not included here. See [Sources and attribution](../../project/sources-and-attribution.md).

[Back to Biomes](../biomes/index.md) · [Hell dimension](../dimensions/hell.md)
