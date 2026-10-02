---
title: Kiln
description: Melt materials, compare alloys, and plan all three pinned Kiln tiers.
---

# Kiln

<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">
<figure class="reference-overview-media"><img src="../../../assets/images/blocks/kiln.webp" alt="Original obsidian kiln workshop illustration" loading="eager" decoding="async"><figcaption>TSR workstation illustration · not the in-game texture</figcaption></figure>
<div class="reference-overview-copy"><p class="reference-eyebrow">Metal workshop · Minecraft 1.21.1</p><h2>From ore to your next alloy</h2><p>Separate melting from mixing, leave room for both molten bars, and choose the right Kiln tier before processing valuable materials.</p><nav class="reference-quick-jumps" aria-label="Kiln guide"><a href="#build-and-upgrade">Build &amp; upgrade</a><a href="#process-materials">Processing</a><a href="#alloy-quantities">Alloy quantities</a><a href="#recipe-browser">Recipe browser</a></nav></div></section>

!!! note "Pinned definitions · live processing untested"
    The three block tiers, tracked capacity settings, fuel and boost logic, **272 melting recipes**, and **14 mixing recipes** were inspected in Tensura 2.0.1.2. Datapacks, scripts, add-ons, or server settings can change the result. No live processing, automation, or upgrade-retention test is recorded.

<span id="Crafting"></span>

## Build and upgrade

Use a **Crafting Table** for each shaped recipe below. Each recipe produces one workstation. Capacity is **per molten bar**, not the sum of both bars, and comes from the [tracked block configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/block_config.toml).

<div class="kiln-tier-grid">
<article class="smithing-recipe"><p class="reference-eyebrow">144 units per bar</p><h3>Kiln</h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Obsidian</li>
<li><strong>1×</strong> Blast Furnace</li>
<li><strong>2×</strong> Cauldron</li>
<li><strong>1×</strong> Netherite Ingot</li>
</ul>
<details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="Kiln crafting recipe"><tbody>
<tr><td>Obsidian</td><td>Netherite Ingot</td><td>Obsidian</td></tr>
<tr><td>Cauldron</td><td>Blast Furnace</td><td>Cauldron</td></tr>
<tr><td>Obsidian</td><td>Obsidian</td><td>Obsidian</td></tr>
</tbody></table></details>
<p class="reference-media-note"><code>tensura:kiln</code></p></article>
<article class="smithing-recipe"><p class="reference-eyebrow">288 units per bar</p><h3>Mithril Kiln</h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Mithril Ingot</li>
<li><strong>2×</strong> Cauldron</li>
<li><strong>1×</strong> Kiln</li>
<li><strong>2×</strong> Netherite Ingot</li>
</ul>
<details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="Mithril Kiln crafting recipe"><tbody>
<tr><td>Mithril Ingot</td><td>Netherite Ingot</td><td>Mithril Ingot</td></tr>
<tr><td>Cauldron</td><td>Kiln</td><td>Cauldron</td></tr>
<tr><td>Mithril Ingot</td><td>Netherite Ingot</td><td>Mithril Ingot</td></tr>
</tbody></table></details>
<p class="reference-media-note"><code>tensura:kiln_mithril</code></p></article>
<article class="smithing-recipe"><p class="reference-eyebrow">576 units per bar</p><h3>Orichalcum Kiln</h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Cauldron</li>
<li><strong>1×</strong> Mithril Kiln</li>
<li><strong>2×</strong> Netherite Ingot</li>
</ul>
<details><summary>Crafting arrangement</summary><table class="smithing-pattern" aria-label="Orichalcum Kiln crafting recipe"><tbody>
<tr><td>Orichalcum Ingot</td><td>Netherite Ingot</td><td>Orichalcum Ingot</td></tr>
<tr><td>Cauldron</td><td>Mithril Kiln</td><td>Cauldron</td></tr>
<tr><td>Orichalcum Ingot</td><td>Netherite Ingot</td><td>Orichalcum Ingot</td></tr>
</tbody></table></details>
<p class="reference-media-note"><code>tensura:kiln_orichalcum</code></p></article>
</div>

Placement needs **two blocks of vertical space**, with a replaceable block above the base. The checked constructor has **hardness 50**, **blast resistance 1,200**, and requires a correct tool for drops. All three tiers are pickaxe-mineable and diamond-tool-tier tagged: use a **diamond-tier pickaxe or better**. A lit Kiln emits **light level 13**; the old article’s “not luminous” entry does not describe its lit state.

!!! warning "Before replacing a workstation"
    Upgrades are Crafting Table recipes using the previous tier as an ingredient, not a verified in-place conversion. Empty the workstation first. Inventory, stored molten material, and boost retention across breaking or upgrading have not been tested; do not assume they transfer intact.

<span id="Usage"></span>

## Process materials

<div class="tensura-reference-article"><ol class="hipokute-growth"><li><strong>Open and load</strong><span>Use an empty hand to open the Kiln. Put one compatible material stack in its input and furnace-compatible fuel in the fuel slot.</span></li><li><strong>Melt into the bars</strong><span>Melting consumes one input item per completed recipe. The left bar holds non-magical metals; the right bar holds magical material. Keep enough capacity for every listed molten output.</span></li><li><strong>Select and collect</strong><span>Choose an available mixing output using the recipe arrows. Collecting it consumes that mixing recipe’s molten quantities. An item preview is not a new source of materials.</span></li></ol></div>

The six packaged molten kinds are **Copper, Gold, Iron, Silver, Magisteel, and Netherite**. Magisteel and Netherite are magical and share the **right** bar; the other four use the **left** bar. Each bar holds one material identity at a time. A different kind already occupying the same bar, or an output exceeding its capacity, prevents that melting recipe from matching.

For a basic Magisteel route, each **Magic Ore Shard** contributes **1 Magisteel unit**. The Pure Magisteel Ingot mixing definition needs **36 Magisteel units**; its nugget needs **4**. These are packaged recipe quantities, not a guarantee that an input stack completes while unattended. [Magic Ore Shard](../magic/magic-ore-shard.md) explains checked acquisition and other uses.

### Fuel and Fire Core boost

Ordinary fuel must pass the furnace fuel check and provide positive burn duration. A Fire Elemental Core boost **does not replace fuel**: melting still checks fuel. While boosted, the implementation advances melting progress by **2 per tick instead of 1**. That is a progress multiplier, not a measured end-to-end throughput claim.

Use a **Fire Elemental Core in the main hand** on either part of the Kiln. With the tracked settings, it needs at least **100 remaining durability**, applies **100 durability damage**, and adds **2,400 ticks** to the existing boost timer. That is nominally **120 seconds at 20 TPS**; pauses and server tick rate affect wall-clock duration. A broken core converts to an Empty Elemental Core. The block reads `fireCoreCost` for the eligibility check but hard-codes the 100-damage call, so changing that setting alone would not establish a matching damage cost.

