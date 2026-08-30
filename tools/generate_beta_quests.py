#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "pack" / "config" / "ftbquests" / "quests" / "chapters"
WIKI_URL = "https://lastnahaj.github.io/Tensura-Sovereign-Rebirth/"
GROUP_ID = "75A5F00000000001"


def item(item_id: str, count: int = 1) -> dict[str, object]:
    return {"type": "item", "item": item_id, "count": count}


def check(title: str) -> dict[str, object]:
    return {"type": "checkmark", "title": title}


ACTS = [
    {
        "filename": "welcome_otherworlder",
        "title": "Act 0 — Welcome, Otherworlder",
        "icon": "minecraft:nether_star",
        "background": "tsr:textures/gui/quests/act_0_welcome_otherworlder.png",
        "quests": [
            ("A New World", "Begin the guided TSR campaign and confirm that you can open and navigate the quest book.", check("Begin Sovereign Rebirth"), None),
            ("The Sovereign Archive", f"The crest above every chapter opens the TSR wiki. Use it for pack-specific guidance and the imported Tensura reference.\n\nWiki: {WIKI_URL}", check("Locate the Wiki Crest"), None),
            ("Take Control", "Review the default controls before danger finds you. Tensura skill slots use Z, X, and C; the player list remains on Tab; conflicting optional controls begin unbound.", check("Review Controls and Video Settings"), None),
            ("Travel Together", "Create or join an FTB Team before shared progression begins. Team membership controls shared quest credit and works alongside the claim system.", check("Create or Join an FTB Team"), None),
            ("Claim Your Ground", "Open the Xaero map and confirm the FTB claim overlay. Claim only the chunks your group needs so shared servers retain room to grow.", check("Create a Test Claim"), None),
            ("First Materials", "Gather enough wood for tools, storage, and a safe starting shelter.", item("minecraft:oak_log", 16), {"item": "minecraft:torch", "count": 16}),
            ("A Place to Work", "Craft a workbench. Most TSR systems branch from ordinary survival crafting, so this remains the first reliable progression checkpoint.", item("minecraft:crafting_table"), {"item": "minecraft:bread", "count": 8}),
            ("Safe Before Strong", "Place light, storage, and a respawn point. A stable base is more valuable than rushing an unknown boss or dimension.", item("minecraft:white_bed"), {"item": "minecraft:iron_ingot", "count": 4}),
        ],
    },
    {
        "filename": "reincarnated",
        "title": "Act 1 — Reincarnated",
        "icon": "minecraft:experience_bottle",
        "background": "tsr:textures/gui/quests/act_0_welcome_otherworlder.png",
        "quests": [
            ("Know Your Race", "Read your race description, innate resistances, Magicule behavior, and visible evolution requirements before choosing a long-term direction.", check("Review Your Race"), None),
            ("Name Your Power", "Open the Tensura interfaces and read every starting skill. A new ability can change combat, movement, survival, or evolution requirements.", check("Review Your Starting Skills"), None),
            ("Sustainable Life", "Secure food before pursuing EP, structures, or long-distance exploration.", item("minecraft:bread", 8), None),
            ("Tools of This World", "Build a dependable mining tool and gather stone, coal, and shelter materials.", item("minecraft:stone_pickaxe"), {"item": "minecraft:coal", "count": 8}),
            ("Magicules Need Armor", "Tensura power does not replace ordinary protection. Gather iron for armor, utility blocks, and early machines.", item("minecraft:iron_ingot", 16), None),
            ("Stand Your Ground", "Carry a shield while learning hostile mob and skill behavior. Defensive timing matters more than raw damage early on.", item("minecraft:shield"), None),
            ("Experience the World", "Earn ordinary experience while watching how EP, Magicules, resistances, and skills progress independently.", item("minecraft:experience_bottle"), None),
            ("Choose a Direction", "Select a first focus: skills and magic, equipment, guild missions, exploration, or nation building. Optional branches can be revisited later.", check("Choose Your First Specialization"), {"item": "minecraft:lapis_lazuli", "count": 8}),
        ],
    },
    {
        "filename": "paths_of_power",
        "title": "Act 2 — Paths of Power",
        "icon": "minecraft:enchanting_table",
        "background": "tsr:textures/gui/quests/act_0_welcome_otherworlder.png",
        "quests": [
            ("Consult Great Sage", "Open Great Sage and learn which information it can provide. Voice input remains disabled by default for privacy and stability.", check("Open Great Sage"), None),
            ("Record What You Learn", "Keep books available for recipes, enchantments, skill notes, and the broader magic branch.", item("minecraft:book", 4), None),
            ("An Arcane Foundation", "Build an enchanting table as the vanilla foundation beneath TSR's wider magic and equipment systems.", item("minecraft:enchanting_table"), None),
            ("A Weapon You Trust", "Prepare a dependable weapon before testing new skills. Use the combat style that supports your race and specialization.", item("minecraft:iron_sword"), None),
            ("Carry Your Journey", "Craft a Sophisticated Backpack. It is TSR's personal storage layer and can grow without replacing your base storage.", item("sophisticatedbackpacks:backpack"), None),
            ("Build Real Storage", "Craft a Sophisticated Storage chest for organized base inventory. Physical storage remains distinct from terminal access.", item("sophisticatedstorage:chest"), None),
            ("One Network, Many Chests", "Craft Tom's Storage Terminal. TSR keeps Tom's as a terminal and network-access layer rather than a second physical storage family.", item("toms_storage:storage_terminal"), None),
            ("Power With Purpose", "Review your skills, magic, gear, backpack, and storage plan together. Avoid upgrades that skip the progression path you actually want to test.", check("Confirm Your Power Build"), {"item": "minecraft:diamond", "count": 1}),
        ],
    },
    {
        "filename": "monsters_among_monsters",
        "title": "Act 3 — Monsters Among Monsters",
        "icon": "minecraft:bow",
        "background": "tsr:textures/gui/quests/act_0_welcome_otherworlder.png",
        "quests": [
            ("Answer the Guild", "Open the Tensura Guild interface and review available progression. Guild work is a guided route into combat without replacing the main campaign.", check("Review Guild Progression"), None),
            ("Find the Wilds", "Craft Nature's Compass and use it carefully. Repeated long-range searches can be expensive while the server is generating terrain.", item("naturescompass:naturescompass"), None),
            ("Mark the Road Home", "Craft or acquire a Waystone before distant expeditions. Activate routes deliberately instead of erasing exploration with unrestricted travel.", item("waystones:waystone"), None),
            ("Loot for Everyone", "Open a generated Lootr container with a teammate and confirm that each player receives a separate inventory.", check("Verify a Lootr Container"), None),
            ("Accept a Contract", "Review Beyond Adventures missions and contracts. They provide repeatable adventure work but do not replace TSR's authored campaign.", check("Review an Adventure Contract"), None),
            ("Prepare the Hunt", "Bring food, ranged options, spare equipment, and a retreat route before challenging a named or structure boss.", item("minecraft:arrow", 32), None),
            ("Challenge a Greater Foe", "Defeat one representative external boss appropriate to your current power. Record missing loot, progression dead ends, or terrain damage as beta findings.", check("Defeat a Representative Boss"), None),
            ("Return With Proof", "Store the rewards, repair equipment, and verify the world saves cleanly before beginning a new progression branch.", check("Complete the First Hunt"), {"item": "minecraft:golden_apple", "count": 1}),
        ],
    },
    {
        "filename": "birth_of_a_nation",
        "title": "Act 4 — Birth of a Nation",
        "icon": "minecolonies:blockhuttownhall",
        "background": "tsr:textures/gui/quests/act_4_birth_of_a_nation.png",
        "quests": [
            ("Choose the Heartland", "Survey flat space, nearby resources, travel routes, and claimed boundaries before placing a colony. Leave enough room for roads and future districts.", check("Choose a Colony Site"), None),
            ("The Builder's Scepter", "Craft the Structurize Build Tool used by MineColonies to preview and place schematics.", item("structurize:sceptergold"), None),
            ("Supply the First Settlers", "Prepare a Supply Camp to establish the colony's first protected foothold.", item("minecolonies:supplycampdeployer"), None),
            ("Raise the Town Hall", "Craft and place the Town Hall through the Build Tool. Confirm its preview fits inside the intended claim area before committing.", item("minecolonies:blockhuttownhall"), None),
            ("Feed a Growing People", "Build a Farmer's Delight Cooking Pot as an early communal food-production milestone.", item("farmersdelight:cooking_pot"), None),
            ("Roads, Beds, Storage", "Give citizens safe paths, housing, food, and physical storage before expanding population or defenses.", check("Stabilize Colony Logistics"), None),
            ("Borders With Meaning", "Align the colony footprint with FTB claims and team access. Test a teammate's allowed interaction without granting operator status.", check("Verify Team Colony Access"), None),
            ("From Colony to Nation", "Complete a stable first district and review Tensura x MineColonies reputation and citizen integration without enabling experimental warfare systems.", check("Establish the First District"), {"item": "minecraft:emerald", "count": 8}),
        ],
    },
    {
        "filename": "beyond_this_world",
        "title": "Act 5 — Beyond This World",
        "icon": "twilightforest:magic_map",
        "background": "tsr:textures/gui/quests/act_4_birth_of_a_nation.png",
        "quests": [
            ("Pack for Another World", "Carry food, blocks, a recovery plan, and a marked return route before crossing a dimension boundary.", item("minecraft:compass"), None),
            ("Enter the Twilight", "Construct and activate a Twilight Forest portal, then confirm the dimension loads without registry or terrain-generation errors.", check("Enter the Twilight Forest"), None),
            ("Map the Forest", "Craft a Twilight Forest Magic Map and use it to select a progression-appropriate destination.", item("twilightforest:magic_map"), None),
            ("Climb Into the Aether", "Construct an Aether portal and verify entry, return travel, and player inventory persistence.", check("Enter the Aether"), None),
            ("Secure the Crossing", "Activate a Waystone or establish another safe route near a validated dimension hub.", item("waystones:waystone"), None),
            ("Structures Worth Finding", "Explore one curated structure without assuming every container or encounter is balanced for your current race.", check("Explore a Curated Structure"), None),
            ("Chart the Unknown", "Carry an ordinary map as a record of the routes and settlements around your established portals.", item("minecraft:map"), None),
            ("Home Through the Gate", "Return to the primary base, unload safely, and confirm all visited dimensions survive a clean server restart.", check("Complete a Dimensional Round Trip"), {"item": "minecraft:ender_pearl", "count": 4}),
        ],
    },
    {
        "filename": "the_harvest_festival",
        "title": "Act 6 — The Harvest Festival",
        "icon": "minecraft:nether_star",
        "background": "tsr:textures/gui/quests/act_4_birth_of_a_nation.png",
        "quests": [
            ("Understand Awakening", "Read the current Demon Lord, Hero, soul, and awakening requirements in the TSR wiki before pursuing an irreversible progression milestone.", check("Review Awakening Requirements"), None),
            ("Fire of the Nether", "Gather Blaze Rods for brewing, Eyes of Ender, and late-game preparation.", item("minecraft:blaze_rod", 8), None),
            ("Skulls of the Withered", "Gather three Wither Skeleton Skulls and prepare a controlled arena away from claims and colony infrastructure.", item("minecraft:wither_skeleton_skull", 3), None),
            ("A Star Is Born", "Defeat the Wither and recover a Nether Star without allowing the fight to destroy another player's work.", item("minecraft:nether_star"), None),
            ("Find the Stronghold", "Prepare Eyes of Ender for the route to the End and keep replacements for losses during travel.", item("minecraft:ender_eye", 12), None),
            ("Souls Are Not Currency", "Confirm the exact soul and alignment requirements for your path. Quest rewards never sell completed awakenings or Ultimate Skills.", check("Verify Your Soul Progress"), None),
            ("Witness and Consequence", "Coordinate awakening tests with teammates so witness, reward, announcement, and protected-area behavior can be observed safely.", check("Prepare a Safe Awakening Test"), None),
            ("The Festival Begins", "Reach the appropriate awakening milestone for your chosen path and record the resulting race, skills, stats, and persistence after restart.", check("Complete an Awakening Milestone"), {"item": "minecraft:golden_apple", "count": 2}),
        ],
    },
    {
        "filename": "sovereign_rebirth",
        "title": "Act 7 — Sovereign Rebirth",
        "icon": "minecraft:beacon",
        "background": "tsr:textures/gui/quests/act_4_birth_of_a_nation.png",
        "quests": [
            ("Ascend With Intent", "Review Ascension's Ultimate awakening path, witness rules, boss mappings, and chamber access before committing rare progression resources.", check("Review Ascension Progression"), None),
            ("Gear That Remembers", "Advance a representative Gear Evolution item and verify its components, history, and progress survive logout and server restart.", check("Validate Evolving Equipment"), None),
            ("Prestige, Not Repetition", "Review SlimeThrone Extras prestige and repeatable systems. The authored campaign does not duplicate its large recurring quest pool.", check("Review Prestige Progression"), None),
            ("Measure the Soul", "Reach or evaluate the next Soul Grade threshold and confirm it agrees with your intended endgame path.", check("Review Soul Grade"), None),
            ("A Light for the Realm", "Construct a Beacon as a visible sign that the settlement has entered late-game infrastructure.", item("minecraft:beacon"), None),
            ("The End Remembered", "Recover the Dragon Egg as proof that the realm can complete vanilla's central boss progression alongside TSR's broader endgame.", item("minecraft:dragon_egg"), None),
            ("Rule Responsibly", "Verify claims, team roles, colony access, backups, and non-operator permissions before calling the realm multiplayer-ready.", check("Complete the Realm Audit"), None),
            ("Sovereign Rebirth", "Complete one full progression loop: reincarnate, evolve, build, awaken, and protect a persistent realm. Continue testing optional branches and report concrete beta findings.", check("Claim Sovereignty"), {"item": "minecraft:diamond", "count": 4}),
        ],
    },
]


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def object_id(act: int, category: int, index: int) -> str:
    return f"75A5{act:02X}{category:02X}{index:08X}"


