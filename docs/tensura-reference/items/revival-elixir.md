---
title: "Revival Elixir"
description: "A high-tier healing drink for living targets: restores up to a full health bar and 20,000 MP, subject to maximum MP."
---

# Revival Elixir

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/revival-elixir.webp" alt="Revival Elixir illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A high-tier healing drink for living targets: restores up to a full health bar and 20,000 MP, subject to maximum MP.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! warning "Registered item · acquisition unverified"
    Despite its name, this item does not resurrect a dead player. HealingPotionItem returns without applying its effect when the target is not alive.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Revival Elixir</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:revival_elixir</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Survival route not verified</div></div>
</aside></div></div>

## Availability

The item is registered in the pinned build, but no survival acquisition route was verified. The reviewed brewing registrations produce Low, High, and Full Potions, not Revival Elixir. Its presence in the creative inventory and dissolving data does not establish a craft, trade, or loot route. Check the server's recipe browser before planning around it.

## How to use

Use normally to drink; the inherited drink duration is 16 ticks (0.8 seconds at 20 TPS). Sneak-use throws a healing-potion projectile. Direct interaction with a living entity applies the effect to that target. Drinking consumes the elixir and returns a Magic Bottle in survival.

## Behavior and limits

At full effect strength, healing equals 100% of the target's maximum health. Magicule restoration adds a fixed 20,000 MP and is capped at the target's maximum MP; it is not 100% MP restoration and does not increase maximum MP. Thrown applications can use a reduced strength multiplier.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Revival Elixir](https://tensura.wiki.gg/wiki/Revival_Elixir) on the Tensura: Reincarnated Wiki, recorded revision `10584`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Source artwork without a verified reusable image license is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/item/consumable/HealingPotionItem.class`
    - `io/github/manasmods/tensura/item/consumable/ManaPotionItem.class`
    - `io/github/manasmods/tensura/entity/projectile/ThrownHealingPotion.class`
    - `io/github/manasmods/tensura/recipe/SpecialRecipeRegister.class`
    - `data/tensura/item_dissolving/revival_elixir.json`
