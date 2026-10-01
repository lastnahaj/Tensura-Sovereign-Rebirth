---
title: Magic Crystals
description: Compare crystal loot rules, absorption, bottle yields, storage, and schematic-gated downgrades for Minecraft 1.21.1.
---

<section class="potion-guide">
<header class="potion-guide-heading">
<p class="reference-eyebrow">Materials field guide · Minecraft 1.21.1</p>
<h1>Choose how to use your crystals</h1>
<p>Keep crystals for crafting, turn them into brewing containers, or recover MP with Absorb &amp; Dissolve. These values are checked against Tensura 2.0.1.2 and TSR’s checked-in configuration.</p>
</header>
<div class="potion-guide-grid">
<article class="potion-guide-card">
<a href="../../magic/low-quality-magic-crystal/" aria-label="Read Low Quality Magic Crystal"><img src="../../../assets/images/items/low-quality-magic-crystal.webp" alt="Low Quality Magic Crystal illustration" loading="lazy" decoding="async"><h2>Low Quality</h2></a>
<dl><div><dt>Absorption</dt><dd>1,000 <small>base MP per crystal</small></dd></div><div><dt>Bottle recipe</dt><dd>3 <small>bottles per crystal + 3 Glass</small></dd></div></dl>
<p>Low fallback · usually 1–2,999 adjusted EP</p>
</article>
<article class="potion-guide-card">
<a href="../../magic/medium-quality-magic-crystal/" aria-label="Read Medium Quality Magic Crystal"><img src="../../../assets/images/items/medium-quality-magic-crystal.webp" alt="Medium Quality Magic Crystal illustration" loading="lazy" decoding="async"><h2>Medium Quality</h2></a>
<dl><div><dt>Absorption</dt><dd>2,500 <small>base MP per crystal</small></dd></div><div><dt>Bottle recipe</dt><dd>6 <small>bottles per crystal + 3 Glass</small></dd></div></dl>
<p>3,000–8,999 adjusted EP · inclusive</p>
</article>
<article class="potion-guide-card">
<a href="../../magic/high-quality-magic-crystal/" aria-label="Read High Quality Magic Crystal"><img src="../../../assets/images/items/high-quality-magic-crystal.webp" alt="High Quality Magic Crystal illustration" loading="lazy" decoding="async"><h2>High Quality</h2></a>
<dl><div><dt>Absorption</dt><dd>5,000 <small>base MP per crystal</small></dd></div><div><dt>Bottle recipe</dt><dd>9 <small>bottles per crystal + 3 Glass</small></dd></div></dl>
<p>9,000+ adjusted EP · inclusive</p>
</article>
</div>
</section>

## Find eligible drops

The shared loot rule requires membership in the `tensura:drop_crystal` entity tag. It tests maximum EP after the namespace multiplier, excludes `MOB_SUMMONED` and `TRIGGERED` spawn types, and requires named-evolution entities to permit crystal drops. A species name or boss label alone is not enough.

The rule checks Medium at **3,000–8,999 inclusive**, then High at **9,000 or more**, then Low as a fallback at **1 or more**. The usual whole-number Low range is 1–2,999. Fractional values between 8,999 and 9,000 fall through to Low; zero EP does not pass the shared rule. Other entity-specific or add-on loot is outside this check.

## Recover MP, not maximum MP

Hold one crystal in your main hand and activate [Absorb & Dissolve](../skills/intrinsic/absorb-dissolve.md). The implementation consumes one item. Base recovery is 1,000 / 2,500 / 5,000 MP for Low / Medium / High, multiplied by the skill’s `magiculeMultiplier`. TSR’s checked-in value is **1.0**. This does not grant permanent maximum MP.

## Store or downgrade

Fill a 3×3 crafting grid with nine same-quality crystals to craft their storage block. Unpacking that block gives nine crystals of the same quality.

At a **Smithing Bench**, with the [Low Magisteel Gear Schematic](items-schematics-low-magisteel-gear-schematic.md):

- One High crystal becomes **two Medium** crystals.
- One Medium crystal becomes **two Low** crystals.

These checked recipes run downward only; they do not prove an upgrade recipe. Without the required schematic, the downgrade route is incomplete.

## Prepare your brewing kit

Combine one crystal with three Glass: Glass–Crystal–Glass across a row, then Glass beneath the crystal. Low produces **3**, Medium **6**, and High **9** [Magic Bottles](../magic/magic-bottle.md). Continue with the [healing-potion guide](healing-potions.md) for filling, cooking, and brewing.

!!! note "Verification scope"
    Registry, recipe, loot-predicate, and configuration checks are not live-server gameplay tests. Server overrides and unreviewed trading routes are not guaranteed here.

[Return to Items](index.md)

## Sources and artwork

The individual [Low](../magic/low-quality-magic-crystal.md), [Medium](../magic/medium-quality-magic-crystal.md), and [High](../magic/high-quality-magic-crystal.md) references cite upstream revisions and exact artifact evidence. Adapted text remains under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Implementation: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR item evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json). The original illustrations are not in-game texture or appearance guarantees.
