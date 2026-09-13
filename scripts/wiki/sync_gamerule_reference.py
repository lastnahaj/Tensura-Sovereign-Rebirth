"""Generate the source-audited 1.21.1 gamerule reference."""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gamerule_reference.json"
OUTPUT = ROOT / "docs" / "tensura-reference" / "gamerules" / "index.md"
CATEGORY_LABELS = {
    "ability": "Skills & abilities",
    "existence": "EP & resources",
    "race": "Race selection",
    "tensura_player": "Player & awakening",
    "tensura_misc": "World & reset",
    "player": "Player systems",
    "misc": "Miscellaneous",
}


def load_manifest() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def display_default(rule: dict) -> str:
    value = rule["default"]
    rendered = str(value).lower() if isinstance(value, bool) else f"{value:,}"
    if rule.get("unit") == "percent":
        rendered += "%"
    return rendered


def command_default(rule: dict) -> str:
    value = rule["default"]
    rendered = str(value).lower() if isinstance(value, bool) else str(value)
    return f'/gamerule {rule["name"]} {rendered}'


def render_rule(rule: dict, sources: dict[str, dict]) -> str:
    source = sources[rule["source"]]
    category_label = "Nightmares systems" if rule["source"] == "nightmares" else CATEGORY_LABELS[rule["category"]]
    search = " ".join(
        [rule["name"], rule["description"], rule["type"], category_label, source["name"], rule.get("flag", "")]
    ).casefold()
    range_text = f'<span><b>Accepted</b>{escape(rule["range"])}</span>' if rule.get("range") else ""
    flag = f'<p class="gamerule-flag">{escape(rule["flag"])}</p>' if rule.get("flag") else ""
    status_class = " gamerule-card--pending" if rule["source"] == "nightmares" else ""
    return f'''<article class="gamerule-card{status_class}" data-gamerule-card data-gamerule-source="{escape(rule['source'])}" data-gamerule-type="{escape(rule['type'])}" data-gamerule-search="{escape(search, quote=True)}">
<header><div><p class="reference-eyebrow">{escape(category_label)}</p><h3><code>{escape(rule['name'])}</code></h3></div><span class="gamerule-source-chip">{escape(source['name'])}</span></header>
<p>{escape(rule['description'])}</p>{flag}
<div class="gamerule-values"><span><b>Default</b>{escape(display_default(rule))}</span><span><b>Type</b>{escape(rule['type'].title())}</span>{range_text}</div>
<div class="gamerule-actions"><code>{escape(command_default(rule))}</code><button type="button" data-gamerule-copy="{escape(command_default(rule), quote=True)}">Copy</button></div>
</article>'''


def render_source(source: dict, rules: list[dict]) -> str:
    pending = source["id"] == "nightmares"
    registration = f'{len(rules)} registered rule{"s" if len(rules) != 1 else ""}' if rules else "Behavior override"
    pack = f'<span>Pack record: <code>{escape(Path(source["pack_manifest"]).name)}</code></span>' if source.get("pack_manifest") else '<span>Not present in current Packwiz manifest</span>'
    pending_class = " gamerule-source-card--pending" if pending else ""
    return f'''<article class="gamerule-source-card{pending_class}">
<div><p class="reference-eyebrow">{escape(source['status'])}</p><h3>{escape(source['name'])}</h3><p>{registration}</p></div>
<dl><div><dt>Build</dt><dd>{escape(source['version'])}</dd></div><div><dt>Minecraft</dt><dd>{escape(source['minecraft'])}</dd></div></dl>
<div class="gamerule-source-meta">{pack}<span>Digest: <code>{escape(source['digest'][:12])}…</code></span></div>
<details><summary>Artifact evidence</summary><code>{escape(source['evidence'])}</code></details>
<a href="{escape(source['source_url'], quote=True)}">Release source ↗</a>
</article>'''


