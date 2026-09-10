"""Render release-scoped Nightmares encounters and materials into shared sections."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data/nightmares_world_reference.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def generate():
    manifest = load_manifest()
    build = manifest["reference_build"]
    result = {}
    for page in manifest["pages"]:
        title = page["display_title"]
        lines = [
            "---", f"title: {title}", "---", "", f"# {title}", "",
            page["summary"], "",
            '!!! warning "1.21.1 reference — server build match pending"', "",
            f'    Verified against Nightmares **{build["version"]}**. The server\'s exact Nightmares release has not been confirmed; availability and settings can differ.', "",
            '<div class="tensura-reference-article">',
            '<div class="druid-container reference-release-stats"><aside class="druid-infobox">',
            f'<div class="druid-title">{html.escape(title)}</div>',
        ]
        for label, value in page["stats"].items():
            lines.append(f'<div class="druid-row"><div class="druid-label">{html.escape(label)}</div><div class="druid-data">{html.escape(value)}</div></div>')
        lines.extend(['</aside></div></div>', "", f'**Registry ID:** `{page["registry_id"]}`', ""])
        for section in page["sections"]:
            lines.extend([f'## {section["title"]}', ""])
            for paragraph in section["paragraphs"]:
                lines.extend([paragraph, ""])
        lines.extend([
            '??? info "Sources and verification"', "",
            f'    [Reference release]({build["source_url"]}) · [Upstream article]({page["source_url"]}) · [Reviewed revision](https://tensuranightmares.wiki.gg/index.php?oldid={page["revision_id"]})', "",
            f'    Artifact SHA-256: `{build["sha256"]}`.', "",
            '    Verification: registry identity and relevant entity definitions or event conditions were inspected in the release artifact. No mod was executed to perform this check.', "",
            '    Evidence classes in `com.github.hvnbael.trnightmare`:', "",
        ])
        for name in page["evidence_classes"]:
            lines.append(f'    - `{name}`')
        lines.extend(["", f'    Adapted source context: Tensura Reincarnated Nightmares Wiki contributors, [CC BY-SA 4.0]({manifest["text_license"]}). Release-specific corrections and verification notes are identified above.', "", f'    {page["media_note"]}', "", '[Back to the collection](index.md)', ""])
        result[page["local_page"]] = "\n".join(lines)
    return result


def records():
    return [{**page, "reference_build_only": True, "_supplementary": True,
             "_omit_media": True, "_html": f'<p>{html.escape(page["summary"])}</p>',
             "_stat_source_note": "Reference release values; server build match pending."}
            for page in load_manifest()["pages"]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for name, content in generate().items():
        path = ROOT / "docs" / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale Nightmares world page: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f'Nightmares world pages {"checked" if args.check else "generated"}: {len(generate())}')


if __name__ == "__main__":
    main()
