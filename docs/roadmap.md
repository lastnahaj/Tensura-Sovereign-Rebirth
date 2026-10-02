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
| Upstream media | Permission review in progress | The importer requires file-specific image licensing and expanded notice checks. One hundred and twenty-eight images were withdrawn or omitted after review; original illustrations replace relevant content media. Legacy footer-derived decisions are not permission verification |
| Skill artwork | Implemented; visual and permission review ongoing | The 575-entry ability catalogue includes 121 school-classified spells, 23 core Battlewill techniques, and 42 core player resistance entries. Reincarnation and Summon Hound Dog are included with original illustrations and checked acquisition/safety notes. Command-only Holy Attack Nullification and Magic Nullification remain reference-only. Legacy media permission review continues |
| Magic learning | Artifact/configuration checked; spell-specific review ongoing | Aspectual, Spiritual, and Summoning filters follow the registry types. The learning guide separates stored-spell tomes, random aspectual tomes, casting costs, and mastery; generic tome support is not treated as proof of every spell's acquisition route |
| Blocks reference | Presentation and targeted artifact checks complete; broader audit ongoing | The 36-entry directory includes Spellbinding Table with original artwork, checked crafting, mining, light, menu capacity, and binding/copying rules. Its legacy address remains available. Ice Ore has checked mining, loot, and Ice Spikes generation details; Magic Engine distinguishes area Magicules from player MP. Live-server behavior remains untested |
| Consumable references | Targeted artifact review complete; broader audit ongoing | Revival Elixir and Cattledeer Milk have original illustrations and checked behavior limits. Their survival supply routes remain unverified. Five unsupported source names are excluded from current item cards while their archived URLs remain available |
| Healing-potion guide | Artifact recipes and effects checked; server gameplay untested | An interactive brewing selector covers four Low, High, and Full Potion combinations. Original artwork, bottle preparation, fixed MP recovery, percentage healing, and the pinned stack limit of 16 are documented |
| Magic Bottle references | Artifact recipes and behavior checked; server gameplay untested | Empty, filled, and vacuumed bottles appear under Items while retaining existing addresses. Source-only filling, cooking times, filled-bottle stacks of 16, and fixed 10 MP recovery from vacuumed water are documented with original illustrations |
| Magic Crystal references | Artifact recipes, loot predicates, and configuration checked; server gameplay untested | Low, Medium, and High crystals appear under Items with original illustrations and a comparison guide. Absorption, bottle yields, same-tier storage, schematic-gated downgrades, and shared-loot exclusions are documented |
| Magic materials | Artifact recipes, loot, and configuration checked; server gameplay untested | Magic Stone and Ore Shard appear under Items with original illustrations. Stone output and schematic requirements, Netherite-tier mining, Silk Touch, Fortune, refining controls, and the configured Metal Slime consumption gate are documented |
| Casting staves | Artifact recipes, constructors, and schematic routes checked; live casting untested | Low Magic Staff and its schematic appear under Items with original artwork. The tier guide compares capacities, cooldowns, durability, and Magic Capacity modifiers. Master Magic Trainer trades, matching Magisteel advancement rewards, and one-copy learning are documented. Caster tutorial thumbnails use the original staff illustration; final merchant prices and prestige retention remain untested |
| Casting walkthrough | Artifact and configuration checked; live casting untested | Binding eligibility, slot checks, modifier-and-scroll spell selection, mode changes, seven unlearned-casting exclusions, and Aura/Magicule versus chant inputs are documented. Stored gear EP is distinguished from ordinary durability; reset and prestige retention remain unverified |
| Tome references | Artifact learning, copying, and chest loot checked; live gameplay untested | Magic Tome and Unbound Tome appear under Items with original artwork. Five Wizard Tower loot definitions, stored versus random learning, failure consumption, cooldowns, single-item table capacity, rarity, stacks, and copying exclusions are documented. Spell-specific supply and add-on retention remain unverified |
| Grimoire references | Base constructors, loot, and evolution chain checked; add-on and gameplay validation pending | Five tier articles and a comparison guide distinguish base slots, item cooldowns, Chant Speed attributes, ordinary durability, gear EP, and casting fuel. The base A-to-Special-A threshold is 80,000 EP; current add-on thresholds and component retention remain unverified. Reviewed source icons are replaced with an original equipment-class illustration |
| Hipokute farming | Artifact growth, harvest, loot, and trade definitions checked; live yields untested | Grass, Flower, and Seeds have distinct original botanical illustrations. The 1.21.1 guide separates the growth-speed gate, Magicule-dependent seed outcome, 50/50 sprout branches, picking, seed returns, and brewing. A conditional probability comparison and harvest panels are available; live timers and merchant offers remain unverified |
| Smithing Bench | Base recipe inventory, menu gates, and consumption checked; live crafting untested | An expandable browser covers 298 packaged recipes and 33 schematic IDs. The workstation crafting arrangement, player-inventory inputs, all-schematic learning gate, and survival consumption are documented with original artwork. Server recipe overrides, blueprint supply for the full catalogue, and multiplayer crafting remain unverified |
| Kiln processing | Base recipes, tier capacities, and boost logic checked; live processing untested | Three upgrade tiers, 272 melting definitions, 14 mixing definitions, and six molten kinds are documented with original artwork and searchable recipes. Zero-default recycling quantities are explicit. Server recipe overrides, automation, processing throughput, and upgrade retention remain unverified |
| Chilled materials | Crafting, cooking, food, loot predicates, and block behavior checked; live gameplay untested | Item and block guides have distinct original artwork. Ten conversion recipes, 36 custom refining definitions, cold-variant initialization, movement multipliers, and walkable-entity exceptions are recorded. Live drop counts, freezing damage, refining access, and piston interactions remain unverified |
| Battlewill learning | Artifact/configuration checked | The manual guide lists 16 configured random results and six verified mastery-triggered successors. Five Petals Thrust's player acquisition route remains unverified; the manual item is excluded from ability cards and progression nodes |
| Race artwork | Implemented; visual review ongoing | Family cards use curated source portraits or original illustrations; Beetle, Mantis, and Scorpion have distinct portraits with reviewed source records and checksum checks. Illustrations are not presented as in-game models |
| Metal Slime evolution | Artifact/configuration checked; server gameplay untested | The family card and race article explain the 100-shard consumption gate, link the material and ability references, and distinguish item-use statistics from inventory holdings. Family-card details use full-width text with improved light-mode contrast. Add-on and prestige-reset interactions remain unverified |
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
