"""Keep documented Nightmares relationships aligned with acquisition reviews."""
from __future__ import annotations

from nightmares_acquisition import review as nightmares_review
from lucifer_acquisition import review as lucifer_review
from belphegor_acquisition import review as belphegor_review
from mammon_acquisition import review as mammon_review


def relationships():
    asmodeus = nightmares_review()['asmodeus']
    lucifer = lucifer_review()['lucifer']
    belphegor = belphegor_review()['belphegor']
    mammon = mammon_review()['mammon']
    return [
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
    ]