??? warning "Why processing can stop"

    Check fuel, the actual input ingredient, both stored material identities, and free capacity **per bar**. Recipe times are required progress ticks, not guaranteed wall-clock seconds. Do not use a resource filename to guess its input: the browser below follows the ingredient inside the JSON definition. Equipment recycling is not a verified way to retain abilities, durability, or components.

## Alloy quantities

Each row describes **one mixing operation**. A dash means that bar is not required by the recipe; it does **not** require the bar to be empty. The minimum tier compares each required bar quantity with tracked capacity and does not prove ingredient acquisition or live availability.

| Output | Left bar units | Right bar units | Minimum capacity tier |
|---|---|---|---|
| Block of High Magisteel ×1 | 45 Iron | 144 Magisteel | Kiln |
| Block of Low Magisteel ×1 | 72 Iron | 36 Magisteel | Kiln |
| Block of Mithril ×1 | 36 Silver | 180 Magisteel | Mithril Kiln |
| Block of Orichalcum ×1 | 36 Gold | 180 Magisteel | Mithril Kiln |
| Block of Pure Magisteel ×1 | — | 324 Magisteel | Orichalcum Kiln |
| Block of Silver ×1 | 81 Silver | — | Kiln |
| High Magisteel Ingot ×1 | 5 Iron | 16 Magisteel | Kiln |
| Low Magisteel Ingot ×1 | 8 Iron | 4 Magisteel | Kiln |
| Mithril Ingot ×1 | 4 Silver | 20 Magisteel | Kiln |
| Orichalcum Ingot ×1 | 4 Gold | 20 Magisteel | Kiln |
| Pure Magisteel Ingot ×1 | — | 36 Magisteel | Kiln |
| Pure Magisteel Nugget ×1 | — | 4 Magisteel | Kiln |
| Silver Ingot ×1 | 9 Silver | — | Kiln |
| Silver Nugget ×1 | 1 Silver | — | Kiln |

## Recipe browser

Search an input, finished output, molten material, registry ID, or resource path. This includes both melting and mixing. Melting counts are units returned from **one input item**. Progress ticks include the serializer’s 100-tick default when a recipe omits `smeltTick`.

!!! warning "Recycling definitions are not always full material returns"
    Fifteen Low Magisteel recycling definitions name Magisteel but omit `primary_count`. The checked serializer defaults that quantity to **0**, not 1. Those cards explicitly show zero Magisteel units and the defined Iron return. Other resource names also differ from their actual ingredients; the displayed input follows the definition rather than silently correcting or guessing it.

