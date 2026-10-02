---
title: Smithing Bench
description: Build the workstation, learn schematic requirements, and browse the pinned equipment recipes.
---

# Smithing Bench

<section data-reference-section="blocks" class="reference-overview reference-theme-world staff-guide-hero smithing-guide-hero">
<figure class="reference-overview-media"><img src="../../../assets/images/blocks/smithing-bench.webp" alt="Original artisan smithing workbench illustration" loading="eager" decoding="async"><figcaption>TSR workstation illustration · not the in-game texture</figcaption></figure>
<div class="reference-overview-copy"><p class="reference-eyebrow">Equipment workshop · Minecraft 1.21.1</p><h2>Turn a blueprint into equipment</h2><p>Build the workstation, learn its recipe gates, and keep the materials in your inventory. Check quantities and every required schematic before committing to a gear set.</p><nav class="reference-quick-jumps" aria-label="Smithing guide"><a href="#build-the-bench">Build the bench</a><a href="#unlock-and-craft">Unlock and craft</a><a href="#browse-packaged-recipes">Recipe browser</a></nav></div></section>

!!! note "Pinned recipe definitions · live crafting untested"
    The bench recipe, menu, schematic checks, and **298 packaged smithing recipes** were inspected in Tensura 2.0.1.2. This is not a claim that every recipe is unchanged on the server. Datapacks, scripts, add-ons, and recipe overrides may change availability or ingredients.

<span id="Crafting"></span>

## Build the bench

At a **Crafting Table**, use **2 Paper**, **1 Crafting Table**, **1 Smithing Table**, and **2 planks**. The shaped recipe uses the two-column arrangement below and produces one Smithing Bench. The material key accepts the `minecraft:planks` tag, not just one wood type.

<div class="smithing-build"><table class="smithing-pattern" aria-label="Two-column bench recipe"><caption>Crafting Table recipe · one bench</caption><tbody><tr><td>Paper</td><td>Paper</td></tr><tr><td>Crafting Table</td><td>Smithing Table</td></tr><tr><td>Planks</td><td>Planks</td></tr></tbody></table><aside><strong>Keep the workstations distinct</strong><p>A vanilla Smithing Table is an ingredient. It is not the Tensura Smithing Bench, and neither is the Spellbinding Table used for caster tools.</p><a href="../../resistances/spellbinding-table/">Compare Spellbinding Table →</a></aside></div>

The checked block has **hardness 3** and belongs to the **axe-mineable** tag. Although an iron-tool-tier tag also lists it, its constructor does not require a correct tool for drops and its ordinary self-drop loot table has no tool condition. Do not treat the old article’s tool icon as proof that an iron pickaxe is required to recover it. Explosion survival still affects its self-drop.

<span id="Usage"></span>

## Unlock and craft

<div class="tensura-reference-article"><ol class="hipokute-growth"><li><strong>Learn all required schematics</strong><span>The survival recipe list is filtered against your learned schematic IDs. A material schematic alone is not enough when a weapon also requires a shape schematic.</span></li><li><strong>Carry the ingredients</strong><span>The recipe input is your player inventory, not a separate shaped bench grid. Matching stacks are counted across the container.</span></li><li><strong>Select the recipe and take its output</strong><span>The survival pickup check requires sufficient materials. Taking the output consumes the recipe quantities from your inventory.</span></li></ol></div>

Use the bench with an empty hand to open its menu. Recipes without schematic requirements can appear without learning a blueprint. Creative/infinite-materials access bypasses both the schematic gate and the normal ingredient check; that is not a survival obtainment route.

A schematic must be **learned**, not merely carried. For example, [Magic Staff Schematic](../magic/magic-staff-schematic.md) is consumed when a new schematic is learned. Blueprint supply is recipe-specific; this browser does not establish how to obtain every listed schematic. [Compare casting staves](../items/magic-staves.md) for checked staff blueprint and material routes.

??? warning "Why a recipe may be missing or its output unavailable"

    Check that you have learned **every** schematic shown, that the materials are in player inventory rather than a nearby chest, and that counts and ingredient tags match. An output preview does not prove you can take it. If the server differs from this base catalogue, inspect its current in-game recipe browser before spending scarce materials. No automated item transfer or live multiplayer crafting has been verified here.

<span id="Gear_Requiring_Smithing_Bench"></span><span id="Monster_Leather"></span><span id="Magisteel"></span><span id="Monster_Drops"></span><span id="Special_Sets/Items"></span><span id="Basic_Material"></span>

## Browse packaged recipes

Search by output, ingredient, schematic, or registry ID. Expand a group to inspect its recipes. Groups use the **first schematic** for navigation only; each recipe still lists **all** required schematics. Quantities describe one craft, not a full armor set.

