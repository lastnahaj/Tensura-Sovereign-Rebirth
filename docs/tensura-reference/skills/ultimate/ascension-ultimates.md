---
title: Ascension Ultimate Skills
description: Interactive reference for the five documented TSR Ascension Ultimate awakenings.
---

<section class="ascension-hero ascension-hero--ultimates"><div><p class="reference-eyebrow">Endgame skill progression</p><h1>Ascension Ultimates</h1><p>Each path replaces a fully mastered Unique skill. Open a card for passives, abilities, costs, cooldowns, and its extra awakening gate.</p></div><nav class="ascension-jump-nav" aria-label="Ultimate skill shortcuts"><a href="#the-timeless-mage">Timeless Mage</a><a href="#the-unbound-jester">Unbound Jester</a><a href="#the-evil-majin">Evil Majin</a><a href="#the-slayer-of-dragons">Slayer of Dragons</a><a href="#the-one-who-seals">One Who Seals</a></nav></section>

<div class="skill-evolution-map" aria-label="Unique to Ultimate skill progression">
<a href="../../ascension/#great-mage">Great Mage</a><span>→</span><a href="#the-timeless-mage">The Timeless Mage</a>
<a href="../../ascension/#imprisoned-jester">Imprisoned Jester</a><span>→</span><a href="#the-unbound-jester">The Unbound Jester</a>
<a href="../../ascension/#bubble-majin">Bubble Majin</a><span>→</span><a href="#the-evil-majin">The Evil Majin</a>
<a href="../../ascension/#dragon-slayer">Dragon Slayer</a><span>→</span><a href="#the-slayer-of-dragons">The Slayer of Dragons</a>
<a href="../../ascension/#sealer">Sealer</a><span>→</span><a href="#the-one-who-seals">The One Who Seals</a>
</div>

!!! warning "Universal gates still apply"
    Every path also needs Ultimate awakening enabled, **5,000,000 Max EP**, True Demon Lord or True Hero status, a fully mastered prerequisite Unique, a valid altar and catalyst, and no active two-hour cooldown. See the [complete ritual guide](../../../ascension-and-awakening.md).

<details class="ascension-entry ascension-entry--ultimate" id="the-timeless-mage" markdown="1">
<summary><img src="../../../../assets/ascension/ultimates/the_timeless_mage.png" alt="The Timeless Mage icon"><span><strong>The Timeless Mage</strong><small>Great Mage → Ultimate</small></span></summary>
<div markdown>

