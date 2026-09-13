<section class="command-reference" data-command-reference>
<header class="command-hero">
<div class="command-hero-copy">
<p class="reference-eyebrow">TSR 1.21.1 operations desk</p>
<h1>Commands by source</h1>
<p>Find the command family you need, see who may run it, and keep similarly named systems separated by the mod that actually registers them.</p>
<div class="command-hero-stats"><span><strong>7</strong> audited artifacts</span><span><strong>6</strong> installed sources</span><span><strong>50</strong> command families</span></div>
</div>
<div class="command-hero-console" aria-hidden="true"><span>TSR COMMAND CONSOLE</span><code>&gt; /stextras player summary</code><code>&gt; /tascension checkultprogress</code><code>&gt; /ability preset set</code><b>READY</b></div>
</header>

<nav class="command-source-nav" aria-label="Command sources"><a href="#tensura">Tensura: Reincarnated</a><a href="#mysticism">Tensura: Mysticism</a><a href="#ascension">Tensura: Ascension</a><a href="#stextras">SlimeThrone Extras</a><a href="#beyond">TR: Beyond Adventures</a><a href="#nightmares">Tensura Nightmares</a><a href="#boss-structure">TenSura Boss Structure</a></nav>

<aside class="command-syntax-guide">
<div><strong><code>&lt;required&gt;</code></strong><span>You must supply a value.</span></div>
<div><strong><code>[optional]</code></strong><span>The command can run without it.</span></div>
<div><strong><code>…</code></strong><span>This page documents a command family; press Tab in game for its exact next argument.</span></div>
</aside>

<div class="command-tools">
<label><span>Search all command families</span><input type="search" data-command-search-input placeholder="Try prestige, soul, ability, admin…" autocomplete="off"></label>
<div class="command-access-filters" aria-label="Filter by access"><button type="button" class="is-active" data-command-access-filter="all" aria-pressed="true">All access</button><button type="button" data-command-access-filter="player" aria-pressed="false">Player</button><button type="button" data-command-access-filter="mixed" aria-pressed="false">Mixed</button><button type="button" data-command-access-filter="moderator" aria-pressed="false">Moderator</button><button type="button" data-command-access-filter="gamemaster" aria-pressed="false">Gamemaster</button><button type="button" data-command-access-filter="owner" aria-pressed="false">Owner</button><button type="button" data-command-access-filter="admin" aria-pressed="false">Admin</button></div>
<p data-command-status aria-live="polite">Showing 50 of 50 command families</p>
</div>

<div class="command-access-legend"><div><span class="command-access command-access--player">Player</span><p>Available from ordinary player command paths.</p></div><div><span class="command-access command-access--mixed">Mixed</span><p>Contains player-facing branches and protected staff branches.</p></div><div><span class="command-access command-access--moderator">Moderator</span><p>Requires moderator-level permission for target inspection.</p></div><div><span class="command-access command-access--gamemaster">Gamemaster</span><p>Protected operator command used to modify gameplay state.</p></div><div><span class="command-access command-access--owner">Owner</span><p>Highest-permission maintenance command.</p></div><div><span class="command-access command-access--admin">Admin</span><p>Protected administrative or diagnostic command.</p></div></div>

<section class="command-source" id="tensura" data-command-source-section="tensura">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed</p><h2>Tensura: Reincarnated</h2><p>Core player controls plus moderator, gamemaster, and world-management tools.</p></div>
<div class="command-build"><strong>2.0.1.2</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>tensura-reincarnated.pw.toml</code></span><span>Digest: <code>f6f0c8ce46b7…</code></span></div>

