"""Build a compact comparison guide from the seven reviewed Sin evolutions."""
from __future__ import annotations

import html
import json
from pathlib import Path
from nightmares_acquisition import review as asmodeus_review
from lucifer_acquisition import review as lucifer_review
from belphegor_acquisition import review as belphegor_review
from mammon_acquisition import review as mammon_review
from leviathan_acquisition import review as leviathan_review
from satanael_acquisition import review as satanael_review
from beelzebuth_acquisition import review as beelzebuth_review

ROOT = Path(__file__).resolve().parents[2]


def routes():
    """Only selected acquisition evidence belongs in this comparison."""
    a, l, b = asmodeus_review()['asmodeus'], lucifer_review()['lucifer'], belphegor_review()['belphegor']
    m, v = mammon_review()['mammon'], leviathan_review()['leviathan']
    s, z = satanael_review()['satanael'], beelzebuth_review()['beelzebuth']
    return [
        (a, 'Lust', 'Master Lust', [f'{a["default_named_requirement"]} recorded entity namings', f'{a["default_breeding_requirement"]} animals bred'], 'Naming and breeding are player counters, not nearby subordinate or animal counts.', 'nightmares_acquisition_review'),
        (l, 'Pride', 'Fully learn Pride; predecessor mastery is not required by this selected check', [f'{l["default_mastered_skill_count"]} currently mastered skill instances', 'Current health at or below the configured ratio (about 40%)'], 'This selected route does not require being hit by an Ultimate Skill.', 'lucifer_acquisition_reference'),
        (s, 'Wrath', 'Master Wrath', [f'{s["default_mob_kills"]} recorded mob kills', f'{s["default_raid_wins"]} recorded raid wins', f'Current health at or below {s["default_health_percent"]}% of maximum'], 'The selected raid condition reads raid wins, not a Rampage effect level.', 'satanael_acquisition_reference'),
        (m, 'Greed', 'Master Greed', [f'{m["default_villager_trades"]} recorded villager trades', f'{m["default_raid_wins"]} recorded raid wins', f'{m["default_gold_blocks"]} Gold Blocks in the main inventory'], 'Repeated trades are not excluded by the statistic predicate. This gold check does not consume the blocks.', 'mammon_acquisition_reference'),
        (v, 'Envy', 'Master Envy', [f'{v["default_raid_wins"]} recorded raid wins'], 'True Hero state is for the separate Stasis learning attempt, not this evolution list. A Stasis notification is not proof of learning.', 'leviathan_acquisition_reference'),
        (b, 'Sloth', 'Master permanent Sloth', [f'{b["default_stored_magicules"]:,} Magicules stored in the Sloth instance', f'{b["default_bed_ticks"]:,} recorded bed-standing ticks and current bed state', f'{b["default_mob_kills"]:,} recorded mob kills'], 'Standing still on a bed is not the same as sleeping. Tracker enablement and real timing need separate checks.', 'belphegor_acquisition_reference'),
        (z, 'Gluttony + Merciless', 'Master both Gluttony and Merciless', [f'{z["default_mob_kills"]:,} recorded mob kills', f'{z["default_cake_slices"]} recorded cake slices eaten', 'Current health at or below 50% of maximum'], 'Both predecessors are required and replaced. The selected capacity default differs from the source’s 1.75M claim; Raphael alteration is separate and unreviewed.', 'beelzebuth_acquisition_reference'),
    ]


