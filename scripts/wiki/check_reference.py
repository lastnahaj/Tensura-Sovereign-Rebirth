#!/usr/bin/env python3
"""Validate generated reference collections, manifests, links, and media."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
REFERENCE_SCRIPT = DOCS / "assets" / "javascripts" / "reference.js"
REFERENCE_ART = (
    DOCS / "assets" / "images" / "reference-races-evolution.png",
    DOCS / "assets" / "images" / "reference-skills-magic.png",
    DOCS / "assets" / "images" / "reference-bestiary.png",
    DOCS / "assets" / "images" / "reference-world-equipment.png",
)
COLLECTIONS = (
    {
        "label": "Tensura",
        "slug": "tensura-reference",
        "data_stem": "upstream_tensura",
        "source_host": "tensura.wiki.gg",
        "asset_namespace": "tensura",
    },
    {
        "label": "TR Mysticism",
        "slug": "mysticism-reference",
        "data_stem": "upstream_mysticism",
        "source_host": "trmysticism.wiki.gg",
        "asset_namespace": "mysticism",
    },
)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def markdown_outside_html(text: str) -> str:
    """Exclude generated raw-HTML rows from Markdown-link detection."""
    return "\n".join(
        line
        for line in text.splitlines()
        if not (line.lstrip().startswith("<") and line.rstrip().endswith(">"))
    )


def validate_collection(spec: dict[str, str], errors: list[str]) -> dict[str, int]:
    label = spec["label"]
    reference = DOCS / spec["slug"]
    data_stem = spec["data_stem"]
    source_host = spec["source_host"]
    asset_prefix = f"assets/upstream/{spec['asset_namespace']}/"
    pages_manifest = load(f"{data_stem}_pages.json")
    media_manifest = load(f"{data_stem}_media.json")
    coverage = load(f"{data_stem}_coverage.json")

    pages = pages_manifest.get("pages", [])
    skipped_pages = pages_manifest.get("skipped_pages", [])
    redirects = pages_manifest.get("redirects", [])
    media = media_manifest.get("media", [])
    expected_pages = coverage.get("pages_imported")
    if len(pages) != expected_pages:
        errors.append(f"{label}: page manifest contains {len(pages)} records; coverage reports {expected_pages}")
    if coverage.get("pages_failed") != len(pages_manifest.get("failed_pages", [])):
        errors.append(f"{label}: page failure count does not match the failure manifest")
    if coverage.get("pages_skipped") != len(skipped_pages):
        errors.append(f"{label}: page skip count does not match the skipped-page manifest")
    if coverage.get("upstream_pages_discovered") != len(pages) + len(skipped_pages) + len(
        pages_manifest.get("failed_pages", [])
    ):
        errors.append(f"{label}: canonical discovery count does not match imported, skipped, and failed pages")
    if coverage.get("redirects_discovered") != len(redirects):
        errors.append(f"{label}: redirect discovery count does not match the redirect manifest")
    if coverage.get("image_file_records_resolved") != len(media):
        errors.append(f"{label}: resolved File-record count does not match the media manifest")
    if coverage.get("images_discovered", 0) < len(media):
        errors.append(f"{label}: media discovery count is smaller than the resolved File-record count")

    redirect_statuses = {"processed": 0, "skipped": 0, "failed": 0}
    for record in redirects:
        status = record.get("status", "failed")
        redirect_statuses[status] = redirect_statuses.get(status, 0) + 1
    for status, key in (
        ("processed", "redirects_processed"),
        ("skipped", "redirects_skipped"),
        ("failed", "redirects_failed"),
    ):
        if coverage.get(key) != redirect_statuses.get(status, 0):
            errors.append(f"{label}: redirect {status} count does not match the redirect manifest")

    local_page_set: set[str] = set()
    for record in pages:
        local_page = record.get("local_page", "")
        if not local_page or local_page in local_page_set:
            errors.append(f"{label}: missing or duplicate local page for {record.get('source_title')}")
            continue
        local_page_set.add(local_page)
        path = DOCS / local_page
        if not path.is_file():
            errors.append(f"{label}: missing generated article {local_page}")
            continue
        text = path.read_text(encoding="utf-8")
        if "## Source and licensing" not in text or record.get("source_url", "") not in text:
            errors.append(f"{label}: missing source attribution in {local_page}")
        if 'class="reference-overview ' not in text or 'class="tensura-reference-article"' not in text:
            errors.append(f"{label}: missing interactive article structure in {local_page}")
        if f"{source_host}/images/" in text or f"{source_host}/images\\" in text:
            errors.append(f"{label}: hotlinked upstream image in {local_page}")

    imported_media = [record for record in media if record.get("import_status") == "imported"]
    failed_media = [record for record in media if record.get("import_status") == "failed"]
    if coverage.get("images_failed") != len(failed_media):
        errors.append(f"{label}: media failure count does not match the media manifest")
    for record in imported_media:
        local_path = record.get("local_path", "")
        if not local_path or not (DOCS / local_path).is_file():
            errors.append(f"{label}: missing imported media file for {record.get('source_title')}")
        elif not local_path.startswith(asset_prefix):
            errors.append(f"{label}: media escaped its asset namespace: {local_path}")
        if not record.get("license") or not record.get("source_file_page"):
            errors.append(f"{label}: incomplete license/source record for {record.get('source_title')}")
        if not record.get("used_on"):
            errors.append(f"{label}: imported but unused media {record.get('source_title')}")

    category_indexes = sorted(path for path in reference.rglob("index.md") if path != reference / "index.md")
    for path in category_indexes:
        text = path.read_text(encoding="utf-8")
        if 'data-reference-directory=' not in text:
            errors.append(f"{label}: missing interactive directory structure in {path.relative_to(DOCS)}")
        hero_title = re.search(
            r'<header class="reference-directory-hero[^>]*>.*?<h1>([^<]+)</h1>',
            text,
            re.DOTALL,
        )
        card_titles = re.findall(r'<div class="reference-card-copy">\s*<h2>([^<]+)</h2>', text)
        if hero_title and any(
            html.unescape(card_title).strip().casefold()
            == html.unescape(hero_title.group(1)).strip().casefold()
            for card_title in card_titles
        ):
            errors.append(f"{label}: directory repeats itself as a card in {path.relative_to(DOCS)}")

    broken: list[str] = []
    for page in sorted(reference.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(markdown_outside_html(text)):
            target = html.unescape(raw_target).strip().split()[0].strip("<>")
            if "\\" in target and not target.startswith(("http://", "https://")):
                errors.append(f"{page.relative_to(ROOT)} -> non-portable backslash link {target}")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if target and not (page.parent / target).resolve().exists():
                broken.append(f"{page.relative_to(ROOT)} -> missing {target}")
        for raw_target in HTML_LINK_RE.findall(text):
            target = html.unescape(raw_target).strip().split()[0].strip("<>")
            if "\\" in target and not target.startswith(("http://", "https://")):
                errors.append(f"{page.relative_to(ROOT)} -> non-portable backslash link {target}")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            rendered_dir = page.parent if page.name == "index.md" else page.with_suffix("")
            candidate = (rendered_dir / target).resolve()
            if target.endswith("/"):
                source_candidate = candidate / "index.md" if candidate.is_dir() else Path(
                    str(candidate).rstrip("\\/") + ".md"
                )
            else:
                source_candidate = candidate
            if not source_candidate.exists():
                broken.append(f"{page.relative_to(ROOT)} -> missing rendered target {target}")
    errors.extend(broken)
    if coverage.get("broken_links_remaining") != len(broken):
        errors.append(
            f"{label}: coverage broken-link count does not match the post-generation audit "
            f"({coverage.get('broken_links_remaining')} reported, {len(broken)} found)"
        )

    return {
        "pages": len(pages),
        "redirects": len(redirects),
        "media": len(media),
        "imported_media": len(imported_media),
    }


def main() -> int:
    errors: list[str] = []
    if not REFERENCE_SCRIPT.is_file():
        errors.append("Missing interactive reference script")
    for asset in REFERENCE_ART:
        if not asset.is_file():
            errors.append(f"Missing reference artwork {asset.relative_to(ROOT)}")

    totals = {"pages": 0, "redirects": 0, "media": 0, "imported_media": 0}
    summaries: list[str] = []
    for spec in COLLECTIONS:
        counts = validate_collection(spec, errors)
        for key, value in counts.items():
            totals[key] += value
        summaries.append(
            f"{spec['label']}: {counts['pages']} articles, {counts['imported_media']} imported images"
        )

    if errors:
        raise SystemExit("Generated reference validation failed:\n- " + "\n- ".join(sorted(set(errors))))

    print(
        "Generated references OK: "
        f"{totals['pages']} articles, {totals['redirects']} redirects, {totals['media']} media records, "
        f"{totals['imported_media']} imported media files, 0 broken local links "
        f"({'; '.join(summaries)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