<section class="smithing-browser" data-smithing-browser data-group-label="material group" aria-label="Packaged Kiln recipes"><div class="smithing-search"><label for="kiln-search">Find a processing recipe<input id="kiln-search" type="search" data-smithing-search placeholder="Try ore shard, mithril, silver, or an item ID" autocomplete="off"></label><button type="button" data-smithing-clear>Clear search</button><p data-smithing-status role="status" aria-live="polite">286 packaged recipes · expand a material group below</p></div>
<details class="smithing-group"><summary>Melting · Copper <span>14 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting #minecraft:copper_ores data/tensura/recipe/melting/copper_ores.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:copper_ores&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:copper ores&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>#minecraft:copper_ores</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_ores.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;tag&quot;: &quot;minecraft:copper_ores&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting chiseled copper data/tensura/recipe/melting/chiseled_copper_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:chiseled_copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:chiseled copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Chiseled Copper</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/chiseled_copper_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:chiseled_copper&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper block data/tensura/recipe/melting/copper_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_block&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper block&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Copper Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper bulb data/tensura/recipe/melting/copper_bulb.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_bulb&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 60, &quot;smelttick&quot;: 450} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper bulb&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 60, &quot;smelttick&quot;: 450}"><p class="reference-eyebrow">melting</p><h3>Copper Bulb</h3>
<ul class="smithing-ingredients">
<li><strong>60 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 450 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_bulb.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_bulb&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 60,
  &quot;smeltTick&quot;: 450
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper door data/tensura/recipe/melting/copper_door.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_door&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 54, &quot;smelttick&quot;: 400} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper door&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 54, &quot;smelttick&quot;: 400}"><p class="reference-eyebrow">melting</p><h3>Copper Door</h3>
<ul class="smithing-ingredients">
<li><strong>54 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 400 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_door.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_door&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 54,
  &quot;smeltTick&quot;: 400
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper grate data/tensura/recipe/melting/copper_grate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_grate&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper grate&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Copper Grate</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_grate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_grate&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper ingot data/tensura/recipe/melting/copper_ingots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_ingot&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 9} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper ingot&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 9}"><p class="reference-eyebrow">melting</p><h3>Copper Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_ingots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 9
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting copper trapdoor data/tensura/recipe/melting/copper_trapdoor.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper_trapdoor&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 27, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:copper trapdoor&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 27, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>Copper Trapdoor</h3>
<ul class="smithing-ingredients">
<li><strong>27 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_trapdoor.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:copper_trapdoor&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 27,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting cut copper data/tensura/recipe/melting/cut_copper_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut_copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Cut Copper</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/cut_copper_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:cut_copper&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting cut copper slab data/tensura/recipe/melting/cut_copper_slab.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut_copper_slab&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 40, &quot;smelttick&quot;: 300} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut copper slab&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 40, &quot;smelttick&quot;: 300}"><p class="reference-eyebrow">melting</p><h3>Cut Copper Slab</h3>
<ul class="smithing-ingredients">
<li><strong>40 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 300 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/cut_copper_slab.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:cut_copper_slab&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 40,
  &quot;smeltTick&quot;: 300
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting cut copper stairs data/tensura/recipe/melting/cut_copper_stairs.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut_copper_stairs&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 54, &quot;smelttick&quot;: 400} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:cut copper stairs&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 54, &quot;smelttick&quot;: 400}"><p class="reference-eyebrow">melting</p><h3>Cut Copper Stairs</h3>
<ul class="smithing-ingredients">
<li><strong>54 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 400 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/cut_copper_stairs.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:cut_copper_stairs&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 54,
  &quot;smeltTick&quot;: 400
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting lightning rod data/tensura/recipe/melting/lightning_rod.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:lightning_rod&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 27, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:lightning rod&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 27, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>Lightning Rod</h3>
<ul class="smithing-ingredients">
<li><strong>27 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/lightning_rod.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:lightning_rod&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 27,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw copper data/tensura/recipe/melting/copper_raw.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw copper&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Raw Copper</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_raw.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_copper&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw copper block data/tensura/recipe/melting/copper_raw_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_copper_block&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 900} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw copper block&quot;}, &quot;primary&quot;: &quot;tensura:copper&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 900}"><p class="reference-eyebrow">melting</p><h3>Raw Copper Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Copper</li>
</ul><p><strong>Required progress:</strong> 900 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/copper_raw_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_copper_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:copper&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 900
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Melting · Gold <span>25 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting #minecraft:gold_ores data/tensura/recipe/melting/gold_ores.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:gold_ores&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:gold ores&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>#minecraft:gold_ores</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_ores.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;tag&quot;: &quot;minecraft:gold_ores&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting gold block data/tensura/recipe/melting/gold_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold_block&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold block&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Gold Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:gold_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting gold ingot data/tensura/recipe/melting/gold_ingots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 9} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold ingot&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 9}"><p class="reference-eyebrow">melting</p><h3>Gold Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_ingots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:gold_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 9
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting gold nugget data/tensura/recipe/melting/gold_nuggets.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold_nugget&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 20} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:gold nugget&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 20}"><p class="reference-eyebrow">melting</p><h3>Gold Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 20 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_nuggets.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:gold_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 20
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden axe data/tensura/recipe/melting/gold_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_axe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden axe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Axe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden boots data/tensura/recipe/melting/gold_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_boots&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden boots&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Golden Boots</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden chestplate data/tensura/recipe/melting/gold_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden chestplate&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Golden Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden great sword data/tensura/recipe/melting/gold_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden great sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Golden Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden helmet data/tensura/recipe/melting/gold_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_helmet&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden helmet&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Golden Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden hoe data/tensura/recipe/melting/gold_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_hoe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden hoe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden katana data/tensura/recipe/melting/gold_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_katana&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden katana&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Katana</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden kodachi data/tensura/recipe/melting/gold_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden kodachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden leggings data/tensura/recipe/melting/gold_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_leggings&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden leggings&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Golden Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden long sword data/tensura/recipe/melting/gold_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden long sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden odachi data/tensura/recipe/melting/gold_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_odachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden odachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Golden Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden pickaxe data/tensura/recipe/melting/gold_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden short sword data/tensura/recipe/melting/gold_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden short sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden shovel data/tensura/recipe/melting/gold_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_shovel&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden shovel&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden sickle data/tensura/recipe/melting/gold_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_sickle&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden sickle&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden spear data/tensura/recipe/melting/gold_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_spear&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden spear&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Golden Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden spear data/tensura/recipe/melting/gold_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_spear&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden spear&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden sword data/tensura/recipe/melting/gold_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden_sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:golden sword&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Golden Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:golden_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting golden tachi data/tensura/recipe/melting/gold_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden_tachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:golden tachi&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Golden Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:golden_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw gold data/tensura/recipe/melting/gold_raw.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_gold&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw gold&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Raw Gold</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_raw.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_gold&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw gold block data/tensura/recipe/melting/gold_raw_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_gold_block&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 900} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw gold block&quot;}, &quot;primary&quot;: &quot;tensura:gold&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 900}"><p class="reference-eyebrow">melting</p><h3>Raw Gold Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 900 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/gold_raw_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_gold_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:gold&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 900
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Melting · Iron <span>25 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting #minecraft:iron_ores data/tensura/recipe/melting/iron_ores.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:iron_ores&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;minecraft:iron ores&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>#minecraft:iron_ores</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_ores.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;tag&quot;: &quot;minecraft:iron_ores&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron axe data/tensura/recipe/melting/iron_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_axe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron axe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Axe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron block data/tensura/recipe/melting/iron_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_block&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron block&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Iron Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron boots data/tensura/recipe/melting/iron_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_boots&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron boots&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Iron Boots</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron chestplate data/tensura/recipe/melting/iron_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron chestplate&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Iron Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron great sword data/tensura/recipe/melting/iron_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron great sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Iron Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron helmet data/tensura/recipe/melting/iron_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_helmet&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron helmet&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Iron Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron hoe data/tensura/recipe/melting/iron_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_hoe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron hoe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron ingot data/tensura/recipe/melting/iron_ingots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 9} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron ingot&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 9}"><p class="reference-eyebrow">melting</p><h3>Iron Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_ingots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 9
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron katana data/tensura/recipe/melting/iron_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_katana&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron katana&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Katana</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron kodachi data/tensura/recipe/melting/iron_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron kodachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron leggings data/tensura/recipe/melting/iron_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_leggings&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron leggings&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Iron Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron long sword data/tensura/recipe/melting/iron_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron long sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron nugget data/tensura/recipe/melting/iron_nuggets.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_nugget&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 20} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron nugget&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 20}"><p class="reference-eyebrow">melting</p><h3>Iron Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 20 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_nuggets.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 20
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron odachi data/tensura/recipe/melting/iron_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_odachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron odachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Iron Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron pickaxe data/tensura/recipe/melting/iron_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron short sword data/tensura/recipe/melting/iron_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron short sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron shovel data/tensura/recipe/melting/iron_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_shovel&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron shovel&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron sickle data/tensura/recipe/melting/iron_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_sickle&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron sickle&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron spear data/tensura/recipe/melting/iron_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_spear&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron spear&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Iron Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron spear data/tensura/recipe/melting/iron_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_spear&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron spear&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron sword data/tensura/recipe/melting/iron_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron_sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:iron sword&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Iron Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:iron_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting iron tachi data/tensura/recipe/melting/iron_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron_tachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:iron tachi&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Iron Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:iron_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw iron data/tensura/recipe/melting/iron_raw.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_iron&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw iron&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Raw Iron</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_raw.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_iron&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw iron block data/tensura/recipe/melting/iron_raw_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw_iron_block&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 900} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:raw iron block&quot;}, &quot;primary&quot;: &quot;tensura:iron&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 900}"><p class="reference-eyebrow">melting</p><h3>Raw Iron Block</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 900 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/iron_raw_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:raw_iron_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:iron&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 900
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Melting · Magisteel <span>160 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite axe data/tensura/recipe/melting/adamantite_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Axe</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite boots data/tensura/recipe/melting/adamantite_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 16} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 16}"><p class="reference-eyebrow">melting</p><h3>Adamantite Boots</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 16
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite chestplate data/tensura/recipe/melting/adamantite_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 16, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 16, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Adamantite Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 16,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite great sword data/tensura/recipe/melting/adamantite_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Adamantite Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite helmet data/tensura/recipe/melting/adamantite_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 16, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 16, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Adamantite Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 16,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite hoe data/tensura/recipe/melting/adamantite_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite ingot data/tensura/recipe/melting/adamantite_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 72, &quot;smelttick&quot;: 400} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 72, &quot;smelttick&quot;: 400}"><p class="reference-eyebrow">melting</p><h3>Adamantite Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>72 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 400 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 72,
  &quot;smeltTick&quot;: 400
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite katana data/tensura/recipe/melting/adamantite_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Katana</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite kodachi data/tensura/recipe/melting/adamantite_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite leggings data/tensura/recipe/melting/adamantite_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 16, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 16, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Adamantite Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 16,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite long sword data/tensura/recipe/melting/adamantite_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite nugget data/tensura/recipe/melting/adamantite_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Adamantite Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite odachi data/tensura/recipe/melting/adamantite_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Adamantite Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite pickaxe data/tensura/recipe/melting/adamantite_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite short sword data/tensura/recipe/melting/adamantite_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite shovel data/tensura/recipe/melting/adamantite_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite sickle data/tensura/recipe/melting/adamantite_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite spear data/tensura/recipe/melting/adamantite_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Adamantite Spear</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite spear data/tensura/recipe/melting/adamantite_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Spear</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite sword data/tensura/recipe/melting/adamantite_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Adamantite Sword</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting adamantite tachi data/tensura/recipe/melting/adamantite_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Adamantite Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of adamantite data/tensura/recipe/melting/adamantite_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 648, &quot;smelttick&quot;: 2000} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:adamantite block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 648, &quot;smelttick&quot;: 2000}"><p class="reference-eyebrow">melting</p><h3>Block of Adamantite</h3>
<ul class="smithing-ingredients">
<li><strong>648 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 2000 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/adamantite_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:adamantite_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 648,
  &quot;smeltTick&quot;: 2000
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of high magisteel data/tensura/recipe/melting/high_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 144, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 45, &quot;smelttick&quot;: 1250} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 144, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 45, &quot;smelttick&quot;: 1250}"><p class="reference-eyebrow">melting</p><h3>Block of High Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>144 units</strong> Magisteel</li>
<li><strong>45 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 1250 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 144,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 45,
  &quot;smeltTick&quot;: 1250
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of hihi&#x27;irokane data/tensura/recipe/melting/hihiirokane_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 972, &quot;smelttick&quot;: 2500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 972, &quot;smelttick&quot;: 2500}"><p class="reference-eyebrow">melting</p><h3>Block of Hihi&#x27;Irokane</h3>
<ul class="smithing-ingredients">
<li><strong>972 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 2500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 972,
  &quot;smeltTick&quot;: 2500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of low magisteel data/tensura/recipe/melting/low_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 36, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 72, &quot;smelttick&quot;: 1000} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 36, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 72, &quot;smelttick&quot;: 1000}"><p class="reference-eyebrow">melting</p><h3>Block of Low Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>36 units</strong> Magisteel</li>