def description_lines(text: str) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        lines.append(paragraph)
    return lines


def quest_snbt(act_index: int, quest_index: int, quest: tuple, previous_id: str | None) -> list[str]:
    title, description, task, reward = quest
    quest_id = object_id(act_index, 1, quest_index)
    task_id = object_id(act_index, 2, quest_index)
    reward_id = object_id(act_index, 3, quest_index)
    x = (quest_index - 1) * 2.75
    lines = ["\t\t{"]
    if previous_id:
        lines.append(f"\t\t\tdependencies: [{quoted(previous_id)}]")
    lines.extend(["\t\t\tdescription: ["])
    for line in description_lines(description):
        lines.append(f"\t\t\t\t{quoted(line)}")
    lines.extend([
        "\t\t\t]",
        f"\t\t\ticon: {{ id: {quoted(task.get('item', 'minecraft:book'))} }}",
        f"\t\t\tid: {quoted(quest_id)}",
    ])
    if reward:
        lines.extend([
            "\t\t\trewards: [{",
            f"\t\t\t\tcount: {reward['count']}",
            f"\t\t\t\tid: {quoted(reward_id)}",
            f"\t\t\t\titem: {{ count: 1, id: {quoted(reward['item'])} }}",
            "\t\t\t\ttype: \"item\"",
            "\t\t\t}]",
        ])
    if quest_index in (1, 8):
        lines.extend(["\t\t\tshape: \"diamond\"", "\t\t\tsize: 1.75d"])
    lines.extend([
        "\t\t\ttasks: [{",
        f"\t\t\t\tid: {quoted(task_id)}",
    ])
    if task["type"] == "item":
        lines.extend([
            f"\t\t\t\tcount: {task['count']}L",
            f"\t\t\t\titem: {{ count: 1, id: {quoted(task['item'])} }}",
            "\t\t\t\ttype: \"item\"",
        ])
    else:
        lines.extend([
            f"\t\t\t\ttitle: {quoted(task['title'])}",
            "\t\t\t\ttype: \"checkmark\"",
        ])
    lines.extend([
        "\t\t\t}]",
        f"\t\t\ttitle: {quoted(title)}",
        f"\t\t\tx: {x:.2f}d",
        "\t\t\ty: -0.5d",
        "\t\t}",
    ])
    return lines


