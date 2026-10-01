---
title: Grimoires
description: Compare grimoire slots, cooldowns, loot routes, and the pinned base equipment evolution chain.
---

<section data-reference-section="items" class="reference-overview reference-theme-abilities staff-guide-hero">
<figure class="reference-overview-media"><img src="../../../assets/images/items/grimoire.webp" alt="Original open grimoire illustration with a cyan spell diagram" loading="eager" decoding="async"><figcaption>TSR illustration · equipment class, not a tier texture</figcaption></figure>
<div class="reference-overview-copy"><p class="reference-eyebrow">Caster equipment · Minecraft 1.21.1</p><h1>Choose your grimoire</h1><p>Five tiers. More room for spells, shorter base item cooldowns, and a linked equipment progression. Start with a book you can obtain, then distinguish its spell loadout, gear EP, and casting fuel.</p>
<nav class="reference-quick-jumps" aria-label="Grimoire guide"><a href="#compare-the-tiers">Compare tiers</a><a href="#follow-the-base-evolution-chain">Evolution chain</a><a href="../../tools/caster-tools-tutorial/">Casting walkthrough</a></nav></div></section>

!!! note "Base artifact values, not a live-server guarantee"
    These values come from Tensura 2.0.1.2. TSR also selects Gear Evolution 1.2.5 and allows datapack chain extensions. The table is a base reference; current stack components, add-on thresholds, and live equipment retention remain unverified.

## Compare the tiers

<section class="potion-guide"><div class="potion-guide-grid">
<article class="potion-guide-card staff-tier-card">
<p class="reference-eyebrow">Common · caster book</p>
<h2><a href="../grimoire-d/">Grimoire D</a></h2>
<p class="staff-capacity"><strong>3</strong><span>base spell slots</span></p>
<dl><div><dt>Item cooldown</dt><dd>40<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+0.00<small>additive, not a percentage</small></dd></div></dl>
<details><summary>Supply &amp; progression</summary>
<p>Candidate in five Tower chest definitions. Read the <a href="../grimoire-d/#availability">item supply notes</a> before planning a trip.</p>
<p><strong>Base durability:</strong> 100; <strong>stack limit:</strong> 1.</p><p><a href="../grimoire-c/">C at 2,500 base gear EP →</a></p></details>
</article>
<article class="potion-guide-card staff-tier-card">
<p class="reference-eyebrow">Uncommon · caster book</p>
<h2><a href="../grimoire-c/">Grimoire C</a></h2>
<p class="staff-capacity"><strong>4</strong><span>base spell slots</span></p>
<dl><div><dt>Item cooldown</dt><dd>30<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+0.05<small>additive, not a percentage</small></dd></div></dl>
<details><summary>Supply &amp; progression</summary>
<p>Candidate in five Tower chest definitions. Read the <a href="../grimoire-c/#availability">item supply notes</a> before planning a trip.</p>
<p><strong>Base durability:</strong> 200; <strong>stack limit:</strong> 1.</p><p><a href="../grimoire-b/">B at 5,000 base gear EP →</a></p></details>
</article>
<article class="potion-guide-card staff-tier-card">
<p class="reference-eyebrow">Uncommon · caster book</p>
<h2><a href="../grimoire-b/">Grimoire B</a></h2>
<p class="staff-capacity"><strong>5</strong><span>base spell slots</span></p>
<dl><div><dt>Item cooldown</dt><dd>20<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+0.10<small>additive, not a percentage</small></dd></div></dl>
<details><summary>Supply &amp; progression</summary>
<p>Candidate in five Tower chest definitions. Read the <a href="../grimoire-b/#availability">item supply notes</a> before planning a trip.</p>
<p><strong>Base durability:</strong> 300; <strong>stack limit:</strong> 1.</p><p><a href="../grimoire-a/">A at 8,000 base gear EP →</a></p></details>
</article>
<article class="potion-guide-card staff-tier-card">
<p class="reference-eyebrow">Rare · caster book</p>
<h2><a href="../grimoire-a/">Grimoire A</a></h2>
<p class="staff-capacity"><strong>6</strong><span>base spell slots</span></p>
<dl><div><dt>Item cooldown</dt><dd>15<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+0.15<small>additive, not a percentage</small></dd></div></dl>
<details><summary>Supply &amp; progression</summary>
<p>Candidate in five Tower chest definitions. Read the <a href="../grimoire-a/#availability">item supply notes</a> before planning a trip.</p>
<p><strong>Base durability:</strong> 400; <strong>stack limit:</strong> 1.</p><p><a href="../grimoire-special-a/">Special A at 80,000 base gear EP →</a></p></details>
</article>
<article class="potion-guide-card staff-tier-card">
<p class="reference-eyebrow">Rare · caster book</p>
<h2><a href="../grimoire-special-a/">Grimoire Special A</a></h2>
<p class="staff-capacity"><strong>7</strong><span>base spell slots</span></p>
<dl><div><dt>Item cooldown</dt><dd>10<small>ticks · not chant time</small></dd></div><div><dt>Chant attribute</dt><dd>+0.20<small>additive, not a percentage</small></dd></div></dl>
<details><summary>Supply &amp; progression</summary>
<p>A-tier evolution; no direct Tower drop verified. Read the <a href="../grimoire-special-a/#availability">item supply notes</a> before planning a trip.</p>
<p><strong>Base durability:</strong> 500; <strong>stack limit:</strong> 1.</p><p>No successor in the base definition</p></details>
</article>
</div></section>

