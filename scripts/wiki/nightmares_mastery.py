"""Apply only class-matched Nightmares mastery defaults to skill articles."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVIEW_URL = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/nightmares_mastery_reference.json'


def review():
    return json.loads((ROOT / 'data/nightmares_mastery_reference.json').read_text(encoding='utf-8'))


def apply(text, decision):
    data = review()
    if decision.get('id') not in data['skills']:
        return text, ''
    value = data['configuration']['default']
    pattern = r'(<div class="druid-data druid-data-PointstoMaster[^>]*>).*?(</div>)'
    text, count = re.subn(pattern, lambda m: m[1] + f'{value:,} (reference default)' + m[2], text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f'Missing mastery infobox: {decision["id"]}')
    # The detailed acquisition guides already explain the same mastery value.
    if decision.get('id') in {'trnightmare:lucifer', 'trnightmare:belphegor'}:
        return text, ''
    note = f'<aside class="skill-evidence-note skill-mastery-note"><strong>Mastery target:</strong> {value:,} points in the reviewed reference default, from <code>{data["configuration"]["key"]}</code>. This is the skill’s own mastery target, not a predecessor unlock condition or a verified server setting. <a href="{REVIEW_URL}">Mastery evidence</a>.</aside>'
    return text, note