<div class="command-entry-grid"><article class="command-entry" data-command-source="tensura" data-command-access="player" data-command-search="/ability … player manage ability presets, slots, skill toggles, skill locks, spatial movement, and spatial storage. tensura preset name|set set toggle toggle all|random lock add|remove|clear|list spatial warp|portal|storage">
<header><code>/ability …</code><span class="command-access command-access--player">Player</span></header>
<p>Manage ability presets, slots, skill toggles, skill locks, spatial movement, and spatial storage.</p>
<div class="command-branches" aria-label="Registered branches"><code>preset name|set</code><code>set</code><code>toggle</code><code>toggle all|random</code><code>lock add|remove|clear|list</code><code>spatial warp|portal|storage</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/AbilityCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="player" data-command-search="/evolve … player attempt a race evolution or eligible demon-lord or hero awakening route. tensura race demonlord hero">
<header><code>/evolve …</code><span class="command-access command-access--player">Player</span></header>
<p>Attempt a race evolution or eligible demon-lord or hero awakening route.</p>
<div class="command-branches" aria-label="Registered branches"><code>race</code><code>demonLord</code><code>hero</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/EvolveCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="player" data-command-search="/nameable player toggle whether the player can receive a name through tensura&#x27;s naming system. tensura">
<header><code>/nameable</code><span class="command-access command-access--player">Player</span></header>
<p>Toggle whether the player can receive a name through Tensura&#x27;s naming system.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/NameCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="mixed" data-command-search="/tensura get … mixed inspect ability, awakening, owner, race, spirit, and stat data. self queries are player-facing; target inspection is protected. tensura ability awakening owner race spirit stat">
<header><code>/tensura get …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Inspect ability, awakening, owner, race, spirit, and stat data. Self queries are player-facing; target inspection is protected.</p>
<div class="command-branches" aria-label="Registered branches"><code>ability</code><code>awakening</code><code>owner</code><code>race</code><code>spirit</code><code>stat</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/TensuraCommands$TensuraCommand$TensuraGetCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="gamemaster" data-command-search="/tensura edit … gamemaster edit or reset abilities, owners, races, spirits, awakening state, and existence stats. tensura ability owner race reset spirit stat">
<header><code>/tensura edit …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Edit or reset abilities, owners, races, spirits, awakening state, and existence stats.</p>
<div class="command-branches" aria-label="Registered branches"><code>ability</code><code>owner</code><code>race</code><code>reset</code><code>spirit</code><code>stat</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/TensuraCommands$TensuraCommand$TensuraEditCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="admin" data-command-search="/tensura worlddata … admin manage persistent world systems and restrictions. tensura bossfight areamagicule labyrinth trulyunique warppad worldrestriction">
<header><code>/tensura worldData …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Manage persistent world systems and restrictions.</p>
<div class="command-branches" aria-label="Registered branches"><code>bossFight</code><code>areaMagicule</code><code>labyrinth</code><code>trulyUnique</code><code>warpPad</code><code>worldRestriction</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/TensuraCommands$TensuraCommand$WorldDataCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="gamemaster" data-command-search="/engrave … gamemaster apply a selected enchantment level to held equipment for one or more entities. tensura">
<header><code>/engrave …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Apply a selected enchantment level to held equipment for one or more entities.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/EngraveCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="owner" data-command-search="/despawn … owner discard the selected entities. tensura">
<header><code>/despawn …</code><span class="command-access command-access--owner">Owner</span></header>
<p>Discard the selected entities.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/DespawnCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="tensura" data-command-access="owner" data-command-search="/syncstorage … owner force selected entity capability storage to synchronize. tensura">
<header><code>/syncStorage …</code><span class="command-access command-access--owner">Owner</span></header>
<p>Force selected entity capability storage to synchronize.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/manasmods/tensura/command/SyncCommand.class</code></details>
</article></div>
</section>
<section class="command-source" id="mysticism" data-command-source-section="mysticism">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed</p><h2>Tensura: Mysticism</h2><p>The current build registers only Soul Energy stat inspection and editing beneath the Mysticism root.</p></div>
<div class="command-build"><strong>2.1.2</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>tensura-mysticism.pw.toml</code></span><span>Digest: <code>cca1bd878b46…</code></span></div>
<p class="command-source-note">The old 1.19.2 article lists soul-quality, contract, and spirit reroll commands that are absent from the pinned 2.1.2 command classes. They are intentionally excluded.</p>
<div class="command-entry-grid"><article class="command-entry" data-command-source="mysticism" data-command-access="mixed" data-command-search="/mysticism get stat … mixed read current or maximum soul energy for yourself or an allowed target. mysticism current soulenergy max soulenergy">
<header><code>/mysticism get stat …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Read current or maximum Soul Energy for yourself or an allowed target.</p>
<div class="command-branches" aria-label="Registered branches"><code>current soulEnergy</code><code>max soulEnergy</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/get/MysticGetStatCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="mysticism" data-command-access="gamemaster" data-command-search="/mysticism edit stat … gamemaster set, add to, or reset current and maximum soul energy values. mysticism current set|add|reset max set|add">
<header><code>/mysticism edit stat …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Set, add to, or reset current and maximum Soul Energy values.</p>
<div class="command-branches" aria-label="Registered branches"><code>current set|add|reset</code><code>max set|add</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/edit/MysticEditStatCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="mysticism" data-command-access="gamemaster" data-command-search="/mysticism edit reset … gamemaster reset soul energy storage using the selected reset path. mysticism soulenergy">
<header><code>/mysticism edit reset …</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Reset Soul Energy storage using the selected reset path.</p>
<div class="command-branches" aria-label="Registered branches"><code>soulEnergy</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>io/github/Memoires/mysticism/command/edit/MysticResetCommand.class</code></details>
</article></div>
</section>
<section class="command-source" id="ascension" data-command-source-section="ascension">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed</p><h2>Tensura: Ascension</h2><p>Ultimate-evolution progress inspection and an administrative awakening-cooldown reset.</p></div>
<div class="command-build"><strong>2.1.2</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-ascension/files/8060740">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>tensura-ascensions.pw.toml</code></span><span>Digest: <code>84cbe87a6641…</code></span></div>