def generate() -> str:
    data = load_manifest()
    sources = {source["id"]: source for source in data["sources"]}
    rules = data["rules"]
    installed_rules = sum(rule["source"] != "nightmares" for rule in rules)
    boolean_count = sum(rule["type"] == "boolean" for rule in rules)
    cards = "\n".join(render_rule(rule, sources) for rule in rules)
    source_cards = "\n".join(render_source(source, [r for r in rules if r["source"] == source["id"]]) for source in data["sources"])
    source_buttons = "".join(
        f'<button type="button" data-gamerule-source-filter="{escape(source["id"])}" aria-pressed="false">{escape(source["name"])}</button>'
        for source in data["sources"] if source["id"] != "stextras"
    )
    return f'''<section class="gamerule-reference" data-gamerule-reference>
<header class="gamerule-hero">
<div><p class="reference-eyebrow">TSR 1.21.1 world policy</p><h1>Gamerules you can trust</h1><p>Search the exact names registered by each reviewed artifact, understand the default, and copy a ready-to-run command without translating an outdated wiki table.</p><div class="gamerule-hero-stats"><span><strong>{len(rules)}</strong> registered rules</span><span><strong>{installed_rules}</strong> installed-source rules</span><span><strong>{boolean_count}</strong> toggles</span></div></div>
<div class="gamerule-hero-terminal" aria-hidden="true"><span>WORLD RULE CONSOLE</span><code>/gamerule skillGriefing false</code><code>/gamerule doAscensionUltimate true</code><b>OPERATOR REQUIRED</b></div>
</header>

<aside class="gamerule-admin-note"><strong>Administrator command</strong><p>Use <code>/gamerule &lt;name&gt;</code> to read the current world value, or <code>/gamerule &lt;name&gt; &lt;value&gt;</code> to change it. Gamerules are stored with the world and require sufficient command permission. A jar default is not proof that the live server still uses that value.</p></aside>

<div class="gamerule-tools">
<label><span>Find a gamerule</span><input type="search" data-gamerule-search-input placeholder="Try EP, awakening, griefing, soul…" autocomplete="off"></label>
<div class="gamerule-filter-row" aria-label="Filter by source"><button type="button" class="is-active" data-gamerule-source-filter="all" aria-pressed="true">All sources</button>{source_buttons}</div>
<div class="gamerule-filter-row" aria-label="Filter by value type"><button type="button" class="is-active" data-gamerule-type-filter="all" aria-pressed="true">All values</button><button type="button" data-gamerule-type-filter="boolean" aria-pressed="false">Toggles</button><button type="button" data-gamerule-type-filter="integer" aria-pressed="false">Numbers</button></div>
<p data-gamerule-status aria-live="polite">Showing {len(rules)} of {len(rules)} registered rules</p>
</div>

<div class="gamerule-grid">{cards}</div>
<div class="gamerule-no-results" data-gamerule-no-results hidden><strong>No matching gamerule</strong><span>Clear the search or reset both filters.</span></div>

<aside class="gamerule-nightmares-note"><strong>Nightmares is isolated on purpose</strong><p>The 1.21.1 reference artifact registers 15 rules, but its content jar is not recorded in TSR's current Packwiz manifest. Those cards are visibly marked as reference-build data. The artifact also disagrees with the current community table on names and defaults; the exact class registration shown here wins.</p></aside>

<section class="gamerule-sources"><div><p class="reference-eyebrow">Build evidence</p><h2>Where each rule came from</h2><p>Four artifacts register rules. SlimeThrone Extras registers none, but its mixins force <code>resetPerSkillLock</code> to zero, so that effective behavior is included too.</p></div><div class="gamerule-source-grid">{source_cards}</div></section>

<details class="gamerule-archive"><summary>Upstream articles, differences, and licensing</summary><p>The old <a href="config-gamerules/">imported Tensura article</a> remains for provenance only. Current community references: <a href="https://tensura.wiki.gg/wiki/Config/Gamerules">Tensura gamerules</a> and <a href="https://tensuranightmares.wiki.gg/wiki/Gamerules">Nightmares gamerules</a>. Their explanatory text is available under CC BY-SA 4.0. Names, defaults, and inclusion on this landing page come from the exact reviewed 1.21.1 classes. Obsolete or mismatched names intentionally excluded: <code>{escape(', '.join(data['excluded_obsolete_names']))}</code>.</p></details>
</section>
'''


def validate(data: dict) -> None:
    assert len(data["rules"]) == 55
    assert len({(rule["source"], rule["name"]) for rule in data["rules"]}) == 55
    assert {rule["type"] for rule in data["rules"]} == {"boolean", "integer"}
    for source in data["sources"]:
        if source.get("pack_manifest"):
            selection = (ROOT / source["pack_manifest"]).read_text(encoding="utf-8")
            assert source["digest"] in selection, f'Gamerule source selection changed: {source["name"]}'
    rules = {(rule["source"], rule["name"]): rule for rule in data["rules"]}
    assert rules[("tensura", "resetPerSkillLock")]["default"] == 0
    assert rules[("nightmares", "trulygodclass")]["default"] is True
    assert rules[("nightmares", "god_skills")]["default"] is False
    assert rules[("ascension", "doAscensionUltimate")]["default"] is True
    assert rules[("mysticism", "uniqueSECost")]["default"] is True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = load_manifest()
    validate(data)
    content = generate()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            raise SystemExit(f"Stale gamerule reference: {OUTPUT}")
    else:
        OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f'Gamerule reference {"checked" if args.check else "generated"}: {len(data["rules"])} rules')


if __name__ == "__main__":
    main()