<li><strong>72 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 1000 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 36,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 72,
  &quot;smeltTick&quot;: 1000
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of magic ore data/tensura/recipe/melting/magic_ore_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic_ore_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic ore block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Block of Magic Ore</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/magic_ore_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:magic_ore_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of mithril data/tensura/recipe/melting/mithril_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 180, &quot;secondary&quot;: &quot;tensura:silver&quot;, &quot;secondary_count&quot;: 36, &quot;smelttick&quot;: 1500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 180, &quot;secondary&quot;: &quot;tensura:silver&quot;, &quot;secondary count&quot;: 36, &quot;smelttick&quot;: 1500}"><p class="reference-eyebrow">melting</p><h3>Block of Mithril</h3>
<ul class="smithing-ingredients">
<li><strong>180 units</strong> Magisteel</li>
<li><strong>36 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 1500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 180,
  &quot;secondary&quot;: &quot;tensura:silver&quot;,
  &quot;secondary_count&quot;: 36,
  &quot;smeltTick&quot;: 1500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of orichalcum data/tensura/recipe/melting/orichalcum_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 180, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 36, &quot;smelttick&quot;: 1500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 180, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 36, &quot;smelttick&quot;: 1500}"><p class="reference-eyebrow">melting</p><h3>Block of Orichalcum</h3>
