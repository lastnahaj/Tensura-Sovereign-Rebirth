---
title: Ascension & Awakening
description: Build the altar, craft a catalyst, meet every gate, and awaken an Ascension Ultimate skill.
---

<section class="ascension-hero ascension-hero--ritual"><div><p class="reference-eyebrow">Late-game field guide</p><h1>Awaken an Ultimate skill</h1><p>Turn a mastered Unique into its Ascension Ultimate through a ten-second altar ritual—and know exactly what the altar checks before it begins.</p><div class="ascension-hero-actions"><a class="md-button md-button--primary" href="./#ritual-readiness">Check readiness</a><a class="md-button" href="../tensura-reference/skills/ultimate/">Compare Ultimates</a></div></div></section>

!!! info "Ascension versus base Tensura awakening"
    This is TSR's **Tensura: Ascension** Unique-to-Ultimate system. The base mod's race-awakening mechanic remains documented in [Races & Awakening](tensura-reference/core-mechanics/races-awakening.md).

## What a successful ritual does

<div class="outcome-strip"><span><b>1</b> mastered Unique is replaced</span><span><b>10s</b> ritual cinematic</span><span><b>+25%</b> Max EP</span><span><b>50/50</b> Aura and Magicule split</span></div>

Your current Aura and Magicule refill to their newly increased maximums. The new Ultimate occupies the prerequisite Unique's progression path; it is not an extra copy alongside it.

## Ritual readiness

The altar checks these gates in order when you right-click it:

<ol class="gate-grid">
<li><b>Awakening enabled</b><span><code>/gamerule doAscensionUltimate</code> must be true.</span></li>
<li><b>5,000,000 Max EP</b><span>Current EP is not the gate; reach the Max EP threshold.</span></li>
<li><b>Awakened status</b><span>Be a True Demon Lord or True Hero. Demon Lord Seed and Hero Egg do not qualify.</span></li>
<li><b>Mastered prerequisite</b><span>Learn and fully master an eligible Unique skill.</span></li>
<li><b>Ultimate tribute</b><span>Satisfy the extra gate for the chosen evolution, if one exists.</span></li>
<li><b>Cooldown clear</b><span>A successful ritual starts a two-hour real-time cooldown stored on your character.</span></li>
</ol>

### Unique → Ultimate map

<div class="skill-evolution-map">
<a href="../tensura-reference/skills/unique/great-mage/">Great Mage</a><span>→</span><a href="../tensura-reference/skills/ultimate/the-timeless-mage/">The Timeless Mage</a>
<a href="../tensura-reference/skills/unique/imprisoned-jester/">Imprisoned Jester</a><span>→</span><a href="../tensura-reference/skills/ultimate/the-unbound-jester/">The Unbound Jester</a>
<a href="../tensura-reference/skills/unique/bubble-majin/">Bubble Majin</a><span>→</span><a href="../tensura-reference/skills/ultimate/the-evil-majin/">The Evil Majin</a>
<a href="../tensura-reference/skills/unique/dragon-slayer/">Dragon Slayer</a><span>→</span><a href="../tensura-reference/skills/ultimate/the-slayer-of-dragons/">The Slayer of Dragons</a>
<a href="../tensura-reference/skills/unique/sealer/">Sealer</a><span>→</span><a href="../tensura-reference/skills/ultimate/the-one-who-seals/">The One Who Seals</a>
</div>

| Ultimate | Additional gate |
| --- | --- |
| The Timeless Mage | Learn all **14 Aspectual magic schools**. |
| The Unbound Jester | Deal **1,000,000 cumulative spirit damage** while Imprisoned Jester is slotted. |
| The Evil Majin | No additional gate is documented beyond the universal gates. |
| The Slayer of Dragons | Provide **30 items** in the `ascension:dragon_essences` tag; consumed. |
| The One Who Seals | Provide a Suppression Stone holding at least **400,000 Max EP**; consumed. |

## Craft the ritual pieces

<div class="recipe-grid">
<article class="recipe-card"><img src="../assets/ascension/mechanics/soul_echo.png" alt="Soul Echo item"><div><p class="reference-eyebrow">Drop</p><h3>Soul Echo</h3><p>A player must kill a custom-named creature or any boss with at least <b>200,000 Max EP</b>. Eight Echoes make one catalyst.</p></div></article>
<article class="recipe-card"><img src="../assets/ascension/mechanics/ultimate_catalyst_recipe.png" alt="Ultimate Catalyst crafting recipe"><div><p class="reference-eyebrow">Craft</p><h3>Ultimate Catalyst</h3><p><b>8 Soul Echoes</b> + <b>1 Tensura Hihiirokane Ingot</b> → 1 catalyst.</p></div></article>
<article class="recipe-card"><img src="../assets/ascension/mechanics/deepslate_magic_block_recipe.png" alt="Deepslate Magic Block crafting recipe"><div><p class="reference-eyebrow">Craft</p><h3>Deepslate Magic Block</h3><p><b>6 Deepslate Bricks</b> + <b>3 Tensura High Quality Magic Crystal Blocks</b> → 1 block.</p></div></article>
<article class="recipe-card"><img src="../assets/ascension/mechanics/awakening_altar_recipe.png" alt="Awakening Altar crafting recipe"><div><p class="reference-eyebrow">Craft</p><h3>Awakening Altar</h3><p><b>1 Tensura Slime Core</b> + <b>2 Tensura Mithril Ingots</b> + <b>4 Crying Obsidian</b>.</p></div></article>
</div>