<div class="command-entry-grid"><article class="command-entry" data-command-source="ascension" data-command-access="mixed" data-command-search="/tascension checkultprogress &lt;ultimate&gt; [player] mixed show the tracked requirements and progress for a registered ascension ultimate skill. ascension">
<header><code>/tascension checkultprogress &lt;ultimate&gt; [player]</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Show the tracked requirements and progress for a registered Ascension ultimate skill.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/simplygray/tensuraaddon/command/AscensionCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="ascension" data-command-access="admin" data-command-search="/tascension cooldown reset &lt;targets&gt; admin clear ascension&#x27;s last-awakening cooldown data for selected players. ascension">
<header><code>/tascension cooldown reset &lt;targets&gt;</code><span class="command-access command-access--admin">Admin</span></header>
<p>Clear Ascension&#x27;s last-awakening cooldown data for selected players.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/simplygray/tensuraaddon/command/AscensionCommands.class</code></details>
</article></div>
</section>
<section class="command-source" id="stextras" data-command-source-section="stextras">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed</p><h2>SlimeThrone Extras</h2><p>Player progression, quest, prestige, schedule, wiki, and staff-diagnostic commands.</p></div>
<div class="command-build"><strong>2.1.2.1</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-slimethrone-extras/files/8313927">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>tensura-slimethrone-extras.pw.toml</code></span><span>Digest: <code>506354ffcf88…</code></span></div>

