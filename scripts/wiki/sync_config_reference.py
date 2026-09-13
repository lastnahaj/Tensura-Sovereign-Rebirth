"""Generate the player-facing configuration control center."""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "config_reference.json"
OUTPUT = ROOT / "docs" / "tensura-reference" / "configuration" / "index.md"
REPO = "https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/"


def load_manifest() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def files_for(group: dict) -> list[Path]:
    files = {ROOT / path for path in group.get("paths", [])}
    for pattern in group.get("globs", []):
        files.update(path for path in ROOT.glob(pattern) if path.is_file())
    return sorted(files)


def render_group(group: dict, sources: dict[str, dict]) -> str:
    files = files_for(group)
    source_chips = "".join(
        f'<span class="config-source-chip">{escape(sources[source]["name"])}</span>'
        for source in group["sources"]
    )
    facts = "".join(f"<li>{escape(fact)}</li>" for fact in group.get("facts", []))
    paths = "".join(
        f'<li><a href="{REPO}{escape(path.relative_to(ROOT).as_posix(), quote=True)}"><code>{escape(path.relative_to(ROOT / "pack" / "config").as_posix())}</code></a></li>'
        for path in files
    )
    search = " ".join(
        [group["title"], group["summary"], group["category"], *group["sources"], *group.get("facts", []), *(path.name for path in files)]
    ).casefold()
    facts_block = f'<ul class="config-facts">{facts}</ul>' if facts else ""
    return f'''<article class="config-card" data-config-card data-config-category="{escape(group['category'])}" data-config-search="{escape(search, quote=True)}">
<header><div class="config-card-icon" aria-hidden="true"><span></span><i></i><b></b></div><div><p class="reference-eyebrow">{escape(group['category'])}</p><h2>{escape(group['title'])}</h2></div><strong class="config-file-count">{len(files)} file{'s' if len(files) != 1 else ''}</strong></header>
<p>{escape(group['summary'])}</p>
<div class="config-source-chips">{source_chips}</div>
{facts_block}
<details><summary>Open tracked files</summary><ul class="config-file-list">{paths}</ul></details>
</article>'''


def generate() -> str:
    data = load_manifest()
    sources = {source["id"]: source for source in data["sources"]}
    all_files = {path for group in data["groups"] for path in files_for(group)}
    source_cards = "".join(
        f'''<a class="config-build-card" href="{escape(source['url'], quote=True)}"><span>{escape(source['name'])}</span><strong>{escape(source['version'])}</strong><small>{escape(source['digest'][:10])}…</small></a>'''
        for source in data["sources"]
    )
    group_cards = "\n".join(render_group(group, sources) for group in data["groups"])
    filters = "".join(
        f'<button type="button" data-config-filter="{category}" aria-pressed="false">{label}</button>'
        for category, label in (("progression", "Progression"), ("gameplay", "Gameplay"), ("world", "World"), ("client", "Client"), ("server", "Server"))
    )
    return f'''<section class="config-reference" data-config-reference>
<header class="config-hero">
<div><p class="reference-eyebrow">TSR 1.21.1 control center</p><h1>Configuration without the guesswork</h1><p>Start with the system you want to change, then open the exact reviewed file that controls it. Values shown here come from the configuration shipped by TSR.</p><div class="config-hero-stats"><span><strong>{len(data['groups'])}</strong> control groups</span><span><strong>{len(all_files)}</strong> tracked files</span><span><strong>{len(data['sources'])}</strong> pinned sources</span></div></div>
<div class="config-hero-console" aria-hidden="true"><span>WORLD POLICY</span><div><i></i><b>Progression</b><em>LOCKED</em></div><div><i></i><b>Mob rules</b><em>TRACKED</em></div><div><i></i><b>Client HUD</b><em>READY</em></div></div>
</header>

<aside class="config-scope-note"><strong>Before changing anything</strong><p>The repository is the pack baseline—not a live-server settings dump. Client files affect presentation; common files affect gameplay; world-scoped settings may require a restart or a new world. Back up the server before changing progression or world-generation rules.</p></aside>

<div class="config-tools">
<label><span>What do you want to configure?</span><input type="search" data-config-search-input placeholder="Try reincarnation, HUD, spawn, prestige…" autocomplete="off"></label>
<div class="config-filters" aria-label="Filter configuration groups"><button type="button" class="is-active" data-config-filter="all" aria-pressed="true">All systems</button>{filters}</div>
<p data-config-status aria-live="polite">Showing {len(data['groups'])} of {len(data['groups'])} control groups</p>
</div>

<div class="config-grid">{group_cards}</div>
<div class="config-no-results" data-config-no-results hidden><strong>No matching control group</strong><span>Clear the search or choose All systems.</span></div>

<section class="config-builds"><div><p class="reference-eyebrow">Build evidence</p><h2>Pinned sources behind these settings</h2><p>Each card opens the release selected by the matching Packwiz manifest. The short digest is shown so a similarly named build cannot be mistaken for TSR's version.</p></div><div class="config-build-grid">{source_cards}</div></section>

<aside class="config-nightmares-note"><strong>About Tensura Nightmares</strong><p>Nightmare Utils is pinned and its optional systems are represented above. The Tensura Nightmares content jar itself is still not recorded by the current Packwiz manifest, so this page does not invent live Nightmares configuration or present reference-build defaults as server settings.</p></aside>

<details class="config-archive"><summary>Upstream and administrator reference</summary><div><a href="config/">Imported Tensura configuration article</a><a href="config-client/">Imported client article</a><a href="config-spawnrate-common/">Historical spawn-rate article</a><a href="../gamerules/">Imported gamerules</a><a href="../../server-administration/">Server administration</a><a href="../../permissions/">Permissions</a></div><p>Imported pages are retained for attribution and historical context. When they disagree with the control center, the tracked 1.21.1 files above are authoritative for this repository.</p></details>
</section>
'''


