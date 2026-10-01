---
title: "Spellbinding Table"
description: "Craft a workstation for binding learned magic to caster tools and copying eligible mastered spells into tomes."
---

# Spellbinding Table

<span class="reference-badge">Tensura: Reincarnated reference</span> <span class="reference-category">Blocks</span>

<section data-reference-section="blocks" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/blocks/spellbinding-table.webp" alt="Spellbinding Table illustration" loading="eager" decoding="async">
<figcaption>TSR block illustration</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Craft a workstation for binding learned magic to caster tools and copying eligible mastered spells into tomes.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#what-it-does">What it does</a><a href="#player-access">Player access</a></nav>
</div>
</section>

!!! info "Pinned Minecraft 1.21.1 build"

    Verified against **Tensura: Reincarnated 2.0.1.2** selected by the TSR pack manifest.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Spellbinding Table</div>
<div class="druid-row"><div class="druid-label">Source</div><div class="druid-data">Tensura: Reincarnated 2.0.1.2</div></div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:spellbinding_table</div></div>
<div class="druid-row"><div class="druid-label">Role</div><div class="druid-data">Spell-binding workstation</div></div>
<div class="druid-row"><div class="druid-label">Visual</div><div class="druid-data">Original illustration; not the in-game texture</div></div>
<div class="druid-row"><div class="druid-label">Player access</div><div class="druid-data">Crafting table; diamond-tier pickaxe for recovery</div></div>
<div class="druid-row"><div class="druid-label">Hardness</div><div class="druid-data">5</div></div>
<div class="druid-row"><div class="druid-label">Blast resistance</div><div class="druid-data">1,200</div></div>
<div class="druid-row"><div class="druid-label">Light level</div><div class="druid-data">7</div></div>
<div class="druid-row"><div class="druid-label">Menu capacity</div><div class="druid-data">One item</div></div>
</aside></div></div>

<span id="Description"></span>

## What it does

Place the table and use it with an empty hand to open its menu. The table's slot accepts **one item** from the `tensura:spell_bindable` tag: caster weapons and Unbound Tomes in the pinned build. Choose an eligible learned spell to bind to a staff or grimoire; ordinary binding requires nonnegative mastery, available capacity, and the spell's equip checks, not full mastery. Binding does not teach a new ability.

For an [Unbound Tome](../items/unbound-tome.md), copying requires a **mastered** spell outside `TOME_COPY_EXCLUDED`. The result is a [Magic Tome](../magic/magic-tome.md) containing that spell. Copy exclusions differ from the restrictions on casting spells you have not learned. Follow the [casting walkthrough](../tools/caster-tools-tutorial.md) for selection controls, mode changes, costs, and the seven unlearned-casting exclusions.

<span id="Usage"></span>

## Player access

### Craft one table

Use a normal crafting table with **1 Magic Stone**, **2 Silver Ingots**, and **4 Crying Obsidian**. No smithing schematic gate appears in this recipe.

| Left | Center | Right |
|---|---|---|
| — | Magic Stone | — |
| Silver Ingot | Crying Obsidian | Silver Ingot |
| Crying Obsidian | Crying Obsidian | Crying Obsidian |

The output is **1 Spellbinding Table**. See [Magic Stone](../magic/magic-stone.md) for its separate schematic-gated material recipe.

### Recover and place

Mine with a **diamond-tier pickaxe or better**. The block requires a correct tool for drops; its block loot entry returns the table subject to the explosion-survival condition. The pinned block has hardness **5**, blast resistance **1,200**, and emits light level **7**. Its shape is three-quarters of a block high, and it supports waterlogging. These are recipe, class, and tag checks—not live-server placement, mining, or casting tests.

[Compare staff tiers](../items/magic-staves.md) before collecting materials for a caster tool. The server's recipe browser remains the final check for recipe overrides.

## Source and licensing

??? info "Sources and verification"

    [Tensura: Reincarnated 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml)

    Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`.

    Upstream article: [Tensura: Reincarnated Wiki revision 12066](https://tensura.wiki.gg/wiki/Spellbinding_Table?oldid=12066). Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

    Packaged implementation evidence:

    - `data/tensura/recipe/spellbinding_table.json`
    - `data/tensura/loot_table/blocks/spellbinding_table.json`
    - `data/minecraft/tags/block/mineable/pickaxe.json`
    - `data/minecraft/tags/block/needs_diamond_tool.json`
    - `data/tensura/tags/item/spell_bindable.json`
    - `data/tensura/tags/manascore_skill/skills/tome_copy_excluded.json`
    - `io/github/manasmods/tensura/block/SpellbindingBlock.class`
    - `io/github/manasmods/tensura/block/entity/SpellbindingBlockEntity.class`
    - `io/github/manasmods/tensura/menu/SpellbindingMenu.class`
    - `io/github/manasmods/tensura/network/c2s/RequestSpellbindingPacket.class`
    - `assets/tensura/models/block/spellbinding_table.json`

    The illustration on this page is original TSR artwork; it is not the in-game texture.

[Back to Blocks](../blocks/index.md)