<div class="command-entry-grid"><article class="command-entry" data-command-source="stextras" data-command-access="player" data-command-search="/stextras wiki player open the slimethrone extras faq link supplied by the mod. stextras">
<header><code>/stextras wiki</code><span class="command-access command-access--player">Player</span></header>
<p>Open the SlimeThrone Extras FAQ link supplied by the mod.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/system/WikiCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras player summary [player] mixed display a compact progression summary for yourself or an allowed target. stextras">
<header><code>/stextras player summary [player]</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Display a compact progression summary for yourself or an allowed target.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/player/PlayerCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras player essence … mixed read or administratively change reincarnation essence. stextras get set add">
<header><code>/stextras player essence …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Read or administratively change Reincarnation Essence.</p>
<div class="command-branches" aria-label="Registered branches"><code>get</code><code>set</code><code>add</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/player/PlayerCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras player soulgrade … mixed read or administratively change soul grade. stextras get set add">
<header><code>/stextras player soulgrade …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Read or administratively change Soul Grade.</p>
<div class="command-branches" aria-label="Registered branches"><code>get</code><code>set</code><code>add</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/player/PlayerCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras player locked-skills … mixed list or manage the ordinary skill-lock pool. stextras list lock &lt;id&gt; unlock &lt;id&gt; clear">
<header><code>/stextras player locked-skills …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>List or manage the ordinary skill-lock pool.</p>
<div class="command-branches" aria-label="Registered branches"><code>list</code><code>lock &lt;id&gt;</code><code>unlock &lt;id&gt;</code><code>clear</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/player/PlayerCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="admin" data-command-search="/stextras player admin-locked-skills … admin manage skills locked by staff policy. stextras list lock &lt;id&gt; unlock &lt;id&gt; clear">
<header><code>/stextras player admin-locked-skills …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Manage skills locked by staff policy.</p>
<div class="command-branches" aria-label="Registered branches"><code>list</code><code>lock &lt;id&gt;</code><code>unlock &lt;id&gt;</code><code>clear</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/player/PlayerCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras quests … mixed browse quest catalogs and active progress, or run protected quest mutations. stextras catalog summary list all|active|completed manage add|remove|complete|reset repeatable cooldown reset">
<header><code>/stextras quests …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Browse quest catalogs and active progress, or run protected quest mutations.</p>
<div class="command-branches" aria-label="Registered branches"><code>catalog</code><code>summary</code><code>list all|active|completed</code><code>manage add|remove|complete|reset</code><code>repeatable cooldown reset</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/quest/QuestCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras race prestige … mixed inspect race-prestige progress or administratively mark and unmark completions. stextras races player quests &lt;id&gt; mark-complete &lt;id&gt; unmark-complete &lt;id&gt;">
<header><code>/stextras race prestige …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Inspect race-prestige progress or administratively mark and unmark completions.</p>
<div class="command-branches" aria-label="Registered branches"><code>races</code><code>player</code><code>quests &lt;id&gt;</code><code>mark-complete &lt;id&gt;</code><code>unmark-complete &lt;id&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/quest/RacePrestigeCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="admin" data-command-search="/stextras required … admin preview or apply the required-quest selection for a prestige count. stextras preview &lt;prestige&gt; apply &lt;prestige&gt; [player]">
<header><code>/stextras required …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Preview or apply the required-quest selection for a prestige count.</p>
<div class="command-branches" aria-label="Registered branches"><code>preview &lt;prestige&gt;</code><code>apply &lt;prestige&gt; [player]</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/quest/RequiredCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="mixed" data-command-search="/stextras schedule … mixed inspect daily and weekly reset timing or administer counts, master state, rolls, and player application. stextras info time daily|weekly count get|set master get|set roll daily|weekly|both apply self|all reset_progress">
<header><code>/stextras schedule …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Inspect daily and weekly reset timing or administer counts, master state, rolls, and player application.</p>
<div class="command-branches" aria-label="Registered branches"><code>info</code><code>time daily|weekly</code><code>count get|set</code><code>master get|set</code><code>roll daily|weekly|both</code><code>apply self|all</code><code>reset_progress</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/system/ScheduleCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="stextras" data-command-access="admin" data-command-search="/stextras debug … admin inspect integration state and open test utilities for staff troubleshooting. stextras open-bench check-effects soulgrade-levels check-lootr">
<header><code>/stextras debug …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Inspect integration state and open test utilities for staff troubleshooting.</p>
<div class="command-branches" aria-label="Registered branches"><code>open-bench</code><code>check-effects</code><code>soulgrade-levels</code><code>check-lootr</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>org/crypticdev/stextras/command/system/DebugCommands.class</code></details>
</article></div>
</section>
<section class="command-source" id="beyond" data-command-source-section="beyond">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed</p><h2>TR: Beyond Adventures</h2><p>Adventure-contract controls, daily reward display settings, quest-day maintenance, and a movement repair tool.</p></div>
<div class="command-build"><strong>1.1.9</strong><span>Minecraft 1.21.1</span><a href="https://modrinth.com/mod/beyond-adventures/version/Ybm5N8pk">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>beyond-adventures.pw.toml</code></span><span>Digest: <code>db5951096dce…</code></span></div>

