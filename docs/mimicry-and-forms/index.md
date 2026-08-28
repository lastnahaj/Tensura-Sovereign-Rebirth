---
title: Mimicry & Forms
description: How TSR connects Tensura absorption skills to its creature-form system.
---

# Mimicry & Forms

<div class="reference-overview" markdown>

<figure class="reference-overview-media reference-overview-media--theme">
<img src="../assets/images/reference-races-evolution.png" alt="A branching fantasy transformation path" loading="eager" decoding="async">
</figure>

<div class="reference-overview-copy" markdown>

<p class="reference-eyebrow">Character system</p>

TSR uses **TensuraMorph** to connect Tensura's absorption fantasy to the **ReMorphed**, **Woodwalkers**, and **CraftedCore** form system.

<span class="tsr-status">Startup verified</span>

</div>

</div>

## Intended progression

Ordinary kill farming is not the practical route to creature forms. The beta configuration raises ReMorphed's ordinary per-creature unlock threshold to **100,000 kills** and disables the creative-mode unlock-all bypass. TensuraMorph applies the same policy so Tensura abilities such as **Predator** and **Gluttony** remain the intended route into mimicry.

## What each mod does

| Component | TSR role |
|---|---|
| TensuraMorph | Connects supported Tensura absorption behavior to form unlocks |
| ReMorphed | Supplies the player-facing form system and configured unlock rules |
| Woodwalkers | Provides the underlying creature-shape mechanics required by ReMorphed |
| CraftedCore | Shared runtime dependency for the form stack |

## Player checklist

1. Build around a supported absorption skill instead of grinding ordinary kills.
2. Use the form interface only after the relevant creature form has been earned.
3. Treat each form as utility or tactical expression, not a replacement for race evolution, EP, skills, or equipment.
4. Report forms that bypass progression, preserve forbidden abilities, or fail after reconnecting.

??? warning "Beta validation boundary"
    Client/server construction and the anti-bypass configuration are verified. Exhaustive creature compatibility, multiplayer synchronization, death persistence, and every absorption-to-form path remain gameplay validation work.

See [Skills, EP & Magicules](../skills-ep-and-magicules.md), [Race & Evolution](../race-and-evolution.md), and the [Compatibility Matrix](../compatibility-matrix.md).
