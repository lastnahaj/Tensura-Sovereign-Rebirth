"""Render reviewed Nightmares acquisition conditions without promoting server coverage."""
from __future__ import annotations

import json
import posixpath
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_acquisition_review.json'


def review():
    return json.loads((ROOT / 'data/nightmares_acquisition_review.json').read_text(encoding='utf-8'))


def link(page, target):
    source_route = page[:-8] if page.endswith('index.md') else page[:-3] + '/'
    target_route = target[:-8] if target.endswith('index.md') else target[:-3] + '/'
    return posixpath.relpath(target_route, source_route) + '/'


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:asmodeus':
        return None
    data = review()
    facts = data['asmodeus']
    lust = link(page, 'tensura-reference/skills/unique/lust.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Lust → Asmodeus. These conditions replace the source’s vague resource wording; they do not confirm live-server availability.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Master Lust</h3><p>Fully master your own <a href="{lust}">Lust</a> skill. Already owning Asmodeus blocks another evolution.</p></div>',
        f'<div><span>02</span><h3>Meet the recorded counters</h3><p>Reference defaults: at least <strong>{facts["default_named_requirement"]} entities named</strong> and <strong>{facts["default_breeding_requirement"]} animals bred</strong>. The player route checks statistics, not a headcount of currently living followers.</p></div>',
        f'<div><span>03</span><h3>Reach maximum Magicules</h3><p>The default capacity requirement is <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>, not current MP or total EP. Configuration can change this threshold.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes Lust after successful learning. Keeping both skills is not promised.</p>',
        f'<details class="skill-source-limits"><summary>Evolution gates and resource details</summary><p>The checked automatic route requires <code>nightmare_ultimates</code> and <code>auto_evolve</code> to be true, plus Asmodeus’s <code>enableUltimateEvolution</code> setting. The two gamerules default to <strong>false</strong> in this reference artifact; the skill setting defaults to true. <a href="{rules}">Review the gamerule reference</a>; active server values have not been checked.</p>',
        '<p>The helper compares <code>EnergyHelper.getMaxMagicule(player) + 0.000001</code> with the skill’s configured acquiring cost. Exactly 1,200,000 meets the default comparison. This is a capacity gate; it does not prove that the final learning pipeline never charges resources.</p>',
        '<p>The subordinate condition’s player branch reads <code>TensuraStats.ENTITY_NAMED</code>. The breeding condition reads <code>Stats.ANIMALS_BRED</code>. Both accept counts equal to the configured minimum. Pet ownership, nearby mobs, and putting an animal into love mode are not the counters inspected here; statistic-update behavior has not been tested live.</p>',
        '<p>A predecessor marked <code>trnightmare_directive_ego</code> or <code>AkashicStarOrderImprint</code> is rejected by the shared helper. After successful learning, that helper records predecessor mastery and forgets Lust. This specific path does not consult <code>lose_unique_on_upgrade</code> before forgetting it; retaining both skills is not promised.</p>',
        '<p>Prerequisites do not establish the event cadence or guarantee a successful grant through the surrounding learning system. Other acquisition routes have not been established by this review.</p></details>',
        f'<p class="skill-evidence-note">Acquisition handlers and defaults checked in <a href="{data["reference_build"]["source_url"]}">Nightmares 1.0.3.2.8 for 1.21.1</a>. <a href="{REVIEW_URL}">Review the class checksums and conditions</a>. Usage values below remain source-described and are not a complete effect audit.</p>',
        '<details class="skill-source-limits"><summary>Client inventory versus running server</summary><p>The September 20 client inventory names the same release file as this reference. The inventory supplies no artifact digest, so a filename match does not verify installed bytes, deployment, effective configuration, or gameplay.</p></details>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:lust':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-asmodeus.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Asmodeus, Lord of Lust →</a> starts from mastered Lust in the reviewed 1.21.1 reference. Naming and breeding statistics, maximum Magicules, configuration, and gamerules also gate the route. The inspected helper removes Lust after successful learning. Mastery alone does not unlock it; server build match remains pending.</aside>'
