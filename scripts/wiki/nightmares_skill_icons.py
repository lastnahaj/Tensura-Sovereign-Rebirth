"""Semantic, code-native symbols for Nightmares reference cards."""
from __future__ import annotations

import html
import re

GLYPHS = {
    "infinity": '<path d="M48 48C22 11 5 71 30 66c18-4 27-44 44-36 24 13-4 57-26 18Z"/>',
    "time": '<circle cx="48" cy="47" r="27"/><path d="M48 25v22l17 9M42 13h12M48 74v8"/>',
    "book": '<path d="M48 30q-13-10-28-6v45q15-4 28 6 13-10 28-6V24q-15-4-28 6Zm0 0v45M28 36l12 4M28 46l12 4M56 40l12-4M56 50l12-4"/>',
    "flame": '<path d="M50 19c8 23-8 26-1 36 3-8 11-12 13-18 20 34-5 47-21 38-22-12-7-36 9-56Z"/>',
    "frost": '<path d="M48 19v58M23 34l50 28M23 62l50-28M38 25l10 9 10-9M38 71l10-9 10 9M25 44l12-1-1-12M71 52l-12 1 1 12"/>',
    "sun": '<circle cx="48" cy="48" r="15"/><path d="M48 18v9M48 69v9M18 48h9M69 48h9M27 27l7 7M62 62l7 7M27 69l7-7M62 34l7-7"/>',
    "moon": '<path d="M58 20a29 29 0 1 0 16 45C42 77 28 40 58 20Z"/><path d="m68 20 3 8 8 3-8 3-3 8-3-8-8-3 8-3Z"/>',
    "wind": '<path d="M20 34h43q20 0 11-14-7-8-14 0M14 47h60M20 60h39q23 0 15 15-7 9-14 0"/>',
    "void": '<ellipse cx="48" cy="48" rx="30" ry="12" transform="rotate(-30 48 48)"/><ellipse cx="48" cy="48" rx="30" ry="12" transform="rotate(30 48 48)"/><circle cx="48" cy="48" r="8"/>',
    "poison": '<path d="M38 22h20M42 22v23L28 68q-3 7 7 7h26q10 0 7-7L54 45V22M35 57h26"/><circle cx="44" cy="63" r="2"/><circle cx="54" cy="68" r="2"/>',
    "scales": '<path d="M48 19v57M33 76h30M24 32h48M28 32 17 56h22Zm40 0L57 56h22ZM17 56q11 13 22 0M57 56q11 13 22 0"/>',
    "crown": '<path d="m22 32 14 12 12-23 12 23 14-12-8 35H30Zm8 43h36M48 49v10"/>',
    "soul": '<path d="M48 20c-22 12-25 31-16 47l10-8 6 15 6-15 10 8c9-16 6-35-16-47Z"/><circle cx="41" cy="44" r="2"/><circle cx="55" cy="44" r="2"/>',
    "eye": '<path d="M22 48q26-31 52 0-26 31-52 0Z"/><circle cx="48" cy="48" r="10"/><path d="M48 38v20"/>',
    "exchange": '<path d="M20 34h54L61 21M74 34 61 47M76 62H22l13 13M22 62l13-13"/>',
    "gift": '<path d="M23 40h50v13H23Zm4 13v24h42V53M48 40v37M48 40c-32-2-22-28-8-18l8 18c32-2 22-28 8-18Z"/>',
    "mirror": '<rect x="30" y="19" width="36" height="58" rx="13"/><path d="m39 51 18-18M41 62l12-12M23 30v36M73 30v36"/>',
    "shield": '<path d="m48 19 25 10-4 28q-5 14-21 22-16-8-21-22l-4-28Z M48 28v38M35 45h26"/>',
    "lock": '<rect x="25" y="42" width="46" height="33" rx="5"/><path d="M34 42V32a14 14 0 0 1 28 0v10M48 56v9"/>',
    "home": '<path d="m19 43 29-24 29 24M27 37v40h42V37M41 77V53h14v24"/>',
    "music": '<path d="M42 61V27l29-7v35M42 37l29-7"/><ellipse cx="32" cy="65" rx="10" ry="7"/><ellipse cx="61" cy="59" rx="10" ry="7"/>',
    "growth": '<path d="M29 68C18 42 36 23 70 23c0 35-17 50-41 45Zm0 0 33-35M42 55V38M42 55h18"/>',
    "craft": '<path d="m39 20-3 11-11 3-7 14 8 9v14l14 7 9-8 14 1 10-12-5-11 4-13-13-11-11 5Z"/><circle cx="47" cy="49" r="12"/>',
    "creation": '<path d="m48 17 7 23 23 8-23 7-7 24-8-24-23-7 23-8ZM22 19v12M16 25h12M72 65v12M66 71h12"/>',
    "destruction": '<path d="m48 17-8 25-23-1 21 14-6 24 16-17 20 14-8-23 19-15-24 1Z M17 19l9 9M74 73l7 7"/>',
    "water": '<path d="M48 19C39 33 27 43 27 56a21 21 0 0 0 42 0C69 43 57 33 48 19Z M32 58q8-7 16 0t16 0"/>',
    "earth": '<path d="m18 68 20-38 13 23 9-17 18 32ZM29 48l9 8 8-7M27 77h42"/>',
    "heart": '<path d="M48 73 25 51C5 29 35 11 48 33c13-22 43-4 23 18ZM35 48h9l5-10 6 20 6-10h7"/>',
    "network": '<circle cx="48" cy="22" r="8"/><circle cx="23" cy="65" r="8"/><circle cx="73" cy="65" r="8"/><path d="M44 29 27 58M52 29l17 29M31 65h34M48 40v14"/>',
    "storage": '<path d="m22 31 26-13 26 13v37L48 81 22 68Zm0 0 26 13 26-13M48 44v37M22 49l26 13 26-13"/>',
    "blade": '<path d="m59 19 17 1-2 17-30 30-14-14ZM24 49l24 24M28 67l-9 9M51 43l14-14"/>',
    "prayer": '<path d="M39 71 28 56l9-27q3-7 8-3v29M57 71l11-15-9-27q-3-7-8-3v29M34 77l14-14 14 14M48 11v8M28 16l6 7M68 16l-6 7"/>',
}

