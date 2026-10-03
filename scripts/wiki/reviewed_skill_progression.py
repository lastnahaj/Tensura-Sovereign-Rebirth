"""Keep documented Nightmares relationships aligned with acquisition reviews."""
from __future__ import annotations

from nightmares_acquisition import review as nightmares_review
from lucifer_acquisition import review as lucifer_review
from belphegor_acquisition import review as belphegor_review
from mammon_acquisition import review as mammon_review
from leviathan_acquisition import review as leviathan_review
from satanael_acquisition import review as satanael_review


def relationships():
    asmodeus = nightmares_review()['asmodeus']
    lucifer = lucifer_review()['lucifer']
    belphegor = belphegor_review()['belphegor']
    mammon = mammon_review()['mammon']
    leviathan = leviathan_review()['leviathan']
    satanael = satanael_review()['satanael']
    return [
        {
            'from': satanael['predecessor'],
            'to': satanael['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: mastered non-temporary Wrath; {satanael["default_mob_kills"]} recorded mob kills; '
                f'{satanael["default_raid_wins"]} recorded raid wins; {satanael["default_max_magicules_requirement"]:,} maximum Magicules; '
                f'current health at or below {satanael["default_health_percent"]}% of maximum. '
                'Gamerules and skill configuration must allow the route. '
                'The helper removes Wrath after success. No Rampage effect is required by the selected list. Server evolution remains unverified.'
            ),
        },
        {
            'from': asmodeus['predecessor'],
            'to': asmodeus['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: fully master Lust; naming statistic at least {asmodeus["default_named_requirement"]}; '
                f'{asmodeus["default_breeding_requirement"]} animals bred; {asmodeus["default_max_magicules_requirement"]:,} maximum Magicules. '
                'Automatic-evolution gamerules and skill configuration must allow the route. '
                'The helper removes Lust after success. Server evolution remains unverified.'
            ),
        },
        {
            'from': lucifer['predecessor'],
            'to': lucifer['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: fully learned, non-temporary Pride; {lucifer["default_mastered_skill_count"]} currently mastered skill instances; '
                f'{lucifer["default_max_magicules_requirement"]:,} maximum Magicules; health at or below the configured ratio (about 40%). '
                'Automatic-evolution gamerules and skill configuration must allow the route. '
                'The helper removes Pride after success. Server evolution remains unverified.'
            ),
        },
        {
            'from': belphegor['predecessor'],
            'to': belphegor['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: mastered permanent Sloth with {belphegor["default_stored_magicules"]:,} stored Magicules; '
                f'{belphegor["default_bed_ticks"]:,} recorded standing-still-on-bed ticks and current bed state; '
                f'{belphegor["default_mob_kills"]:,} recorded mob kills; {belphegor["default_max_magicules_requirement"]:,} maximum Magicules. '
                'Gamerules, skill configuration, and bed tracking must allow the route. '
                'The helper removes Sloth after success. Server evolution remains unverified.'
            ),
        },
        {
            'from': mammon['predecessor'],
            'to': mammon['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: mastered non-temporary Greed; {mammon["default_villager_trades"]} recorded villager trades; '
                f'{mammon["default_raid_wins"]} recorded raid wins; {mammon["default_gold_blocks"]} Gold Blocks in the main inventory; '
                f'{mammon["default_max_magicules_requirement"]:,} maximum Magicules. '
                'Gamerules and skill configuration must allow the route. '
                'The selected gold check does not consume blocks; the helper removes Greed after success. Server evolution remains unverified.'
            ),
        },
        {
            'from': leviathan['predecessor'],
            'to': leviathan['registry_id'],
            'kind': 'Reference-build evolution',
            'requirements': (
                f'Reference defaults: mastered non-temporary Envy; {leviathan["default_raid_wins"]} recorded raid wins; '
                f'{leviathan["default_max_magicules_requirement"]:,} maximum Magicules. '
                'Gamerules and skill configuration must allow the route. '
                'The helper removes Envy after success. True Hero state belongs to the separate Stasis reward check. Server evolution remains unverified.'
            ),
        },
        {
            'from': leviathan['registry_id'],
            'to': 'trnightmare:stasis',
            'kind': 'Reference-build conditional learning',
            'requirements': (
                'Reference check: True Hero state and own fully learned, non-temporary Leviathan; Leviathan mastery is not required. '
                'The helper attempts Stasis learning and does not check the result before sending its notification. Server learning remains unverified.'
            ),
        },
    ]
