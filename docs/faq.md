# FAQ

## What is TSR?

**Tensura: Sovereign Rebirth** is a Minecraft RPG/civilization modpack that connects Tensura character progression, evolving equipment, guilds, subordinates, settlement building, bosses, dimensions, prestige, and awakening into one curated progression model.

## What is Tensura: Reincarnated?

It is the base mod that provides TSR's reincarnation, races, EP, Magicules, Aura, abilities, mobs, world content, and core progression. Browse the local [Tensura Reference](tensura-reference/index.md) for the maintained article library.

## Which Minecraft, loader, and Java versions are required?

TSR targets **Minecraft 1.21.1**, **NeoForge 21.1.248**, and **Java 21**. Historical upstream articles may describe older releases but do not change TSR's target.

## Why NeoForge? Can I use Fabric?

The frozen mod set and its compatibility stack target NeoForge. TSR is not a Fabric pack, and no compatible Fabric distribution is maintained.

## What does Version 1 Beta mean?

It means the pack is in staged assembly and validation. Core Tensura, civilization/magic, gear, forging, backpacks, storage, and terminal systems have recorded runtime passes. Later world, multiplayer, client, performance, export, campaign, and release-candidate gates remain incomplete.

## Is Apotheosis included?

No. [Gear Evolution](gear-evolution.md) is the authoritative equipment progression system.

## Does TSR use AE2 or Refined Storage?

No. Sophisticated Storage owns physical storage, Sophisticated Backpacks owns personal storage, and Tom's is retained only for terminal and wireless access.

## Why is a Nightmare utility library present if Nightmare content is excluded?

Tensura x MineColonies requires Nightmare Utils as a dependency. The library is included only to satisfy that integration. Its autocast, trading, spawn-profile, and skill-reward systems are disabled, and its test skills are excluded from Skill Books rewards.

## How does EP work?

Use the base [Existence Points](tensura-reference/core-mechanics/existence-points.md) article for the maintained mechanics and version context. TSR does not publish guessed thresholds or unsupported external-boss values.

## What are Magicules and Aura?

They are separate base Tensura resources. See [EP, Magicule, Aura](tensura-reference/core-mechanics/ep-magicule-aura.md) and [Skills, EP & Magicules](skills-ep-and-magicules.md).

## How do races evolve?

Start with the [Race Directory](tensura-reference/races/index.md) and [Evolution Relationships](tensura-reference/races/evolution-trees.md). TSR restricts high-tier Origins races from ordinary starter pools; further gating is documented only when verified.

## How do skills work?

Browse [Intrinsic](tensura-reference/skills/intrinsic/index.md), [Common](tensura-reference/skills/common/index.md), [Extra](tensura-reference/skills/extra/index.md), [Unique](tensura-reference/skills/unique/index.md), and [Resistance](tensura-reference/resistances/index.md) directories. TSR uses Skill Books as a controlled reward layer.

## How does storage work, and why is Tom's restricted?

Sophisticated Backpacks owns personal storage; Sophisticated Storage owns physical base storage; Tom's is limited to access terminals and required linking infrastructure. The beta baseline removes 18 non-terminal recipes and bounds scan and wireless ranges. See [Storage & Logistics](storage-and-logistics.md).

## How do quests work? Is the campaign finished?

FTB Quests owns the planned eight-act handcrafted campaign, while SlimeThrone owns its separate repeatable/prestige ecosystem. The handcrafted quest files do not yet exist in tracked pack source, so the campaign is **Planned**, not implemented. See [Campaign](campaign.md).

## Is MineColonies required?

It is a major civilization branch and part of TSR's identity, but the design supports parallel character, guild, equipment, magic, boss, and exploration tracks. Final campaign requirements are not claimed before quest authoring.

## Are all bosses or test candidates guaranteed to ship?

No. Base bosses, external boss branches, and optional candidates remain distinct. Candidates must pass their compatibility, balance, performance, and world-generation gates before promotion.

## How does multiplayer progression work?

FTB Teams and Chunks own teams and claims; LuckPerms owns permissions; MineColonies owns settlements. Whether a condition is personal, team-based, settlement-based, or server-wide must be verified during quest capability and multiplayer testing.

## Why not add every structure mod?

TSR prioritizes terrain compatibility, generation reliability, density, exploration pacing, and server cost over raw structure count. See [World Generation](world-generation.md).

## What is SlimeThrone Prestige?

It is the pack's authoritative repeatable/prestige and Soul Grade layer. It remains separate from the handcrafted FTB campaign. See [Prestige & Soul Grade](prestige-and-soul-grade.md).

## Where are bugs reported?

Use the repository's [issue forms](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/issues/new/choose) and include the TSR version, environment, reproduction steps, and sanitized logs.

## Where did the base reference come from?

It is adapted from the official Tensura: Reincarnated Wiki through a revision-tracked MediaWiki API pipeline. See [Upstream Attribution](project/upstream-attribution.md) and [Ingestion Coverage](project/ingestion-coverage.md). Media without an explicit reusable File-page license is not redistributed.
