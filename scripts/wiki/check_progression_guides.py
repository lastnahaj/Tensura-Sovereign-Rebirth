"""Validate pack-scoped progression guides and their interactive components."""

from pathlib import Path
import tomllib

from bs4 import BeautifulSoup
import yaml


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
SITE = ROOT / "site"


def read_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


nav = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))["nav"]
mechanics = next(item["Mechanics"] for item in nav if "Mechanics" in item)
progression = next(item["Progression"] for item in mechanics if isinstance(item, dict) and "Progression" in item)
expected_pages = {
    "progression-overview.md",
    "prestige-and-soul-grade.md",
    "quests-and-reincarnation-essence.md",
    "race-prestige-requirements.md",
    "beyond-adventures.md",
    "ascension-and-awakening.md",
}
assert {next(iter(item.values())) for item in progression} == expected_pages, "Progression navigation is incomplete"

skill_config = read_toml(ROOT / "pack/config/stextras/skill_lock_config.toml")
prestige_config = read_toml(ROOT / "pack/config/stextras/prestige_config.toml")
beyond_config = read_toml(ROOT / "pack/config/beyond_gacha_c.toml")
beyond_manifest = read_toml(ROOT / "pack/mods/beyond-adventures.pw.toml")
extras_manifest = read_toml(ROOT / "pack/mods/tensura-slimethrone-extras.pw.toml")

prestige_source = (DOCS / "prestige-and-soul-grade.md").read_text(encoding="utf-8")
assert skill_config["getNeededEPToUnlockSkill"] == 10_000_000
assert "10,000,000 EP" in prestige_source
assert str(skill_config["getSoulGradeCostToUnlockSkill"]) + " Soul Grade" in prestige_source
assert skill_config["maxLocksPerLevel"] == [0, 1, 1, 2, 2, 2, 3]
assert prestige_config["ignoreLockedSkillsOnReset"] is False
for skill_id in skill_config["validSkillsTOLock"]:
    display_name = skill_id.split(":", 1)[1].replace("_", " ").title()
    assert display_name in prestige_source, f"Configured lockable skill missing from guide: {display_name}"

race_page = BeautifulSoup((SITE / "race-prestige-requirements/index.html").read_text(encoding="utf-8"), "html.parser")
assert len(race_page.select("[data-prestige-card]")) == 18, "Race-prestige directory must contain 18 challenges"
assert race_page.select_one("[data-prestige-search]") and race_page.select_one("[data-prestige-count]")
assert prestige_config["ImmediateRaceQuests"] is False
assert prestige_config["disabledRacePrestigeRaces"] == []
assert prestige_config["prestigeQuestRerollMode"] == "NONE"
assert prestige_config["questREBoost"] is True
assert prestige_config["questREBoostAmount"] == 0.05
assert prestige_config["questREBoostDaily"] is True and prestige_config["questREBoostWeekly"] is True
assert prestige_config["questREBoostRequired"] is False and prestige_config["questREBoostRepeatable"] is False

prestige_page = BeautifulSoup((SITE / "prestige-and-soul-grade/index.html").read_text(encoding="utf-8"), "html.parser")
assert prestige_page.select_one("[data-soul-grade-calculator]")
assert prestige_page.select_one("script[src$='progression-guide.js']")

quest_source = (DOCS / "quests-and-reincarnation-essence.md").read_text(encoding="utf-8")
for expected_count in ("229", "47", "688", "18", "1,000"):
    assert expected_count in quest_source, f"Quest guide missing verified count: {expected_count}"

assert extras_manifest["filename"] == "SlimeThroneExtras-neoforge-2.1.2.1.jar"
assert beyond_manifest["filename"] == "Beyond_Adventures-Neoforge-1.1.9.jar"
assert beyond_manifest["download"]["hash-format"] == "sha512"
beyond_source = (DOCS / "beyond-adventures.md").read_text(encoding="utf-8")
assert beyond_manifest["download"]["hash"] in beyond_source
assert "Tensura: Dungeon is not installed" in beyond_source
assert "Dungeon NPC shops" in beyond_source and "Colosseum systems" in beyond_source
assert beyond_config["targeting"]["maxCharactersDeployed"] == 3
assert beyond_config["targeting"]["gachaCharacterGriefing"] is False
assert beyond_config["general"]["enableDailyPopup"] is True

for asset in ("prestige-progression.webp", "beyond-adventures.webp"):
    assert (DOCS / "assets/images/guides" / asset).is_file(), f"Missing progression guide artwork: {asset}"

print("Progression guides passed: pack versions, configuration, 18 race challenges, interactivity, and 1.21.1 scope")
