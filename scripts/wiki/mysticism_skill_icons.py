"""Original pictorial icons for active skills without reusable source media."""
from __future__ import annotations

import html


MOTIFS = {
    "mysticism:mithril_strength": (
        "#aee9f6", "#477e9e",
        '<path d="m22 73 7-25 9-7 7 6 2-13 9-4 7 6 5-2 6 7-3 23-15 13Z" fill="url(#metal)" stroke="#e3fbff" stroke-width="2.4" stroke-linejoin="round"/>'
        '<path d="m29 48 8-7 8 6 2-13 9-4 7 6 5-2" fill="none" stroke="#fff" stroke-opacity=".72" stroke-width="2"/>'
        '<path d="m29 64 13-4 13 6 14-5M43 47l1 13m14-20-3 26" fill="none" stroke="#38627f" stroke-width="2.2"/>'
        '<path d="m23 72 12-5 18 9-15 6Z" fill="#133f60" stroke="#a8eefa" stroke-width="1.5"/>'
        '<path d="M19 31h14m-7-7v14M74 20h10m-5-5v10" stroke="#b6f7ff" stroke-width="2" stroke-linecap="round"/>',
    ),
    "mysticism:gravity_flux": (
        "#c8adff", "#63429f",
        '<ellipse cx="48" cy="49" rx="33" ry="15" transform="rotate(-25 48 49)" fill="none" stroke="#cdb8ff" stroke-width="3" opacity=".7"/>'
        '<ellipse cx="48" cy="49" rx="33" ry="15" transform="rotate(34 48 49)" fill="none" stroke="#7bdaf8" stroke-width="2" opacity=".7"/>'
        '<circle cx="48" cy="49" r="19" fill="url(#core)" stroke="#eadcff" stroke-width="2.5"/>'
        '<path d="M37 43q10-11 21-1M40 57q9 7 16-2" fill="none" stroke="#f9efff" stroke-opacity=".62" stroke-width="2"/>'
        '<path d="m15 37 7-10 10 6-4 11-11 2Zm59 25 10 5-4 11-12-1-3-10Z" fill="#a796d8" stroke="#eee5ff" stroke-width="1.5"/>'
        '<circle cx="24" cy="28" r="3" fill="#fff1cb"/><circle cx="76" cy="69" r="3" fill="#a9f3ff"/>',
    ),
    "mysticism:clangorous_soul": (
        "#f5d391", "#7f592f",
        '<path d="M29 57q-4-19 7-27l12-8 12 8q11 8 7 27L48 75Z" fill="url(#metal)" stroke="#ffe7ac" stroke-width="2.5"/>'
        '<path d="m35 32-9-12m35 12 9-12M32 49 19 44m45 5 13-5" fill="none" stroke="#d9b77b" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M34 48h28M39 59l9 8 9-8" fill="none" stroke="#55432c" stroke-width="3"/>'
        '<circle cx="41" cy="42" r="3" fill="#172331"/><circle cx="55" cy="42" r="3" fill="#172331"/>'
        '<path d="M15 33q-8 15 0 29m66-29q8 15 0 29M9 25Q-2 48 9 70m78-45q11 23 0 45" fill="none" stroke="#9cebf4" stroke-width="2.4" opacity=".8"/>'
        '<path d="m40 75-8 8m24-8 8 8" stroke="#d8c190" stroke-width="3" stroke-linecap="round"/>',
    ),
    "mysticism:fourth_wall": (
        "#a5e9fa", "#35688e",
        '<path d="M20 21h22m12 0h22v22m0 11v22H54m-12 0H20V54m0-12V21" fill="none" stroke="#d3f6ff" stroke-width="5" stroke-linecap="square"/>'
        '<path d="m48 27 7 14 15 7-15 7-7 15-7-15-15-7 15-7Z" fill="url(#core)" stroke="#e6ffff" stroke-width="2"/>'
        '<path d="m48 34 3 11 11 3-11 3-3 11-3-11-11-3 11-3Z" fill="#dffaff"/>'
        '<path d="m11 14 9 9m65-9-9 9M11 82l9-9m65 9-9-9" stroke="#d9b6fb" stroke-width="2.5" opacity=".75"/>'
        '<path d="M37 21 48 9l11 12m-22 55 11 11 11-11" fill="none" stroke="#7bcce9" stroke-width="1.7" opacity=".58"/>',
    ),
}


def icon(identifier: str, title: str) -> str | None:
    if identifier not in MOTIFS:
        return None
    bright, dark, motif = MOTIFS[identifier]
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" role="img">'
        f'<title>{html.escape(title)} icon</title>'
        '<defs>'
        f'<radialGradient id="field"><stop stop-color="{dark}" stop-opacity=".68"/><stop offset="1" stop-color="#0a182a"/></radialGradient>'
        f'<linearGradient id="metal" x2="1" y2="1"><stop stop-color="#f4fcff"/><stop offset=".48" stop-color="{bright}"/><stop offset="1" stop-color="{dark}"/></linearGradient>'
        f'<radialGradient id="core"><stop stop-color="#f4ffff"/><stop offset=".42" stop-color="{bright}"/><stop offset="1" stop-color="{dark}"/></radialGradient>'
        '</defs>'
        '<rect x="1" y="1" width="94" height="94" rx="17" fill="url(#field)"/>'
        f'<rect x="3" y="3" width="90" height="90" rx="15" fill="none" stroke="{bright}" stroke-opacity=".6" stroke-width="2"/>'
        '<path d="M15 12h16M12 15v16M81 12H65M84 15v16M15 84h16M12 81V65M81 84H65M84 81V65" fill="none" stroke="#f4e1b5" stroke-opacity=".6" stroke-width="1.5"/>'
        f'{motif}</svg>\n'
    )
