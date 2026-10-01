---
title: "Unbound Tome"
description: "Copy an eligible mastered spell into a Magic Tome at the Spellbinding Table. The blank item does not learn or randomly roll a spell when held."
---

# Unbound Tome

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-tome.webp" alt="Unbound Tome illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Copy an eligible mastered spell into a Magic Tome at the Spellbinding Table. The blank item does not learn or randomly roll a spell when held.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Chest loot and copying checks verified"
    The blank tome is Rare and stacks to 16 in the selected artifact, despite the unfinished upstream infobox. Full mastery does not bypass the copying exclusions.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Unbound Tome</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:unbound_tome</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Chest loot and copying checks verified</div></div>
</aside></div></div>

<span id="Obtainment"></span>

## Availability

Unbound Tome entries appear in the selected artifact's Buried, Burnt, Frozen, Rotted, and Ruined Wizard Tower chest loot tables. Their presence verifies a randomized loot definition, not a guaranteed tome in every chest. A complete supply route, world-generation behavior, and live-server overrides are not verified here.

<span id="Usage"></span>

## How to use

Place one blank tome in the [Spellbinding Table](../resistances/spellbinding-table.md). Its container limit is one item. Choose an eligible magic you have mastered. The server checks the magic tag, nonnegative mastery, unbindable exclusion, isMastered, and TOME_COPY_EXCLUDED before replacing the blank with a Magic Tome containing the selected spell ID. Copying does not automatically teach the recipient; they must use the resulting tome through the normal learning system.

## Behavior and limits

TensuraMaterialItems registers this item as Rare with a stack limit of 16. The selected copying tag excludes all Spiritual magic, Summon Medium Elemental, and Summon Greater Elemental. This copying list is different from the seven [unlearned casting exclusions](../tools/caster-tools-tutorial.md#learning-required). Other spell and add-on checks can still reject copying. Availability after resets or prestige and every spell-specific eligibility route remain untested.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Unbound tome](https://tensura.wiki.gg/wiki/Unbound_tome) on the Tensura: Reincarnated Wiki, recorded revision `13340`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraMaterialItems.class`
    - `io/github/manasmods/tensura/menu/SpellbindingMenu.class`
    - `io/github/manasmods/tensura/block/entity/SpellbindingBlockEntity.class`
    - `io/github/manasmods/tensura/network/c2s/RequestSpellbindingPacket.class`
    - `io/github/manasmods/tensura/item/misc/MagicTomeItem.class`
    - `data/tensura/tags/manascore_skill/skills/tome_copy_excluded.json`
    - `data/tensura/loot_table/chests/buried_wizard_tower.json`
    - `data/tensura/loot_table/chests/burnt_wizard_tower.json`
    - `data/tensura/loot_table/chests/frozen_wizard_tower.json`
    - `data/tensura/loot_table/chests/rotted_wizard_tower.json`
    - `data/tensura/loot_table/chests/ruined_wizard_tower.json`