<section class="smithing-browser" data-smithing-browser aria-label="Packaged smithing recipes">
<div class="smithing-search"><label for="smithing-search">Find a recipe<input id="smithing-search" type="search" data-smithing-search placeholder="Try silver, staff, monster leather, or an item ID" autocomplete="off"></label><button type="button" data-smithing-clear>Clear search</button><p data-smithing-status role="status" aria-live="polite">298 packaged recipes · expand a schematic group below</p></div>
<details class="smithing-group"><summary>Adamantite Gear Schematic <span>19 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite axe tensura:adamantite_axe adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Adamantite Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_axe.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite boots tensura:adamantite_boots adamantite gear schematic adamantite ingot {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Adamantite Ingot</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_boots.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite chestplate tensura:adamantite_chestplate adamantite gear schematic adamantite ingot {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Adamantite Ingot</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_chestplate.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite great sword tensura:adamantite_great_sword adamantite gear schematic + great sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:great_sword_schematic">
<h3>Adamantite Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_great_sword.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite helmet tensura:adamantite_helmet adamantite gear schematic adamantite ingot {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Adamantite Ingot</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_helmet.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite hoe tensura:adamantite_hoe adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Adamantite Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_hoe.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite katana tensura:adamantite_katana adamantite gear schematic + japanese sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:japanese_sword_schematic">
<h3>Adamantite Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_katana.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite kodachi tensura:adamantite_kodachi adamantite gear schematic + short sword schematic + japanese sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Adamantite Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_kodachi.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite leggings tensura:adamantite_leggings adamantite gear schematic adamantite ingot {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Adamantite Ingot</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_leggings.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite long sword tensura:adamantite_long_sword adamantite gear schematic + long sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:long_sword_schematic">
<h3>Adamantite Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_long_sword.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite odachi tensura:adamantite_odachi adamantite gear schematic + great sword schematic + japanese sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Adamantite Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_odachi.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite pickaxe tensura:adamantite_pickaxe adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Adamantite Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_pickaxe.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite scythe tensura:adamantite_scythe adamantite gear schematic + great sword schematic + spear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Adamantite Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Adamantite Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_scythe.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite short sword tensura:adamantite_short_sword adamantite gear schematic + short sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:short_sword_schematic">
<h3>Adamantite Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_short_sword.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite shovel tensura:adamantite_shovel adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Adamantite Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_shovel.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite sickle tensura:adamantite_sickle adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Adamantite Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_sickle.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite spear tensura:adamantite_spear adamantite gear schematic + spear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:spear_schematic">
<h3>Adamantite Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Adamantite Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_spear.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite sword tensura:adamantite_sword adamantite gear schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic">
<h3>Adamantite Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_sword.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="adamantite tachi tensura:adamantite_tachi adamantite gear schematic + long sword schematic + japanese sword schematic adamantite ingot stick {&quot;item&quot;: &quot;tensura:adamantite_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:adamantite_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Adamantite Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Adamantite Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Adamantite Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:adamantite_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/adamantite_tachi.json</code></p><p>Required IDs: tensura:adamantite_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Ant Carapace Gear Schematic <span>5 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="ant carapace boots tensura:ant_carapace_boots ant carapace gear schematic giant ant carapace gold ingot {&quot;item&quot;: &quot;tensura:giant_ant_carapace&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:ant_carapace_gear_schematic">
<h3>Ant Carapace Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Giant Ant Carapace</li>
<li><strong>1×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Ant Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ant_carapace_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/ant_carapace_boots.json</code></p><p>Required IDs: tensura:ant_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="ant carapace chestplate tensura:ant_carapace_chestplate ant carapace gear schematic giant ant carapace gold ingot {&quot;item&quot;: &quot;tensura:giant_ant_carapace&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:ant_carapace_gear_schematic">
<h3>Ant Carapace Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Giant Ant Carapace</li>
<li><strong>4×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Ant Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ant_carapace_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/ant_carapace_chestplate.json</code></p><p>Required IDs: tensura:ant_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="ant carapace helmet tensura:ant_carapace_helmet ant carapace gear schematic giant ant carapace gold ingot {&quot;item&quot;: &quot;tensura:giant_ant_carapace&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:ant_carapace_gear_schematic">
<h3>Ant Carapace Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Giant Ant Carapace</li>
<li><strong>2×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Ant Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ant_carapace_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/ant_carapace_helmet.json</code></p><p>Required IDs: tensura:ant_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="ant carapace leggings tensura:ant_carapace_leggings ant carapace gear schematic giant ant carapace gold ingot {&quot;item&quot;: &quot;tensura:giant_ant_carapace&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:ant_carapace_gear_schematic">
<h3>Ant Carapace Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Giant Ant Carapace</li>
<li><strong>3×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Ant Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ant_carapace_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/ant_carapace_leggings.json</code></p><p>Required IDs: tensura:ant_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="ant crossbow tensura:ant_crossbow ant carapace gear schematic giant ant leg steel thread tripwire hook iron ingot {&quot;item&quot;: &quot;tensura:giant_ant_leg&quot;} {&quot;item&quot;: &quot;tensura:steel_thread&quot;} {&quot;item&quot;: &quot;minecraft:tripwire_hook&quot;} {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} tensura:ant_carapace_gear_schematic">
<h3>Ant Crossbow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Giant Ant Leg</li>
<li><strong>2×</strong> Steel Thread</li>
<li><strong>1×</strong> Tripwire Hook</li>
<li><strong>1×</strong> Iron Ingot</li>
</ul>
<p><strong>Learn all:</strong> Ant Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ant_crossbow</code></p><p>Resource: <code>data/tensura/recipe/smithing/ant_crossbow.json</code></p><p>Required IDs: tensura:ant_carapace_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Anti-Magic Mask Schematic <span>1 recipe</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="anti-magic mask tensura:anti_magic_mask anti-magic mask schematic pure magisteel ingot clay ball red dye {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:clay_ball&quot;} {&quot;item&quot;: &quot;minecraft:red_dye&quot;} tensura:anti_magic_mask_schematic">
<h3>Anti-Magic Mask <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>2×</strong> Clay Ball</li>
<li><strong>1×</strong> Red Dye</li>
</ul>
<p><strong>Learn all:</strong> Anti-Magic Mask Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:anti_magic_mask</code></p><p>Resource: <code>data/tensura/recipe/smithing/anti_magic_mask.json</code></p><p>Required IDs: tensura:anti_magic_mask_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Armorsaurus Scalemail Gear Schematic <span>5 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="armorsaurus scalemail boots tensura:armorsaurus_scalemail_boots armorsaurus scalemail gear schematic armorsaurus scale {&quot;item&quot;: &quot;tensura:armorsaurus_scale&quot;} tensura:armorsaurus_scalemail_gear_schematic">
<h3>Armorsaurus Scalemail Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Armorsaurus Scale</li>
</ul>
<p><strong>Learn all:</strong> Armorsaurus Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:armorsaurus_scalemail_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/armorsaurus_scalemail_boots.json</code></p><p>Required IDs: tensura:armorsaurus_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="armorsaurus scalemail chestplate tensura:armorsaurus_scalemail_chestplate armorsaurus scalemail gear schematic armorsaurus scale monster leather (d) {&quot;item&quot;: &quot;tensura:armorsaurus_scale&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:armorsaurus_scalemail_gear_schematic">
<h3>Armorsaurus Scalemail Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Armorsaurus Scale</li>
<li><strong>2×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Armorsaurus Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:armorsaurus_scalemail_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/armorsaurus_scalemail_chestplate.json</code></p><p>Required IDs: tensura:armorsaurus_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="armorsaurus scalemail helmet tensura:armorsaurus_scalemail_helmet armorsaurus scalemail gear schematic armorsaurus scale monster leather (d) {&quot;item&quot;: &quot;tensura:armorsaurus_scale&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:armorsaurus_scalemail_gear_schematic">
<h3>Armorsaurus Scalemail Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Armorsaurus Scale</li>
<li><strong>3×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Armorsaurus Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:armorsaurus_scalemail_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/armorsaurus_scalemail_helmet.json</code></p><p>Required IDs: tensura:armorsaurus_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="armorsaurus scalemail leggings tensura:armorsaurus_scalemail_leggings armorsaurus scalemail gear schematic armorsaurus scale monster leather (d) {&quot;item&quot;: &quot;tensura:armorsaurus_scale&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:armorsaurus_scalemail_gear_schematic">
<h3>Armorsaurus Scalemail Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Armorsaurus Scale</li>
<li><strong>2×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Armorsaurus Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:armorsaurus_scalemail_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/armorsaurus_scalemail_leggings.json</code></p><p>Required IDs: tensura:armorsaurus_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="armorsaurus shield tensura:armorsaurus_shield armorsaurus scalemail gear schematic + shield schematic armorsaurus shell armorsaurus scale low magisteel ingot {&quot;item&quot;: &quot;tensura:armorsaurus_shell&quot;} {&quot;item&quot;: &quot;tensura:armorsaurus_scale&quot;} {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} tensura:armorsaurus_scalemail_gear_schematic tensura:shield_schematic">
<h3>Armorsaurus Shield <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Armorsaurus Shell</li>
<li><strong>3×</strong> Armorsaurus Scale</li>
<li><strong>1×</strong> Low Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Armorsaurus Scalemail Gear Schematic + Shield Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:armorsaurus_shield</code></p><p>Resource: <code>data/tensura/recipe/smithing/armorsaurus_shield.json</code></p><p>Required IDs: tensura:armorsaurus_scalemail_gear_schematic, tensura:shield_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Basic Bows Schematic <span>5 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="invisible arrow tensura:invisible_arrow basic bows schematic flint stick invisible feather {&quot;item&quot;: &quot;minecraft:flint&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;tensura:invisible_feather&quot;} tensura:basic_bows_schematic">
<h3>Invisible Arrow <span>×6</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Flint</li>
<li><strong>1×</strong> Stick</li>
<li><strong>1×</strong> Invisible Feather</li>
</ul>
<p><strong>Learn all:</strong> Basic Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:invisible_arrow</code></p><p>Resource: <code>data/tensura/recipe/smithing/invisible_arrow.json</code></p><p>Required IDs: tensura:basic_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="long bow tensura:long_bow basic bows schematic stick string {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} tensura:basic_bows_schematic">
<h3>Long Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Stick</li>
<li><strong>4×</strong> String</li>
</ul>
<p><strong>Learn all:</strong> Basic Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:long_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/long_bow.json</code></p><p>Required IDs: tensura:basic_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="short bow tensura:short_bow basic bows schematic stick string {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} tensura:basic_bows_schematic">
<h3>Short Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Stick</li>
<li><strong>2×</strong> String</li>
</ul>
<p><strong>Learn all:</strong> Basic Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:short_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/short_bow.json</code></p><p>Required IDs: tensura:basic_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="speared fin arrow tensura:speared_fin_arrow basic bows schematic flint stick spear toro fin {&quot;item&quot;: &quot;minecraft:flint&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;tensura:spear_toro_fin&quot;} tensura:basic_bows_schematic">
<h3>Speared Fin Arrow <span>×6</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Flint</li>
<li><strong>1×</strong> Stick</li>
<li><strong>1×</strong> Spear Toro Fin</li>
</ul>
<p><strong>Learn all:</strong> Basic Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:speared_fin_arrow</code></p><p>Resource: <code>data/tensura/recipe/smithing/speared_fin_arrow.json</code></p><p>Required IDs: tensura:basic_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="war bow tensura:war_bow basic bows schematic stick string {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} tensura:basic_bows_schematic">
<h3>War Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Stick</li>
<li><strong>5×</strong> String</li>
</ul>
<p><strong>Learn all:</strong> Basic Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:war_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/war_bow.json</code></p><p>Required IDs: tensura:basic_bows_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Charybdis Scalemail Gear Schematic <span>7 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="charybdis scalemail boots tensura:charybdis_scalemail_boots charybdis scalemail gear schematic charybdis scale {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} tensura:charybdis_scalemail_gear_schematic">
<h3>Charybdis Scalemail Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Charybdis Scale</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:charybdis_scalemail_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/charybdis_scalemail_boots.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="charybdis scalemail chestplate tensura:charybdis_scalemail_chestplate charybdis scalemail gear schematic charybdis scale {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} tensura:charybdis_scalemail_gear_schematic">
<h3>Charybdis Scalemail Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Charybdis Scale</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:charybdis_scalemail_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/charybdis_scalemail_chestplate.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="charybdis scalemail helmet tensura:charybdis_scalemail_helmet charybdis scalemail gear schematic charybdis scale {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} tensura:charybdis_scalemail_gear_schematic">
<h3>Charybdis Scalemail Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Charybdis Scale</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:charybdis_scalemail_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/charybdis_scalemail_helmet.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="charybdis scalemail leggings tensura:charybdis_scalemail_leggings charybdis scalemail gear schematic charybdis scale {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} tensura:charybdis_scalemail_gear_schematic">
<h3>Charybdis Scalemail Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Charybdis Scale</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:charybdis_scalemail_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/charybdis_scalemail_leggings.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="tempest scale knife tensura:tempest_scale_knife charybdis scalemail gear schematic + high magisteel gear schematic + short sword schematic charybdis scale high magisteel ingot stick {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:charybdis_scalemail_gear_schematic tensura:high_magisteel_gear_schematic tensura:short_sword_schematic">
<h3>Tempest Scale Knife <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Charybdis Scale</li>
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic + High Magisteel Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:tempest_scale_knife</code></p><p>Resource: <code>data/tensura/recipe/smithing/tempest_scale_knife.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic, tensura:high_magisteel_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="tempest scale shield tensura:tempest_scale_shield charybdis scalemail gear schematic + shield schematic charybdis scale high magisteel ingot {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} tensura:charybdis_scalemail_gear_schematic tensura:shield_schematic">
<h3>Tempest Scale Shield <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>6×</strong> Charybdis Scale</li>
<li><strong>1×</strong> High Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic + Shield Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:tempest_scale_shield</code></p><p>Resource: <code>data/tensura/recipe/smithing/tempest_scale_shield.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic, tensura:shield_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="tempest scale sword tensura:tempest_scale_sword charybdis scalemail gear schematic + high magisteel gear schematic + long sword schematic charybdis scale high magisteel ingot stick {&quot;item&quot;: &quot;tensura:charybdis_scale&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:charybdis_scalemail_gear_schematic tensura:high_magisteel_gear_schematic tensura:long_sword_schematic">
<h3>Tempest Scale Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Charybdis Scale</li>
<li><strong>2×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Charybdis Scalemail Gear Schematic + High Magisteel Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:tempest_scale_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/tempest_scale_sword.json</code></p><p>Required IDs: tensura:charybdis_scalemail_gear_schematic, tensura:high_magisteel_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Dagger Schematic <span>2 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="centipede dagger tensura:centipede_dagger dagger schematic centipede stinger stick string {&quot;item&quot;: &quot;tensura:centipede_stinger&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} tensura:hunting_knife_schematic">
<h3>Centipede Dagger <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Centipede Stinger</li>
<li><strong>1×</strong> Stick</li>
<li><strong>1×</strong> String</li>
</ul>
<p><strong>Learn all:</strong> Dagger Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:centipede_dagger</code></p><p>Resource: <code>data/tensura/recipe/smithing/centipede_dagger.json</code></p><p>Required IDs: tensura:hunting_knife_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="spider dagger tensura:spider_dagger dagger schematic spider fang stick string {&quot;item&quot;: &quot;tensura:spider_fang&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} tensura:hunting_knife_schematic">
<h3>Spider Dagger <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Spider Fang</li>
<li><strong>1×</strong> Stick</li>
<li><strong>1×</strong> String</li>
</ul>
<p><strong>Learn all:</strong> Dagger Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:spider_dagger</code></p><p>Resource: <code>data/tensura/recipe/smithing/spider_dagger.json</code></p><p>Required IDs: tensura:hunting_knife_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Dark Set Schematic <span>3 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="dark boots tensura:dark_boots dark set schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:dark_set_schematic">
<h3>Dark Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Dark Set Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:dark_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/dark_boots.json</code></p><p>Required IDs: tensura:dark_set_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="dark jacket tensura:dark_jacket dark set schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:dark_set_schematic">
<h3>Dark Jacket <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Dark Set Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:dark_jacket</code></p><p>Resource: <code>data/tensura/recipe/smithing/dark_jacket.json</code></p><p>Required IDs: tensura:dark_set_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="dark leggings tensura:dark_leggings dark set schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:dark_set_schematic">
<h3>Dark Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Dark Set Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:dark_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/dark_leggings.json</code></p><p>Required IDs: tensura:dark_set_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Diamond Gear Schematic <span>10 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="diamond great sword tensura:diamond_great_sword diamond gear schematic + great sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:great_sword_schematic">
<h3>Diamond Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_great_sword.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond katana tensura:diamond_katana diamond gear schematic + japanese sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:japanese_sword_schematic">
<h3>Diamond Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_katana.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond kodachi tensura:diamond_kodachi diamond gear schematic + short sword schematic + japanese sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Diamond Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_kodachi.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond long sword tensura:diamond_long_sword diamond gear schematic + long sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:long_sword_schematic">
<h3>Diamond Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_long_sword.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond odachi tensura:diamond_odachi diamond gear schematic + great sword schematic + japanese sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Diamond Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_odachi.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond scythe tensura:diamond_scythe diamond gear schematic + great sword schematic + spear schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Diamond Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Diamond</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_scythe.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond short sword tensura:diamond_short_sword diamond gear schematic + short sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:short_sword_schematic">
<h3>Diamond Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_short_sword.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond sickle tensura:diamond_sickle diamond gear schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic">
<h3>Diamond Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Diamond</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_sickle.json</code></p><p>Required IDs: tensura:diamond_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond spear tensura:diamond_spear diamond gear schematic + spear schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:spear_schematic">
<h3>Diamond Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Diamond</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_spear.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="diamond tachi tensura:diamond_tachi diamond gear schematic + long sword schematic + japanese sword schematic diamond stick {&quot;item&quot;: &quot;minecraft:diamond&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:diamond_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Diamond Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Diamond</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Diamond Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:diamond_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/diamond_tachi.json</code></p><p>Required IDs: tensura:diamond_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Gold Gear Schematic <span>11 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="blade tiger scythe tensura:blade_tiger_scythe gold gear schematic + great sword schematic + spear schematic blade tiger tail gold ingot stick {&quot;item&quot;: &quot;tensura:blade_tiger_tail&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Blade Tiger Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Blade Tiger Tail</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:blade_tiger_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/blade_tiger_scythe.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden great sword tensura:golden_great_sword gold gear schematic + great sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:great_sword_schematic">
<h3>Golden Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_great_sword.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden katana tensura:golden_katana gold gear schematic + japanese sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:japanese_sword_schematic">
<h3>Golden Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_katana.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden kodachi tensura:golden_kodachi gold gear schematic + short sword schematic + japanese sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Golden Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_kodachi.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden long sword tensura:golden_long_sword gold gear schematic + long sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:long_sword_schematic">
<h3>Golden Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_long_sword.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden odachi tensura:golden_odachi gold gear schematic + great sword schematic + japanese sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Golden Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_odachi.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden scythe tensura:golden_scythe gold gear schematic + great sword schematic + spear schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Golden Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_scythe.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden short sword tensura:golden_short_sword gold gear schematic + short sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:short_sword_schematic">
<h3>Golden Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_short_sword.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden sickle tensura:golden_sickle gold gear schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic">
<h3>Golden Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_sickle.json</code></p><p>Required IDs: tensura:gold_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden spear tensura:golden_spear gold gear schematic + spear schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:spear_schematic">
<h3>Golden Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_spear.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="golden tachi tensura:golden_tachi gold gear schematic + long sword schematic + japanese sword schematic gold ingot stick {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:gold_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Golden Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Gold Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:golden_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/golden_tachi.json</code></p><p>Required IDs: tensura:gold_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Great Sword Schematic <span>6 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="stone great sword tensura:stone_great_sword great sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic">
<h3>Stone Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_great_sword.json</code></p><p>Required IDs: tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="stone odachi tensura:stone_odachi great sword schematic + japanese sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Stone Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_odachi.json</code></p><p>Required IDs: tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="stone scythe tensura:stone_scythe great sword schematic + spear schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic tensura:spear_schematic">
<h3>Stone Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:stone_tool_materials</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_scythe.json</code></p><p>Required IDs: tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden great sword tensura:wooden_great_sword great sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic">
<h3>Wooden Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_great_sword.json</code></p><p>Required IDs: tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden odachi tensura:wooden_odachi great sword schematic + japanese sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Wooden Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_odachi.json</code></p><p>Required IDs: tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden scythe tensura:wooden_scythe great sword schematic + spear schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:great_sword_schematic tensura:spear_schematic">
<h3>Wooden Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> #minecraft:planks</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_scythe.json</code></p><p>Required IDs: tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>High Magisteel Gear Schematic <span>23 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel axe tensura:high_magisteel_axe high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_axe.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel boots tensura:high_magisteel_boots high magisteel gear schematic high magisteel ingot {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> High Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_boots.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel chestplate tensura:high_magisteel_chestplate high magisteel gear schematic high magisteel ingot monster leather (c) {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> High Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_chestplate.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel great sword tensura:high_magisteel_great_sword high magisteel gear schematic + great sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:great_sword_schematic">
<h3>High Magisteel Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_great_sword.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel helmet tensura:high_magisteel_helmet high magisteel gear schematic high magisteel ingot {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> High Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_helmet.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel hoe tensura:high_magisteel_hoe high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_hoe.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel katana tensura:high_magisteel_katana high magisteel gear schematic + japanese sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:japanese_sword_schematic">
<h3>High Magisteel Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_katana.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel kodachi tensura:high_magisteel_kodachi high magisteel gear schematic + short sword schematic + japanese sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>High Magisteel Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_kodachi.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel leggings tensura:high_magisteel_leggings high magisteel gear schematic high magisteel ingot monster leather (c) {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> High Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_leggings.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel long sword tensura:high_magisteel_long_sword high magisteel gear schematic + long sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:long_sword_schematic">
<h3>High Magisteel Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_long_sword.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel odachi tensura:high_magisteel_odachi high magisteel gear schematic + great sword schematic + japanese sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>High Magisteel Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_odachi.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel pickaxe tensura:high_magisteel_pickaxe high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_pickaxe.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel scythe tensura:high_magisteel_scythe high magisteel gear schematic + great sword schematic + spear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>High Magisteel Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_scythe.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel short sword tensura:high_magisteel_short_sword high magisteel gear schematic + short sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:short_sword_schematic">
<h3>High Magisteel Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_short_sword.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel shovel tensura:high_magisteel_shovel high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_shovel.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel sickle tensura:high_magisteel_sickle high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_sickle.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel spear tensura:high_magisteel_spear high magisteel gear schematic + spear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:spear_schematic">
<h3>High Magisteel Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_spear.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel sword tensura:high_magisteel_sword high magisteel gear schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>High Magisteel Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_sword.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magisteel tachi tensura:high_magisteel_tachi high magisteel gear schematic + long sword schematic + japanese sword schematic high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>High Magisteel Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magisteel_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magisteel_tachi.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="ice blade tensura:ice_blade high magisteel gear schematic + long sword schematic high magisteel ingot element core (water) ender eye stick {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:element_core_water&quot;} {&quot;item&quot;: &quot;minecraft:ender_eye&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:long_sword_schematic">
<h3>Ice Blade <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> High Magisteel Ingot</li>
<li><strong>2×</strong> Element Core (Water)</li>
<li><strong>1×</strong> Ender Eye</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:ice_blade</code></p><p>Resource: <code>data/tensura/recipe/smithing/ice_blade.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="medium magic staff tensura:medium_magic_staff high magisteel gear schematic + magic staff schematic magic stone high magisteel ingot stick {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:magic_staff_schematic">
<h3>Medium Magic Staff <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> High Magisteel Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Magic Staff Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:medium_magic_staff</code></p><p>Resource: <code>data/tensura/recipe/smithing/medium_magic_staff.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:magic_staff_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="sissie tooth pickaxe tensura:sissie_tooth_pickaxe high magisteel gear schematic sissie tooth high magisteel ingot stick {&quot;item&quot;: &quot;tensura:sissie_tooth&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic">
<h3>Sissie Tooth Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Sissie Tooth</li>
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:sissie_tooth_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/sissie_tooth_pickaxe.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="staff of slime tensura:slime_staff high magisteel gear schematic + magic staff schematic slime core high magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:slime_core&quot;} {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:high_magisteel_gear_schematic tensura:magic_staff_schematic">
<h3>Staff of Slime <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Slime Core</li>
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> High Magisteel Gear Schematic + Magic Staff Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:slime_staff</code></p><p>Resource: <code>data/tensura/recipe/smithing/slime_staff.json</code></p><p>Required IDs: tensura:high_magisteel_gear_schematic, tensura:magic_staff_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Hihi&#x27;Irokane Gear Schematic <span>19 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane axe tensura:hihiirokane_axe hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_axe.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane boots tensura:hihiirokane_boots hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Hihi&#x27;Irokane Ingot</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_boots.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane chestplate tensura:hihiirokane_chestplate hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Hihi&#x27;Irokane Ingot</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_chestplate.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane great sword tensura:hihiirokane_great_sword hihi&#x27;irokane gear schematic + great sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:great_sword_schematic">
<h3>Hihi&#x27;Irokane Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_great_sword.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane helmet tensura:hihiirokane_helmet hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Hihi&#x27;Irokane Ingot</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_helmet.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane hoe tensura:hihiirokane_hoe hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_hoe.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane katana tensura:hihiirokane_katana hihi&#x27;irokane gear schematic + japanese sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:japanese_sword_schematic">
<h3>Hihi&#x27;Irokane Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_katana.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane kodachi tensura:hihiirokane_kodachi hihi&#x27;irokane gear schematic + short sword schematic + japanese sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Hihi&#x27;Irokane Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_kodachi.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane leggings tensura:hihiirokane_leggings hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Hihi&#x27;Irokane Ingot</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_leggings.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane long sword tensura:hihiirokane_long_sword hihi&#x27;irokane gear schematic + long sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:long_sword_schematic">
<h3>Hihi&#x27;Irokane Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_long_sword.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane odachi tensura:hihiirokane_odachi hihi&#x27;irokane gear schematic + great sword schematic + japanese sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Hihi&#x27;Irokane Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_odachi.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane pickaxe tensura:hihiirokane_pickaxe hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_pickaxe.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane scythe tensura:hihiirokane_scythe hihi&#x27;irokane gear schematic + great sword schematic + spear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Hihi&#x27;Irokane Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_scythe.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane short sword tensura:hihiirokane_short_sword hihi&#x27;irokane gear schematic + short sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:short_sword_schematic">
<h3>Hihi&#x27;Irokane Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_short_sword.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane shovel tensura:hihiirokane_shovel hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_shovel.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane sickle tensura:hihiirokane_sickle hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_sickle.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane spear tensura:hihiirokane_spear hihi&#x27;irokane gear schematic + spear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:spear_schematic">
<h3>Hihi&#x27;Irokane Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_spear.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane sword tensura:hihiirokane_sword hihi&#x27;irokane gear schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic">
<h3>Hihi&#x27;Irokane Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_sword.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="hihi&#x27;irokane tachi tensura:hihiirokane_tachi hihi&#x27;irokane gear schematic + long sword schematic + japanese sword schematic hihi&#x27;irokane ingot stick {&quot;item&quot;: &quot;tensura:hihiirokane_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:hihiirokane_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Hihi&#x27;Irokane Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Hihi&#x27;Irokane Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Hihi&#x27;Irokane Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:hihiirokane_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/hihiirokane_tachi.json</code></p><p>Required IDs: tensura:hihiirokane_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Iron Gear Schematic <span>10 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="iron great sword tensura:iron_great_sword iron gear schematic + great sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:great_sword_schematic">
<h3>Iron Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_great_sword.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron katana tensura:iron_katana iron gear schematic + japanese sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:japanese_sword_schematic">
<h3>Iron Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_katana.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron kodachi tensura:iron_kodachi iron gear schematic + short sword schematic + japanese sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Iron Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_kodachi.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron long sword tensura:iron_long_sword iron gear schematic + long sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:long_sword_schematic">
<h3>Iron Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_long_sword.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron odachi tensura:iron_odachi iron gear schematic + great sword schematic + japanese sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Iron Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_odachi.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron scythe tensura:iron_scythe iron gear schematic + great sword schematic + spear schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Iron Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Iron Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_scythe.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron short sword tensura:iron_short_sword iron gear schematic + short sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:short_sword_schematic">
<h3>Iron Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_short_sword.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron sickle tensura:iron_sickle iron gear schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic">
<h3>Iron Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Iron Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_sickle.json</code></p><p>Required IDs: tensura:iron_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron spear tensura:iron_spear iron gear schematic + spear schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:spear_schematic">
<h3>Iron Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Iron Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_spear.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="iron tachi tensura:iron_tachi iron gear schematic + long sword schematic + japanese sword schematic iron ingot stick {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:iron_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Iron Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Iron Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Iron Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:iron_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/iron_tachi.json</code></p><p>Required IDs: tensura:iron_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Japanese Sword Schematic <span>2 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="stone katana tensura:stone_katana japanese sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:japanese_sword_schematic">
<h3>Stone Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_katana.json</code></p><p>Required IDs: tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden katana tensura:wooden_katana japanese sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:japanese_sword_schematic">
<h3>Wooden Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_katana.json</code></p><p>Required IDs: tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Knight Spider Carapace Gear Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="knight spider carapace boots tensura:knight_spider_carapace_boots knight spider carapace gear schematic knight spider carapace monster leather (d) {&quot;item&quot;: &quot;tensura:knight_spider_carapace&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:knight_spider_carapace_gear_schematic">
<h3>Knight Spider Carapace Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Knight Spider Carapace</li>
<li><strong>1×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Knight Spider Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:knight_spider_carapace_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/knight_spider_carapace_boots.json</code></p><p>Required IDs: tensura:knight_spider_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="knight spider carapace chestplate tensura:knight_spider_carapace_chestplate knight spider carapace gear schematic knight spider carapace monster leather (d) {&quot;item&quot;: &quot;tensura:knight_spider_carapace&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:knight_spider_carapace_gear_schematic">
<h3>Knight Spider Carapace Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Knight Spider Carapace</li>
<li><strong>3×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Knight Spider Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:knight_spider_carapace_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/knight_spider_carapace_chestplate.json</code></p><p>Required IDs: tensura:knight_spider_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="knight spider carapace helmet tensura:knight_spider_carapace_helmet knight spider carapace gear schematic knight spider carapace monster leather (d) {&quot;item&quot;: &quot;tensura:knight_spider_carapace&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:knight_spider_carapace_gear_schematic">
<h3>Knight Spider Carapace Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Knight Spider Carapace</li>
<li><strong>2×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Knight Spider Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:knight_spider_carapace_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/knight_spider_carapace_helmet.json</code></p><p>Required IDs: tensura:knight_spider_carapace_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="knight spider carapace leggings tensura:knight_spider_carapace_leggings knight spider carapace gear schematic knight spider carapace monster leather (d) {&quot;item&quot;: &quot;tensura:knight_spider_carapace&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:knight_spider_carapace_gear_schematic">
<h3>Knight Spider Carapace Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Knight Spider Carapace</li>
<li><strong>4×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Knight Spider Carapace Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:knight_spider_carapace_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/knight_spider_carapace_leggings.json</code></p><p>Required IDs: tensura:knight_spider_carapace_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Kunai Schematic <span>2 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="kunai tensura:kunai kunai schematic iron nugget {&quot;item&quot;: &quot;minecraft:iron_nugget&quot;} tensura:kunai_schematic">
<h3>Kunai <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Iron Nugget</li>
</ul>
<p><strong>Learn all:</strong> Kunai Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:kunai</code></p><p>Resource: <code>data/tensura/recipe/smithing/kunai.json</code></p><p>Required IDs: tensura:kunai_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel kunai tensura:pure_magisteel_kunai kunai schematic + pure magisteel gear schematic pure magisteel nugget gold nugget {&quot;item&quot;: &quot;tensura:pure_magisteel_nugget&quot;} {&quot;item&quot;: &quot;minecraft:gold_nugget&quot;} tensura:kunai_schematic tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Kunai <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Pure Magisteel Nugget</li>
<li><strong>2×</strong> Gold Nugget</li>
</ul>
<p><strong>Learn all:</strong> Kunai Schematic + Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_kunai</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_kunai.json</code></p><p>Required IDs: tensura:kunai_schematic, tensura:pure_magisteel_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Long Sword Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="stone long sword tensura:stone_long_sword long sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:long_sword_schematic">
<h3>Stone Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_long_sword.json</code></p><p>Required IDs: tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="stone tachi tensura:stone_tachi long sword schematic + japanese sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Stone Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_tachi.json</code></p><p>Required IDs: tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden long sword tensura:wooden_long_sword long sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:long_sword_schematic">
<h3>Wooden Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_long_sword.json</code></p><p>Required IDs: tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden tachi tensura:wooden_tachi long sword schematic + japanese sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Wooden Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_tachi.json</code></p><p>Required IDs: tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Low Magisteel Gear Schematic <span>27 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="daemon core tensura:daemon_core low magisteel gear schematic magic stone daemon essence {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:daemon_essence&quot;} tensura:low_magisteel_gear_schematic">
<h3>Daemon Core <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>8×</strong> Daemon Essence</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:daemon_core</code></p><p>Resource: <code>data/tensura/recipe/smithing/daemon_core.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="empty element core tensura:element_core_empty low magisteel gear schematic magic stone medium quality magic crystal {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:medium_quality_magic_crystal&quot;} tensura:low_magisteel_gear_schematic">
<h3>Empty Element Core <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>8×</strong> Medium Quality Magic Crystal</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:element_core_empty</code></p><p>Resource: <code>data/tensura/recipe/smithing/element_core_empty.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="kanabo tensura:kanabo low magisteel gear schematic goblin club low magisteel ingot gold ingot {&quot;item&quot;: &quot;tensura:goblin_club&quot;} {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:low_magisteel_gear_schematic">
<h3>Kanabo <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Goblin Club</li>
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>2×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:kanabo</code></p><p>Resource: <code>data/tensura/recipe/smithing/kanabo.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magic staff tensura:low_magic_staff low magisteel gear schematic + magic staff schematic magic stone low magisteel ingot stick {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:magic_staff_schematic">
<h3>Low Magic Staff <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> Low Magisteel Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Magic Staff Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magic_staff</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magic_staff.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:magic_staff_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel axe tensura:low_magisteel_axe low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_axe.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel boots tensura:low_magisteel_boots low magisteel gear schematic low magisteel ingot {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Low Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_boots.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel chestplate tensura:low_magisteel_chestplate low magisteel gear schematic low magisteel ingot monster leather (d) {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Low Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_chestplate.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel great sword tensura:low_magisteel_great_sword low magisteel gear schematic + great sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:great_sword_schematic">
<h3>Low Magisteel Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_great_sword.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel helmet tensura:low_magisteel_helmet low magisteel gear schematic low magisteel ingot {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Low Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_helmet.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel hoe tensura:low_magisteel_hoe low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_hoe.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel katana tensura:low_magisteel_katana low magisteel gear schematic + japanese sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:japanese_sword_schematic">
<h3>Low Magisteel Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_katana.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel kodachi tensura:low_magisteel_kodachi low magisteel gear schematic + short sword schematic + japanese sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Low Magisteel Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_kodachi.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel leggings tensura:low_magisteel_leggings low magisteel gear schematic low magisteel ingot monster leather (d) {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Low Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_leggings.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel long sword tensura:low_magisteel_long_sword low magisteel gear schematic + long sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:long_sword_schematic">
<h3>Low Magisteel Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_long_sword.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel odachi tensura:low_magisteel_odachi low magisteel gear schematic + great sword schematic + japanese sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Low Magisteel Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_odachi.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel pickaxe tensura:low_magisteel_pickaxe low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_pickaxe.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel scythe tensura:low_magisteel_scythe low magisteel gear schematic + great sword schematic + spear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Low Magisteel Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_scythe.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel short sword tensura:low_magisteel_short_sword low magisteel gear schematic + short sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:short_sword_schematic">
<h3>Low Magisteel Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_short_sword.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel shovel tensura:low_magisteel_shovel low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_shovel.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel sickle tensura:low_magisteel_sickle low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_sickle.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel spear tensura:low_magisteel_spear low magisteel gear schematic + spear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:spear_schematic">
<h3>Low Magisteel Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_spear.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel sword tensura:low_magisteel_sword low magisteel gear schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Magisteel Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_sword.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low magisteel tachi tensura:low_magisteel_tachi low magisteel gear schematic + long sword schematic + japanese sword schematic low magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:low_magisteel_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Low Magisteel Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Low Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_magisteel_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_magisteel_tachi.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="low quality magic crystal tensura:low_quality_magic_crystal low magisteel gear schematic medium quality magic crystal {&quot;item&quot;: &quot;tensura:medium_quality_magic_crystal&quot;} tensura:low_magisteel_gear_schematic">
<h3>Low Quality Magic Crystal <span>×2</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Medium Quality Magic Crystal</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:low_quality_magic_crystal</code></p><p>Resource: <code>data/tensura/recipe/smithing/low_quality_magic_crystal.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="magic stone tensura:magic_stone low magisteel gear schematic low magisteel ingot low quality magic crystal {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:low_quality_magic_crystal&quot;} tensura:low_magisteel_gear_schematic">
<h3>Magic Stone <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Low Magisteel Ingot</li>
<li><strong>8×</strong> Low Quality Magic Crystal</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:magic_stone</code></p><p>Resource: <code>data/tensura/recipe/smithing/magic_stone.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="medium quality magic crystal tensura:medium_quality_magic_crystal low magisteel gear schematic high quality magic crystal {&quot;item&quot;: &quot;tensura:high_quality_magic_crystal&quot;} tensura:low_magisteel_gear_schematic">
<h3>Medium Quality Magic Crystal <span>×2</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Quality Magic Crystal</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:medium_quality_magic_crystal</code></p><p>Resource: <code>data/tensura/recipe/smithing/medium_quality_magic_crystal.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="warp core tensura:warp_core low magisteel gear schematic magic stone low magisteel ingot element core (space) ender pearl {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:low_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:element_core_space&quot;} {&quot;item&quot;: &quot;minecraft:ender_pearl&quot;} tensura:low_magisteel_gear_schematic">
<h3>Warp Core <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>4×</strong> Low Magisteel Ingot</li>
<li><strong>2×</strong> Element Core (Space)</li>
<li><strong>2×</strong> Ender Pearl</li>
</ul>
<p><strong>Learn all:</strong> Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:warp_core</code></p><p>Resource: <code>data/tensura/recipe/smithing/warp_core.json</code></p><p>Required IDs: tensura:low_magisteel_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Mithril Gear Schematic <span>21 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="enchanted silver apple tensura:enchanted_silver_apple mithril gear schematic silver apple mithril ingot {&quot;item&quot;: &quot;tensura:silver_apple&quot;} {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} tensura:mithril_gear_schematic">
<h3>Enchanted Silver Apple <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Silver Apple</li>
<li><strong>8×</strong> Mithril Ingot</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:enchanted_silver_apple</code></p><p>Resource: <code>data/tensura/recipe/smithing/enchanted_silver_apple.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril axe tensura:mithril_axe mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_axe.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril boots tensura:mithril_boots mithril gear schematic mithril ingot gold ingot {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Mithril Ingot</li>
<li><strong>2×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_boots.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril chestplate tensura:mithril_chestplate mithril gear schematic mithril ingot gold ingot monster leather (b) {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Mithril Ingot</li>
<li><strong>4×</strong> Gold Ingot</li>
<li><strong>2×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_chestplate.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril great sword tensura:mithril_great_sword mithril gear schematic + great sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:great_sword_schematic">
<h3>Mithril Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_great_sword.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril helmet tensura:mithril_helmet mithril gear schematic mithril ingot feather {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:feather&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Mithril Ingot</li>
<li><strong>3×</strong> Feather</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_helmet.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril hoe tensura:mithril_hoe mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_hoe.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril katana tensura:mithril_katana mithril gear schematic + japanese sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:japanese_sword_schematic">
<h3>Mithril Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_katana.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril kodachi tensura:mithril_kodachi mithril gear schematic + short sword schematic + japanese sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Mithril Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_kodachi.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril leggings tensura:mithril_leggings mithril gear schematic mithril ingot gold ingot monster leather (b) {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Mithril Ingot</li>
<li><strong>3×</strong> Gold Ingot</li>
<li><strong>2×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_leggings.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril long sword tensura:mithril_long_sword mithril gear schematic + long sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:long_sword_schematic">
<h3>Mithril Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_long_sword.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril odachi tensura:mithril_odachi mithril gear schematic + great sword schematic + japanese sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Mithril Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_odachi.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril pickaxe tensura:mithril_pickaxe mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_pickaxe.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril scythe tensura:mithril_scythe mithril gear schematic + great sword schematic + spear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Mithril Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_scythe.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril short sword tensura:mithril_short_sword mithril gear schematic + short sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:short_sword_schematic">
<h3>Mithril Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_short_sword.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril shovel tensura:mithril_shovel mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_shovel.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril sickle tensura:mithril_sickle mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_sickle.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril spear tensura:mithril_spear mithril gear schematic + spear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:spear_schematic">
<h3>Mithril Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_spear.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril sword tensura:mithril_sword mithril gear schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic">
<h3>Mithril Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_sword.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="mithril tachi tensura:mithril_tachi mithril gear schematic + long sword schematic + japanese sword schematic mithril ingot gold ingot stick {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:mithril_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Mithril Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:mithril_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/mithril_tachi.json</code></p><p>Required IDs: tensura:mithril_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="race reset scroll tensura:race_reset_scroll mithril gear schematic mithril ingot magic stone monster leather (a) paper {&quot;item&quot;: &quot;tensura:mithril_ingot&quot;} {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} {&quot;item&quot;: &quot;minecraft:paper&quot;} tensura:mithril_gear_schematic">
<h3>Race Reset Scroll <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Mithril Ingot</li>
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> Monster Leather (A)</li>
<li><strong>4×</strong> Paper</li>
</ul>
<p><strong>Learn all:</strong> Mithril Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:race_reset_scroll</code></p><p>Resource: <code>data/tensura/recipe/smithing/race_reset_scroll.json</code></p><p>Required IDs: tensura:mithril_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Monster Leather Gear Schematic <span>23 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="bat glider tensura:bat_glider monster leather gear schematic giant bat wing monster leather (c) magic stone {&quot;item&quot;: &quot;tensura:giant_bat_wing&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} {&quot;item&quot;: &quot;tensura:magic_stone&quot;} tensura:monster_leather_gear_schematic">
<h3>Bat Glider <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Giant Bat Wing</li>
<li><strong>2×</strong> Monster Leather (C)</li>
<li><strong>1×</strong> Magic Stone</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:bat_glider</code></p><p>Resource: <code>data/tensura/recipe/smithing/bat_glider.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather boots (a) tensura:monster_leather_boots_a monster leather gear schematic monster leather (a) {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Boots (A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_boots_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_boots_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather boots (b) tensura:monster_leather_boots_b monster leather gear schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Boots (B) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_boots_b</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_boots_b.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather boots (c) tensura:monster_leather_boots_c monster leather gear schematic monster leather (c) {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Boots (C) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_boots_c</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_boots_c.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather boots (d) tensura:monster_leather_boots_d monster leather gear schematic monster leather (d) {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Boots (D) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_boots_d</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_boots_d.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather boots (special a) tensura:monster_leather_boots_special_a monster leather gear schematic monster leather (special a) {&quot;item&quot;: &quot;tensura:monster_leather_special_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Boots (Special A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (Special A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_boots_special_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_boots_special_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather chestplate (a) tensura:monster_leather_chestplate_a monster leather gear schematic monster leather (a) {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Chestplate (A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_chestplate_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_chestplate_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather chestplate (b) tensura:monster_leather_chestplate_b monster leather gear schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Chestplate (B) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_chestplate_b</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_chestplate_b.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather chestplate (c) tensura:monster_leather_chestplate_c monster leather gear schematic monster leather (c) {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Chestplate (C) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_chestplate_c</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_chestplate_c.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather chestplate (d) tensura:monster_leather_chestplate_d monster leather gear schematic monster leather (d) {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Chestplate (D) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_chestplate_d</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_chestplate_d.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather chestplate (special a) tensura:monster_leather_chestplate_special_a monster leather gear schematic monster leather (special a) {&quot;item&quot;: &quot;tensura:monster_leather_special_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Chestplate (Special A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Monster Leather (Special A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_chestplate_special_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_chestplate_special_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather helmet (a) tensura:monster_leather_helmet_a monster leather gear schematic monster leather (a) {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Helmet (A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_helmet_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_helmet_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather helmet (b) tensura:monster_leather_helmet_b monster leather gear schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Helmet (B) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_helmet_b</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_helmet_b.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather helmet (c) tensura:monster_leather_helmet_c monster leather gear schematic monster leather (c) {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Helmet (C) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_helmet_c</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_helmet_c.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather helmet (d) tensura:monster_leather_helmet_d monster leather gear schematic monster leather (d) {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Helmet (D) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_helmet_d</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_helmet_d.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather helmet (special a) tensura:monster_leather_helmet_special_a monster leather gear schematic monster leather (special a) {&quot;item&quot;: &quot;tensura:monster_leather_special_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Helmet (Special A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (Special A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_helmet_special_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_helmet_special_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather leggings (a) tensura:monster_leather_leggings_a monster leather gear schematic monster leather (a) {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Leggings (A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_leggings_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_leggings_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather leggings (b) tensura:monster_leather_leggings_b monster leather gear schematic monster leather (b) {&quot;item&quot;: &quot;tensura:monster_leather_b&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Leggings (B) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (B)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_leggings_b</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_leggings_b.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather leggings (c) tensura:monster_leather_leggings_c monster leather gear schematic monster leather (c) {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Leggings (C) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (C)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_leggings_c</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_leggings_c.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather leggings (d) tensura:monster_leather_leggings_d monster leather gear schematic monster leather (d) {&quot;item&quot;: &quot;tensura:monster_leather_d&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Leggings (D) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (D)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_leggings_d</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_leggings_d.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster leather leggings (special a) tensura:monster_leather_leggings_special_a monster leather gear schematic monster leather (special a) {&quot;item&quot;: &quot;tensura:monster_leather_special_a&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Leather Leggings (Special A) <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Monster Leather (Special A)</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_leather_leggings_special_a</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_leather_leggings_special_a.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="monster saddle tensura:monster_saddle monster leather gear schematic monster leather (c) pure magisteel nugget steel thread {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} {&quot;item&quot;: &quot;tensura:pure_magisteel_nugget&quot;} {&quot;item&quot;: &quot;tensura:steel_thread&quot;} tensura:monster_leather_gear_schematic">
<h3>Monster Saddle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Monster Leather (C)</li>
<li><strong>8×</strong> Pure Magisteel Nugget</li>
<li><strong>2×</strong> Steel Thread</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:monster_saddle</code></p><p>Resource: <code>data/tensura/recipe/smithing/monster_saddle.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="winged shoes tensura:winged_shoes monster leather gear schematic + low magisteel gear schematic monster leather (c) dragon peacock feather magic stone {&quot;item&quot;: &quot;tensura:monster_leather_c&quot;} {&quot;item&quot;: &quot;tensura:dragon_peacock_feather&quot;} {&quot;item&quot;: &quot;tensura:magic_stone&quot;} tensura:monster_leather_gear_schematic tensura:low_magisteel_gear_schematic">
<h3>Winged Shoes <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Monster Leather (C)</li>
<li><strong>4×</strong> Dragon Peacock Feather</li>
<li><strong>1×</strong> Magic Stone</li>
</ul>
<p><strong>Learn all:</strong> Monster Leather Gear Schematic + Low Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:winged_shoes</code></p><p>Resource: <code>data/tensura/recipe/smithing/winged_shoes.json</code></p><p>Required IDs: tensura:monster_leather_gear_schematic, tensura:low_magisteel_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Orichalcum Gear Schematic <span>20 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum axe tensura:orichalcum_axe orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_axe.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum boots tensura:orichalcum_boots orichalcum gear schematic orichalcum ingot gold ingot {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Gold Ingot</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_boots.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum chestplate tensura:orichalcum_chestplate orichalcum gear schematic orichalcum ingot gold ingot monster leather (a) {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Orichalcum Ingot</li>
<li><strong>4×</strong> Gold Ingot</li>
<li><strong>2×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_chestplate.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum great sword tensura:orichalcum_great_sword orichalcum gear schematic + great sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:great_sword_schematic">
<h3>Orichalcum Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_great_sword.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum helmet tensura:orichalcum_helmet orichalcum gear schematic orichalcum ingot gold ingot monster leather (a) {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Gold Ingot</li>
<li><strong>2×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_helmet.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum hoe tensura:orichalcum_hoe orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_hoe.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum katana tensura:orichalcum_katana orichalcum gear schematic + japanese sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:japanese_sword_schematic">
<h3>Orichalcum Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_katana.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum kodachi tensura:orichalcum_kodachi orichalcum gear schematic + short sword schematic + japanese sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Orichalcum Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_kodachi.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum leggings tensura:orichalcum_leggings orichalcum gear schematic orichalcum ingot gold ingot monster leather (a) {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Orichalcum Ingot</li>
<li><strong>3×</strong> Gold Ingot</li>
<li><strong>2×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_leggings.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum long sword tensura:orichalcum_long_sword orichalcum gear schematic + long sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:long_sword_schematic">
<h3>Orichalcum Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_long_sword.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum odachi tensura:orichalcum_odachi orichalcum gear schematic + great sword schematic + japanese sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Orichalcum Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_odachi.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum pickaxe tensura:orichalcum_pickaxe orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_pickaxe.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum scythe tensura:orichalcum_scythe orichalcum gear schematic + great sword schematic + spear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Orichalcum Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Orichalcum Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_scythe.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum short sword tensura:orichalcum_short_sword orichalcum gear schematic + short sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:short_sword_schematic">
<h3>Orichalcum Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_short_sword.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum shovel tensura:orichalcum_shovel orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_shovel.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum sickle tensura:orichalcum_sickle orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Orichalcum Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_sickle.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum spear tensura:orichalcum_spear orichalcum gear schematic + spear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:spear_schematic">
<h3>Orichalcum Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Orichalcum Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_spear.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum sword tensura:orichalcum_sword orichalcum gear schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic">
<h3>Orichalcum Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_sword.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="orichalcum tachi tensura:orichalcum_tachi orichalcum gear schematic + long sword schematic + japanese sword schematic orichalcum ingot stick {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:orichalcum_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Orichalcum Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:orichalcum_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/orichalcum_tachi.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="skill reset scroll tensura:skill_reset_scroll orichalcum gear schematic orichalcum ingot pure magisteel ingot magic stone monster leather (a) paper {&quot;item&quot;: &quot;tensura:orichalcum_ingot&quot;} {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} {&quot;item&quot;: &quot;minecraft:paper&quot;} tensura:orichalcum_gear_schematic">
<h3>Skill Reset Scroll <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Orichalcum Ingot</li>
<li><strong>1×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> Monster Leather (A)</li>
<li><strong>3×</strong> Paper</li>
</ul>
<p><strong>Learn all:</strong> Orichalcum Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:skill_reset_scroll</code></p><p>Resource: <code>data/tensura/recipe/smithing/skill_reset_scroll.json</code></p><p>Required IDs: tensura:orichalcum_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Pierrot Mask Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="angry pierrot mask tensura:angry_pierrot_mask pierrot mask schematic high magisteel ingot clay ball red dye orange dye blue dye {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:clay_ball&quot;} {&quot;item&quot;: &quot;minecraft:red_dye&quot;} {&quot;item&quot;: &quot;minecraft:orange_dye&quot;} {&quot;item&quot;: &quot;minecraft:blue_dye&quot;} tensura:pierrot_mask_schematic">
<h3>Angry Pierrot Mask <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>3×</strong> Clay Ball</li>
<li><strong>1×</strong> Red Dye</li>
<li><strong>1×</strong> Orange Dye</li>
<li><strong>1×</strong> Blue Dye</li>
</ul>
<p><strong>Learn all:</strong> Pierrot Mask Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:angry_pierrot_mask</code></p><p>Resource: <code>data/tensura/recipe/smithing/angry_pierrot_mask.json</code></p><p>Required IDs: tensura:pierrot_mask_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="crazy pierrot mask tensura:crazy_pierrot_mask pierrot mask schematic high magisteel ingot clay ball yellow dye black dye {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:clay_ball&quot;} {&quot;item&quot;: &quot;minecraft:yellow_dye&quot;} {&quot;item&quot;: &quot;minecraft:black_dye&quot;} tensura:pierrot_mask_schematic">
<h3>Crazy Pierrot Mask <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>3×</strong> Clay Ball</li>
<li><strong>1×</strong> Yellow Dye</li>
<li><strong>1×</strong> Black Dye</li>
</ul>
<p><strong>Learn all:</strong> Pierrot Mask Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:crazy_pierrot_mask</code></p><p>Resource: <code>data/tensura/recipe/smithing/crazy_pierrot_mask.json</code></p><p>Required IDs: tensura:pierrot_mask_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="teardrop mask tensura:teary_pierrot_mask pierrot mask schematic high magisteel ingot clay ball pink dye yellow dye red dye {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:clay_ball&quot;} {&quot;item&quot;: &quot;minecraft:pink_dye&quot;} {&quot;item&quot;: &quot;minecraft:yellow_dye&quot;} {&quot;item&quot;: &quot;minecraft:red_dye&quot;} tensura:pierrot_mask_schematic">
<h3>Teardrop Mask <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>3×</strong> Clay Ball</li>
<li><strong>1×</strong> Pink Dye</li>
<li><strong>1×</strong> Yellow Dye</li>
<li><strong>1×</strong> Red Dye</li>
</ul>
<p><strong>Learn all:</strong> Pierrot Mask Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:teary_pierrot_mask</code></p><p>Resource: <code>data/tensura/recipe/smithing/teary_pierrot_mask.json</code></p><p>Required IDs: tensura:pierrot_mask_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wonder pierrot mask tensura:wonder_pierrot_mask pierrot mask schematic high magisteel ingot clay ball purple dye red dye pink dye {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:clay_ball&quot;} {&quot;item&quot;: &quot;minecraft:purple_dye&quot;} {&quot;item&quot;: &quot;minecraft:red_dye&quot;} {&quot;item&quot;: &quot;minecraft:pink_dye&quot;} tensura:pierrot_mask_schematic">
<h3>Wonder Pierrot Mask <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>3×</strong> Clay Ball</li>
<li><strong>1×</strong> Purple Dye</li>
<li><strong>1×</strong> Red Dye</li>
<li><strong>1×</strong> Pink Dye</li>
</ul>
<p><strong>Learn all:</strong> Pierrot Mask Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wonder_pierrot_mask</code></p><p>Resource: <code>data/tensura/recipe/smithing/wonder_pierrot_mask.json</code></p><p>Required IDs: tensura:pierrot_mask_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Pure Magisteel Gear Schematic <span>22 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="character reset scroll tensura:character_reset_scroll pure magisteel gear schematic pure magisteel ingot magic stone monster leather (a) paper {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} {&quot;item&quot;: &quot;minecraft:paper&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Character Reset Scroll <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> Monster Leather (A)</li>
<li><strong>3×</strong> Paper</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:character_reset_scroll</code></p><p>Resource: <code>data/tensura/recipe/smithing/character_reset_scroll.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="dragon knuckle tensura:dragon_knuckle pure magisteel gear schematic pure magisteel ingot pink dye {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:pink_dye&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Dragon Knuckle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Pure Magisteel Ingot</li>
<li><strong>3×</strong> Pink Dye</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:dragon_knuckle</code></p><p>Resource: <code>data/tensura/recipe/smithing/dragon_knuckle.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="high magic staff tensura:high_magic_staff pure magisteel gear schematic + magic staff schematic magic stone pure magisteel ingot stick {&quot;item&quot;: &quot;tensura:magic_stone&quot;} {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:magic_staff_schematic">
<h3>High Magic Staff <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Magic Stone</li>
<li><strong>2×</strong> Pure Magisteel Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Magic Staff Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:high_magic_staff</code></p><p>Resource: <code>data/tensura/recipe/smithing/high_magic_staff.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:magic_staff_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel axe tensura:pure_magisteel_axe pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_axe.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel boots tensura:pure_magisteel_boots pure magisteel gear schematic pure magisteel ingot {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Pure Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_boots.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel chestplate tensura:pure_magisteel_chestplate pure magisteel gear schematic pure magisteel ingot monster leather (a) {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Pure Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_chestplate.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel great sword tensura:pure_magisteel_great_sword pure magisteel gear schematic + great sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:great_sword_schematic">
<h3>Pure Magisteel Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_great_sword.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel helmet tensura:pure_magisteel_helmet pure magisteel gear schematic pure magisteel ingot {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Pure Magisteel Ingot</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_helmet.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel hoe tensura:pure_magisteel_hoe pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_hoe.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel katana tensura:pure_magisteel_katana pure magisteel gear schematic + japanese sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:japanese_sword_schematic">
<h3>Pure Magisteel Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_katana.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel kodachi tensura:pure_magisteel_kodachi pure magisteel gear schematic + short sword schematic + japanese sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Pure Magisteel Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_kodachi.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel leggings tensura:pure_magisteel_leggings pure magisteel gear schematic pure magisteel ingot monster leather (a) {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;tensura:monster_leather_a&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Pure Magisteel Ingot</li>
<li><strong>2×</strong> Monster Leather (A)</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_leggings.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel long sword tensura:pure_magisteel_long_sword pure magisteel gear schematic + long sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:long_sword_schematic">
<h3>Pure Magisteel Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_long_sword.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel odachi tensura:pure_magisteel_odachi pure magisteel gear schematic + great sword schematic + japanese sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Pure Magisteel Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_odachi.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel pickaxe tensura:pure_magisteel_pickaxe pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_pickaxe.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel scythe tensura:pure_magisteel_scythe pure magisteel gear schematic + great sword schematic + spear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Pure Magisteel Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_scythe.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel short sword tensura:pure_magisteel_short_sword pure magisteel gear schematic + short sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:short_sword_schematic">
<h3>Pure Magisteel Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_short_sword.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel shovel tensura:pure_magisteel_shovel pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_shovel.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel sickle tensura:pure_magisteel_sickle pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_sickle.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel spear tensura:pure_magisteel_spear pure magisteel gear schematic + spear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:spear_schematic">
<h3>Pure Magisteel Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>4×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_spear.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel sword tensura:pure_magisteel_sword pure magisteel gear schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic">
<h3>Pure Magisteel Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_sword.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="pure magisteel tachi tensura:pure_magisteel_tachi pure magisteel gear schematic + long sword schematic + japanese sword schematic pure magisteel ingot gold ingot stick {&quot;item&quot;: &quot;tensura:pure_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:gold_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:pure_magisteel_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Pure Magisteel Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Pure Magisteel Ingot</li>
<li><strong>1×</strong> Gold Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Pure Magisteel Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:pure_magisteel_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/pure_magisteel_tachi.json</code></p><p>Required IDs: tensura:pure_magisteel_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Serpent Scalemail Gear Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="serpent scalemail boots tensura:serpent_scalemail_boots serpent scalemail gear schematic serpent scale silver ingot {&quot;item&quot;: &quot;tensura:serpent_scale&quot;} {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:serpent_scalemail_gear_schematic">
<h3>Serpent Scalemail Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Serpent Scale</li>
<li><strong>1×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Serpent Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:serpent_scalemail_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/serpent_scalemail_boots.json</code></p><p>Required IDs: tensura:serpent_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="serpent scalemail chestplate tensura:serpent_scalemail_chestplate serpent scalemail gear schematic serpent scale silver ingot {&quot;item&quot;: &quot;tensura:serpent_scale&quot;} {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:serpent_scalemail_gear_schematic">
<h3>Serpent Scalemail Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Serpent Scale</li>
<li><strong>3×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Serpent Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:serpent_scalemail_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/serpent_scalemail_chestplate.json</code></p><p>Required IDs: tensura:serpent_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="serpent scalemail helmet tensura:serpent_scalemail_helmet serpent scalemail gear schematic serpent scale silver ingot {&quot;item&quot;: &quot;tensura:serpent_scale&quot;} {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:serpent_scalemail_gear_schematic">
<h3>Serpent Scalemail Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Serpent Scale</li>
<li><strong>3×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Serpent Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:serpent_scalemail_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/serpent_scalemail_helmet.json</code></p><p>Required IDs: tensura:serpent_scalemail_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="serpent scalemail leggings tensura:serpent_scalemail_leggings serpent scalemail gear schematic serpent scale silver ingot {&quot;item&quot;: &quot;tensura:serpent_scale&quot;} {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:serpent_scalemail_gear_schematic">
<h3>Serpent Scalemail Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Serpent Scale</li>
<li><strong>3×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Serpent Scalemail Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:serpent_scalemail_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/serpent_scalemail_leggings.json</code></p><p>Required IDs: tensura:serpent_scalemail_gear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Short Sword Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="stone kodachi tensura:stone_kodachi short sword schematic + japanese sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Stone Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_kodachi.json</code></p><p>Required IDs: tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="stone short sword tensura:stone_short_sword short sword schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:short_sword_schematic">
<h3>Stone Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:stone_tool_materials</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_short_sword.json</code></p><p>Required IDs: tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden kodachi tensura:wooden_kodachi short sword schematic + japanese sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Wooden Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_kodachi.json</code></p><p>Required IDs: tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden short sword tensura:wooden_short_sword short sword schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:short_sword_schematic">
<h3>Wooden Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:planks</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_short_sword.json</code></p><p>Required IDs: tensura:short_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Silver Gear Schematic <span>20 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="silver apple tensura:silver_apple silver gear schematic apple silver ingot {&quot;item&quot;: &quot;minecraft:apple&quot;} {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:silver_gear_schematic">
<h3>Silver Apple <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Apple</li>
<li><strong>8×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_apple</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_apple.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver axe tensura:silver_axe silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Axe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Silver Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_axe</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_axe.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver boots tensura:silver_boots silver gear schematic silver ingot {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:silver_gear_schematic">
<h3>Silver Boots <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_boots</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_boots.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver chestplate tensura:silver_chestplate silver gear schematic silver ingot {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:silver_gear_schematic">
<h3>Silver Chestplate <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>8×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_chestplate</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_chestplate.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver great sword tensura:silver_great_sword silver gear schematic + great sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:great_sword_schematic">
<h3>Silver Great Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Great Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_great_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_great_sword.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:great_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver helmet tensura:silver_helmet silver gear schematic silver ingot {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:silver_gear_schematic">
<h3>Silver Helmet <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_helmet</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_helmet.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver hoe tensura:silver_hoe silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Hoe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Silver Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_hoe</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_hoe.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver katana tensura:silver_katana silver gear schematic + japanese sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:japanese_sword_schematic">
<h3>Silver Katana <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_katana</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_katana.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver kodachi tensura:silver_kodachi silver gear schematic + short sword schematic + japanese sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:short_sword_schematic tensura:japanese_sword_schematic">
<h3>Silver Kodachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Short Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_kodachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_kodachi.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:short_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver leggings tensura:silver_leggings silver gear schematic silver ingot {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} tensura:silver_gear_schematic">
<h3>Silver Leggings <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>7×</strong> Silver Ingot</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_leggings</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_leggings.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver long sword tensura:silver_long_sword silver gear schematic + long sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:long_sword_schematic">
<h3>Silver Long Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Long Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_long_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_long_sword.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:long_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver odachi tensura:silver_odachi silver gear schematic + great sword schematic + japanese sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:great_sword_schematic tensura:japanese_sword_schematic">
<h3>Silver Odachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Great Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_odachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_odachi.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:great_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver pickaxe tensura:silver_pickaxe silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Pickaxe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Silver Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_pickaxe</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_pickaxe.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver scythe tensura:silver_scythe silver gear schematic + great sword schematic + spear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:great_sword_schematic tensura:spear_schematic">
<h3>Silver Scythe <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Silver Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Great Sword Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_scythe</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_scythe.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:great_sword_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver short sword tensura:silver_short_sword silver gear schematic + short sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:short_sword_schematic">
<h3>Silver Short Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Short Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_short_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_short_sword.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:short_sword_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver shovel tensura:silver_shovel silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Shovel <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Silver Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_shovel</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_shovel.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver sickle tensura:silver_sickle silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Sickle <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Silver Ingot</li>
<li><strong>2×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_sickle</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_sickle.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver spear tensura:silver_spear silver gear schematic + spear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:spear_schematic">
<h3>Silver Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Silver Ingot</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_spear.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver sword tensura:silver_sword silver gear schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic">
<h3>Silver Sword <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_sword</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_sword.json</code></p><p>Required IDs: tensura:silver_gear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="silver tachi tensura:silver_tachi silver gear schematic + long sword schematic + japanese sword schematic silver ingot stick {&quot;item&quot;: &quot;tensura:silver_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:silver_gear_schematic tensura:long_sword_schematic tensura:japanese_sword_schematic">
<h3>Silver Tachi <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Silver Ingot</li>
<li><strong>1×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Silver Gear Schematic + Long Sword Schematic + Japanese Sword Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:silver_tachi</code></p><p>Resource: <code>data/tensura/recipe/smithing/silver_tachi.json</code></p><p>Required IDs: tensura:silver_gear_schematic, tensura:long_sword_schematic, tensura:japanese_sword_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Spatial Blade Schematic <span>2 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="severer blade tensura:severer_blade spatial blade schematic iron ingot ender pearl {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:ender_pearl&quot;} tensura:spatial_blade_schematic">
<h3>Severer Blade <span>×3</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Iron Ingot</li>
<li><strong>1×</strong> Ender Pearl</li>
</ul>
<p><strong>Learn all:</strong> Spatial Blade Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:severer_blade</code></p><p>Resource: <code>data/tensura/recipe/smithing/severer_blade.json</code></p><p>Required IDs: tensura:spatial_blade_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="spatial blade tensura:spatial_blade spatial blade schematic high magisteel ingot stick severer blade {&quot;item&quot;: &quot;tensura:high_magisteel_ingot&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} {&quot;item&quot;: &quot;tensura:severer_blade&quot;} tensura:spatial_blade_schematic">
<h3>Spatial Blade <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> High Magisteel Ingot</li>
<li><strong>1×</strong> Stick</li>
<li><strong>1×</strong> Severer Blade</li>
</ul>
<p><strong>Learn all:</strong> Spatial Blade Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:spatial_blade</code></p><p>Resource: <code>data/tensura/recipe/smithing/spatial_blade.json</code></p><p>Required IDs: tensura:spatial_blade_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Spear Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="beast horn spear tensura:beast_horn_spear spear schematic beast horn stick {&quot;item&quot;: &quot;tensura:beast_horn&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:spear_schematic">
<h3>Beast Horn Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Beast Horn</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:beast_horn_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/beast_horn_spear.json</code></p><p>Required IDs: tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="stone spear tensura:stone_spear spear schematic #minecraft:stone_tool_materials stick {&quot;tag&quot;: &quot;minecraft:stone_tool_materials&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:spear_schematic">
<h3>Stone Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:stone_tool_materials</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:stone_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/stone_spear.json</code></p><p>Required IDs: tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="unicorn horn spear tensura:unicorn_horn_spear spear schematic unicorn horn stick {&quot;item&quot;: &quot;tensura:unicorn_horn&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:spear_schematic">
<h3>Unicorn Horn Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Unicorn Horn</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:unicorn_horn_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/unicorn_horn_spear.json</code></p><p>Required IDs: tensura:spear_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="wooden spear tensura:wooden_spear spear schematic #minecraft:planks stick {&quot;tag&quot;: &quot;minecraft:planks&quot;} {&quot;item&quot;: &quot;minecraft:stick&quot;} tensura:spear_schematic">
<h3>Wooden Spear <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> #minecraft:planks</li>
<li><strong>3×</strong> Stick</li>
</ul>
<p><strong>Learn all:</strong> Spear Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:wooden_spear</code></p><p>Resource: <code>data/tensura/recipe/smithing/wooden_spear.json</code></p><p>Required IDs: tensura:spear_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Spider Bows Schematic <span>4 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="long spider bow tensura:long_spider_bow spider bows schematic knight spider leg #tensura:strong_thread {&quot;item&quot;: &quot;tensura:knight_spider_leg&quot;} {&quot;tag&quot;: &quot;tensura:strong_thread&quot;} tensura:spider_bows_schematic">
<h3>Long Spider Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>4×</strong> Knight Spider Leg</li>
<li><strong>4×</strong> #tensura:strong_thread</li>
</ul>
<p><strong>Learn all:</strong> Spider Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:long_spider_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/long_spider_bow.json</code></p><p>Required IDs: tensura:spider_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="short spider bow tensura:short_spider_bow spider bows schematic knight spider leg #tensura:strong_thread {&quot;item&quot;: &quot;tensura:knight_spider_leg&quot;} {&quot;tag&quot;: &quot;tensura:strong_thread&quot;} tensura:spider_bows_schematic">
<h3>Short Spider Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Knight Spider Leg</li>
<li><strong>2×</strong> #tensura:strong_thread</li>
</ul>
<p><strong>Learn all:</strong> Spider Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:short_spider_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/short_spider_bow.json</code></p><p>Required IDs: tensura:spider_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="spider bow tensura:spider_bow spider bows schematic knight spider leg #tensura:strong_thread {&quot;item&quot;: &quot;tensura:knight_spider_leg&quot;} {&quot;tag&quot;: &quot;tensura:strong_thread&quot;} tensura:spider_bows_schematic">
<h3>Spider Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>3×</strong> Knight Spider Leg</li>
<li><strong>3×</strong> #tensura:strong_thread</li>
</ul>
<p><strong>Learn all:</strong> Spider Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:spider_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/spider_bow.json</code></p><p>Required IDs: tensura:spider_bows_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="war spider bow tensura:war_spider_bow spider bows schematic knight spider leg #tensura:strong_thread {&quot;item&quot;: &quot;tensura:knight_spider_leg&quot;} {&quot;tag&quot;: &quot;tensura:strong_thread&quot;} tensura:spider_bows_schematic">
<h3>War Spider Bow <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>5×</strong> Knight Spider Leg</li>
<li><strong>5×</strong> #tensura:strong_thread</li>
</ul>
<p><strong>Learn all:</strong> Spider Bows Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:war_spider_bow</code></p><p>Resource: <code>data/tensura/recipe/smithing/war_spider_bow.json</code></p><p>Required IDs: tensura:spider_bows_schematic</p></details>
</article>
</div></details>
<details class="smithing-group"><summary>Web Gun Schematic <span>5 recipes</span></summary><div class="smithing-recipe-grid">
<article class="smithing-recipe" data-smithing-recipe data-search="copper shell tensura:copper_shell web gun schematic copper ingot {&quot;item&quot;: &quot;minecraft:copper_ingot&quot;} tensura:web_gun_schematic">
<h3>Copper Shell <span>×4</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Copper Ingot</li>
</ul>
<p><strong>Learn all:</strong> Web Gun Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:copper_shell</code></p><p>Resource: <code>data/tensura/recipe/smithing/copper_shell.json</code></p><p>Required IDs: tensura:web_gun_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="sticky steel web cartridge tensura:sticky_steel_web_cartridge web gun schematic copper shell sticky thread steel thread gunpowder {&quot;item&quot;: &quot;tensura:copper_shell&quot;} {&quot;item&quot;: &quot;tensura:sticky_thread&quot;} {&quot;item&quot;: &quot;tensura:steel_thread&quot;} {&quot;item&quot;: &quot;minecraft:gunpowder&quot;} tensura:web_gun_schematic">
<h3>Sticky Steel Web Cartridge <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Copper Shell</li>
<li><strong>4×</strong> Sticky Thread</li>
<li><strong>4×</strong> Steel Thread</li>
<li><strong>1×</strong> Gunpowder</li>
</ul>
<p><strong>Learn all:</strong> Web Gun Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:sticky_steel_web_cartridge</code></p><p>Resource: <code>data/tensura/recipe/smithing/sticky_steel_web_cartridge.json</code></p><p>Required IDs: tensura:web_gun_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="sticky web cartridge tensura:sticky_web_cartridge web gun schematic copper shell sticky thread gunpowder {&quot;item&quot;: &quot;tensura:copper_shell&quot;} {&quot;item&quot;: &quot;tensura:sticky_thread&quot;} {&quot;item&quot;: &quot;minecraft:gunpowder&quot;} tensura:web_gun_schematic">
<h3>Sticky Web Cartridge <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Copper Shell</li>
<li><strong>4×</strong> Sticky Thread</li>
<li><strong>1×</strong> Gunpowder</li>
</ul>
<p><strong>Learn all:</strong> Web Gun Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:sticky_web_cartridge</code></p><p>Resource: <code>data/tensura/recipe/smithing/sticky_web_cartridge.json</code></p><p>Required IDs: tensura:web_gun_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="web cartridge tensura:web_cartridge web gun schematic copper shell string gunpowder {&quot;item&quot;: &quot;tensura:copper_shell&quot;} {&quot;item&quot;: &quot;minecraft:string&quot;} {&quot;item&quot;: &quot;minecraft:gunpowder&quot;} tensura:web_gun_schematic">
<h3>Web Cartridge <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>1×</strong> Copper Shell</li>
<li><strong>8×</strong> String</li>
<li><strong>1×</strong> Gunpowder</li>
</ul>
<p><strong>Learn all:</strong> Web Gun Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:web_cartridge</code></p><p>Resource: <code>data/tensura/recipe/smithing/web_cartridge.json</code></p><p>Required IDs: tensura:web_gun_schematic</p></details>
</article>
<article class="smithing-recipe" data-smithing-recipe data-search="web gun tensura:web_gun web gun schematic iron ingot redstone {&quot;item&quot;: &quot;minecraft:iron_ingot&quot;} {&quot;item&quot;: &quot;minecraft:redstone&quot;} tensura:web_gun_schematic">
<h3>Web Gun <span>×1</span></h3>
<ul class="smithing-ingredients">
<li><strong>2×</strong> Iron Ingot</li>
<li><strong>1×</strong> Redstone</li>
</ul>
<p><strong>Learn all:</strong> Web Gun Schematic</p>
<details class="smithing-evidence"><summary>Recipe identifiers</summary><p>Output: <code>tensura:web_gun</code></p><p>Resource: <code>data/tensura/recipe/smithing/web_gun.json</code></p><p>Required IDs: tensura:web_gun_schematic</p></details>
</article>
</div></details>
<p data-smithing-empty hidden>No matching recipe. Try a shorter material or schematic name.</p></section>

## Recipe coverage

The upstream catalogue’s **Dark Set**, **Silver Set**, **Ant Set**, and **Clown Masks** names remain useful starting points. This base recipe register contains Dark equipment, Silver equipment, Ant Carapace equipment, and Pierrot masks with ingredient and schematic definitions. A set label is not a promise that every expected piece exists, and a packaged recipe is not proof of live-server availability.

## Source and licensing

[Smithing Bench source article, recorded revision 13111](https://tensura.wiki.gg/wiki/Blocks/Smithing_Bench?oldid=13111). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Implementation: [Tensura 2.0.1.2](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml) · [recipe evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/smithing_reference.json). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

The original workstation illustration is conceptual artwork, not a game texture. The source File page did not establish reusable image permission; the [media ledger](../../project/sources-and-attribution.md) records the review.

??? info "Implementation evidence"

    - `data/tensura/recipe/smithing_bench.json` and all 298 `data/tensura/recipe/smithing/*.json` resources
    - `SmithingBenchBlock`, `SmithingBenchMenu`, `SmithingBenchMenu$1`, `SmithingBenchRecipe`, and its `Serializer`
    - `data/tensura/loot_table/blocks/smithing_bench.json`
    - `data/minecraft/tags/block/mineable/axe.json` and `needs_iron_tool.json`

[Back to Blocks](index.md) · [Browse equipment materials](../items/index.md) · [Learn about Spellbinding Table](../resistances/spellbinding-table.md)