Boss detection also recognizes supported bosses from **The Aether, Twilight Forest, L_Ender's Cataclysm, Bosses'Rise,** and **Mowzie's Mobs** when those mods are installed. Ascension also provides generalized Tensura EP integration for those five mods.

## Build the Awakening Altar

<div class="altar-layout" markdown="1">
<div class="altar-plan" role="img" aria-label="Top-down altar plan: altar in the center, four pillars at diagonal offsets, a 37-block brick interior, and 20 bottom slabs on the perimeter"><span class="altar-legend">Top view · floor is one block below altar</span><div class="altar-octagon"><i class="pillar p1">P</i><i class="pillar p2">P</i><i class="altar-center">A</i><i class="pillar p3">P</i><i class="pillar p4">P</i></div><p><b>A</b> Altar · <b>P</b> Pillar bases · outer rim: bottom slabs</p></div>
<div markdown>

### Material checklist

- **1** Awakening Altar
- **45** Deepslate Bricks: 37 floor interior + 8 in pillars
- **20** bottom-half Deepslate Brick Slabs on the perimeter
- **4** Deepslate Magic Blocks
- **4** Tensura Pure Magisteel Blocks

The floor sits one block below altar level and uses a rounded, approximately 9×9 octagon: **57 positions total**, with 20 perimeter slabs and 37 interior bricks. The illustration is a schematic, not a block-by-block blueprint.

</div></div>

Place the four pillar bases at offsets **(−2, −2), (+2, −2), (−2, +2), (+2, +2)** from the altar. Each pillar is four blocks high:

| Height | Block |
| --- | --- |
| Y+3 | Tensura Pure Magisteel Block |
| Y+2 | Deepslate Bricks |
| Y+1 | Deepslate Magic Block |
| Y+0 | Deepslate Bricks |

!!! warning "Most common construction mistake"
    All 20 perimeter slabs must be **bottom-half slabs**. A top slab can make a visually complete altar fail validation.

## Perform the ritual

<div class="ritual-steps">
<article><b>1</b><h3>Load</h3><p>Drop one Ultimate Catalyst on the altar. Purple enchant particles, an amethyst chime, and a floating catalyst icon confirm absorption.</p></article>
<article><b>2</b><h3>Validate</h3><p>Right-click the altar. Failed gates leave the loaded catalyst intact so you can correct the problem.</p></article>
<article><b>3</b><h3>Stay close</h3><p>Remain within <b>8 blocks</b> throughout the ten-second cinematic. Leaving cancels the ritual and consumes the catalyst.</p></article>
<article><b>4</b><h3>Awaken</h3><p>Your mastered Unique is replaced, Max EP increases, resources refill, witnesses are rewarded, and the cooldown starts.</p></article>
</div>

### Witness rewards

Every eligible witness within **16 blocks** independently gains **2% of the awakener's Max EP** as Max EP. Eligible witnesses are other players and non-player living entities given a Tensura true name through the Naming menu. The reward is not subtracted from the awakening player.

## Troubleshooting

| Message or symptom | What to fix |
| --- | --- |
| Ultimate awakening disabled | Set `doAscensionUltimate` to true. |
| Altar pattern incomplete | Recheck all 57 floor positions, bottom slab orientation, pillar offsets, and layers. |
| Soul too unrefined | Reach 5,000,000 Max EP. |
| Only a True Demon Lord or True Hero may awaken | Seed and Egg precursor states do not count. Complete the awakening first. |
| No mastered Unique eligible | Learn and fully master one of the mapped prerequisite Uniques. |
| Every Ultimate available already awakened | This character has no remaining documented eligible awakening. |
| Soul still recovering | Wait for the two-hour real-time cooldown or ask an administrator to reset it. |

### Administrator controls

```text
/gamerule doAscensionUltimate <true|false>
/tascension cooldown reset <targets>
```

## Other Ascension additions

### Regeneration Suppression

[Blockade](tensura-reference/skills/extra/blockade.md) applies Regeneration Suppression, which force-disables Self Regen, Ultraspeed Regen, and Infinite Regen on its target. [The Timeless Mage's Zoltraak](tensura-reference/skills/ultimate/the-timeless-mage.md) applies a three-second suppression window that saves and then restores the target's previous regeneration toggles.

### Training and enchantments

- **Hyperbolic Chamber:** dangerous Magicule-gated training dimension with **3× EP gain**. [Read the travel guide](hyperbolic-chamber.md).
- **Serrated:** weapon enchantment that applies Bleeding.
- **EP Attunement:** allows EP to be attached to weapons, armor, and tools that are not supported automatically.
