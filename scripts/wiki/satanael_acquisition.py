"""Render the reviewed Wrath evolution route with exact health and stat gates."""
from __future__ import annotations

import json
from pathlib import Path
from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/satanael_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/satanael_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:satanael':
        return None
    data = review()
    facts = data['satanael']
    wrath = link(page, 'tensura-reference/skills/unique/wrath.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Wrath → Satanael. The selected checks use recorded victories and current health, not a Rampage effect level.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Master Wrath and record victories</h3><p>Fully learn and master your own non-temporary <a href="{wrath}">Wrath</a>. Reference defaults: at least <strong>{facts["default_mob_kills"]} recorded mob kills</strong> and <strong>{facts["default_raid_wins"]} recorded raid wins</strong>.</p></div>',
        f'<div><span>02</span><h3>Reach the capacity gate</h3><p>The reference default is <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>, not current MP or total EP. Automatic-evolution gamerules and Satanael’s configuration must allow the route.</p></div>',
        f'<div><span>03</span><h3>Meet the current-health check</h3><p>Default: health at or below <strong>{facts["default_health_percent"]}% of maximum health</strong> when eligibility is checked. This is a ratio, not 40 HP. Deliberately taking damage does not guarantee evolution or protection from death.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes Wrath after successful learning. Live eligibility, exact trigger timing, and effective server settings remain unverified.</p>',
        '<details class="skill-source-limits"><summary>Health, victory counters, and source corrections</summary><p>The health predicate requires positive maximum health and accepts <code>getHealth() / getMaxHealth() &lt;= satanaelHP / 100.0</code>. The reviewed default is 40. The source says “under 40%”; this selected implementation uses an inclusive comparison.</p>',
        '<p>Victories are checked through <code>Stats.MOB_KILLS</code> and <code>Stats.RAID_WIN</code>, accepting their configured minimums. A Hero of the Village effect or nearby monsters does not replace these counters. The raid condition’s identifier mentions Rampage, but its class reads raid wins; no Rampage-effect condition appears in this four-condition list.</p></details>',
        f'<details class="skill-source-limits"><summary>Evolution settings and predecessor replacement</summary><p>The selected path requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Satanael’s <code>enableUltimateEvolution</code>. The gamerules default to false; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>. Already owning Satanael prevents another evolution.</p>',
        '<p>The shared helper checks maximum Magicules with a 0.000001 tolerance, rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>, and forgets Wrath after successful learning. This capacity check does not establish every learning charge, alternate route, or live event cadence.</p></details>',
        f'<p class="skill-evidence-note"><a href="{REVIEW_URL}">Acquisition evidence and class checksums</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Usage effects retain their source attribution and are not a complete effect audit.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:wrath':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-satanael.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Satanael, Lord of Wrath →</a> requires mastered non-temporary Wrath, recorded mob kills and raid wins, maximum Magicules, a current-health ratio, and enabled settings in the reviewed path. The helper removes Wrath after success; live evolution remains unverified.</aside>'
