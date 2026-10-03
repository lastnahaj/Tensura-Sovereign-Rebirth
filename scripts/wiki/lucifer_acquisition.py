"""Render the selected Pride-to-Lucifer checks separately from older source claims."""
from __future__ import annotations

import json
from pathlib import Path

from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/lucifer_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/lucifer_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:lucifer':
        return None
    data = review()
    facts = data['lucifer']
    pride = link(page, 'tensura-reference/skills/unique/pride.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Pride → Lucifer. The source mixes older mastery and Ultimate-hit wording with its obtainment table; the selected automatic check is described here instead.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Finish learning Pride</h3><p>Have your own fully learned, non-temporary <a href="{pride}">Pride</a>. This check does not specifically require Pride to be mastered. Already owning Lucifer blocks another evolution.</p></div>',
        f'<div><span>02</span><h3>Build a mastered repertoire</h3><p>Reference default: at least <strong>{facts["default_mastered_skill_count"]} mastered skill instances</strong> in your current learned-skill storage. This is not 100 mastery points or a lifetime count of skills you no longer hold.</p></div>',
        f'<div><span>03</span><h3>Check capacity and health</h3><p>Reference defaults: <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong> and a health ratio at or below the configured threshold, about <strong>40% of maximum health</strong>. These are not current MP, total EP, or spiritual health.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes Pride after successful learning. Server settings and live eligibility remain unverified; do not risk a character assuming this reference route is enabled.</p>',
        f'<details class="skill-source-limits"><summary>Evolution gates and exact comparisons</summary><p>The checked automatic route requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Lucifer’s <code>enableUltimateEvolution</code> setting. The gamerules default to false in the reference artifact; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>. No server values were read or changed.</p>',
        '<p>The Pride predicate checks a non-temporary instance with nonnegative mastery. The condition list counts learned skill instances whose <code>isMastered(entity)</code> predicate returns true; it does not limit the count to Unique Skills or add previously forgotten skills.</p>',
        '<p>The helper uses maximum Magicules plus a 0.000001 comparison tolerance, accepting the configured acquiring-cost threshold. The health predicate requires positive maximum health, then checks <code>getHealth() / getMaxHealth() &lt;= configured percentage</code>. The reference setting is a float initialized to 0.4, not a strict below-40% comparison.</p>',
        '<p>No Ultimate-skill hit condition appears in this selected acquisition path. That does not establish every alternative trigger or inherited interaction. Event cadence, the complete learning pipeline, and successful live evolution remain untested.</p>',
        '<p>The shared helper rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>. After successful learning it records predecessor mastery and forgets Pride without consulting <code>lose_unique_on_upgrade</code> in this path.</p></details>',
        f'<p class="skill-evidence-note">Default Lucifer mastery is <strong>{facts["default_lucifer_mastery"]:,}</strong> from <code>{facts["mastery_config_key"]}</code>, replacing the source’s 5,000 value. This is Lucifer’s mastery target, not its acquisition count. <a href="{REVIEW_URL}">Acquisition and configuration evidence</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Usage effects remain source-described rather than fully audited.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:pride':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-lucifer.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Lucifer, Lord of Pride →</a> uses fully learned, non-temporary Pride in the reviewed automatic path. Its mastered-skill count, health ratio, maximum Magicules, and settings must also qualify. The helper removes Pride after success. Server build match and live evolution remain unverified.</aside>'
