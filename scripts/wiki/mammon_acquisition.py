"""Render the reviewed Greed evolution route with precise player counters."""
from __future__ import annotations

import json
from pathlib import Path
from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/mammon_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/mammon_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:mammon':
        return None
    data = review()
    facts = data['mammon']
    greed = link(page, 'tensura-reference/skills/unique/greed.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Greed → Mammon. The trade requirement counts recorded trades, not distinct villagers.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Master Greed and trade</h3><p>Fully learn and master your own non-temporary <a href="{greed}">Greed</a>. Reference default: at least <strong>{facts["default_villager_trades"]} recorded villager trades</strong>. Meeting the same villager repeatedly is not excluded by this statistic predicate.</p></div>',
        f'<div><span>02</span><h3>Record victories and carry gold</h3><p>Reference defaults: at least <strong>{facts["default_raid_wins"]} recorded raid wins</strong> and <strong>{facts["default_gold_blocks"]} Gold Blocks</strong> in the main inventory, including its hotbar. Placed blocks, chest contents, and offhand holdings do not satisfy this inventory scan.</p></div>',
        f'<div><span>03</span><h3>Reach the capacity gate</h3><p>The reference default is <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>, not current MP or total EP. Gamerules and Mammon’s evolution setting must also allow the route.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes Greed after successful learning. The selected gold predicate does not consume its seven blocks; that is not a guarantee about every surrounding acquisition path. Live eligibility and server configuration remain unverified.</p>',
        '<details class="skill-source-limits"><summary>Trades, raids, and inventory comparisons</summary><p>The player checks read <code>Stats.TRADED_WITH_VILLAGER</code> and <code>Stats.RAID_WIN</code>, accepting values equal to their configured minimums. These are not a count of nearby villagers or the presence of a Hero of the Village effect. How the server updates these statistics has not been tested.</p>',
        '<p>The gold condition sums matching <code>minecraft:gold_block</code> item counts across <code>Player.getInventory().items</code>. Separate stacks can contribute to the same threshold. Armor, offhand, external storage, nested container contents, and world blocks are not traversed. The registered condition’s consumption flag is false.</p></details>',
        f'<details class="skill-source-limits"><summary>Evolution gates and predecessor replacement</summary><p>The selected automatic path requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Mammon’s <code>enableUltimateEvolution</code>. The gamerules default to false; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>. Already owning Mammon blocks another evolution.</p>',
        '<p>The learned-skill predicate requires a non-temporary Greed instance with nonnegative mastery; the condition list additionally requires Greed mastery. The shared helper checks maximum Magicules with a 0.000001 tolerance, rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>, and forgets Greed after successful learning.</p>',
        '<p>A capacity comparison does not establish all final learning charges. Trigger cadence, alternative routes, add-on interactions, and successful live evolution remain unverified.</p></details>',
        f'<p class="skill-evidence-note"><a href="{REVIEW_URL}">Acquisition evidence and class checksums</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed 1.21.1 release</a>. Usage effects remain source-described, not a complete effect audit.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:greed':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-mammon.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Mammon, Lord of Greed →</a> requires mastered non-temporary Greed, recorded trades and raid wins, carried Gold Blocks, maximum Magicules, and enabled settings in the reviewed route. The helper removes Greed after success; server build match and live evolution remain unverified.</aside>'
