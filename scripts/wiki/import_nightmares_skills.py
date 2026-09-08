"""Import registry-matched Nightmares skill references from the reviewed cache.

Only the skill collection is in scope. No race imports, game installation, or
server-version assertions are made here. Run audit_nightmares_skills.py first.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import sync_tensura_wiki as wiki
from audit_nightmares_skills import REFERENCE

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".build/nightmares-skill-audit"
MANIFEST = ROOT / "data/nightmares_skill_reference.json"
# The source explicitly excludes this variant from normal gameplay acquisition.
HELD = {"trnightmare:sandalphon_punishment": "The source lists no normal gameplay obtainment route."}


def clean_title(value):
    return value.strip("｢｣「」 ")


def import_pages():
    report = json.loads((CACHE / "report.json").read_text(encoding="utf-8"))
    if report["reference_build"] != REFERENCE:
        raise ValueError("The audit does not match the configured reference release")
    wiki.configure_source("tensura")
    wiki.WIKI_ROOT = "https://tensuranightmares.wiki.gg"
    wiki.SOURCE_WIKI_NAME = "Tensura Reincarnated Nightmares Wiki"
    wiki.SOURCE_BADGE = "Tensura Nightmares reference"
    records, held = [], []
    for page in report["pages"]:
        identifier = page["registry_id"]
        if not identifier or identifier in HELD:
            held.append({"source_title": page["source_title"], "source_url": page["source_url"], "revision_id": page["revision_id"], "registry_id": identifier, "reason": HELD.get(identifier, "No unambiguous match to the reference registry.")})
            continue
        registry = report["registry"][identifier]
        category = registry["registry_category"]
        slug = identifier.split(":", 1)[1].replace("_", "-")
        parsed = json.loads((CACHE / f'api/parse/{page["page_id"]}-{page["revision_id"]}.json').read_text(encoding="utf-8"))["parse"]
        if parsed["revid"] != page["revision_id"]:
            raise ValueError(f"Cached source revision mismatch: {page['source_title']}")
        record = {"page_id": page["page_id"], "display_title": clean_title(page["display_title"]), "source_title": page["source_title"], "source_url": page["source_url"], "revision_id": page["revision_id"], "upstream_modified": page["modified"], "category": category, "local_page": f"tensura-reference/{category}/nightmares-{slug}.md", "registry_id": identifier, "asset": f"assets/icons/skills/{identifier.replace(':', '-')}.svg", "_html": parsed["text"]}
        record["upstream_categories"] = page["collection_categories"]
        record["obtainment_rows"] = [row for row in page["rows"] if row["section"].casefold() == "obtaining" and row["text"] not in {"", "None", "NA", "N/A", "[[]]"}]
        records.append(record)
    if len({record["registry_id"] for record in records}) != len(records):
        raise ValueError("Two source articles resolved to one registry entry")
    canonical = {wiki.normalize_title(record["source_title"]): record for record in records}
    for record in records:
        # Images are not automatically covered by the article text license.
        # Existing TSR emblems provide local media without relabeling game art.
        body, _, _, _ = wiki.clean_article_html(record, canonical, {}, {})
        soup = BeautifulSoup(body, "html.parser")
        for element in list(soup.find_all(True)):
            for attr in list(element.attrs):
                if attr.lower().startswith("on"):
                    del element[attr]
            if element.name in {"iframe", "object", "embed", "form", "input"}:
                element.decompose()
        for anchor in soup.select("a[href]"):
            if re.match(r"\s*(?:javascript|data):", anchor["href"], re.I):
                del anchor["href"]
        # Remove WIP editorial banners rather than treating them as gameplay.
        for node in soup.find_all(string=re.compile(r"Remove this once finalized", re.I)):
            node.extract()
        partial = False
        for paragraph in soup.find_all("p"):
            if re.fullmatch(r"\s*W\.?I\.?P\.?\s*", paragraph.get_text(), re.I):
                partial = True
                paragraph.decompose()
        record["source_partial"] = partial
        body = str(soup)
        record["summary"] = wiki.article_summary(record, body)
        if record["summary"].startswith("Upstream reference information"):
            for item in soup.select("li"):
                if item.find_parent(class_="druid-container"):
                    continue
                summary = re.sub(r"^\[[^]]+\]\s*", "", item.get_text(" ", strip=True))
                if len(summary) >= 24:
                    record["summary"] = summary[:357].rsplit(" ", 1)[0] + "…" if len(summary) > 360 else summary
                    break
        record["description"] = record["summary"]
        for frame in soup.select(".druid-main-image"):
            frame.decompose()
        body = re.sub(r"[ \t]+\n", "\n", str(soup))
        output = wiki.render_page(record, body, [], None, 0, [])
        output = re.sub(r'(<figure class="reference-overview-media[^>]*>).*?(</figure>)', lambda m: m[1] + f'<img src="{wiki.rendered_asset_relative_url(record["local_page"], record["asset"])}" alt="{html.escape(record["display_title"], quote=True)} emblem" width="96" height="96"><figcaption>TSR skill emblem</figcaption>' + m[2], output, count=1, flags=re.S)
        output += "\nSkill emblems are original TSR interface icons, not in-game artwork.\n"
        destination = ROOT / "docs" / record["local_page"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output, encoding="utf-8", newline="\n")
        record.pop("_html")
    manifest = {"schema": 1, "reference_build": REFERENCE, "text_license": report["text_license"], "pages": records, "held_pages": held, "registry": report["registry"], "registry_without_article": report["registry_without_article"]}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    wiki.configure_source("tensura")
    from sync_skill_catalogue import generate
    for name, content in generate().items():
        path = ROOT / "docs" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Nightmares skills imported: {len(records)} reference-build entries; {len(held)} held sources")


if __name__ == "__main__":
    import_pages()
