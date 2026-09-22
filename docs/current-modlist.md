---
title: Current Modlist
description: Search the 299 artifacts in the current TSR 1.21.1 client candidate and review additions, removals, and verification status.
---

# Current Modlist

<section class="modlist-hero">
<img src="../assets/images/reference-world-equipment.png" alt="A fantasy landscape with equipment in the foreground" loading="eager" decoding="async">
<div>
<p class="reference-eyebrow">September 20, 2026 candidate</p>
<h2>299 current client artifacts</h2>
<p>Search the exact 1.21.1 NeoForge candidate by project, version, filename, or system. Candidate presence and runtime verification remain separate.</p>
</div>
</section>

<div class="mod-iteration-strip">
<article><span>Current candidate</span><strong>299</strong><small>artifact records</small></article>
<article><span>Previous snapshot</span><strong>249</strong><small>August 31</small></article>
<article><span>Last full smoke</span><strong>239</strong><small>client profile</small></article>
<article class="mod-iteration-strip__gate"><span>Release gate</span><strong>Pending</strong><small>full candidate validation</small></article>
</div>

<div class="tsr-link-grid" markdown>

- **[Character systems](progression-overview.md)**<br>
  Tensura progression, races, skills, evolution, magicules, and awakening.

- **[Adventure & world](adventure-travel-and-loot/index.md)**<br>
  Bosses, dimensions, structures, exploration, travel, and loot.

- **[Kingdom systems](minecolonies-and-nations.md)**<br>
  Colonies, quests, teams, claims, shops, and multiplayer progression.

- **[Technology & crafting](forging-and-metalworks.md)**<br>
  Create, Mekanism, forging, storage, building, and production.

</div>

!!! info "Snapshot scope"
    This snapshot enumerates the current **client candidate** captured on September 20, 2026. Presence confirms that an artifact is in this iteration; it does not mean the complete 299-artifact set has passed cold-start, dedicated-server, restart, gameplay, or redistribution gates. The last fully recorded client smoke remains the 239-mod profile.

!!! warning "Compatibility records still apply"
    The snapshot includes Ice & Fire with its Tensura bridge and Tensura: Unique Monsters. Their appearance in a client list does not by itself clear the dedicated-server blockers recorded in the [Compatibility Matrix](compatibility-matrix.md). They remain outside verified release claims until the current exact artifacts pass the required server test matrix.

## What changed in this iteration

<div class="mod-change-grid">
<article class="mod-change-card mod-change-card--added">
<span>Added since August 31</span>
<strong>58 project identities</strong>
<p>Includes TR: Nightmare, Elite Tensura, the current EMI suite, expanded Create and Aether support, Quark, Bountiful, Small Ships, and additional Twilight Forest content.</p>
</article>
<article class="mod-change-card mod-change-card--updated">
<span>Updated artifacts</span>
<strong>8 replacements</strong>
<p>Includes Tensura: Reincarnated 2.0.1.3, Magicule Engineering 1.2, Tensura MineColonies Integration 0.2.3, and current supporting releases.</p>
</article>
<article class="mod-change-card mod-change-card--removed">
<span>Removed from the current candidate</span>
<strong>Retired systems stay retired</strong>
<p>TensuraMorph, ReMorphed, Tensura Guild, and Woodwalkers are not part of the current iteration. Their old progression pages are retained only as clearly marked historical records.</p>
</article>
</div>

??? note "Complete identity changes from the 249-mod snapshot"
    **Removed identities:** ChatManager; foxablazeaqzl's Built-in Tensura Skill Wiki; Just Enough Resources; Minecolonies Mages; ReMorphed; Tensura Guild; Tensura Magic Growth; and TensuraMorph.

    **Already absent and still removed:** Woodwalkers. It was part of an older design baseline, but not the August 31 snapshot or the current candidate.

    **Artifact replacements:** Bosses'Rise x Tensura Compatibility; FTB Chunks; Legendary Monsters x Tensura Compat; Simple Voice Chat; Structurize; Tensura MineColonies Integration; Tensura: Magicule Engineering; and Tensura: Reincarnated.

<section class="current-modlist" data-modlist-source="assets/data/current-client-modlist.json">
<div class="current-modlist-tools">
<label>
<span>Search the current modlist</span>
<input type="search" class="current-modlist-search" placeholder="Try Tensura, Create, Mekanism, 1.21.1…" autocomplete="off">
</label>
<div class="current-modlist-filters" role="group" aria-label="Filter modlist by system"></div>
<p class="current-modlist-status" aria-live="polite">Loading current modlist…</p>
</div>
<div class="current-modlist-grid"></div>
<p class="current-modlist-empty" hidden>No matching mods. Try a broader search or another system.</p>
<noscript>The searchable modlist requires JavaScript. The exact snapshot is available as <a href="../assets/data/current-client-modlist.json">JSON</a>.</noscript>
</section>

## Reproducibility note

The downloadable JSON preserves the project name, declared version, exact filename, enabled state, and official distribution URL for every current artifact. The public modlist is an inventory, not a substitute for the compatibility matrix or release evidence; newly added and replaced artifacts are not silently promoted to Verified status.
