---
title: Sources & Attribution
description: The public source ledger for TSR wiki facts, adapted articles, media, version checks, and external references.
---

<section class="source-ledger-hero">
<div>
<p class="reference-eyebrow">PUBLIC SOURCE LEDGER</p>
<h1>Know where every layer comes from</h1>
<p>TSR separates adapted wiki material, artifact-verified facts, official documentation, and inherited outbound links. A source can explain upstream behavior without proving that the same feature is active in the current server build.</p>
<div class="source-ledger-stats">
<span><strong>3</strong> revision-tracked wiki collections</span>
<span><strong>1.21.1</strong> runtime boundary</span>
<span><strong>Per-file</strong> media review</span>
</div>
</div>
<aside class="source-ledger-key" aria-label="Source evidence key">
<span>Evidence key</span>
<div><i class="source-dot source-dot--adapted"></i><b>Adapted</b><small>Text or media reused with attribution</small></div>
<div><i class="source-dot source-dot--verified"></i><b>Verified</b><small>Checked against an exact artifact or config</small></div>
<div><i class="source-dot source-dot--reference"></i><b>Reference</b><small>Consulted without wholesale copying</small></div>
</aside>
</section>

!!! info "Live source audit · September 22, 2026"
    All **299** current mod project URLs resolved with no invalid source records. The stored Tensura and Mysticism records also passed local provenance checks with no missing upstream pages or media. The live wikis have **165 newer article revisions** than the September 5 import snapshot (155 Tensura, 10 Mysticism); those changes are queued for review rather than silently replacing the revision-pinned local copy. The [complete audit report](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/live-source-audit-2026-09-22.json) records every changed revision.

## What counts as proof?

<div class="source-principles">
<article><span>01</span><h3>Installed evidence wins</h3><p>Exact JARs, registries, recipes, configuration, and recorded runtime tests decide what TSR can claim is available.</p></article>
<article><span>02</span><h3>Versions stay attached</h3><p>An upstream page can describe another release. Its information is not promoted into the 1.21.1 guide until the matching behavior is confirmed.</p></article>
<article><span>03</span><h3>Reuse is explicit</h3><p>Adapted text and media retain source links, revision records, license evidence, and required attribution. Research-only sources are labeled separately.</p></article>
</div>

## Adapted reference collections

These collections contribute adapted material to the public wiki. Individual generated articles link to the exact source article and revision used.

<div class="source-collection-grid">
<article>
<header><span class="source-status source-status--adapted">Adapted · CC BY-SA 4.0</span><h3>Tensura: Reincarnated Wiki</h3></header>
<p>The base reference for races, skills, magic, mobs, equipment, structures, commands, and mechanics.</p>
<footer><a href="https://tensura.wiki.gg/">Open source wiki</a><a href="../upstream-attribution/">Attribution record</a><a href="../ingestion-coverage/">Coverage audit</a></footer>
</article>
<article>
<header><span class="source-status source-status--adapted">Adapted · CC BY-SA 4.0</span><h3>Tensura Reincarnated: Mysticism Wiki</h3></header>
<p>The upstream Mysticism reference, version-filtered and merged into TSR's unified race and ability navigation.</p>
<footer><a href="https://trmysticism.wiki.gg/">Open source wiki</a><a href="../mysticism-upstream-attribution/">Attribution record</a><a href="../mysticism-ingestion-coverage/">Coverage audit</a></footer>
</article>
<article>
<header><span class="source-status source-status--adapted">Adapted · CC BY-SA 4.0</span><h3>Tensura Reincarnated Nightmares Wiki</h3></header>
<p>Selected 1.21.1 skills, resistances, bosses, and world references. Every adapted entry records its reviewed revision and matching release evidence.</p>
<footer><a href="https://tensuranightmares.wiki.gg/">Open source wiki</a><a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_skill_reference.json">Skill evidence</a><a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_world_reference.json">World evidence</a></footer>
</article>
</div>