def generate(policy):
    decisions = {d['id']: (page, d) for page, d in policy['pages'].items() if d['status'] in {'registered', 'reference'}}
    artwork = json.loads((ROOT / 'data/skill_artwork.json').read_text(encoding='utf-8'))['entries']
    reference = asmodeus_review()['reference_build']
    lines = [
        '---', 'title: Sin Ultimate Evolution Planner',
        'description: Compare seven reviewed Nightmares evolution routes, capacity gates, and predecessor requirements.',
        'hide:', '  - navigation', '  - toc', '---', '',
        '<div class="sin-evolution-planner">',
        '<header class="sin-planner-heading"><p class="reference-eyebrow">Nightmares · 1.21.1 reference guide</p><h1>Plan your next Ultimate.</h1><p>Compare seven Sin evolutions. Open a route to see the preparation it needs, then follow its complete skill guide.</p><nav aria-label="Planner navigation"><a href="../tensura-reference/skills/ultimate/">← Ultimate Skills</a><a href="../tensura-reference/skills/unique/">Find your predecessor</a></nav></header>',
        '<aside class="sin-planner-scope"><strong>Reference defaults, not a server eligibility checker.</strong><p>These selected automatic paths were inspected in Nightmares 1.0.3.2.8. The live server’s artifact and settings have not been matched. Meeting the visible defaults does not guarantee evolution.</p></aside>',
        '<section class="sin-planner-basics" aria-label="Shared evolution checks"><div><span>01 · Ownership</span><h2>Use your own predecessor</h2><p>Borrowed or temporary skill instances are not a substitute for the inspected ownership checks. Pride’s mastery requirement differs from the other routes.</p></div><div><span>02 · Capacity</span><h2>Compare maximum Magicules</h2><p>The capacity gate is not current MP or total EP. It does not establish every final learning charge.</p></div><div><span>03 · Settings</span><h2>Check rules before grinding</h2><p>These paths require the automatic-evolution gamerules and skill settings. Both gamerules default to false in the reference build.</p></div></section>',
        '<div class="sin-route-list" aria-label="Seven reviewed evolution routes">',
    ]
    for facts, predecessor, preparation, conditions, caution, register in routes():
        page, decision = decisions[facts['registry_id']]
        asset = decision.get('asset')
        if not asset or facts['registry_id'] not in artwork:
            raise ValueError(f'Planner route has no reviewed artwork: {facts["registry_id"]}')
        name = decision['title'].split(',')[0].strip('「」')
        slug = facts['registry_id'].split(':')[1]
        picture = f'<img src="../{html.escape(asset, quote=True)}" alt="" width="64" height="64" loading="lazy">'
        capacity = facts['default_max_magicules_requirement']
        lines.append(f'<details class="sin-route" id="{slug}"><summary>{picture}<span class="sin-route-title"><span>{html.escape(predecessor)} →</span><strong>{html.escape(name)}</strong></span><span class="sin-route-capacity"><strong>{capacity:,}</strong><span>maximum Magicules</span></span></summary><div class="sin-route-body">')
        lines.append(f'<div><p class="sin-route-label">Preparation</p><h2>{html.escape(preparation)}</h2><ul>')
        lines.extend(f'<li>{html.escape(condition)}</li>' for condition in conditions)
        lines.append('</ul><p class="sin-route-ownership">All routes also require their own non-temporary predecessor instances and enabled settings. The inspected completion helper replaces the predecessor skill or skills after successful learning.</p></div>')
        target = '../' + page.removesuffix('.md') + '/'
        evidence_url = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/' + register + '.json'
        lines.append(f'<div class="sin-route-notes"><p class="sin-route-label">Important distinction</p><p>{html.escape(caution)}</p><a class="sin-route-guide" href="{target}">Open the complete {html.escape(name)} guide →</a><a class="sin-route-evidence" href="{evidence_url}">Implementation evidence</a>')
        media = artwork[facts['registry_id']].get('media')
        if media:
            lines.append(f'<p class="sin-route-credit">Icon: <a href="{html.escape(media["source_file_page"], quote=True)}">{html.escape(media["source_title"])}</a> · <a href="{html.escape(media["license_url"], quote=True)}">{html.escape(media["license"])}</a>. Article credits retain upload and modification details.</p>')
        else:
            lines.append('<p class="sin-route-credit">Original TSR illustration, not an in-game icon. Full artwork provenance is retained in the skill article.</p>')
        lines.append('</div></div></details>')
    lines.extend([
        '</div>',
        '<footer class="sin-planner-footer"><h2>When a route will not trigger</h2><p>Check the complete article before spending resources or taking damage. Stored reserves, inventory holdings, recorded statistics, and current state are different gates. Imprinted predecessors can also be rejected by the helper.</p><p>The seven resulting Sin Ultimates use a reviewed 15,000-point mastery default. That is their own mastery target, not a universal predecessor-unlock threshold. Trigger timing, reset persistence, alternative routes, effective settings, and live success remain unverified.</p>',
        f'<nav aria-label="Planner sources"><a href="{reference["source_url"]}">Reviewed mod release</a><a href="../tensura-reference/gamerules/">Gamerules</a><a href="../project/sources-and-attribution/">Sources &amp; artwork credits</a></nav></footer>',
        '</div>', '',
    ])
    return '\n'.join(lines)
