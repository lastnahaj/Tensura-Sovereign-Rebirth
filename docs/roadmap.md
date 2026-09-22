# Version 1 Beta Roadmap

<section class="roadmap-iteration">
<div>
<p class="reference-eyebrow">CURRENT ITERATION</p>
<h2>299-artifact client candidate</h2>
<p>The September 20 inventory is now the public working roster. It includes Nightmares and the expanded adventure, world, interface, and integration layers, but the full candidate still requires clean client and dedicated-server validation.</p>
</div>
<dl>
<div><dt>Target</dt><dd>Minecraft 1.21.1</dd></div>
<div><dt>Loader</dt><dd>NeoForge</dd></div>
<div><dt>Last full client smoke</dt><dd>239 mods</dd></div>
<div><dt>Current release state</dt><dd>Under validation</dd></div>
</dl>
</section>

!!! danger "Removed systems are not roadmap targets"
    TensuraMorph, ReMorphed, Tensura Guild, and Woodwalkers are removed from the current iteration. Their historical documentation does not make their mechanics available in the pack. See the [Current Modlist](current-modlist.md#what-changed-in-this-iteration) for the complete snapshot delta.

| Area | Status | Evidence / next gate |
|---|---|---|
| v0.1 design authority | Verified | Project identity, progression ownership, storage architecture, and frozen manifest retained |
| NeoForge runtime foundation | Verified | Minecraft 1.21.1, NeoForge 21.1.248, Java 21; clean server world and restart recorded |
| Core Tensura progression | Verified startup/configuration | Phase 2 cold starts, client resource load, and configuration reconstruction recorded |
| Current 299-artifact candidate | Under Validation | Inventory captured September 20; clean client, dedicated-server, restart, registry, and representative gameplay passes remain |
| Tensura Nightmares | Documented candidate | Exact 1.21.1 artifact is present; skill, race, boss, item, and world coverage is being kept version-gated to artifact and upstream evidence |
| Ascension and Elite Tensura | Documented candidate | Exact candidate artifacts are present; acquisition paths, evolution rules, bosses, and cross-mod behavior still require runtime confirmation where artifact evidence is insufficient |
| TR Addon 2.0.1 | Blocked | ManasCore custom-registry construction race; newer official artifact required |
| Unique Monsters compatibility | Deferred-blocked | Official 1.0.2 artifact can race ManasCore skill-registry construction; no diagnostic bridge is active or distributed |
| MineColonies and integrated magic | Verified startup; gameplay Under Validation | Client construction flow and server startup pass; long-running citizen/settlement play remains |
| Gear, forging, backpacks, storage | Verified startup; gameplay Under Validation | Phase 4A client/server/configuration passes; evolution retention and multiplayer contention remain |
| Upstream Tensura reference | Implemented | 988 articles discovered, 975 relevant pages imported, 13 non-content pages skipped, 0 page failures |
| Mysticism reference | Implemented; curation ongoing | 377 articles discovered, 365 relevant pages imported, 12 non-content pages skipped, 0 page failures; 1.21.1 artifact filtering and unified navigation review continue |
| Nightmares reference | In progress | Reviewed 1.21.1 skills and world content are merged into normal sections; remaining content needs the same evidence and presentation pass |
| Sources and attribution | Implemented; review queue active | Public ledger, revision attribution, and media provenance are linked; the September 22 live audit found 0 invalid mod URLs and 165 newer upstream article revisions awaiting review |
| Upstream media | Implemented | File-page CC BY-SA declaration verified; media imported with per-file exception checks and attribution records |
| Terratonic terrain | Playable startup verified; gameplay Under Validation | Terralith, Tectonic, and required libraries are active; extended exploration and density profiling remain |
| Adventure, bosses, dimensions | Playable startup verified; gameplay Under Validation | Selected targets construct in the assembled runtime; extended progression and encounter testing remain |
| Curated structures | Planned / Under Validation | One-at-a-time density, collision, restart, and generation profiling required |
| FancyMenu and Drippy branding | Playable verified | Supplied TSR artwork is active for menu and early loading presentation; graphical main-menu smoke passed |
| Decoration layer | Playable startup verified; gameplay Under Validation | Frozen selection is active in the assembled profile; recipe and multiplayer building tests remain |
| FTB teams, claims, permissions, audit | Playable startup verified; gameplay Under Validation | Quest loading passes; non-OP behavior and Tensura protection checks remain |
| Client QoL and optimization | Playable startup verified; gameplay Under Validation | Full graphical main-menu smoke passed; representative long-session rendering profiles remain |
| CurseForge export | Private beta ready | Native launcher manifest and overrides validate; tester-machine launcher import remains |
| Modrinth export | Private beta only / publication blocked | Local `.mrpack` format validates; public publication still needs allowed-domain sources or redistribution permission for embedded third-party files |
| Quest capability audit | Initial implementation verified | Eight onboarding quests, custom background, rewards, dependencies, and wiki link load on server |
| Handcrafted campaign | In progress | Playable 8-quest first-steps chapter is complete; the planned 8 Acts / 32 Chapters / approximately 512 quests are not complete |
| Multiplayer validation | Planned | Progression ownership, persistence, claims, storage contention, and restart matrix |
| Release candidate | Planned | Freeze the 299-artifact roster or record removals, then complete fresh client/server installs, gameplay smoke matrix, exports, performance, and documentation review |

## Completion rule

Nothing moves to **Verified** because it is discussed, staged, or present in a manifest. The required subsystem test and its evidence must exist in the repository's phase reports or release-candidate validation record.

## Iteration maintenance rule

Every roster change must update the searchable modlist, the removal record, relevant source links, compatibility status, and this roadmap in the same documentation cycle. A removed mod must disappear from current-player guidance; historical pages may remain only when their retired status is unmistakable.
