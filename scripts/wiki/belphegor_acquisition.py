"""Render reviewed Sloth evolution conditions with explicit reference scope."""
from __future__ import annotations

import json
from pathlib import Path
from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/belphegor_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/belphegor_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    if decision.get('id') != 'trnightmare:belphegor':
        return None
    data = review()
    facts = data['belphegor']
    sloth = link(page, 'tensura-reference/skills/unique/sloth.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Sloth → Belphegor. Separate the skill’s stored reserve, your maximum Magicules, and the bed-progress counter.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Prepare Sloth’s reserve</h3><p>Fully master your own permanent <a href="{sloth}">Sloth</a>. Its <code>storedMagicule</code> tag must hold at least <strong>{facts["default_stored_magicules"]:,} stored Magicules</strong> by default. Current player MP is not this reserve.</p></div>',
        f'<div><span>02</span><h3>Build bed progress</h3><p>The default is <strong>{facts["default_bed_ticks"]:,} recorded ticks</strong> standing still on a bed. The condition also requires you to be on a bed when checked. Sleeping through a night is not the predicate inspected here.</p></div>',
        f'<div><span>03</span><h3>Meet the player thresholds</h3><p>Reference defaults: at least <strong>{facts["default_mob_kills"]:,} recorded mob kills</strong> and <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>. These are a player statistic and a capacity gate, not held items or current MP.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the selected helper removes Sloth after successful learning. Gamerules, skill configuration, and the bed tracker must permit the route. Active server settings and successful evolution remain unverified.</p>',
        '<details class="skill-source-limits"><summary>Bed progress: ticks, standing, and configuration</summary>',
        '<p>The configured bed minutes are multiplied by 60 × 20. At the default of 10 minutes this is 12,000 ticks, nominally ten minutes at 20 ticks per second. No wall-clock timer or reliable live completion time has been verified.</p>',
        '<p>The predicate checks a server player, horizontal movement squared no greater than 0.0001, and sampled bounding-box overlap with a block tagged <code>BEDS</code>. It then requires <code>designer_bed_still_ticks</code> to meet the threshold. Ordinary sleeping state is not checked.</p>',
        '<p>The inspected tick helper increments the counter while this bed predicate is true. Leaving the bed does not reset the counter in that helper, but you must be on a bed when eligibility is evaluated. Other reset and persistence paths remain unverified.</p>',
        '<p>The shared tracker uses Designer’s separate <code>slothBedMinutesRequired</code> setting, default 60, to enable tracking. A nonpositive value resets the counter to zero. That setting does not replace Belphegor’s default ten-minute threshold. The handler calls the tracker on its server-player tick path; effective runtime cadence remains untested.</p></details>',
        f'<details class="skill-source-limits"><summary>Evolution gates and exact counters</summary><p>The selected route requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Belphegor’s <code>enableUltimateEvolution</code>. The two gamerules default to false; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>. Already owning Belphegor blocks another evolution.</p>',
        '<p>The reserve predicate reads Sloth’s skill-instance tag; the kill predicate reads <code>Stats.MOB_KILLS</code>. Both accept the configured minimum. The shared helper checks maximum Magicules with a 0.000001 tolerance; this does not prove the complete learning pipeline never charges resources.</p>',
        '<p>The helper rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>, records predecessor mastery, and forgets Sloth after successful learning. Keeping both skills is not promised. Alternative routes and surrounding event ordering remain unverified.</p></details>',
        f'<p class="skill-evidence-note">Belphegor’s default mastery target is <strong>{facts["default_mastery"]:,}</strong> from <code>{facts["mastery_config_key"]}</code>, replacing the source’s 5,000 value. <a href="{REVIEW_URL}">Acquisition evidence</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Usage effects remain source-described, not a complete effect audit.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:sloth':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-belphegor.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Belphegor, Lord of Sloth →</a> requires mastered permanent Sloth, its stored reserve, bed-progress ticks, recorded mob kills, maximum Magicules, and enabled settings in the reviewed route. The helper removes Sloth after success; server build match and live evolution remain unverified.</aside>'