## Follow the base evolution chain

These are **equipment EP** thresholds, not player EP requirements or a count of spell casts. The pinned finite-tier definitions and checked evolution method give:

| Current book | Base initialized EP | Base evolution threshold | Successor |
|---|---:|---:|---|
| [D](grimoire-d.md) | 1,000 | 2,500 | [C](grimoire-c.md) |
| [C](grimoire-c.md) | 2,500 | 5,000 | [B](grimoire-b.md) |
| [B](grimoire-b.md) | 5,000 | 8,000 | [A](grimoire-a.md) |
| [A](grimoire-a.md) | 8,000 | 80,000 | [Special A](grimoire-special-a.md) |

A evolves toward Special A at **80,000 EP** in the base artifact; the older upstream article says 100,000. The death-handler path requires initialized gear components, checks the threshold, and refuses the ordinary tier transition when **Stagnation** is present. Existing gear component patches are carried to the replacement stack before the next tier is initialized; this is not a promise that every add-on component survives.

Special A has no successor and omits maxEP in its JSON, but the checked **GearExistenceData codec defaults that field to 2,000,000**. The base initializer uses its **80,000 minimum EP** when initializing a fresh eligible stack. Existing components and add-on overrides can differ; this is not infinite EP or proof of another tier.

Gear EP gain depends on the death-handler input, game rules, item EP_GAIN, and enchantments including Lethargy, Vigor, and Growth. It is rounded in the checked base helper. A fixed number of kills or casts is not verified. Use [Gear Evolution](../../gear-evolution.md) for TSR’s wider equipment system; current add-on threshold and retention behavior still needs gameplay checks.

## Find a book, then bind a loadout

D, C, B, and A are candidates in Buried, Burnt, Frozen, Rotted, and Ruined Wizard Tower chest definitions. Relative loot weights are not guaranteed drops or per-tower percentages. No Special A direct entry or ordinary grimoire crafting recipe was found in those packaged resources.

Bind compatible learned spells at the [Spellbinding Table](../resistances/spellbinding-table.md). Magic Capacity adds its enchantment level to base slots. Binding does not teach spells. The [casting walkthrough](../tools/caster-tools-tutorial.md) covers modifier-and-scroll selection, mode changes, unlearned-casting exclusions, and costs.

## Separate three resource concepts

- **Gear EP:** the equipment progression value used for base tier thresholds.
- **EP_DURABILITY:** the stored gear resource checked for a contribution toward MP casting costs when the required conditions apply.
- **Ordinary durability:** the item’s separate damageable durability; the base maxima are 100 / 200 / 300 / 400 / 500.

An initialized book is not unlimited fuel, and gear EP support does not waive Aura costs. Raw Chant Speed bonuses are not percentage discounts or final wall-clock casting times.

## Sources and artwork

Implementation: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [item and tier evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/item_reference.json). Individual tier articles credit their upstream revisions under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

[Gear Evolution selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-gear-evolution.pw.toml) · [tracked configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/gearevolution-common.toml). Configuration inspection is not a live-server evolution or prestige-retention test.

The open-book illustration is original TSR artwork shared by the five tier references. It represents the equipment class, not five different verified textures. The upstream inventory images have no verified reusable image license and are not reproduced.

[Return to Items](index.md)
