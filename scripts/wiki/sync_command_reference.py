"""Generate the 1.21.1 command reference from the audited command manifest."""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "command_reference.json"
OUTPUT = ROOT / "docs" / "tensura-reference" / "commands" / "index.md"


def load_manifest() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def render_entry(entry: dict, source_id: str) -> str:
    search = " ".join(
        [entry["command"], entry["access"], entry["purpose"], source_id, *entry["branches"]]
    ).casefold()
    branches = ""
    if entry["branches"]:
        chips = "".join(f"<code>{escape(branch)}</code>" for branch in entry["branches"])
        branches = f'<div class="command-branches" aria-label="Registered branches">{chips}</div>'
    return f'''<article class="command-entry" data-command-source="{source_id}" data-command-access="{escape(entry['access'].casefold())}" data-command-search="{escape(search, quote=True)}">
<header><code>{escape(entry['command'])}</code><span class="command-access command-access--{escape(entry['access'].casefold())}">{escape(entry['access'])}</span></header>
<p>{escape(entry['purpose'])}</p>
{branches}
<details class="command-evidence"><summary>Artifact evidence</summary><code>{escape(entry['evidence'])}</code></details>
</article>'''


def render_source(source: dict) -> str:
    entries = "\n".join(render_entry(entry, source["id"]) for entry in source["entries"])
    if not entries:
        entries = '<div class="command-empty-source">No command classes are registered by this artifact.</div>'
    note = f'<p class="command-source-note">{escape(source["note"])}</p>' if source.get("note") else ""
    pack = ""
    if source.get("pack_manifest"):
        pack = f'<span>Pack record: <code>{escape(Path(source["pack_manifest"]).name)}</code></span>'
    return f'''<section class="command-source" id="{escape(source['id'])}" data-command-source-section="{escape(source['id'])}">
<header class="command-source-header">
<div><p class="reference-eyebrow">{escape(source['status'])}</p><h2>{escape(source['name'])}</h2><p>{escape(source['summary'])}</p></div>
<div class="command-build"><strong>{escape(source['version'])}</strong><span>Minecraft {escape(source['minecraft'])}</span><a href="{escape(source['source_url'], quote=True)}">Release source ↗</a></div>
</header>
<div class="command-source-meta">{pack}<span>Digest: <code>{escape(source['digest'][:12])}…</code></span></div>
{note}
<div class="command-entry-grid">{entries}</div>
</section>'''


def generate() -> str:
    data = load_manifest()
    sources = data["sources"]
    entry_count = sum(len(source["entries"]) for source in sources)
    installed = sum(source["status"].startswith("Installed") for source in sources)
    source_links = "".join(
        f'<a href="#{escape(source["id"])}">{escape(source["name"])}</a>' for source in sources
    )
    access_buttons = "".join(
        f'<button type="button" data-command-access-filter="{escape(access.casefold())}" aria-pressed="false">{escape(access)}</button>'
        for access in data["legend"]
    )
    source_sections = "\n".join(render_source(source) for source in sources)
    legend = "".join(
        f'<div><span class="command-access command-access--{escape(access.casefold())}">{escape(access)}</span><p>{escape(text)}</p></div>'
        for access, text in data["legend"].items()
    )
    return f'''<section class="command-reference" data-command-reference>
<header class="command-hero">
<div class="command-hero-copy">
<p class="reference-eyebrow">TSR 1.21.1 operations desk</p>
<h1>Commands by source</h1>
<p>Find the command family you need, see who may run it, and keep similarly named systems separated by the mod that actually registers them.</p>
<div class="command-hero-stats"><span><strong>{len(sources)}</strong> audited artifacts</span><span><strong>{installed}</strong> installed sources</span><span><strong>{entry_count}</strong> command families</span></div>
</div>
<div class="command-hero-console" aria-hidden="true"><span>TSR COMMAND CONSOLE</span><code>&gt; /stextras player summary</code><code>&gt; /tascension checkultprogress</code><code>&gt; /ability preset set</code><b>READY</b></div>
</header>

<nav class="command-source-nav" aria-label="Command sources">{source_links}</nav>

<aside class="command-syntax-guide">
<div><strong><code>&lt;required&gt;</code></strong><span>You must supply a value.</span></div>
<div><strong><code>[optional]</code></strong><span>The command can run without it.</span></div>
<div><strong><code>…</code></strong><span>This page documents a command family; press Tab in game for its exact next argument.</span></div>
</aside>

<div class="command-tools">
<label><span>Search all command families</span><input type="search" data-command-search-input placeholder="Try prestige, soul, ability, admin…" autocomplete="off"></label>
<div class="command-access-filters" aria-label="Filter by access"><button type="button" class="is-active" data-command-access-filter="all" aria-pressed="true">All access</button>{access_buttons}</div>
<p data-command-status aria-live="polite">Showing {entry_count} of {entry_count} command families</p>
</div>

<div class="command-access-legend">{legend}</div>

{source_sections}

<div class="command-no-results" data-command-no-results hidden><strong>No matching command family</strong><span>Clear the search or switch back to All access.</span></div>

<aside class="command-verification-note">
<strong>What “verified” means here</strong>
<p>Names, roots, branches, and permission tiers come from the exact 1.21.1 artifacts recorded above. Runtime configuration can still disable a branch or change who receives permission. Nightmares is clearly marked separately because its reference jar is not yet matched to TSR's current pack manifest.</p>
</aside>

<details class="command-archive-note"><summary>Historical imported command pages</summary><p>The raw <a href="commands/">Tensura import</a> and <a href="../../mysticism-reference/commands/commands/">Mysticism 1.19.2 import</a> remain available for provenance. They are not the current command reference and may contain obsolete syntax.</p></details>
</section>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = generate()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            raise SystemExit(f"Stale command reference: {OUTPUT}")
    else:
        OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f'Command reference {"checked" if args.check else "generated"}: {sum(len(s["entries"]) for s in load_manifest()["sources"])} families')


if __name__ == "__main__":
    main()