<div class="command-entry-grid"><article class="command-entry" data-command-source="beyond" data-command-access="admin" data-command-search="/beyondadv announcecontracts enabled &lt;bool&gt; admin enable or disable contract announcements. beyond">
<header><code>/beyondadv announceContracts enabled &lt;bool&gt;</code><span class="command-access command-access--admin">Admin</span></header>
<p>Enable or disable contract announcements.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/quest/command/BeyondAdvCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="beyond" data-command-access="mixed" data-command-search="/beyondadv dailyrewardpopup enabled &lt;bool&gt; mixed control the daily reward popup preference. beyond">
<header><code>/beyondadv dailyrewardpopup enabled &lt;bool&gt;</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Control the daily reward popup preference.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/quest/command/BeyondAdvCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="beyond" data-command-access="admin" data-command-search="/beyondadv forcerecall &lt;target&gt; admin recall deployed character contracts belonging to the target player. beyond">
<header><code>/beyondadv forcerecall &lt;target&gt;</code><span class="command-access command-access--admin">Admin</span></header>
<p>Recall deployed character contracts belonging to the target player.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/quest/command/BeyondAdvCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="beyond" data-command-access="admin" data-command-search="/beyondadv quest day … admin inspect, set, or add beyond&#x27;s stored quest day. beyond get set &lt;day&gt; add &lt;days&gt;">
<header><code>/beyondadv quest day …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Inspect, set, or add Beyond&#x27;s stored quest day.</p>
<div class="command-branches" aria-label="Registered branches"><code>get</code><code>set &lt;day&gt;</code><code>add &lt;days&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/quest/command/BeyondAdvCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="beyond" data-command-access="admin" data-command-search="/beyondadv quest mxp reset admin reset the stored mxp schedule state. beyond">
<header><code>/beyondadv quest mxp reset</code><span class="command-access command-access--admin">Admin</span></header>
<p>Reset the stored MXP schedule state.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/quest/command/BeyondAdvCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="beyond" data-command-access="gamemaster" data-command-search="/charactermovementfix &lt;target&gt; gamemaster clear lingering movement-interference effects from a beyond character entity. beyond">
<header><code>/characterMovementFix &lt;target&gt;</code><span class="command-access command-access--gamemaster">Gamemaster</span></header>
<p>Clear lingering movement-interference effects from a Beyond character entity.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/trbeyond/command/GachaLingeringEffectFixCommand.class</code></details>
</article></div>
</section>
<section class="command-source" id="nightmares" data-command-source-section="nightmares">
<header class="command-source-header">
<div><p class="reference-eyebrow">Reference build · server match pending</p><h2>Tensura Nightmares</h2><p>A large command surface for souls, deals, titles, egos, faiths, families, Domiciles, stats, skill evolution, and EMC integration.</p></div>
<div class="command-build"><strong>1.0.3.2.8</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated-nightmares/files/8679382">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Digest: <code>94b37573cb24…</code></span></div>
<p class="command-source-note">This command list is verified against the named 1.21.1 reference release. The exact Nightmares jar deployed by TSR is not yet recorded in the current pack manifest, so availability on the live server must be confirmed with tab completion.</p>
<div class="command-entry-grid"><article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/trnightmare … mixed primary nightmares tree for soul inspection, controls, deal maker operations, memory tools, raphael tools, and staff utilities. nightmares elementsoul soultrait checksoul control dealcreate dealmaker info memoryseal|memoryundo raphael_name|raphaelsocial investigate pack">
<header><code>/trnightmare …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Primary Nightmares tree for soul inspection, controls, Deal Maker operations, memory tools, Raphael tools, and staff utilities.</p>
<div class="command-branches" aria-label="Registered branches"><code>elementsoul</code><code>soultrait</code><code>checksoul</code><code>control</code><code>dealcreate</code><code>dealmaker</code><code>info</code><code>memoryseal|memoryundo</code><code>raphael_name|raphaelsocial</code><code>investigate</code><code>pack</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/NightmareCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/skill … mixed inspect, confirm, or administratively force nightmares skill-evolution paths. nightmares checkevoconditions evolutionconfirm forceskillevolution">
<header><code>/skill …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Inspect, confirm, or administratively force Nightmares skill-evolution paths.</p>
<div class="command-branches" aria-label="Registered branches"><code>checkevoconditions</code><code>evolutionconfirm</code><code>forceskillevolution</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/SkillEvolutionCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/qol stats … mixed view or edit existence and minecraft statistic values through the nightmares quality-of-life tree. nightmares overview target existence list|get|set|add minecraft list|get|set">
<header><code>/qol stats …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>View or edit existence and Minecraft statistic values through the Nightmares quality-of-life tree.</p>
<div class="command-branches" aria-label="Registered branches"><code>overview</code><code>target</code><code>existence list|get|set|add</code><code>minecraft list|get|set</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/QOLCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="admin" data-command-search="/stat … admin administer nihility, spiritrons, and entity-awakening state. nightmares nihility add|set spiritrons add|set entityawakening status|enforce">
<header><code>/stat …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Administer Nihility, Spiritrons, and entity-awakening state.</p>
<div class="command-branches" aria-label="Registered branches"><code>nihility add|set</code><code>spiritrons add|set</code><code>entityawakening status|enforce</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/StatCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/title … mixed list, activate, or clear owned titles; staff branches grant, create, and remove titles. nightmares list activate &lt;id&gt; clear admin grant|create|remove">
<header><code>/title …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>List, activate, or clear owned titles; staff branches grant, create, and remove titles.</p>
<div class="command-branches" aria-label="Registered branches"><code>list</code><code>activate &lt;id&gt;</code><code>clear</code><code>admin grant|create|remove</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/TitleCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/ego … mixed spawn, rename, inspect, mute, edit, or administer ego and manas state. nightmares spawn respawn rename stat mute name edit clear-all admin">
<header><code>/ego …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Spawn, rename, inspect, mute, edit, or administer ego and Manas state.</p>
<div class="command-branches" aria-label="Registered branches"><code>spawn</code><code>respawn</code><code>rename</code><code>stat</code><code>mute</code><code>name</code><code>edit</code><code>clear-all</code><code>admin</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/EgoCommands.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/faith … mixed create, join, list, inspect, or administer nightmares faith organizations. nightmares list join create faithful name admin">
<header><code>/faith …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Create, join, list, inspect, or administer Nightmares faith organizations.</p>
<div class="command-branches" aria-label="Registered branches"><code>list</code><code>join</code><code>create</code><code>faithful name</code><code>admin</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/FaithCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="player" data-command-search="/family … player create a family, invite players, accept invitations, and list members. nightmares create &lt;name&gt; invite &lt;player&gt; accept list">
<header><code>/family …</code><span class="command-access command-access--player">Player</span></header>
<p>Create a family, invite players, accept invitations, and list members.</p>
<div class="command-branches" aria-label="Registered branches"><code>create &lt;name&gt;</code><code>invite &lt;player&gt;</code><code>accept</code><code>list</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/FamilyCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="admin" data-command-search="/dragonrelation … admin read, add, or set a player&#x27;s relationship score for a named true dragon. nightmares get add &lt;amount&gt; set &lt;amount&gt;">
<header><code>/dragonrelation …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Read, add, or set a player&#x27;s relationship score for a named True Dragon.</p>
<div class="command-branches" aria-label="Registered branches"><code>get</code><code>add &lt;amount&gt;</code><code>set &lt;amount&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DragonRelationCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="player" data-command-search="/dragonname … player attempt a true dragon surname action when its relationship and resource requirements are satisfied. nightmares &lt;dragon&gt; surname &lt;name&gt;">
<header><code>/dragonname …</code><span class="command-access command-access--player">Player</span></header>
<p>Attempt a True Dragon surname action when its relationship and resource requirements are satisfied.</p>
<div class="command-branches" aria-label="Registered branches"><code>&lt;dragon&gt; surname &lt;name&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DragonNameCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/awaken … mixed check awakening progress or force an allowed awakening type through the protected branch. nightmares check awakening &lt;type&gt;">
<header><code>/awaken …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Check awakening progress or force an allowed awakening type through the protected branch.</p>
<div class="command-branches" aria-label="Registered branches"><code>check</code><code>awakening &lt;type&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/AwakeningCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="player" data-command-search="/truedragonnucleation … player use azathoth&#x27;s true dragon nucleation operation for an eligible named dragon. nightmares sacrifice &lt;dragon&gt;">
<header><code>/TrueDragonNucleation …</code><span class="command-access command-access--player">Player</span></header>
<p>Use Azathoth&#x27;s True Dragon Nucleation operation for an eligible named dragon.</p>
<div class="command-branches" aria-label="Registered branches"><code>sacrifice &lt;dragon&gt;</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/AzathothCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/domicile … mixed manage domicile access, kicking, locking, safety, and allow/block lists. nightmares whitelist add|remove|list blacklist add|remove|list kick lock togglesafety">
<header><code>/domicile …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Manage Domicile access, kicking, locking, safety, and allow/block lists.</p>
<div class="command-branches" aria-label="Registered branches"><code>whitelist add|remove|list</code><code>blacklist add|remove|list</code><code>kick</code><code>lock</code><code>togglesafety</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DomicileCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/domicilestore … mixed manage the corresponding domicile store access controls. nightmares whitelist blacklist kick lock togglesafety">
<header><code>/domicilestore …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Manage the corresponding Domicile store access controls.</p>
<div class="command-branches" aria-label="Registered branches"><code>whitelist</code><code>blacklist</code><code>kick</code><code>lock</code><code>togglesafety</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DomicileCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="admin" data-command-search="/resetdomicile … admin reset selected domicile regions or generated components. nightmares base shop canino">
<header><code>/resetdomicile …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Reset selected Domicile regions or generated components.</p>
<div class="command-branches" aria-label="Registered branches"><code>base</code><code>shop</code><code>canino</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DomicileCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="player" data-command-search="/setselfname &lt;name&gt; player set the preferred self-name used by compatible nightmares systems. nightmares">
<header><code>/setSelfName &lt;name&gt;</code><span class="command-access command-access--player">Player</span></header>
<p>Set the preferred self-name used by compatible Nightmares systems.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/SelfNameCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/deal … mixed inspect, confirm, end, claim, or administer soul deals and their inventories. nightmares &lt;uuid&gt; confirm end souldeal soulinventory soulvomit acceptdealfor forcedealbreak stealsoul">
<header><code>/deal …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Inspect, confirm, end, claim, or administer soul deals and their inventories.</p>
<div class="command-branches" aria-label="Registered branches"><code>&lt;uuid&gt;</code><code>confirm</code><code>end</code><code>souldeal</code><code>soulinventory</code><code>soulvomit</code><code>acceptdealfor</code><code>forcedealbreak</code><code>stealsoul</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/main/command/DealCommand.class</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="mixed" data-command-search="/emc · /knowledge · /showbag … mixed nightmares&#x27; packaged emc, knowledge, and alchemical bag command integration. nightmares emc add|remove|set|get|test knowledge learn|unlearn|test|clear showbag">
<header><code>/emc · /knowledge · /showbag …</code><span class="command-access command-access--mixed">Mixed</span></header>
<p>Nightmares&#x27; packaged EMC, knowledge, and Alchemical Bag command integration.</p>
<div class="command-branches" aria-label="Registered branches"><code>emc add|remove|set|get|test</code><code>knowledge learn|unlearn|test|clear</code><code>showbag</code></div>
<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/emc/pe/network/commands/</code></details>
</article>
<article class="command-entry" data-command-source="nightmares" data-command-access="admin" data-command-search="/setemc · /removeemc · /resetemc · /dumpmissingemc … admin protected emc value maintenance and missing-value diagnostics. nightmares">
<header><code>/setemc · /removeemc · /resetemc · /dumpmissingemc …</code><span class="command-access command-access--admin">Admin</span></header>
<p>Protected EMC value maintenance and missing-value diagnostics.</p>