def chapter_snbt(act_index: int, act: dict[str, object]) -> str:
    chapter_id = object_id(act_index, 0, 1)
    first_id = object_id(act_index, 1, 1)
    previous_id = object_id(act_index - 1, 1, 8) if act_index else None
    lines = [
        "{",
        f"\tautofocus_id: {quoted(first_id)}",
        "\tdefault_hide_dependency_lines: false",
        "\tdefault_min_width: 260",
        "\tdefault_quest_shape: \"circle\"",
        f"\tfilename: {quoted(act['filename'])}",
        "\tgroup: \"\"",
        f"\ticon: {{ id: {quoted(act['icon'])} }}",
        f"\tid: {quoted(chapter_id)}",
        "\timages: [",
        "\t\t{",
        "\t\t\talpha: 45",
        "\t\t\theight: 17.0d",
        f"\t\t\timage: {quoted(act['background'])}",
        "\t\t\torder: -10",
        "\t\t\trotation: 0.0d",
        "\t\t\twidth: 30.0d",
        "\t\t\tx: 9.625d",
        "\t\t\ty: 2.5d",
        "\t\t}",
        "\t\t{",
        f"\t\t\tclick: {quoted(WIKI_URL)}",
        "\t\t\theight: 3.0d",
        f"\t\t\thover: [{quoted('Open the TSR Wiki and Tensura Reference')}]",
        "\t\t\timage: \"tsr:textures/gui/quests/wiki_crest.png\"",
        "\t\t\torder: 5",
        "\t\t\trotation: 0.0d",
        "\t\t\twidth: 3.0d",
        "\t\t\tx: -2.25d",
        "\t\t\ty: -4.5d",
        "\t\t}",
        "\t]",
        f"\torder_index: {act_index}",
        "\tprogression_mode: \"linear\"",
        "\tquest_links: [ ]",
        "\tquests: [",
    ]
    for quest_index, quest in enumerate(act["quests"], 1):
        lines.extend(quest_snbt(act_index, quest_index, quest, previous_id))
        previous_id = object_id(act_index, 1, quest_index)
    lines.extend(["\t]", f"\ttitle: {quoted(act['title'])}", "}", ""])
    return "\n".join(lines)


def main() -> None:
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    expected = set()
    for act_index, act in enumerate(ACTS):
        path = CHAPTERS_DIR / f"{act['filename']}.snbt"
        expected.add(path.name)
        path.write_text(chapter_snbt(act_index, act), encoding="utf-8", newline="\n")
    for path in CHAPTERS_DIR.glob("*.snbt"):
        if path.name not in expected:
            path.unlink()
    print(f"Generated {len(ACTS)} chapters and {sum(len(act['quests']) for act in ACTS)} quests")


if __name__ == "__main__":
    main()