def validate(data: dict) -> None:
    for source in data["sources"]:
        manifest = (ROOT / source["manifest"]).read_text(encoding="utf-8")
        assert source["digest"] in manifest, f'Source selection changed: {source["name"]}'
    for group in data["groups"]:
        assert files_for(group), f'Configuration group has no files: {group["id"]}'
    config = ROOT / "pack" / "config"
    reincarnation = tomllib.loads((config / "tensura/reincarnation_config.toml").read_text(encoding="utf-8"))
    assert len(reincarnation["Races"]["startingRaces"]) == 28
    assert len(reincarnation["Skills"]["startingSkills"]) == 78
    assert reincarnation["Skills"]["skillNumber"] == 1
    spawns = tomllib.loads((config / "tensura/entity/spawn_rate_config.toml").read_text(encoding="utf-8"))
    assert len(spawns["SpawnChance"]) == 43
    hud = tomllib.loads((config / "tensura/client/hud_config.toml").read_text(encoding="utf-8"))
    assert hud["tensuraHud"] is True and hud["vanillaHud"] is False
    prestige = tomllib.loads((config / "stextras/prestige_config.toml").read_text(encoding="utf-8"))
    assert prestige["allowRepeatedPrestigeBossKills"] is True
    assert prestige["ImmediateRaceQuests"] is False and prestige["prestigeQuestRerollMode"] == "NONE"
    beyond = tomllib.loads((config / "beyond_gacha_c.toml").read_text(encoding="utf-8"))
    assert beyond["targeting"]["maxCharactersDeployed"] == 3
    assert beyond["targeting"]["gachaCharacterGriefing"] is False
    for name in ("autocast.json", "mob_trading.json", "skill_rewards.json", "spawn_profiles.json"):
        assert json.loads((config / "nightmareutils" / name).read_text(encoding="utf-8"))["enabled"] is False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = load_manifest()
    validate(data)
    content = generate()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            raise SystemExit(f"Stale configuration reference: {OUTPUT}")
    else:
        OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f'Configuration reference {"checked" if args.check else "generated"}: {len(data["groups"])} groups')


if __name__ == "__main__":
    main()
