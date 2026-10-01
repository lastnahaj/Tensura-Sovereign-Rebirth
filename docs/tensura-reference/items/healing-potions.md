---
title: Healing Potions
description: Compare verified brewing routes, healing, MP recovery, and bottle preparation for the pinned 1.21.1 build.
---

<section class="potion-guide" data-potion-planner>
<header class="potion-guide-heading">
<p class="reference-eyebrow">Field alchemy · Minecraft 1.21.1</p>
<h1>Build your recovery kit</h1>
<p>Match the bottle and Hipokute ingredient to the potion you need. These four brewing combinations are checked against Tensura 2.0.1.2.</p>
</header>
<div class="potion-planner-controls">
<label for="potion-base">Bottle base<select id="potion-base" data-potion-base><option value="water">Magic Bottle of Water</option><option value="vacuumed">Vacuumed Magic Bottle of Water</option></select></label>
<label for="potion-reagent">Ingredient<select id="potion-reagent" data-potion-reagent><option value="grass">Hipokute Grass</option><option value="flower">Hipokute Flower</option></select></label>
</div>
<p class="potion-planner-status" aria-live="polite" data-potion-status>Choose a bottle and ingredient to highlight the matching brewing result.</p>
<div class="potion-guide-grid">
<article class="potion-guide-card" data-potion-result="water:grass" data-potion-title="Low Potion">
<span class="potion-selected" data-potion-selected hidden>Matching brew</span>
<a href="../low-potion/" aria-label="Read Low Potion"><img src="../../../assets/images/items/low-potion.webp" alt="Low Potion illustration" loading="lazy" decoding="async"><h2>Low Potion</h2></a>
<dl><div><dt>Health restored</dt><dd>33% <small>of maximum HP</small></dd></div><div><dt>MP restored</dt><dd>100 <small>fixed MP</small></dd></div></dl>
<ul class="potion-recipe-list" aria-label="Low Potion brewing recipes"><li><span>Magic Bottle of Water</span><b aria-hidden="true">+</b><span>Hipokute Grass</span></li></ul>
</article>
<article class="potion-guide-card" data-potion-result="water:flower vacuumed:grass" data-potion-title="High Potion">
<span class="potion-selected" data-potion-selected hidden>Matching brew</span>
<a href="../high-potion/" aria-label="Read High Potion"><img src="../../../assets/images/items/high-potion.webp" alt="High Potion illustration" loading="lazy" decoding="async"><h2>High Potion</h2></a>
<dl><div><dt>Health restored</dt><dd>66% <small>of maximum HP</small></dd></div><div><dt>MP restored</dt><dd>1,000 <small>fixed MP</small></dd></div></dl>
<ul class="potion-recipe-list" aria-label="High Potion brewing recipes"><li><span>Magic Bottle of Water</span><b aria-hidden="true">+</b><span>Hipokute Flower</span></li><li><span>Vacuumed Magic Bottle of Water</span><b aria-hidden="true">+</b><span>Hipokute Grass</span></li></ul>
</article>
<article class="potion-guide-card" data-potion-result="vacuumed:flower" data-potion-title="Full Potion">
<span class="potion-selected" data-potion-selected hidden>Matching brew</span>
<a href="../full-potion/" aria-label="Read Full Potion"><img src="../../../assets/images/items/full-potion.webp" alt="Full Potion illustration" loading="lazy" decoding="async"><h2>Full Potion</h2></a>
<dl><div><dt>Health restored</dt><dd>99% <small>of maximum HP</small></dd></div><div><dt>MP restored</dt><dd>10,000 <small>fixed MP</small></dd></div></dl>
<ul class="potion-recipe-list" aria-label="Full Potion brewing recipes"><li><span>Vacuumed Magic Bottle of Water</span><b aria-hidden="true">+</b><span>Hipokute Flower</span></li></ul>
</article>
</div>
<p class="potion-guide-footnote">Original TSR illustrations, not in-game textures. Healing values assume full effect strength; thrown splash strength can be lower. MP recovery is capped at maximum MP.</p>
</section>

<div class="tensura-reference-article"><p>Brewing recipes are distinct from Tensura Refining recipes. The planner only represents the ordinary brewing registrations.</p></div>

## Prepare the bottles

1. Craft Magic Bottles from three Glass and one Magic Crystal. The pinned recipes yield **3** bottles with a Low Quality crystal, **6** with Medium Quality, or **9** with High Quality. Place Glass around the crystal in the top row and a third Glass below it.
2. Use an empty Magic Bottle on a water source to fill it. The item checks interaction permission and source-water targeting.
3. For a vacuumed base, cook the filled bottle: **60 ticks** in a furnace or smoker, or **180 ticks** on a campfire. That is 3 or 9 seconds at 20 TPS, excluding setup and any fuel requirements.

**Ingredient references:** [Hipokute Grass](hipokute-grass.md) · [Hipokute Flower](hipokute-flower.md) · [Magic Bottle](../magic/magic-bottle.md) · [Filled bottle](../magic/magic-bottle-of-water.md)

## Use the potion safely

Drink normally, sneak-use to throw, or interact directly with a living target. Drinking takes **16 ticks** and returns an empty Magic Bottle in survival. The pinned potion stack limit is **16**. These items restore current health and MP; they do not raise permanent maximums or resurrect dead players.

!!! note "Server recipe check"
    The recipes, values, and controls above are artifact-verified. Server-specific recipe changes and gameplay interactions have not been tested here. Check the in-game recipe browser before collecting materials.

[Return to Items](index.md) · [Revival Elixir and its acquisition limits](revival-elixir.md)

## Source and licensing

Recipe and effect verification: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

The source articles and recorded revisions are cited in the individual [Low](low-potion.md), [High](high-potion.md), and [Full](full-potion.md) potion references. Adapted text remains under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Original illustrations and File-page reviews are recorded in the public artwork register.

??? info "Artifact evidence"

    - `SpecialRecipeRegister`: four potion container mixes.
    - `TensuraConsumableItems`, `HealingPotionItem`, `ManaPotionItem`: heal fractions, fixed MP, stack size, controls, and living-target checks.
    - `MagicBottleItem`: source-water filling.
    - `data/minecraft/recipe/bottles_of_low_crystal.json`, `bottles_of_medium_crystal.json`, `bottles_of_high_crystal.json`: bottle crafting.
    - `data/minecraft/recipe/vacuumed_magic_bottle_of_water_from_smelting.json` and matching Tensura smoking/campfire recipes: preparation times.
