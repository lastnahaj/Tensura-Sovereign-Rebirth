"""Separate race forms from upstream navigation and overview pages."""
import json
from functools import lru_cache
from pathlib import Path

RACE_GUIDES = {
    "tensura-reference/races/races.md",
    "mysticism-reference/races/races.md",
    "mysticism-reference/races/angel.md",
}

# These boundaries follow race identities, not graph reachability. A conversion
# between two identities remains a cross-family link rather than merging cards.
FAMILY_PARTITIONS = {
    "Human": ("tensura", "human enlightened-human human-saint divine-human"),
    "Wight": ("tensura", "wight wight-king spirit-skeleton divine-skeleton"),
    "Ghoul": ("tensura", "ghoul vampire vampire-overcomer vampire-lord divine-vampire"),
    "Goblin": ("tensura", "goblin hobgoblin enlightened-hobgoblin hobgoblin-saint"),
    "Ogre": ("tensura", "ogre enlightened-ogre kijin death-oni divine-fighter divine-oni mystic-oni spirit-oni wicked-oni"),
    "Mantis": ("mysticism", "mantis preying-mantis preying-mantis-insectar preying-mantis-savant divine-preying-mantis lixivant-mantis lixivant-mantis-insectar lixivant-mantis-savant divine-lixivant-mantis steel-soul-insect corrosion-soul-insect"),
    "Scorpion": ("mysticism", "scorpion deathstalker-scorpion deathstalker-scorpion-insectar deathstalker-scorpion-saint divine-deathstalker-scorpion loxodrome-scorpion loxodrome-scorpion-insectar loxodrome-scorpion-savant divine-loxodrome-scorpion singularity-scorpion singularity-scorpion-insectar singularity-scorpion-savant divine-singularity-scorpion gravity-soul-insect poison-soul-insect"),
    "Spider": ("mysticism", "spider black-spider black-spider-insectar black-spider-saint divine-black-spider knight-spider knight-spider-insectar knight-spider-saint divine-knight-spider silk-soul-insect"),
    "Phantom": ("mysticism", "phantom field-officer general staff-officer mystic-angel"),
    "Tengu": ("mysticism", "tengu tengu-saint divine-tengu"),
}

PARTITION_BY_PAGE = {
    f"{source}-reference/races/{'races-' if source == 'tensura' else ''}{slug}.md": family
    for family, (source, slugs) in FAMILY_PARTITIONS.items()
    for slug in slugs.split()
}


def family_partition(page: str) -> str | None:
    return PARTITION_BY_PAGE.get(page) or race_reference()['pages'].get(page, {}).get('family')


@lru_cache(maxsize=1)
def race_reference() -> dict:
    path = Path(__file__).resolve().parents[2] / 'data/race_reference.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'pages': {}}


def is_race_form(record: dict) -> bool:
    return (
        record["category"] == "races"
        and record["local_page"] not in RACE_GUIDES
        and record["display_title"].strip().casefold() != "races"
        and race_reference()['pages'].get(record['local_page'], {}).get('status') == 'registered'
    )