# Symbol choices describe the title's subject, not an unverified game effect.
GROUPS = {
    "infinity": "infinity",
    "time": "time_traveler yog_sothoth yog-sotohort stasis acceleration cessation spacetime_manipulation spacetime_domination projection_sorcery acnologia_lord_of_ancient_times",
    "book": "divine_wisdom_core forbidden_knowledge raphael_knowledge raphael_wisdom akashic_records grimoire necronomicon lemegeton",
    "flame": "amaterasu agni cthugha velgrynd_lord_of_scorch satanael freezing_flame",
    "frost": "cthulhu gabriel velzard_lord_of_frost",
    "sun": "sunshine glorious haniel hamiel metatron surya secret_of_grace goddess_incarnation",
    "moon": "tsukiyomi coffin_of_darkness lunatic astaroth",
    "wind": "hastur veldora_lord_of_storms",
    "void": "nodens azathoth void_resistance nuclear_resistance",
    "poison": "deadly_poison samael",
    "scales": "michael sandalphon_judgment uriel_lord_of_oath uriel_lord_of_vow deal_maker",
    "crown": "lucifer susanoo dominator lord_of_magewolves title_manager gilgamesh_king_of_uruk arelkos true_hero",
    "soul": "soul_shrine belial sentient_being tenebrosum ego_management demonic_power mystic_aura",
    "eye": "faust investigator concentrator future_attack_prediction mood_maker",
    "exchange": "snatch divide alternative holy_demonic_inversion witches_envy witches_greed leviathan mammon scavenger nyarlathotep",
    "gift": "gift astraea raguel endorse",
    "mirror": "imitator mimicry alteration",
    "shield": "avalon saint ideal",
    "lock": "lock",
    "home": "domicile inner_world",
    "music": "cadence elegy",
    "growth": "carnation shub_niggurath food_chain",
    "craft": "processor robotnic designer amatsumara auto_battle_mode",
    "creation": "astral_light material_creation artist hand_of_creation elementalist",
    "destruction": "ending breaker abaddon hand_of_destruction",
    "water": "deluge",
    "earth": "velgaia_lord_of_earth babylon",
    "heart": "asmodeus tempter azazel friendship magic_regeneration godspeed_regeneration",
    "network": "handler",
    "storage": "skill_storage beelzebub beelzebuth tantalus gilgamesh_lord_of_treasures",
    "blade": "stripes",
    "prayer": "prayer sariel astarte zehirete secret_of_faith cultist belphegor",
}
THEMES = {identifier: theme for theme, names in GROUPS.items() for identifier in names.split()}
COLORS = {"flame": "#ffbb80", "frost": "#8be5ff", "sun": "#ffe09a", "moon": "#b9b2ff", "time": "#d0aeff", "void": "#c7a2ff", "poison": "#b6e67c", "growth": "#9be8ac", "heart": "#ffaebd", "destruction": "#ffafa5", "scales": "#f3d397", "crown": "#f3d397"}


def icon(identifier, title):
    name = identifier.split(":", 1)[1]
    if name not in THEMES:
        raise ValueError(f"No reviewed icon subject for {identifier}")
    theme = THEMES[name]
    color = COLORS.get(theme, "#74ddec")
    suffix = "".join(word[0] for word in re.findall(r"[A-Za-z]+", title.split(",")[-1]) if word.casefold() not in {"of", "the"})[:3].upper()
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 112" role="img"><title>{html.escape(title)} emblem</title><rect x="1" y="1" width="94" height="110" rx="18" fill="#0b172a" stroke="{color}" stroke-opacity=".4"/><g fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{GLYPHS[theme]}</g><path d="M26 89h44" stroke="{color}" stroke-opacity=".4"/><text x="48" y="104" text-anchor="middle" fill="{color}" font-family="sans-serif" font-size="10" font-weight="700" letter-spacing="2">{suffix}</text></svg>\n'