!!! note "Ascension content"
    Ascension facts are checked against the selected 1.21.1 artifact and the [official Ascension project page](https://www.curseforge.com/minecraft/mc-mods/tensura-ascensions). Runtime claims remain limited to evidence that can be reproduced from the public project records and the exact candidate artifact.

## First-party guides used for verification

These sources explain their own projects. TSR uses them for fact-checking and routes players to them where a local guide would otherwise duplicate maintained documentation. Unless a page explicitly says that material was adapted, these are **references rather than copied content**.

<div class="source-directory-grid">
<article><span>Tensura progression</span><h3>SlimeThrone Extras</h3><p>Prestige, Soul Grade, racial requirements, quests, and Reincarnation Essence.</p><a href="https://slimethrone.net/help/topics/slimethrone-extras-faq/">Official help center →</a></article>
<article><span>Tensura systems</span><h3>Elite Tensura</h3><p>Skills, acquisition paths, Saiyan races, bosses, nations, titles, and commands. The site currently documents a newer release than TSR's candidate artifact, so every fact remains version-gated.</p><a href="https://elitetensura.com/">Maintainer wiki →</a></article>
<article><span>Character reference</span><h3>Tensura core</h3><p>Current public documentation for the central mod and its supported mechanics.</p><a href="https://tensura.wiki.gg/">Official community wiki →</a></article>
<article><span>Addon reference</span><h3>Mysticism & Nightmares</h3><p>Dedicated upstream collections for both installed content families.</p><a href="https://trmysticism.wiki.gg/">Mysticism →</a><a href="https://tensuranightmares.wiki.gg/">Nightmares →</a></article>
</div>

<details class="source-ledger-details">
<summary>World, adventure, and boss documentation</summary>

| Project | Maintainer or official source | TSR use |
|---|---|---|
| The Aether | [Aether Wiki](https://aether.wiki.gg/) | Dimension, progression, mobs, structures, and items |
| Eternal Starlight | [Maintainer wiki repository](https://github.com/LeoMinecraftModding/eternal-starlight-wiki) | Dimension progression, entities, items, and world content |
| Deeper and Darker | [Maintainer wiki](https://github.com/KyaniteMods/DeeperAndDarker/wiki) | Otherside progression and content reference |
| L_Ender's Cataclysm | [Official wiki](https://lendercataclysm.wiki.gg/) | Boss, structure, and reward verification |
| Ice and Fire: Community Edition | [Maintainer documentation](https://docs.iafenvoy.com/docs/mod/ice-and-fire-ce/) | 1.21.1 creature and equipment reference |
| Terralith | [Stardust Labs](https://www.stardustlabs.net/terralith) | Terrain and biome context |
| Repurposed Structures | [Maintainer wiki](https://github.com/TelepathicGrunt/RepurposedStructures/wiki) | Structure variants and configuration |
| When Dungeons Arise, Bosses' Rise, Legendary Monsters, and Mowzie's Mobs | Their official distribution pages and exact installed artifacts | Encounter presence and version checks; third-party guide sites are not authoritative |

</details>

<details class="source-ledger-details">
<summary>Building, technology, equipment, and utility documentation</summary>

| Project | Maintainer or official source | TSR use |
|---|---|---|
| Create | [Create Wiki](https://wiki.createmod.net/) | Core machines, logistics, and Ponder-supported systems |
| Mekanism | [Mekanism Wiki](https://wiki.aidancbrady.com/wiki/Home) | Machines, power, processing, and generators |
| MineColonies | [MineColonies Wiki](https://minecolonies.com/wiki/) | Colony buildings, workers, research, and administration |
| Iron's Spells 'n Spellbooks | [Iron's Spells Wiki](https://iron.wiki/) | Spell schools, equipment, mobs, and structures |
| Silent Gear | [Maintainer wiki](https://github.com/SilentChaos512/Silent-Gear/wiki) | Material and gear construction reference |
| Farmer's Delight | [Maintainer wiki](https://github.com/vectorwing/FarmersDelight/wiki) | Cooking and food systems |
| Supplementaries | [Maintainer wiki](https://github.com/MehVahdJukaar/Supplementaries/wiki) | Building blocks and utility mechanics |
| Quark | [Official feature site](https://quarkmod.net/) | Enabled feature reference |
| Waystones | [Maintainer documentation](https://mods.twelveiterations.com/minecraft/waystones) | Travel behavior and configuration |
| Bountiful | [Maintainer documentation](https://kambrik.ejekta.io/mods/bountiful/) | Bounty boards and objectives |
| EMI | [Maintainer wiki](https://github.com/emilyploszaj/emi/wiki/) | Recipe-viewer behavior and pack customization |
| Iron Furnaces | [Maintainer wiki](https://github.com/Qelifern/IronFurnaces/wiki) | Furnace tiers and upgrades; older pages require artifact checks |
| Small Ships | [Maintainer wiki](https://github.com/talhanation/wiki/wiki/Small-Ships-Wiki) | Vessel controls and content; version-sensitive |

</details>

<details class="source-ledger-details">
<summary>Inherited outbound references</summary>

Some adapted articles already contained links to other knowledge bases or media. TSR preserves useful outbound links while keeping them distinct from material adapted into this site.

| Destination | Why it may appear | Reuse status |
|---|---|---|
| [Minecraft Wiki](https://minecraft.wiki/) | Vanilla items, entities, mechanics, and terminology | External reference only |
| [Tensura: Reincarnated community references](https://tensurareincarnated.wiki.gg/) | Links inherited from Mysticism articles | External reference only; not a TSR adaptation source |
| [Minecraft Fandom archive](https://minecraft.fandom.com/wiki/Minecraft_Wiki) and other Fandom pages | Older links retained by an upstream article | External reference only; replaced with a primary source when practical |
| [YouTube](https://www.youtube.com/) | Tutorials or demonstrations linked by an upstream page | External media; the creator retains ownership |
| [CurseForge](https://www.curseforge.com/minecraft) and [Modrinth](https://modrinth.com/mods) | Project ownership, files, dependencies, loaders, and release notes | Distribution metadata and version evidence |
| [GitHub](https://github.com/) | Maintainer documentation, releases, issues, or source repositories | First-party technical reference where the linked repository is maintained by the project team |

</details>

## Distribution pages and installed artifacts

Official CurseForge and Modrinth project pages are used to identify authorship, supported Minecraft versions, loaders, dependencies, release files, and changelogs. They do not by themselves prove that a candidate mod has passed TSR's runtime gates. The [Current Modlist](../current-modlist.md), [September 20 inventory record](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/client-mod-inventory-2026-09-20.json), [Mod Manifest](../mod-manifest.md), and [Compatibility Matrix](../compatibility-matrix.md) record those separate decisions.

The strongest verification layer is local and reproducible:

- exact JAR filename and version metadata;
- registries, recipes, tags, language entries, and packaged resources;
- tracked TSR configuration and datapacks;
- client and dedicated-server startup records;
- targeted gameplay or integration tests where a startup test is insufficient.

## Media and image attribution

Imported media is accepted only when its source File page supplies reusable license evidence and no restrictive exception applies. The source URL, File page, revision, license evidence, local path, and associated articles are retained in the repository's media records. Files marked non-free, fair use, or otherwise incompatible are excluded.

The machine-readable records are available in the public repository: [Tensura media provenance](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/upstream_tensura_media.json) and [Mysticism media provenance](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/upstream_mysticism_media.json). These records are the detailed source-of-truth behind the human-readable ledger.

TSR-created branding, diagrams, icons, and concept artwork are identified as project assets. A visual inspired by a game system is not presented as an upstream screenshot or official franchise artwork. Links inherited from an adapted article—including Minecraft Wiki, Fandom, YouTube, or another mod wiki—remain outbound references and do not mean TSR copied material from those destinations.

## Reporting a source problem

If a page has a missing credit, wrong version, dead link, or claim that does not match the 1.21.1 runtime, open a [GitHub issue](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/issues). Include the TSR page, the disputed statement or asset, and the best primary source available.

This ledger documents provenance; it does not transfer ownership of Minecraft, Tensura, any mod, or any upstream artwork to TSR.
