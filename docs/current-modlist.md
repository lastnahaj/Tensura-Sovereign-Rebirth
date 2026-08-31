---
title: Current Modlist
description: Search and filter the 249 mods enumerated by the current TSR client snapshot.
---

# Current Modlist

<section class="modlist-hero">
<img src="../assets/images/reference-world-equipment.png" alt="A fantasy landscape with equipment in the foreground" loading="eager" decoding="async">
<div>
<p class="reference-eyebrow">Current client snapshot</p>
<h2>249 loaded mod identities</h2>
<p>Search by mod, version, or JAR filename. Use a system filter to narrow the pack without scrolling through a wall of text.</p>
</div>
</section>

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
    This snapshot enumerates the current **client** profile as of August 31, 2026. Presence here confirms the mod identity appeared in that launcher snapshot; it does not replace the recorded cold-start, server-restart, gameplay, or redistribution gates. The last fully recorded release-candidate smoke remains the 239-mod client profile.

!!! warning "Compatibility records still apply"
    The snapshot includes Ice & Fire with its Tensura bridge and Tensura: Unique Monsters. Their appearance in a client list does not by itself clear the dedicated-server blockers recorded in the [Compatibility Matrix](compatibility-matrix.md). They remain outside verified release claims until the current exact artifacts pass the required server test matrix.

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

The snapshot contains 45 filenames not present in the previous 209-entry inventory reference and omits five older filenames. Nineteen current filenames do not yet have an exact matching Packwiz filename record, including local modules, newly added content, and previously blocked compatibility entries. Those items are visible here for transparency but are not silently promoted into a public release.
