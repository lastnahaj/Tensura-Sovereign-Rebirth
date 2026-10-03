---
title: Mysticism Commands
description: Selected 2.1.2 command paths, read-only Soul Energy queries, and administrative access boundaries.
---

# Mysticism Commands

<section class="reference-overview reference-theme-evolution staff-guide-hero smithing-guide-hero"><figure class="reference-overview-media"><img src="../../../assets/images/guides/soul-energy.webp" alt="Original soul-flame illustration" loading="eager" decoding="async"><figcaption>Original TSR soul-system artwork · not an interface</figcaption></figure><div class="reference-overview-copy"><p class="reference-eyebrow">Mysticism 2.1.2 · Minecraft 1.21.1</p><h2>Inspect your energy. Keep administration separate.</h2><p>Use the selected command tree rather than the old mixed-version table. Read-only self queries and protected stat changes have different permission declarations.</p><nav class="reference-quick-jumps" aria-label="Mysticism command guide"><a href="#read-your-own-energy">Self queries</a><a href="#registered-command-families">Command families</a><a href="#version-and-permission-limits">Version limits</a></nav></div></section>

<div class="tensura-reference-article" markdown="1">

## Read your own energy

| Read-only self query | Selected implementation |
| --- | --- |
| `/mysticism get stat soulEnergy current` | Reports current Soul Energy storage |
| `/mysticism get stat soulEnergy max` | Reports the maximum Soul Energy attribute’s **base value**, not its total with modifiers |

Both self-query methods declare **Player** access and require a player sender. Target-selection variants add the target before `soulEnergy` and declare **Moderator** access. These are artifact registration checks, not successful live-server command tests. Server permission overrides and completion behavior remain untested.

## Registered command families

<div class="command-entry-grid">
<article class="command-entry" data-command-source="mysticism" data-command-access="mixed" data-command-search="/mysticism get stat … mixed read current soul energy or its base maximum attribute. self queries declare player access; target queries declare moderator access. mysticism soulenergy current|max &lt;target&gt; soulenergy current|max">
<header><code>/mysticism get stat …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Read current Soul Energy or its base maximum attribute. Self queries declare Player access; target queries declare Moderator access.</p>
<div class="command-branches" aria-label="Registered branches"><code>soulEnergy current|max</code><code>&lt;target&gt; soulEnergy current|max</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/get/MysticGetStatCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="mysticism" data-command-access="gamemaster" data-command-search="/mysticism edit stat … gamemaster set or add current or maximum soul energy. maximum edits also declare an optional resetcurrent argument; there is no current-reset branch here. mysticism &lt;targets&gt; soulenergy current set|add &lt;amount&gt; &lt;targets&gt; soulenergy max set|add &lt;amount&gt; [resetcurrent]">
<header><code>/mysticism edit stat …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Set or add current or maximum Soul Energy. Maximum edits also declare an optional resetCurrent argument; there is no current-reset branch here.</p>
<div class="command-branches" aria-label="Registered branches"><code>&lt;targets&gt; soulEnergy current set|add &lt;amount&gt;</code><code>&lt;targets&gt; soulEnergy max set|add &lt;amount&gt; [resetCurrent]</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/edit/MysticEditStatCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="mysticism" data-command-access="gamemaster" data-command-search="/mysticism reset … gamemaster reroll current and maximum soul energy for selected players. this administrative root is separate from stat editing and normal player progression. mysticism &lt;players&gt; soulenergy">
<header><code>/mysticism reset …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Reroll current and maximum Soul Energy for selected players. This administrative root is separate from stat editing and normal player progression.</p>
<div class="command-branches" aria-label="Registered branches"><code>&lt;players&gt; soulEnergy</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/edit/MysticResetCommand.class</code></details>
</article>
</div>

The cards use command patterns: angle brackets are required arguments, vertical bars are alternatives, and square brackets indicate an optional argument. Use the server’s completion suggestions; do not paste punctuation from a pattern as literal syntax.

!!! warning "Administrative reset is not a player progression route"
    Stat edits and the separate `/mysticism reset` root declare **Gamemaster** access. The reset handler rerolls current and maximum Soul Energy for selected players. It is not a skill reset, prestige command, or ordinary method for increasing a player’s capacity. No state-changing command was executed for this review.

## Version and permission limits

??? info "Why the older table is not used as current syntax"

    The upstream article contains both 1.19.2 and 1.21.1 tables. Soul Quality, spirit-contract dissolution, contract inspection, and spirit-element reroll commands from the old table are not declared by the selected 2.1.2 command tree. Its stat-edit methods also do not declare a `current reset` branch; the separately registered reset class sits directly beneath `/mysticism`, not beneath `/mysticism edit`.

    Current storage, the base maximum attribute, optional maximum-edit arguments, and administrative rerolls are separate operations. Declared permission levels do not prove effective server access or protection against overrides.

## Source and licensing

[Commands](https://trmysticism.wiki.gg/wiki/Commands), recorded revision `2887`, Mysticism Wiki, supplies the historical topic. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The [selected 2.1.2 artifact](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529), [command reference](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/command_reference.json), and [annotation review](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/mysticism_command_review.json) support the checked paths and access declarations. These are **not live gameplay or permission tests**.

The illustration is original TSR thematic artwork, not a screenshot or an in-game icon. The unrelated source editorial portrait is omitted. [Sources and attribution](../../project/sources-and-attribution.md).

[Commands by source](../../tensura-reference/commands/index.md#mysticism) · [Soul Energy](../other/soul-energy.md) · [Prestige and Soul Grade](../../prestige-and-soul-grade.md)

</div>
