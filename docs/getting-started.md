---
title: Getting Started
description: A visual first-hour guide to joining TSR, surviving reincarnation, and choosing a progression path.
---

<div class="onboarding-hero">
<img src="../assets/images/sovereign_rebirth_a_magical_kingdom.png" alt="A luminous fantasy kingdom beneath a blue night sky" loading="eager" decoding="async">
<div class="onboarding-hero-shade"></div>
<div class="onboarding-hero-copy">
<p class="reference-eyebrow">New player field guide</p>
<h1>Begin your sovereign story</h1>
<p>Join the realm, understand your reincarnation, secure a home, and choose the first path that sounds fun. This guide turns your opening hour into a few useful decisions.</p>
<div class="onboarding-hero-actions">
<a class="md-button md-button--primary" href="#your-first-hour">Start the first-hour route</a>
<a class="md-button" href="../current-modlist/">Browse the current modlist</a>
</div>
</div>
</div>

<section class="server-pulse" data-server-status data-server-address="tsr.infinitegamingservers.com" aria-labelledby="realm-status-title">
  <div class="server-pulse-heading">
    <div>
      <p class="reference-eyebrow">Live realm</p>
      <h2 id="realm-status-title">Who is adventuring right now?</h2>
    </div>
    <span class="server-state" data-status-label>Checking…</span>
  </div>
  <p class="server-address"><span>Join address</span><strong>tsr.infinitegamingservers.com</strong></p>
  <div class="server-stat-grid">
    <div><strong data-status-online>—</strong><span>Online</span></div>
    <div><strong data-status-max>—</strong><span>Capacity</span></div>
    <div><strong data-status-version>—</strong><span>Version</span></div>
  </div>
  <p class="server-message" data-status-message>Requesting the latest cached public server status.</p>
  <ul class="server-player-list" data-status-players aria-label="Publicly reported online players">
    <li class="server-player-empty">Checking the public player sample…</li>
  </ul>
  <div class="server-pulse-actions">
    <button type="button" data-copy-server>Copy server address</button>
    <button type="button" data-status-refresh>Refresh status</button>
    <span data-status-updated aria-live="polite"></span>
  </div>
  <p class="server-fine-print">Status is provided by the public Minecraft status service and may be cached for up to five minutes. Player names appear only when the server shares a public sample.</p>
</section>

## Your first hour

<div class="first-hour-route" id="your-first-hour">
  <article data-step="1">
    <span>00–10</span>
    <h3>Read your reincarnation</h3>
    <p>Finish character creation, then inspect your race and starting abilities before committing to fights. A starting form is the beginning of a route—not your permanent ceiling.</p>
    <a href="../tensura-reference/core-mechanics/reincarnation/">Reincarnation guide →</a>
  </article>
  <article data-step="2">
    <span>10–25</span>
    <h3>Establish a safe foothold</h3>
    <p>Collect basic food and materials, set a return point, and avoid testing every unfamiliar creature at once. TSR's world contains encounters meant for later progression.</p>
    <a href="../adventure-travel-and-loot/">Travel and loot →</a>
  </article>
  <article data-step="3">
    <span>25–45</span>
    <h3>Learn your power loop</h3>
    <p>EP tracks broad character power; Magicules, Aura, mastery, and skills have distinct jobs. Check the controls menu for your active bindings instead of assuming a default key.</p>
    <a href="../skills-ep-and-magicules/">Understand resources →</a>
  </article>
  <article data-step="4">
    <span>45–60</span>
    <h3>Claim and choose</h3>
    <p>Create or join an FTB team, protect your first home, then choose a progression route. You can change direction later—TSR is designed around parallel tracks.</p>
    <a href="../teams-and-claims/">Protect your home →</a>
  </article>
</div>

!!! tip "Three habits that prevent most early frustration"
    Read tooltips before spending rare resources, verify keybinds in the current Controls screen, and treat quest or guide status labels literally. Installed content may still be undergoing balance or integration validation.

## Field checklist

<section class="onboarding-checklist" data-onboarding-checklist>
  <div class="onboarding-checklist-heading">
    <div>
      <p class="reference-eyebrow">Saved only in this browser</p>
      <h3>Your opening tasks</h3>
    </div>
    <button type="button" data-checklist-reset>Reset</button>
  </div>
  <progress value="0" max="5" aria-label="Opening task progress"></progress>
  <p data-checklist-count aria-live="polite">0 of 5 field tasks complete</p>
  <div class="onboarding-checklist-items">
    <label><input type="checkbox" data-check-id="reincarnation"><span><strong>Understand your reincarnation</strong>Read your race page and inspect your starting abilities.</span></label>
    <label><input type="checkbox" data-check-id="controls"><span><strong>Review your controls</strong>Resolve conflicts and identify the menus or ability inputs you actually use.</span></label>
    <label><input type="checkbox" data-check-id="shelter"><span><strong>Secure food and shelter</strong>Create a stable return point before taking on distant encounters.</span></label>
    <label><input type="checkbox" data-check-id="claim"><span><strong>Join a team and claim home</strong>Use FTB Teams and Chunks before valuable building begins.</span></label>
    <label><input type="checkbox" data-check-id="path"><span><strong>Choose a first route</strong>Pick character power, adventure, engineering, or nation building below.</span></label>
  </div>
</section>

## Choose a path, not a class

Your starting choice is a direction, not a lock-in. These routes use systems present in the current 249-mod client snapshot; exact balance and campaign gates remain subject to beta validation.

