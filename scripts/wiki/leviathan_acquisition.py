"""Render the reviewed Envy evolution and conditional Stasis learning attempt."""
from __future__ import annotations

import json
from pathlib import Path
from nightmares_acquisition import link

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/leviathan_acquisition_reference.json'


def review():
    return json.loads((ROOT / 'data/leviathan_acquisition_reference.json').read_text(encoding='utf-8'))


def acquisition(page, decision):
    identifier = decision.get('id')
    if identifier not in {'trnightmare:leviathan', 'trnightmare:stasis'}:
        return None
    data = review()
    facts = data['leviathan']
    envy = link(page, 'tensura-reference/skills/unique/envy.md')
    leviathan = link(page, 'tensura-reference/skills/ultimate/nightmares-leviathan.md')
    stasis = link(page, 'tensura-reference/skills/unique/nightmares-stasis.md')
    rules = link(page, 'tensura-reference/gamerules/index.md')
    if identifier == 'trnightmare:stasis':
        return ''.join([
            '<div class="nightmares-acquisition-review">',
            '<p><strong>Reviewed conditional learning attempt:</strong> Leviathan’s Envious Hero helper attempts to learn Stasis for eligible players. The attempt is not a confirmed live-server grant.</p>',
            '<div class="skill-reading-guide">',
            '<div><span>01</span><h3>Already be a True Hero</h3><p>The helper requires a player whose Tensura existence data reports <code>isTrueHero()</code>. A name, Hero of the Village effect, prestige grade, or raid-win statistic is not the flag checked here. This review does not establish the awakening route.</p></div>',
            f'<div><span>02</span><h3>Finish learning Leviathan</h3><p>Have your own fully learned, non-temporary <a href="{leviathan}">Leviathan</a>. This reward check does not require Leviathan mastery. Already having fully learned Stasis prevents another attempt.</p></div>',
            '<div><span>03</span><h3>Confirm actual learning</h3><p>The helper calls the normal skill-learning system. Check your skill menu and learning state; its notification is not proof that the call succeeded. The complete learning charges and live result remain unverified.</p></div>',
            '</div>',
            '<details class="skill-source-limits"><summary>Reward checks, callback order, and limits</summary><p>The inspected helper checks a Player entity, True Hero state, and <code>hasSkillFully</code> for Leviathan; it then exits if that same predicate already accepts Stasis. The base predicate requires a non-temporary owned instance with nonnegative mastery, not a mastered skill.</p>',
            '<p>It calls <code>SkillHelper.learnSkill(player, UniqueSkills.STASIS)</code>, discards the boolean result, then sends a message. A message is therefore not success proof. Leviathan’s tick callback invokes the helper before its toggle-state return; toggling Leviathan on is not a prerequisite in that selected callback. Effective timing, other gates, and live delivery remain untested.</p>',
            '<p>The selected successful Leviathan evolution also invokes the helper. This does not establish every alternative Stasis route or the full inherited learning pipeline.</p></details>',
            f'<p class="skill-evidence-note"><a href="{REVIEW_URL}">Conditional learning evidence</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Stasis’s usage values remain source-described rather than fully audited.</p>',
            '</div>',
        ]), True
    return ''.join([
        '<div class="nightmares-acquisition-review">',
        '<p><strong>Reviewed reference-build evolution route:</strong> Envy → Leviathan. True Hero state belongs to its separate Stasis reward check, not this selected evolution requirement list.</p>',
        '<div class="skill-reading-guide">',
        f'<div><span>01</span><h3>Master your own Envy</h3><p>Fully learn and master your non-temporary <a href="{envy}">Envy</a>. Already owning Leviathan blocks another evolution.</p></div>',
        f'<div><span>02</span><h3>Record raid victories</h3><p>Reference default: at least <strong>{facts["default_raid_wins"]} recorded raid wins</strong>, checked through <code>Stats.RAID_WIN</code>. Having a Hero of the Village effect is not this statistic.</p></div>',
        f'<div><span>03</span><h3>Meet capacity and settings</h3><p>Reference default: <strong>{facts["default_max_magicules_requirement"]:,} maximum Magicules</strong>, not current MP or total EP. The automatic-evolution gamerules and skill configuration must allow the route.</p></div>',
        '</div>',
        '<p><strong>Before evolving:</strong> the inspected helper removes Envy after successful learning. Active server rules, complete learning charges, and live evolution remain unverified.</p>',
        f'<details class="skill-source-limits"><summary>Evolution gates and exact comparisons</summary><p>The selected path requires <code>nightmare_ultimates</code>, <code>auto_evolve</code>, and Leviathan’s <code>enableUltimateEvolution</code>. The gamerules default to false; the skill setting defaults to true. <a href="{rules}">Review the gamerules</a>.</p>',
        '<p>The condition list checks mastered Envy and the configured raid-win count, accepting the minimum. The shared helper checks maximum Magicules with a 0.000001 tolerance and rejects predecessor tags <code>trnightmare_directive_ego</code> and <code>AkashicStarOrderImprint</code>. It forgets Envy after successful learning; keeping both skills is not promised.</p>',
        '<p>The condition identifier’s name mentions insanity, but its actual class reads the raid-win statistic. No Insanity effect or True Hero condition appears in this selected list. This does not establish alternative triggers or current server eligibility.</p></details>',
        f'<p><strong>Conditional reward:</strong> Leviathan’s Envious Hero helper attempts to learn <a href="{stasis}">Stasis</a> when the player is already a True Hero and has fully learned Leviathan. Mastery is not required by that reward check. Read Stasis’s guide for the notification and learning limits.</p>',
        f'<p class="skill-evidence-note"><a href="{REVIEW_URL}">Acquisition and reward evidence</a> · <a href="{data["reference_build"]["source_url"]}">Reviewed release</a>. Other usage effects remain source-described, not a complete effect audit.</p>',
        '</div>',
    ]), True


def successor(page, decision):
    if decision.get('id') != 'tensura:envy':
        return ''
    target = link(page, 'tensura-reference/skills/ultimate/nightmares-leviathan.md')
    return f'<aside class="skill-evidence-note skill-successor-note"><strong>Nightmares evolution:</strong> <a href="{target}">Leviathan, Lord of Envy →</a> requires mastered non-temporary Envy, recorded raid wins, maximum Magicules, and enabled settings in the reviewed path. The helper removes Envy after success. True Hero state is part of its separate Stasis reward check; server build match and live evolution remain unverified.</aside>'