<ul class="smithing-ingredients">
<li><strong>180 units</strong> Magisteel</li>
<li><strong>36 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 1500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 180,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 36,
  &quot;smeltTick&quot;: 1500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of pure magisteel data/tensura/recipe/melting/pure_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 324, &quot;smelttick&quot;: 1500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel block&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 324, &quot;smelttick&quot;: 1500}"><p class="reference-eyebrow">melting</p><h3>Block of Pure Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>324 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 1500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 324,
  &quot;smeltTick&quot;: 1500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting deepslate magic ore data/tensura/recipe/melting/deepslate_magic_ore.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:deepslate_magic_ore&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:deepslate magic ore&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Deepslate Magic Ore</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/deepslate_magic_ore.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:deepslate_magic_ore&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting dragon knuckle data/tensura/recipe/melting/dragon_knuckle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:dragon_knuckle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 300} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:dragon knuckle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 300}"><p class="reference-eyebrow">melting</p><h3>Dragon Knuckle</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 300 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/dragon_knuckle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:dragon_knuckle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 300
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel axe data/tensura/recipe/melting/high_magisteel_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Axe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel boots data/tensura/recipe/melting/high_magisteel_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Boots</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel chestplate data/tensura/recipe/melting/high_magisteel_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel great sword data/tensura/recipe/melting/high_magisteel_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel helmet data/tensura/recipe/melting/high_magisteel_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel hoe data/tensura/recipe/melting/high_magisteel_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel ingot data/tensura/recipe/melting/high_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 16, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 5, &quot;smelttick&quot;: 250} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 16, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 5, &quot;smelttick&quot;: 250}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Magisteel</li>
<li><strong>5 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 250 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 16,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 5,
  &quot;smeltTick&quot;: 250
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel katana data/tensura/recipe/melting/high_magisteel_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Katana</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel kodachi data/tensura/recipe/melting/high_magisteel_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel leggings data/tensura/recipe/melting/high_magisteel_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel long sword data/tensura/recipe/melting/high_magisteel_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel nugget data/tensura/recipe/melting/high_magisteel_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 40} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 40}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 40 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 40
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel odachi data/tensura/recipe/melting/high_magisteel_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel pickaxe data/tensura/recipe/melting/high_magisteel_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel scythe data/tensura/recipe/melting/high_magisteel_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_scythe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel scythe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Scythe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_scythe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel short sword data/tensura/recipe/melting/high_magisteel_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel shovel data/tensura/recipe/melting/high_magisteel_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel sickle data/tensura/recipe/melting/high_magisteel_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel spear data/tensura/recipe/melting/high_magisteel_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Spear</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel sword data/tensura/recipe/melting/high_magisteel_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting high magisteel tachi data/tensura/recipe/melting/high_magisteel_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high_magisteel_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:high magisteel tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>High Magisteel Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
<li><strong>0 units</strong> Iron · omitted count defaults to zero</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/high_magisteel_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:high_magisteel_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane axe data/tensura/recipe/melting/hihiirokane_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Axe</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane boots data/tensura/recipe/melting/hihiirokane_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 24} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 24}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Boots</h3>
<ul class="smithing-ingredients">
<li><strong>24 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 24
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane chestplate data/tensura/recipe/melting/hihiirokane_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 24, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 24, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>24 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 24,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane great sword data/tensura/recipe/melting/hihiirokane_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane helmet data/tensura/recipe/melting/hihiirokane_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 24, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 24, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>24 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 24,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane hoe data/tensura/recipe/melting/hihiirokane_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane ingot data/tensura/recipe/melting/hihiirokane_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 108, &quot;smelttick&quot;: 500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 108, &quot;smelttick&quot;: 500}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>108 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 108,
  &quot;smeltTick&quot;: 500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane katana data/tensura/recipe/melting/hihiirokane_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Katana</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane kodachi data/tensura/recipe/melting/hihiirokane_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane leggings data/tensura/recipe/melting/hihiirokane_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 24, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 24, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>24 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 24,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane long sword data/tensura/recipe/melting/hihiirokane_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane nugget data/tensura/recipe/melting/hihiirokane_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 150} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 150}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 150 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 150
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane odachi data/tensura/recipe/melting/hihiirokane_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane pickaxe data/tensura/recipe/melting/hihiirokane_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane short sword data/tensura/recipe/melting/hihiirokane_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane shovel data/tensura/recipe/melting/hihiirokane_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane sickle data/tensura/recipe/melting/hihiirokane_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane spear data/tensura/recipe/melting/hihiirokane_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Spear</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane spear data/tensura/recipe/melting/hihiirokane_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Spear</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane sword data/tensura/recipe/melting/hihiirokane_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Sword</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting hihi&#x27;irokane tachi data/tensura/recipe/melting/hihiirokane_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 12, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:hihiirokane tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 12, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Hihi&#x27;Irokane Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>12 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/hihiirokane_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:hihiirokane_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 12,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting kanabo data/tensura/recipe/melting/kanabo.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:kanabo&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:kanabo&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Kanabo</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/kanabo.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:kanabo&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel axe data/tensura/recipe/melting/low_magisteel_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Axe</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel boots data/tensura/recipe/melting/low_magisteel_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Boots</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel chestplate data/tensura/recipe/melting/low_magisteel_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 2, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 2, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 2,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel great sword data/tensura/recipe/melting/low_magisteel_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel helmet data/tensura/recipe/melting/low_magisteel_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 2, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 2, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 2,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel hoe data/tensura/recipe/melting/low_magisteel_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel ingot data/tensura/recipe/melting/low_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 8, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 8, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
<li><strong>8 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 8,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel katana data/tensura/recipe/melting/low_magisteel_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Katana</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel kodachi data/tensura/recipe/melting/low_magisteel_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel leggings data/tensura/recipe/melting/low_magisteel_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 2, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 2, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
<li><strong>2 units</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 2,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel long sword data/tensura/recipe/melting/low_magisteel_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel odachi data/tensura/recipe/melting/low_magisteel_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel pickaxe data/tensura/recipe/melting/low_magisteel_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel scythe data/tensura/recipe/melting/low_magisteel_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_scythe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel scythe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Scythe</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_scythe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel short sword data/tensura/recipe/melting/low_magisteel_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel shovel data/tensura/recipe/melting/low_magisteel_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel sickle data/tensura/recipe/melting/low_magisteel_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel spear data/tensura/recipe/melting/low_magisteel_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Spear</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel sword data/tensura/recipe/melting/low_magisteel_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Sword</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting low magisteel tachi data/tensura/recipe/melting/low_magisteel_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low_magisteel_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:low magisteel tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;secondary&quot;: &quot;tensura:iron&quot;, &quot;secondary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Low Magisteel Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>0 units</strong> Magisteel · omitted count defaults to zero</li>
<li><strong>1 unit</strong> Iron</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/low_magisteel_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:low_magisteel_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;secondary&quot;: &quot;tensura:iron&quot;,
  &quot;secondary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting magic ore data/tensura/recipe/melting/magic_ore.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic_ore&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic ore&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Magic Ore</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/magic_ore.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:magic_ore&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting magic ore data/tensura/recipe/melting/magic_ore_shard.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic_ore_shard&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:magic ore shard&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Magic Ore</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/magic_ore_shard.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:magic_ore_shard&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril axe data/tensura/recipe/melting/mithril_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Axe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril boots data/tensura/recipe/melting/mithril_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Mithril Boots</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril chestplate data/tensura/recipe/melting/mithril_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Mithril Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril great sword data/tensura/recipe/melting/mithril_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Mithril Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril helmet data/tensura/recipe/melting/mithril_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Mithril Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril hoe data/tensura/recipe/melting/mithril_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril ingot data/tensura/recipe/melting/mithril_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 20, &quot;secondary&quot;: &quot;tensura:silver&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 300} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 20, &quot;secondary&quot;: &quot;tensura:silver&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 300}"><p class="reference-eyebrow">melting</p><h3>Mithril Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>20 units</strong> Magisteel</li>