**Extra gate:** Learn all **14 Aspectual magic schools**. **Previous:** [Great Mage](../ascension.md#great-mage).

### Passives

- On grant, learns every Aspectual and Spiritual magic and sets each to maximum mastery.
- Chant Annulment permanently skips chants.
- Toggle: **+29 Ability Mastery Gain** (about 30× mastery gain on every other skill), level-3 Perfect Analytical Appraisal in a **30-block** radius, and magic that bypasses resistance and nullification.
- Toggle: vanilla `mayFly` creative flight and immunity to Magic Jamming.

### Abilities

- **Create Tome:** Opens the Great Mage tome menu. The GUI charges its own XP per craft; the skill has no cooldown.
- **Zoltraak:** Hold a black-and-white beam up to **30 blocks**. Every **0.5 seconds** it deals **10% target Max HP** as `ascension:zoltraak`, bypassing armor, resistance, invulnerability, PvP-off, and iframes. Each hit suppresses regeneration for **3 seconds**, temporarily disabling and then restoring regen toggles. If your Max EP is at least **1.5×** the target's, the first hit kills instantly. Cooldown: **20s / 5s mastered**.
- **Magic Dominate:** Makes the aimed entity forget one random Aspectual or Spiritual magic. Cooldown: **20s / 10s mastered**.

[Prepare the altar and ritual](../../../ascension-and-awakening.md)

</div></details>

<details class="ascension-entry ascension-entry--ultimate" id="the-unbound-jester" markdown="1">
<summary><img src="../../../../assets/ascension/ultimates/the_unbound_jester.png" alt="The Unbound Jester icon"><span><strong>The Unbound Jester</strong><small>Imprisoned Jester → Ultimate</small></span></summary>
<div markdown>

**Extra gate:** Deal **1,000,000 cumulative spirit damage** while Imprisoned Jester is slotted. **Previous:** [Imprisoned Jester](../ascension.md#imprisoned-jester).

### Passives

- In slot: **+50% physical damage**, **+50% magic damage**, **30% crit chance**, and **+100% crit damage**.
- Always forces alignment to **Chaos**. Toggle reflects **25% of all incoming physical and magic damage**.
- **The Bit Goes On:** A lethal hit is cancelled; you become invisible, invulnerable, and Slow Falling for **5 seconds**, while Aura and Magicule drain to 5%. Internal cooldown: **5 minutes**.

### Abilities

- **Chaos Theater:** Held **8-block sphere** centered on you. Each pulse deals `EP × 0.00015` playerAttack damage—**1,500 at the 10M EP cap**—to HP and SHP through `directSpiritualHurt`, costing **5% Max Aura per pulse**. It uses chaos-spade particles and sound at **35% volume**. Release cooldown: **30s / 10s mastered**.
- **Curtain Call:** Every enemy in **16 blocks** takes your current HP as damage to HP and SHP; casting does not kill you. Cooldown: **60s**.
- **Final Punishment:** Applies an undispellable **Sentence** within **16 blocks** when your EP is at least **1.5×** the target's. It deals **5% target Max HP per second for 10 seconds**. A death during Sentence permanently grants you **25% of the target's EP as Max EP**. Cooldown: **60s / 10s mastered**.

[Prepare the altar and ritual](../../../ascension-and-awakening.md)

</div></details>

<details class="ascension-entry ascension-entry--ultimate" id="the-evil-majin" markdown="1">
<summary><img src="../../../../assets/ascension/ultimates/the_evil_majin.png" alt="The Evil Majin icon"><span><strong>The Evil Majin</strong><small>Bubble Majin → Ultimate</small></span></summary>
<div markdown>

**Extra gate:** No additional gate is documented beyond the universal requirements. **Previous:** [Bubble Majin](../ascension.md#bubble-majin).

### Passives

- Toggle: auto-heal to full every **10 seconds** and cleanse harmful potion effects every **5 seconds**.
- Toggle: reflect basic projectiles at **1.5× speed**; reflected Tensura projectiles deal **2× damage**.

### Abilities

- **Storage:** Opens **81 slots**, each capped at **666 items**. No cooldown.
- **Candy for me!:** A **12-block sphere** instantly kills enemies you outclass: caster EP at least **2×** a normal mob or **5×** a boss. EP and eligible skills merge into one Majin Candy; Ultimate skills are excluded, and the candy retains **20%** of absorbed EP. PvP is config-gated. Cooldown: **20s / 5s mastered**.
- **Hunger:** Held **16-block** pink predation mist at half normal Gluttony size. It ticks **8 damage**, drains EP, and plunders skills without corrosion damage. Sneak+click cycles **none → blocks → fluid → all** consumption. No resource cost. Release cooldown: **20s / 5s mastered**.

[Prepare the altar and ritual](../../../ascension-and-awakening.md)

</div></details>

<details class="ascension-entry ascension-entry--ultimate" id="the-slayer-of-dragons" markdown="1">
<summary><img src="../../../../assets/ascension/ultimates/the_slayer_of_dragons.png" alt="The Slayer of Dragons icon"><span><strong>The Slayer of Dragons</strong><small>Dragon Slayer → Ultimate</small></span></summary>
<div markdown>

**Extra gate:** Consume **30 items** in the `ascension:dragon_essences` tag. **Previous:** [Dragon Slayer](../ascension.md#dragon-slayer).

### Passives

- Toggle: eating Dragon Essence or dragon flesh grants **+30 Max HP permanently**, uncapped until death.
- Toggle: every dragon kill permanently adds **+50,000 Max EP** (split 50/50 Aura/Magicule) and **+1 Armor** through a single growing modifier.
- Prevents a True Hero awakening on Seraphim from mis-routing into Fallen Angel.

### Abilities

- **Dragon Infusion:** Consumes a Dragon Heart for **+40,000 EP**, or **+50,000 mastered**. Cooldown: **10s**.
- **Draconic Rage:** Strength XX, Strengthen V, +30 attack damage, and Resistance III for **300 seconds**. Cooldown: **300s**.
- **Dragon King Roar:** Held breath stream with **25 base damage**, **2× normal breath range**, and a **40% narrower** cone. Active FLAME, WATER, or LIGHTNING Domination multiplies damage. Release cooldown: **30s**; mastered damage: **50**.

[Prepare the altar and ritual](../../../ascension-and-awakening.md)

</div></details>

<details class="ascension-entry ascension-entry--ultimate" id="the-one-who-seals" markdown="1">
<summary><img src="../../../../assets/ascension/ultimates/the_one_who_seals.png" alt="The One Who Seals icon"><span><strong>The One Who Seals</strong><small>Sealer → Ultimate</small></span></summary>
<div markdown>

**Extra gate:** Supply a Suppression Stone holding at least **400,000 Max EP**; the stone is consumed. **Previous:** [Sealer](../ascension.md#sealer).

### Passive

Every kill grants **+0.5 Max SHP**, up to **20,000 cumulative Max SHP**.

### Abilities

- **Seal:** Standard sealing action at **16 blocks**. Cooldown: **30s / 20s mastered**.
- **Suppress:** Bottle **20% Max EP**, or **30% mastered**, from yourself or a sneak-target within **16 blocks**. The stone can be used later. Cooldown: **60s**.
- **Enough is Enough:** Steal a chosen skill from a target within **16 blocks**. You need at least **2× target EP** for an ordinary skill or **3×** for a Unique. The skill arrives at **0 mastery**. Cooldown: **60s / 10s mastered**.

[Prepare the altar and ritual](../../../ascension-and-awakening.md)

</div></details>
