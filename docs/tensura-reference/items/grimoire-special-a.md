---
title: "Grimoire Special A"
description: "A 7-slot caster book with a 10-tick base item cooldown. Compare its loot route, spell controls, and base gear progression."
---

# Grimoire Special A

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section data-reference-section="items" class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/grimoire.webp" alt="Grimoire Special A illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A 7-slot caster book with a 10-tick base item cooldown. Compare its loot route, spell controls, and base gear progression.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! info "Base evolution route checked"
    Item constructors, base gear data, and the stated supply route are checked against Tensura 2.0.1.2. TSR also uses Gear Evolution; its overrides, current stack components, and live casting/evolution behavior are not verified by this base-artifact check.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats reference-item-stats"><aside class="druid-infobox">
<div class="druid-title">Grimoire Special A</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:grimoire_special_a</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Base evolution route checked</div></div>
<div class="druid-row"><div class="druid-label">Rarity</div><div class="druid-data">Rare</div></div>
<div class="druid-row"><div class="druid-label">Stack limit</div><div class="druid-data">1</div></div>
<div class="druid-row"><div class="druid-label">Base spell slots</div><div class="druid-data">7</div></div>
<div class="druid-row"><div class="druid-label">Base item cooldown</div><div class="druid-data">10 ticks</div></div>
<div class="druid-row"><div class="druid-label">Base durability</div><div class="druid-data">500</div></div>
<div class="druid-row"><div class="druid-label">Chant Speed attribute</div><div class="druid-data">+0.20</div></div>
</aside></div></div>

<span id="Obtainment"></span>

## Availability

The pinned base gear data maps [Grimoire A](grimoire-a.md) to this item at **80,000 gear EP**, not the 100,000 stated in the older upstream article. No direct Special A entry was found in the five reviewed Wizard Tower chest definitions. No ordinary packaged crafting recipe mentioning these grimoire IDs was found. Server datapacks, trades, and add-on overrides remain separate checks.

<span id="Usage"></span>

## How to use

Put the book in the [Spellbinding Table](../resistances/spellbinding-table.md) and bind eligible learned magic. Ordinary binding needs nonnegative mastery, capacity, and equip checks—not full mastery. Hold the book and use it to cast the selected stored spell; an empty spell list cannot cast. Use your assigned **Next Ability Mode** modifier plus scroll to select a spell, or modifier plus item use to change its mode. See the [casting walkthrough](../tools/caster-tools-tutorial.md) for exclusions and resource checks. Binding and casting do not automatically teach the stored spell.

<span id="Description"></span>

## Behavior and limits

The fresh item constructor has **7 base spell slots**, **10 ticks** of item cooldown, **500 durability**, and **Rare** rarity. Magic Capacity adds its enchantment level to the slot calculation. The held Chant Speed attribute adds **+0.20**; this is not a percentage reduction or a promised final casting time.

The Special A gear JSON contains no successor or explicit maximum EP. The checked GearExistenceData codec supplies a **2,000,000 maximum EP** default. Its minimum is **80,000 EP** when the base initializer applies; it is not an unlimited EP item or a further evolution route.

Progression EP and `EP_DURABILITY` are distinct from ordinary item durability. The checked Magic resource method can draw MP contribution from stored gear EP when its conditions are met; it does not bypass Aura costs or make casting free. [Compare all five tiers](grimoires.md) for base thresholds and the server-override limits. The shared illustration represents grimoire equipment, not the exact appearance of this tier.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Grimoire(Special A)](https://tensura.wiki.gg/wiki/Grimoire(Special_A)) on the Tensura: Reincarnated Wiki, recorded revision `12846`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraToolItems.class`
    - `io/github/manasmods/tensura/item/weapon/spell/SimpleSpellCastItem.class`
    - `io/github/manasmods/tensura/handler/GearHandler.class`
    - `io/github/manasmods/tensura/handler/DeathHandler.class`
    - `io/github/manasmods/tensura/data/existence/gear/GearExistenceData.class`
    - `io/github/manasmods/tensura/ability/Magic.class`
    - `data/tensura/gear_existence/grimoire_special_a.json`
    - `data/tensura/tags/item/magic_grimoires.json`
    - `data/tensura/loot_table/chests/buried_wizard_tower.json`
    - `data/tensura/loot_table/chests/burnt_wizard_tower.json`
    - `data/tensura/loot_table/chests/frozen_wizard_tower.json`
    - `data/tensura/loot_table/chests/rotted_wizard_tower.json`
    - `data/tensura/loot_table/chests/ruined_wizard_tower.json`
