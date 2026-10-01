---
title: "Magic Tome"
description: "Read a tome to attempt learning its stored spell. Chest loot can assign a spell before use; a tome with no stored spell instead draws from the aspectual-magic tag."
---

# Magic Tome

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/magic-tome.webp" alt="Magic Tome illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>Read a tome to attempt learning its stored spell. Chest loot can assign a spell before use; a tome with no stored spell instead draws from the aspectual-magic tag.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! warning "Chest loot and learning behavior verified"
    A resolved learning attempt can consume the tome even if learning fails or the spell is already known. It is not a guaranteed new spell or a random result from every magic school.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Magic Tome</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:magic_tome</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Chest loot and learning behavior verified</div></div>
</aside></div></div>

<span id="Obtainment"></span>

## Availability

The selected artifact's Buried, Burnt, Frozen, Rotted, and Ruined Wizard Tower chest loot tables contain Magic Tome entries. Their apply_skill_data functions assign a stored spell from the corresponding loot tag. These are randomized loot definitions, not guaranteed contents in each chest or proof that every spell can appear. Server generation, datapack overrides, and complete spell-specific supply routes remain untested.

## How to use

Use the tome and release after at least ten ticks. A stored SKILL ID resolves to that spell and attempts SkillHelper.learnSkill with its acquirement mastery. Without a stored spell, the method randomly selects from the ASPECTUAL_MAGIC tag. It does not use every registered magic school or the Skill Study Book pool. Read the [magic learning guide](../../magic-learning.md) before spending it.

## Behavior and limits

MagicTomeItem registers Rare rarity, stack size one, and fire resistance. After a resolved survival learning attempt, it consumes one item and adds a 200-tick cooldown even if learning fails. Infinite-material players are exempt from consumption and cooldown. Ten ticks and 200 ticks are nominal tick counts, not guaranteed wall-clock durations. A copied tome can also be created from an eligible mastered spell using an [Unbound Tome](../items/unbound-tome.md).

[Return to Items](../items/index.md)

## Source and licensing

Upstream reference: [Magic Tome](https://tensura.wiki.gg/wiki/Magic_Tome) on the Tensura: Reincarnated Wiki, recorded revision `13289`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/item/misc/MagicTomeItem.class`
    - `io/github/manasmods/tensura/data/template/function/ApplySkillDataFunction.class`
    - `data/tensura/loot_table/chests/buried_wizard_tower.json`
    - `data/tensura/loot_table/chests/burnt_wizard_tower.json`
    - `data/tensura/loot_table/chests/frozen_wizard_tower.json`
    - `data/tensura/loot_table/chests/rotted_wizard_tower.json`
    - `data/tensura/loot_table/chests/ruined_wizard_tower.json`