<section class="onboarding-paths" data-onboarding-paths>
  <div class="onboarding-path-tabs" role="tablist" aria-label="First progression paths">
    <button id="path-power-tab" type="button" role="tab" aria-selected="true" aria-controls="path-power">Evolve</button>
    <button id="path-hunt-tab" type="button" role="tab" aria-selected="false" aria-controls="path-hunt" tabindex="-1">Explore</button>
    <button id="path-forge-tab" type="button" role="tab" aria-selected="false" aria-controls="path-forge" tabindex="-1">Engineer</button>
    <button id="path-nation-tab" type="button" role="tab" aria-selected="false" aria-controls="path-nation" tabindex="-1">Found a nation</button>
  </div>
  <div class="onboarding-path-panel path-theme-power" id="path-power" role="tabpanel" aria-labelledby="path-power-tab">
    <img src="../assets/images/reference-races-evolution.png" alt="A lineup of evolving fantasy races" loading="lazy" decoding="async">
    <div>
      <p class="reference-eyebrow">Character progression</p>
      <h3>Grow through races, skills, and mastery</h3>
      <p>Learn how EP, Magicules, Aura, skills, and evolution requirements connect before chasing a specific final form.</p>
      <a href="../race-and-evolution/">Race and evolution</a>
      <a href="../skills-ep-and-magicules/">Skills and resources</a>
      <a href="../tensura-reference/skills/unique/">Browse Unique Skills</a>
    </div>
  </div>
  <div class="onboarding-path-panel path-theme-hunt" id="path-hunt" role="tabpanel" aria-labelledby="path-hunt-tab" hidden>
    <img src="../assets/images/reference-bestiary.png" alt="A fantasy bestiary of creatures and bosses" loading="lazy" decoding="async">
    <div>
      <p class="reference-eyebrow">Adventure progression</p>
      <h3>Travel, hunt, and conquer carefully</h3>
      <p>Follow missions or your own map, unlock travel options, share generated loot fairly, and check encounter validation before challenging bosses or dimensions.</p>
      <a href="../adventure-travel-and-loot/">Adventure, travel, and loot</a>
      <a href="../bosses-and-dimensions/">Bosses and dimensions</a>
      <a href="../tensura-reference/mobs/">Browse the bestiary</a>
    </div>
  </div>
  <div class="onboarding-path-panel path-theme-forge" id="path-forge" role="tabpanel" aria-labelledby="path-forge-tab" hidden>
    <img src="../assets/images/reference-world-equipment.png" alt="Equipment and structures in a magical world" loading="lazy" decoding="async">
    <div>
      <p class="reference-eyebrow">Equipment and technology</p>
      <h3>Forge gear and build useful systems</h3>
      <p>Start with Gear Evolution and storage, then explore the installed metalworking, Create, and Mekanism layers as recipes and progression make them available.</p>
      <a href="../gear-evolution/">Gear Evolution</a>
      <a href="../forging-and-metalworks/">Forging and Metalworks</a>
      <a href="../storage-and-logistics/">Storage and logistics</a>
    </div>
  </div>
  <div class="onboarding-path-panel path-theme-nation" id="path-nation" role="tabpanel" aria-labelledby="path-nation-tab" hidden>
    <img src="../assets/images/sovereign_rebirth_a_magical_kingdom.png" alt="A developed fantasy settlement" loading="lazy" decoding="async">
    <div>
      <p class="reference-eyebrow">Civilization progression</p>
      <h3>Turn a shelter into a sovereignty</h3>
      <p>Protect land first, then grow a MineColonies settlement. Core citizen and reputation integration is active; more volatile diplomacy and warfare features remain disabled in the beta baseline.</p>
      <a href="../minecolonies-and-nations/">MineColonies and nations</a>
      <a href="../teams-and-claims/">Teams and claims</a>
      <a href="../subordinates-and-naming/">Subordinates and naming</a>
    </div>
  </div>
</section>

## When you are stuck

<div class="stuck-grid">
  <article><span>?</span><div><h3>I do not understand a race or skill</h3><p>Use the searchable <a href="../tensura-reference/">Tensura Reference</a>. Race pages expose evolution relationships; skill pages retain official descriptions and source attribution.</p></div></article>
  <article><span>⌨</span><div><h3>A menu or ability will not open</h3><p>Open Minecraft's Controls screen, search the relevant mod or action, and resolve conflicts. Pack updates and personal bindings can make remembered defaults inaccurate.</p></div></article>
  <article><span>⌂</span><div><h3>My base is vulnerable</h3><p>Review <a href="../teams-and-claims/">Teams & Claims</a>. Claim protection is the first line of defense; report destructive interactions that bypass it.</p></div></article>
  <article><span>!</span><div><h3>I found behavior the guide says is unverified</h3><p>Check the <a href="../compatibility-matrix/">Compatibility Matrix</a> and <a href="../roadmap/">Roadmap</a>. “Installed,” “starts,” and “fully validated” are intentionally different claims.</p></div></article>
</div>

## Reliable reference points

- The [Current Modlist](current-modlist.md) is the newest captured client snapshot and names its own verification limits.
- The [Progression Overview](progression-overview.md) separates the major parallel systems.
- The [Mod Guide Directory](mod-guide-directory/index.md) routes players to system-specific guides.
- The imported Tensura and Mysticism references preserve official wiki.gg article revisions, File-page attribution, and license evidence. See [Upstream Attribution](project/upstream-attribution.md) and [Mysticism Attribution](project/mysticism-upstream-attribution.md).
- Live activity uses the public [Minecraft Server Status API](https://api.mcsrvstat.us/). It does not receive your Minecraft credentials and the page never displays the server's resolved backend address.

!!! warning "Beta truth matters"
    TSR is playable, but extended progression, multiplayer balance, structure density, permissions, and the complete handcrafted campaign are still under validation. This guide does not promote planned systems into completed features.
