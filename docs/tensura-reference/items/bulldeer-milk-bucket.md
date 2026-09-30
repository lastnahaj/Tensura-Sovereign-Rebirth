---
title: "Cattledeer Milk Bucket"
description: "A registered milk consumable with an older Bulldeer name; normal Cattledeer milking produces vanilla Milk instead."
---

# Cattledeer Milk Bucket

<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Items &amp; Materials</span>

<section class="reference-overview reference-theme-world">
<figure class="reference-overview-media reference-overview-media--source">
<img src="../../../assets/images/items/cattledeer-milk.webp" alt="Cattledeer Milk Bucket illustration" loading="eager" decoding="async">
<figcaption>TSR item illustration · not the in-game texture</figcaption>
</figure>
<div class="reference-overview-copy">
<p class="reference-eyebrow">At a glance</p>
<p>A registered milk consumable with an older Bulldeer name; normal Cattledeer milking produces vanilla Milk instead.</p>
<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#availability">Availability</a><a href="#how-to-use">How to use</a></nav>
</div>
</section>

!!! warning "Registered item · acquisition unverified"
    Do not confuse this registered item with the result of milking a Cattledeer. In the reviewed build, using an empty bucket on that mob explicitly returns minecraft:milk_bucket.

<div class="tensura-reference-article"><div class="druid-container reference-release-stats"><aside class="druid-infobox">
<div class="druid-title">Cattledeer Milk Bucket</div>
<div class="druid-row"><div class="druid-label">Registry ID</div><div class="druid-data">tensura:bucket_of_cattledeer_milk</div></div>
<div class="druid-row"><div class="druid-label">Build</div><div class="druid-data">Tensura 2.0.1.2 · Minecraft 1.21.1</div></div>
<div class="druid-row"><div class="druid-label">Obtainment</div><div class="druid-data">Survival route not verified</div></div>
</aside></div></div>

## Availability

No survival route for the separate Cattledeer Milk Bucket was verified. CattledeerEntity.mobInteract checks for an empty bucket and creates vanilla Milk. A Monstrous Diet advancement criterion references the separate Tensura item, but an advancement requirement is not an acquisition method.

## How to use

The separate item is constructed as Minecraft's MilkBucketItem with a stack limit of one. Its base-class behavior is milk consumption, not a unique skill-unlock or evolution item. This is an implementation check; interactions with server-specific effects have not been tested in gameplay.

## Behavior and limits

The older source title is Bulldeer Milk Bucket. The current registry uses bucket_of_cattledeer_milk. This article retains its original URL so existing links continue to work.

[Return to Items](index.md)

## Source and licensing

Upstream reference: [Bulldeer Milk Bucket](https://tensura.wiki.gg/wiki/Bulldeer_Milk_Bucket) on the Tensura: Reincarnated Wiki, recorded revision `9200`. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The unfinished source artwork is not reproduced.

Implementation check: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [TSR pack selection](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/mods/tensura-reincarnated.pw.toml). Artifact SHA-1: `f6f0c8ce46b77a1996c5986d029411878142112f`. Registration and code checks are not live-server gameplay tests.

The illustration is original TSR artwork, not a source game texture or an in-game appearance guarantee.

??? info "Artifact evidence"

    - `io/github/manasmods/tensura/registry/item/TensuraConsumableItems.class`
    - `io/github/manasmods/tensura/entity/monster/CattledeerEntity.class`
    - `data/tensura/advancement/monstrous_diet.json`
