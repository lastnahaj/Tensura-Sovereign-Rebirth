"""Render the reviewed two-predecessor Beelzebuth route and source limits."""
from __future__ import annotations

import json
from pathlib import Path
from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/beelzebuth_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/beelzebuth_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:beelzebuth':
        return None
    data = review()
    facts = data['beelzebuth']
    gluttony = link(page, 'tensura-reference/skills/unique/gluttony.md')
    merciless = link(page, 'tensura-reference/skills/unique/merciless.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build automatic route:</strong> Gluttony + Merciless → Beelzebuth. Both predecessor skills are required; neither is an independent unlock.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Master both predecessors</h3><p>Fully learn and master your own non-temporary <a href="{gluttony}">Gluttony</a> and <a href="{merciless}">Merciless</a>. Having only one of them does not satisfy this route.</p></div>',
        f'<div><span>02</span><h3>Build the recorded counters</h3><p>Reference defaults: at least <strong>{facts["default_mob_kills"]:,} recorded mob kills</strong> and <strong>{facts["default_cake_slices"]} recorded cake slices eaten</strong>. The cake gate is a statistic, not a number of whole cakes or cakes held in inventory.</p></div>',
        f'<div><span>03</span><h3>Meet capacity and current health</h3><p>Selected capacity default: <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>. Current health must be at or below <strong>50% of maximum health</strong>; rules and learning gates must also allow the route. Taking damage does not guarantee evolution.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes both Gluttony and Merciless after successful learning. Complete learning charges, live eligibility, and effective server settings remain unverified.</p>',
        '<details class="skill-source-limits"><summary>Why the reviewed capacity differs from the source</summary><p>The source lists 1,750,000 MP. In the inspected automatic path, the completion helper calls <code>getDefaultAcquiringMagiculeCost()</code>, which reads <code>Beelzebuth.mpAcquirement</code> with a default of 1,500,000. The separate <code>beelzebuthMP</code> field defaults to 1,750,000 but is not read by this selected capacity path. This does not establish every alternate route or server override.</p>',
        '<p>The helper compares maximum Magicules with a 0.000001 tolerance. Current MP and total EP are not that capacity check; the comparison alone does not establish all final learning charges.</p></details>',
        '<details class="skill-source-limits"><summary>Cake, health, and inherited learning checks</summary><p>The condition list checks <code>Stats.MOB_KILLS</code>, <code>Stats.EAT_CAKE_SLICE</code>, mastery of both predecessors, and the health ratio. The cake predicate requires a ServerPlayer, accepts the configured minimum, and reads zero if statistic access fails. Inventory, dropped cakes, and placed-but-uneaten cakes do not replace the recorded slice count.</p>',
        '<p>The health check requires positive maximum health and accepts <code>getHealth() / getMaxHealth() &lt;= beelzebuthHPThreshold</code>, whose default is 0.5. The selected inherited learning check also rejects spectators, Rest, Infinite Imprisonment, forced sleeping, Bats Mode, and Shadow Step. This review does not test live statistic updates or all interacting add-ons.</p></details>',
        f'<details class="skill-source-limits"><summary>Settings, replacement, and the separate Raphael claim</summary><p>The automatic route requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and <code>enableUltimateEvolution</code>. The gamerules default to false; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>. Already owning Beelzebuth blocks the selected acquisition. Despite its name, the inspected <code>hasEvolved</code> helper only checks current skill ownership; it does not establish a permanent evolution-history lock.</p>',
        '<p>The completion helper rejects imprinted predecessor tags and forgets both predecessor skills after successful learning. The source also describes alteration with mastered Raphael, Gluttony, and Merciless. That separate alteration implementation is not reviewed here and is not combined with the automatic conditions or presented as a verified unlock.</p></details>',
        f'<p class="skill-evidence-note"><a href="{REVIEW_URL}">Acquisition evidence and class checksums</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Effects retain their source attribution; live acquisition and full effect behavior remain unverified.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') not in {'tensura:gluttony', 'tensura:merciless'}:
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-beelzebuth.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Beelzebuth, Lord of Gluttony →</a> requires both mastered non-temporary Gluttony and Merciless, recorded mob kills and cake slices, maximum Magicules, current health, and enabled settings in the reviewed automatic path. Both predecessors are removed after success. The source’s separate Raphael alteration route and live evolution remain unverified.</aside>'