<li><strong>4 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 300 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 20,
  &quot;secondary&quot;: &quot;tensura:silver&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 300
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril katana data/tensura/recipe/melting/mithril_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Katana</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril kodachi data/tensura/recipe/melting/mithril_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril leggings data/tensura/recipe/melting/mithril_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Mithril Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril long sword data/tensura/recipe/melting/mithril_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril nugget data/tensura/recipe/melting/mithril_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 60} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 60}"><p class="reference-eyebrow">melting</p><h3>Mithril Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 60 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 60
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril odachi data/tensura/recipe/melting/mithril_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Mithril Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril pickaxe data/tensura/recipe/melting/mithril_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril short sword data/tensura/recipe/melting/mithril_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril shovel data/tensura/recipe/melting/mithril_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril sickle data/tensura/recipe/melting/mithril_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril spear data/tensura/recipe/melting/mithril_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Mithril Spear</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril spear data/tensura/recipe/melting/mithril_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Spear</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril sword data/tensura/recipe/melting/mithril_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Mithril Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting mithril tachi data/tensura/recipe/melting/mithril_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:mithril tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Mithril Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/mithril_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:mithril_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum axe data/tensura/recipe/melting/orichalcum_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Axe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum boots data/tensura/recipe/melting/orichalcum_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Boots</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum chestplate data/tensura/recipe/melting/orichalcum_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum great sword data/tensura/recipe/melting/orichalcum_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum helmet data/tensura/recipe/melting/orichalcum_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum hoe data/tensura/recipe/melting/orichalcum_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum ingot data/tensura/recipe/melting/orichalcum_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 20, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 300} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 20, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 300}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>20 units</strong> Magisteel</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 300 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 20,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 300
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum katana data/tensura/recipe/melting/orichalcum_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Katana</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum kodachi data/tensura/recipe/melting/orichalcum_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum leggings data/tensura/recipe/melting/orichalcum_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum long sword data/tensura/recipe/melting/orichalcum_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum nugget data/tensura/recipe/melting/orichalcum_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 60} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 60}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 60 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 60
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum odachi data/tensura/recipe/melting/orichalcum_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum pickaxe data/tensura/recipe/melting/orichalcum_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum short sword data/tensura/recipe/melting/orichalcum_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum shovel data/tensura/recipe/melting/orichalcum_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum sickle data/tensura/recipe/melting/orichalcum_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum spear data/tensura/recipe/melting/orichalcum_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Spear</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum spear data/tensura/recipe/melting/orichalcum_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Spear</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum sword data/tensura/recipe/melting/orichalcum_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Sword</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting orichalcum tachi data/tensura/recipe/melting/orichalcum_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:orichalcum tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Orichalcum Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/orichalcum_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:orichalcum_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel axe data/tensura/recipe/melting/pure_magisteel_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel axe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Axe</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel boots data/tensura/recipe/melting/pure_magisteel_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel boots&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Boots</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel chestplate data/tensura/recipe/melting/pure_magisteel_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel chestplate&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel great sword data/tensura/recipe/melting/pure_magisteel_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel great sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel helmet data/tensura/recipe/melting/pure_magisteel_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel helmet&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel hoe data/tensura/recipe/melting/pure_magisteel_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel hoe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel ingot data/tensura/recipe/melting/pure_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 36, &quot;smelttick&quot;: 300} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel ingot&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 36, &quot;smelttick&quot;: 300}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>36 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 300 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 36,
  &quot;smeltTick&quot;: 300
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel katana data/tensura/recipe/melting/pure_magisteel_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel katana&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Katana</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel kodachi data/tensura/recipe/melting/pure_magisteel_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel kodachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel kunai data/tensura/recipe/melting/pure_magisteel_kunai.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_kunai&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel kunai&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Kunai</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_kunai.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_kunai&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel leggings data/tensura/recipe/melting/pure_magisteel_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 8, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel leggings&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 8, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 8,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel long sword data/tensura/recipe/melting/pure_magisteel_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel long sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel nugget data/tensura/recipe/melting/pure_magisteel_nugget.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 60} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel nugget&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 60}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 60 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 60
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel odachi data/tensura/recipe/melting/pure_magisteel_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel odachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel pickaxe data/tensura/recipe/melting/pure_magisteel_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel short sword data/tensura/recipe/melting/pure_magisteel_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel short sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel shovel data/tensura/recipe/melting/pure_magisteel_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel shovel&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel sickle data/tensura/recipe/melting/pure_magisteel_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel sickle&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel spear data/tensura/recipe/melting/pure_magisteel_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Spear</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel spear data/tensura/recipe/melting/pure_magisteel_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel spear&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Spear</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel sword data/tensura/recipe/melting/pure_magisteel_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel sword&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Sword</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting pure magisteel tachi data/tensura/recipe/melting/pure_magisteel_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure_magisteel_tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:pure magisteel tachi&quot;}, &quot;primary&quot;: &quot;tensura:magisteel&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Pure Magisteel Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/pure_magisteel_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:pure_magisteel_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:magisteel&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Melting · Netherite <span>23 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting ancient debris data/tensura/recipe/melting/ancient_debris.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:ancient_debris&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:ancient debris&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Ancient Debris</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/ancient_debris.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:ancient_debris&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite axe data/tensura/recipe/melting/netherite_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_axe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite axe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Axe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite block data/tensura/recipe/melting/netherite_block.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_block&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 144, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 324, &quot;smelttick&quot;: 500} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite block&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 144, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 324, &quot;smelttick&quot;: 500}"><p class="reference-eyebrow">melting</p><h3>Netherite Block</h3>
<ul class="smithing-ingredients">
<li><strong>144 units</strong> Netherite</li>
<li><strong>324 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 500 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 144,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 324,
  &quot;smeltTick&quot;: 500
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite boots data/tensura/recipe/melting/netherite_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_boots&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 8} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite boots&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 8}"><p class="reference-eyebrow">melting</p><h3>Netherite Boots</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
<li><strong>8 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 8
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite chestplate data/tensura/recipe/melting/netherite_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 8, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite chestplate&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 8, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Netherite Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
<li><strong>8 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 8,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite great sword data/tensura/recipe/melting/netherite_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite great sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Netherite Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite helmet data/tensura/recipe/melting/netherite_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_helmet&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 8, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite helmet&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 8, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Netherite Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
<li><strong>8 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 8,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite hoe data/tensura/recipe/melting/netherite_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_hoe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite hoe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite ingot data/tensura/recipe/melting/netherite_ingot.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_ingot&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 16, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 36} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite ingot&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 16, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 36}"><p class="reference-eyebrow">melting</p><h3>Netherite Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>16 units</strong> Netherite</li>
<li><strong>36 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 16,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 36
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite katana data/tensura/recipe/melting/netherite_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_katana&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite katana&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Katana</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite kodachi data/tensura/recipe/melting/netherite_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite kodachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite leggings data/tensura/recipe/melting/netherite_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_leggings&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 8, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite leggings&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 8, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Netherite Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
<li><strong>8 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 8,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite long sword data/tensura/recipe/melting/netherite_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite long sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite odachi data/tensura/recipe/melting/netherite_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_odachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite odachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Netherite Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite pickaxe data/tensura/recipe/melting/netherite_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite scrap data/tensura/recipe/melting/netherite_scrap.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_scrap&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite scrap&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Scrap</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Netherite</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_scrap.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_scrap&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite scythe data/tensura/recipe/melting/netherite_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_scythe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite scythe&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4}"><p class="reference-eyebrow">melting</p><h3>Netherite Scythe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_scythe&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite short sword data/tensura/recipe/melting/netherite_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite short sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite shovel data/tensura/recipe/melting/netherite_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_shovel&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite shovel&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite sickle data/tensura/recipe/melting/netherite_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_sickle&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite sickle&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite spear data/tensura/recipe/melting/netherite_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_spear&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite spear&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite sword data/tensura/recipe/melting/netherite_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite_sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;minecraft:netherite sword&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Netherite Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;minecraft:netherite_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting netherite tachi data/tensura/recipe/melting/netherite_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite_tachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary_count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary_count&quot;: 4, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:netherite tachi&quot;}, &quot;primary&quot;: &quot;tensura:netherite&quot;, &quot;primary count&quot;: 1, &quot;secondary&quot;: &quot;tensura:gold&quot;, &quot;secondary count&quot;: 4, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Netherite Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Netherite</li>
<li><strong>4 units</strong> Gold</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/netherite_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:netherite_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:netherite&quot;,
  &quot;primary_count&quot;: 1,
  &quot;secondary&quot;: &quot;tensura:gold&quot;,
  &quot;secondary_count&quot;: 4,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Melting · Silver <span>25 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting #tensura:silver_ores data/tensura/recipe/melting/silver_ores.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;tensura:silver_ores&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 200} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;tag&quot;: &quot;tensura:silver ores&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 200}"><p class="reference-eyebrow">melting</p><h3>#tensura:silver_ores</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 200 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_ores.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;tag&quot;: &quot;tensura:silver_ores&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 200
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of raw silver data/tensura/recipe/melting/silver_raw_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:raw_silver_block&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 900} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:raw silver block&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 900}"><p class="reference-eyebrow">melting</p><h3>Block of Raw Silver</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 900 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_raw_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:raw_silver_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 900
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting block of silver data/tensura/recipe/melting/silver_blocks.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_block&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 81, &quot;smelttick&quot;: 600} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver block&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 81, &quot;smelttick&quot;: 600}"><p class="reference-eyebrow">melting</p><h3>Block of Silver</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 600 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_blocks.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_block&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 81,
  &quot;smeltTick&quot;: 600
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting raw silver data/tensura/recipe/melting/silver_raw.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:raw_silver&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 9, &quot;smelttick&quot;: 120} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:raw silver&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 9, &quot;smelttick&quot;: 120}"><p class="reference-eyebrow">melting</p><h3>Raw Silver</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 120 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_raw.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:raw_silver&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 9,
  &quot;smeltTick&quot;: 120
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver axe data/tensura/recipe/melting/silver_axe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_axe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver axe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Axe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_axe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_axe&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver boots data/tensura/recipe/melting/silver_boots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_boots&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 2} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver boots&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 2}"><p class="reference-eyebrow">melting</p><h3>Silver Boots</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_boots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_boots&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 2
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver chestplate data/tensura/recipe/melting/silver_chestplate.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_chestplate&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 225} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver chestplate&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 225}"><p class="reference-eyebrow">melting</p><h3>Silver Chestplate</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 225 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_chestplate.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_chestplate&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 225
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver great sword data/tensura/recipe/melting/silver_great_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_great_sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver great sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Silver Great Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_great_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_great_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver helmet data/tensura/recipe/melting/silver_helmet.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_helmet&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 125} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver helmet&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 125}"><p class="reference-eyebrow">melting</p><h3>Silver Helmet</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 125 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_helmet.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_helmet&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 125
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver hoe data/tensura/recipe/melting/silver_hoe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_hoe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver hoe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Hoe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_hoe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_hoe&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver ingot data/tensura/recipe/melting/silver_ingots.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_ingot&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 9} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver ingot&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 9}"><p class="reference-eyebrow">melting</p><h3>Silver Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_ingots.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_ingot&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 9
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver katana data/tensura/recipe/melting/silver_katana.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_katana&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver katana&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Katana</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_katana.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_katana&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver kodachi data/tensura/recipe/melting/silver_kodachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_kodachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver kodachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Kodachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_kodachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_kodachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver leggings data/tensura/recipe/melting/silver_leggings.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_leggings&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 2, &quot;smelttick&quot;: 175} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver leggings&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 2, &quot;smelttick&quot;: 175}"><p class="reference-eyebrow">melting</p><h3>Silver Leggings</h3>
<ul class="smithing-ingredients">
<li><strong>2 units</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 175 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_leggings.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_leggings&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 2,
  &quot;smeltTick&quot;: 175
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver long sword data/tensura/recipe/melting/silver_long_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_long_sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver long sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Long Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_long_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_long_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver nugget data/tensura/recipe/melting/silver_nuggets.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_nugget&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 20} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver nugget&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 20}"><p class="reference-eyebrow">melting</p><h3>Silver Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 20 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_nuggets.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_nugget&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 20
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver odachi data/tensura/recipe/melting/silver_odachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_odachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver odachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Silver Odachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_odachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_odachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver pickaxe data/tensura/recipe/melting/silver_pickaxe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver pickaxe&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Pickaxe</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_pickaxe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_pickaxe&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver short sword data/tensura/recipe/melting/silver_short_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_short_sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver short sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Short Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_short_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_short_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver shovel data/tensura/recipe/melting/silver_shovel.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_shovel&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver shovel&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Shovel</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_shovel.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_shovel&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver sickle data/tensura/recipe/melting/silver_sickle.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_sickle&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver sickle&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Sickle</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_sickle.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_sickle&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver spear data/tensura/recipe/melting/silver_scythe.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_spear&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver spear&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1}"><p class="reference-eyebrow">melting</p><h3>Silver Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 100 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_scythe.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver spear data/tensura/recipe/melting/silver_spear.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_spear&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver spear&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Spear</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_spear.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_spear&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver sword data/tensura/recipe/melting/silver_sword.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 50} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver sword&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 50}"><p class="reference-eyebrow">melting</p><h3>Silver Sword</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 50 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_sword.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_sword&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 50
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="melting" data-search="melting silver tachi data/tensura/recipe/melting/silver_tachi.json {&quot;type&quot;: &quot;tensura:kiln_melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver_tachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary_count&quot;: 1, &quot;smelttick&quot;: 75} {&quot;type&quot;: &quot;tensura:kiln melting&quot;, &quot;input&quot;: {&quot;item&quot;: &quot;tensura:silver tachi&quot;}, &quot;primary&quot;: &quot;tensura:silver&quot;, &quot;primary count&quot;: 1, &quot;smelttick&quot;: 75}"><p class="reference-eyebrow">melting</p><h3>Silver Tachi</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver</li>
</ul><p><strong>Required progress:</strong> 75 ticks</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/melting/silver_tachi.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_melting&quot;,
  &quot;input&quot;: {
    &quot;item&quot;: &quot;tensura:silver_tachi&quot;
  },
  &quot;primary&quot;: &quot;tensura:silver&quot;,
  &quot;primary_count&quot;: 1,
  &quot;smeltTick&quot;: 75
}</code></pre></details>
</article>
</div></details>
<details class="smithing-group"><summary>Mixing · finished materials <span>14 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of high magisteel data/tensura/recipe/mixing/high_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left_count&quot;: 45, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:high_magisteel_block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 144} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left count&quot;: 45, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:high magisteel block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 144}"><p class="reference-eyebrow">mixing</p><h3>Block of High Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>45 units</strong> Iron · left bar</li>
<li><strong>144 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/high_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:iron&quot;,
  &quot;left_count&quot;: 45,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:high_magisteel_block&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 144
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of low magisteel data/tensura/recipe/mixing/low_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left_count&quot;: 72, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:low_magisteel_block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 36} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left count&quot;: 72, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:low magisteel block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 36}"><p class="reference-eyebrow">mixing</p><h3>Block of Low Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>72 units</strong> Iron · left bar</li>
<li><strong>36 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/low_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:iron&quot;,
  &quot;left_count&quot;: 72,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:low_magisteel_block&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 36
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of mithril data/tensura/recipe/mixing/mithril_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left_count&quot;: 36, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:mithril_block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 180} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left count&quot;: 36, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:mithril block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 180}"><p class="reference-eyebrow">mixing</p><h3>Block of Mithril</h3>
<ul class="smithing-ingredients">
<li><strong>36 units</strong> Silver · left bar</li>
<li><strong>180 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/mithril_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:silver&quot;,
  &quot;left_count&quot;: 36,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:mithril_block&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 180
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of orichalcum data/tensura/recipe/mixing/orichalcum_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:gold&quot;, &quot;left_count&quot;: 36, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:orichalcum_block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 180} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:gold&quot;, &quot;left count&quot;: 36, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:orichalcum block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 180}"><p class="reference-eyebrow">mixing</p><h3>Block of Orichalcum</h3>
<ul class="smithing-ingredients">
<li><strong>36 units</strong> Gold · left bar</li>
<li><strong>180 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/orichalcum_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:gold&quot;,
  &quot;left_count&quot;: 36,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:orichalcum_block&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 180
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of pure magisteel data/tensura/recipe/mixing/pure_magisteel_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure_magisteel_block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 324} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure magisteel block&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 324}"><p class="reference-eyebrow">mixing</p><h3>Block of Pure Magisteel</h3>
<ul class="smithing-ingredients">
<li><strong>324 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/pure_magisteel_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:pure_magisteel_block&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 324
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing block of silver data/tensura/recipe/mixing/silver_block.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left_count&quot;: 81, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver_block&quot;}} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left count&quot;: 81, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver block&quot;}}"><p class="reference-eyebrow">mixing</p><h3>Block of Silver</h3>
<ul class="smithing-ingredients">
<li><strong>81 units</strong> Silver · left bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/silver_block.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:silver&quot;,
  &quot;left_count&quot;: 81,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:silver_block&quot;
  }
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing high magisteel ingot data/tensura/recipe/mixing/high_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left_count&quot;: 5, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:high_magisteel_ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 16} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left count&quot;: 5, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:high magisteel ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 16}"><p class="reference-eyebrow">mixing</p><h3>High Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>5 units</strong> Iron · left bar</li>
<li><strong>16 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/high_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:iron&quot;,
  &quot;left_count&quot;: 5,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:high_magisteel_ingot&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 16
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing low magisteel ingot data/tensura/recipe/mixing/low_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left_count&quot;: 8, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:low_magisteel_ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:iron&quot;, &quot;left count&quot;: 8, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:low magisteel ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 4}"><p class="reference-eyebrow">mixing</p><h3>Low Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>8 units</strong> Iron · left bar</li>
<li><strong>4 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/low_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:iron&quot;,
  &quot;left_count&quot;: 8,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:low_magisteel_ingot&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing mithril ingot data/tensura/recipe/mixing/mithril_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left_count&quot;: 4, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:mithril_ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 20} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left count&quot;: 4, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:mithril ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 20}"><p class="reference-eyebrow">mixing</p><h3>Mithril Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Silver · left bar</li>
