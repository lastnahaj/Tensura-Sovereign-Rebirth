#!/usr/bin/env python3
"""Validate the generated Tensura reference, manifests, links, and media."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
REFERENCE = DOCS / "tensura-reference"
DATA = ROOT / "data"
REFERENCE_SCRIPT = DOCS / "assets" / "javascripts" / "reference.js"
REFERENCE_ART = (
    DOCS / "assets" / "images" / "reference-races-evolution.png",
    DOCS / "assets" / "images" / "reference-skills-magic.png",
    DOCS / "assets" / "images" / "reference-bestiary.png",
    DOCS / "assets" / "images" / "reference-world-equipment.png",
)


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    pages_manifest = load("upstream_tensura_pages.json")
    media_manifest = load("upstream_tensura_media.json")
    coverage = load("upstream_tensura_coverage.json")

    if not REFERENCE_SCRIPT.is_file():
        errors.append("Missing interactive reference script")
    for asset in REFERENCE_ART:
        if not asset.is_file():
            errors.append(f"Missing reference artwork {asset.relative_to(ROOT)}")

    pages = pages_manifest.get("pages", [])
    skipped_pages = pages_manifest.get("skipped_pages", [])
    redirects = pages_manifest.get("redirects", [])
    media = media_manifest.get("media", [])
    expected_pages = coverage.get("pages_imported")
    if len(pages) != expected_pages:
        errors.append(f"Page manifest contains {len(pages)} records; coverage reports {expected_pages}")
    if coverage.get("pages_failed") != len(pages_manifest.get("failed_pages", [])):
        errors.append("Page failure count does not match the failure manifest")
    if coverage.get("pages_skipped") != len(skipped_pages):
        errors.append("Page skip count does not match the skipped-page manifest")
    if coverage.get("upstream_pages_discovered") != len(pages) + len(skipped_pages) + len(
        pages_manifest.get("failed_pages", [])
    ):
        errors.append("Canonical discovery count does not match imported, skipped, and failed pages")
    if coverage.get("redirects_discovered") != len(redirects):
        errors.append("Redirect discovery count does not match the redirect manifest")
    if coverage.get("image_file_records_resolved") != len(media):
        errors.append("Resolved File-record count does not match the media manifest")
    if coverage.get("images_discovered", 0) < len(media):
        errors.append("Media discovery count is smaller than the resolved File-record count")
    redirect_statuses = {"processed": 0, "skipped": 0, "failed": 0}
    for record in redirects:
        redirect_statuses[record.get("status", "failed")] = redirect_statuses.get(
            record.get("status", "failed"), 0
        ) + 1
    for status, key in (
        ("processed", "redirects_processed"),
        ("skipped", "redirects_skipped"),
        ("failed", "redirects_failed"),
    ):
        if coverage.get(key) != redirect_statuses.get(status, 0):
            errors.append(f"Redirect {status} count does not match the redirect manifest")

    local_page_set: set[str] = set()
    for record in pages:
        local_page = record.get("local_page", "")
        if not local_page or local_page in local_page_set:
            errors.append(f"Missing or duplicate local page for {record.get('source_title')}")
            continue
        local_page_set.add(local_page)
        path = DOCS / local_page
        if not path.is_file():
            errors.append(f"Missing generated article {local_page}")
            continue
        text = path.read_text(encoding="utf-8")
        if "## Source and licensing" not in text or record.get("source_url", "") not in text:
            errors.append(f"Missing source attribution in {local_page}")
        if 'class="reference-overview ' not in text or 'class="tensura-reference-article"' not in text:
            errors.append(f"Missing interactive article structure in {local_page}")
        if "tensura.wiki.gg/images/" in text or "tensura.wiki.gg/images\\" in text:
            errors.append(f"Hotlinked upstream image in {local_page}")

    imported_media = [record for record in media if record.get("import_status") == "imported"]
    for record in imported_media:
        local_path = record.get("local_path", "")
        if not local_path or not (DOCS / local_path).is_file():
            errors.append(f"Missing imported media file for {record.get('source_title')}")
        if not record.get("license") or not record.get("source_file_page"):
            errors.append(f"Incomplete license/source record for {record.get('source_title')}")
        if not record.get("used_on"):
            errors.append(f"Imported but unused media {record.get('source_title')}")

    category_indexes = sorted(path for path in REFERENCE.rglob("index.md") if path != REFERENCE / "index.md")
    for path in category_indexes:
        text = path.read_text(encoding="utf-8")
        if 'data-reference-directory=' not in text:
            errors.append(f"Missing interactive directory structure in {path.relative_to(DOCS)}")
        hero_title = re.search(
            r'<header class="reference-directory-hero[^>]*>.*?<h1>([^<]+)</h1>',
            text,
            re.DOTALL,
        )
        card_titles = re.findall(
            r'<div class="reference-card-copy">\s*<h2>([^<]+)</h2>',
            text,
        )
        if hero_title and any(
            html.unescape(card_title).strip().casefold()
            == html.unescape(hero_title.group(1)).strip().casefold()
            for card_title in card_titles
        ):
            errors.append(f"Directory repeats itself as a card in {path.relative_to(DOCS)}")

    markdown_link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    html_link_re = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)
    broken: list[str] = []
    for page in sorted(REFERENCE.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        for raw_target in markdown_link_re.findall(text):
            target = html.unescape(raw_target).strip().split()[0].strip("<>")
            if "\\" in target and not target.startswith(("http://", "https://")):
                errors.append(f"{page.relative_to(ROOT)} -> non-portable backslash link {target}")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if target and not (page.parent / target).resolve().exists():
                broken.append(f"{page.relative_to(ROOT)} -> missing {target}")
        for raw_target in html_link_re.findall(text):
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
                source_candidate = (
                    candidate / "index.md"
                    if candidate.is_dir()
                    else Path(str(candidate).rstrip("\\/") + ".md")
                )
            else:
                source_candidate = candidate
            if not source_candidate.exists():
                broken.append(f"{page.relative_to(ROOT)} -> missing rendered target {target}")
    errors.extend(broken)
    if coverage.get("broken_links_remaining") != len(broken):
        errors.append(
            "Coverage broken-link count does not match the post-generation audit "
            f"({coverage.get('broken_links_remaining')} reported, {len(broken)} found)"
        )

    if errors:
        raise SystemExit("Generated Tensura reference validation failed:\n- " + "\n- ".join(sorted(set(errors))))

    print(
        "Generated Tensura reference OK: "
        f"{len(pages)} articles, {len(redirects)} redirects, {len(media)} media records, "
        f"{len(imported_media)} imported media files, 0 broken local links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