<details class="command-evidence"><summary>Artifact evidence</summary><code>com/github/hvnbael/trnightmare/emc/pe/network/commands/</code></details>
</article></div>
</section>
<section class="command-source" id="boss-structure" data-command-source-section="boss-structure">
<header class="command-source-header">
<div><p class="reference-eyebrow">Installed · no command classes</p><h2>TenSura Boss Structure</h2><p>The pinned artifact adds structures and encounters but registers no command classes.</p></div>
<div class="command-build"><strong>1.0.3.3</strong><span>Minecraft 1.21.1</span><a href="https://www.curseforge.com/minecraft/mc-mods/tensura-boss-structure/files/8614357">Release source ↗</a></div>
</header>
<div class="command-source-meta"><span>Pack record: <code>tensura-boss-structure.pw.toml</code></span><span>Digest: <code>14f670015944…</code></span></div>

<div class="command-entry-grid"><div class="command-empty-source">No command classes are registered by this artifact.</div></div>
</section>

<div class="command-no-results" data-command-no-results hidden><strong>No matching command family</strong><span>Clear the search or switch back to All access.</span></div>

<aside class="command-verification-note">
<strong>What “verified” means here</strong>
<p>Names, roots, branches, and permission tiers come from the exact 1.21.1 artifacts recorded above. Runtime configuration can still disable a branch or change who receives permission. Nightmares is clearly marked separately because its reference jar is not yet matched to TSR's current pack manifest.</p>
</aside>

<details class="command-archive-note"><summary>Historical imported command pages</summary><p>The raw <a href="commands/">Tensura import</a> and <a href="../../mysticism-reference/commands/commands/">Mysticism 1.19.2 import</a> remain available for provenance. They are not the current command reference and may contain obsolete syntax.</p></details>
</section>