<li><strong>20 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/mithril_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:silver&quot;,
  &quot;left_count&quot;: 4,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:mithril_ingot&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 20
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing orichalcum ingot data/tensura/recipe/mixing/orichalcum_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:gold&quot;, &quot;left_count&quot;: 4, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:orichalcum_ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 20} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:gold&quot;, &quot;left count&quot;: 4, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:orichalcum ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 20}"><p class="reference-eyebrow">mixing</p><h3>Orichalcum Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Gold · left bar</li>
<li><strong>20 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/orichalcum_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:gold&quot;,
  &quot;left_count&quot;: 4,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:orichalcum_ingot&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 20
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing pure magisteel ingot data/tensura/recipe/mixing/pure_magisteel_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure_magisteel_ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 36} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure magisteel ingot&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 36}"><p class="reference-eyebrow">mixing</p><h3>Pure Magisteel Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>36 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/pure_magisteel_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:pure_magisteel_ingot&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 36
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing pure magisteel nugget data/tensura/recipe/mixing/pure_magisteel_nugget.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure_magisteel_nugget&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right_count&quot;: 4} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:pure magisteel nugget&quot;}, &quot;right&quot;: &quot;tensura:magisteel&quot;, &quot;right count&quot;: 4}"><p class="reference-eyebrow">mixing</p><h3>Pure Magisteel Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>4 units</strong> Magisteel · right bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/pure_magisteel_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:pure_magisteel_nugget&quot;
  },
  &quot;right&quot;: &quot;tensura:magisteel&quot;,
  &quot;right_count&quot;: 4
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing silver ingot data/tensura/recipe/mixing/silver_ingot.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left_count&quot;: 9, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver_ingot&quot;}} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left count&quot;: 9, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver ingot&quot;}}"><p class="reference-eyebrow">mixing</p><h3>Silver Ingot</h3>
<ul class="smithing-ingredients">
<li><strong>9 units</strong> Silver · left bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/silver_ingot.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:silver&quot;,
  &quot;left_count&quot;: 9,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:silver_ingot&quot;
  }
}</code></pre></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-kiln-kind="mixing" data-search="mixing silver nugget data/tensura/recipe/mixing/silver_nugget.json {&quot;type&quot;: &quot;tensura:kiln_mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left_count&quot;: 1, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver_nugget&quot;}} {&quot;type&quot;: &quot;tensura:kiln mixing&quot;, &quot;left&quot;: &quot;tensura:silver&quot;, &quot;left count&quot;: 1, &quot;output&quot;: {&quot;count&quot;: 1, &quot;id&quot;: &quot;tensura:silver nugget&quot;}}"><p class="reference-eyebrow">mixing</p><h3>Silver Nugget</h3>
<ul class="smithing-ingredients">
<li><strong>1 unit</strong> Silver · left bar</li>
</ul><p><strong>Output per operation:</strong> 1</p>
<details class="smithing-evidence"><summary>Recipe definition</summary><p>Resource: <code>data/tensura/recipe/mixing/silver_nugget.json</code></p><pre><code>{
  &quot;type&quot;: &quot;tensura:kiln_mixing&quot;,
  &quot;left&quot;: &quot;tensura:silver&quot;,
  &quot;left_count&quot;: 1,
  &quot;output&quot;: {
    &quot;count&quot;: 1,
    &quot;id&quot;: &quot;tensura:silver_nugget&quot;
  }
}</code></pre></details>
</article>
</div></details>
<p data-smithing-empty hidden>No matching processing recipe. Try a shorter input or material name.</p></section>

## Source and licensing

[Kiln source article, recorded revision 12020](https://tensura.wiki.gg/wiki/Blocks/Kiln?oldid=12020). Adapted article text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Implementation: [Tensura 2.0.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [recipe evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/kiln_reference.json). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

The workstation illustration is original TSR conceptual artwork, not a game texture or GUI screenshot. The reviewed Kiln and Kiln GUI File pages did not establish reusable image permission; their withdrawal is recorded in the [source and media ledger](../../project/sources-and-attribution.md).

??? info "Implementation evidence"

    - `KilnBlock`, `KilnBlockEntity`, `KilnBlockEntity$1`, `KilnMenu`, `TensuraMixingSlot`, `KilnMeltingRecipe`, its `Serializer`, and `KilnMixingRecipe`
    - Three workstation crafting recipes, 272 melting definitions, 14 mixing definitions, and six `data/tensura/kiln_molten/*.json` resources
    - `data/minecraft/tags/block/mineable/pickaxe.json`, `needs_diamond_tool.json`, and `data/tensura/loot_table/blocks/kiln.json`
    - Tracked `pack/config/tensura/block_config.toml` Kiln settings

[Back to Blocks](index.md) · [Smithing Bench](blocks-smithing-bench.md) · [Equipment materials](../items/index.md)
