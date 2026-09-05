#!/usr/bin/env python3
"""Audit every recorded upstream wiki page and media source against MediaWiki.

This is intentionally read-only. It compares the repository's provenance records
with the current page revision, file-page revision, and uploaded-file hash at the
two official wiki.gg sources used by the project.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections.abc import Iterable
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "tensura": {
        "api": "https://tensura.wiki.gg/api.php",
        "host": "tensura.wiki.gg",
        "pages": ROOT / "data" / "upstream_tensura_pages.json",
        "media": ROOT / "data" / "upstream_tensura_media.json",
    },
    "mysticism": {
        "api": "https://trmysticism.wiki.gg/api.php",
        "host": "trmysticism.wiki.gg",
        "pages": ROOT / "data" / "upstream_mysticism_pages.json",
        "media": ROOT / "data" / "upstream_mysticism_media.json",
    },
}
MODLIST = ROOT / "docs" / "assets" / "data" / "current-client-modlist.json"


def chunks(items: list[Any], size: int) -> Iterable[list[Any]]:
    for offset in range(0, len(items), size):
        yield items[offset : offset + size]


def canonical_title(value: str) -> str:
    # MediaWiki normalizes spaces and the first character, but later characters
    # remain case-sensitive (for example Hihiirokane and HihiIrokane coexist).
    normalized = " ".join(value.replace("_", " ").split())
    return normalized[:1].upper() + normalized[1:]


class Auditor:
    def __init__(self, timeout: float, pace: float) -> None:
        self.timeout = timeout
        self.pace = pace
        retry = Retry(
            total=4,
            connect=4,
            read=4,
            backoff_factor=0.8,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset({"GET"}),
        )
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "TSRSourceAudit/1.0 "
                    "(+https://github.com/lastnahaj/Tensura-Sovereign-Rebirth)"
                )
            }
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

    def query(self, api: str, **params: Any) -> dict[str, Any]:
        payload = {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            **params,
        }
        response = self.session.get(api, params=payload, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise RuntimeError(f"MediaWiki API error: {data['error']}")
        if self.pace:
            time.sleep(self.pace)
        return data


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_page_records(
    auditor: Auditor, api: str, records: list[dict[str, Any]]
) -> tuple[dict[str, int], list[dict[str, Any]]]:
    counts = {"checked": 0, "current": 0, "changed": 0, "missing": 0}
    findings: list[dict[str, Any]] = []
    by_id = {int(record["page_id"]): record for record in records if record.get("page_id")}
    seen: set[int] = set()

    for batch in chunks(list(by_id), 50):
        result = auditor.query(
            api,
            pageids="|".join(str(page_id) for page_id in batch),
            prop="info|revisions",
            rvprop="ids|timestamp",
        )
        for page in result.get("query", {}).get("pages", []):
            page_id = page.get("pageid")
            if page_id not in by_id or page.get("missing"):
                continue
            seen.add(page_id)
            record = by_id[page_id]
            revision = (page.get("revisions") or [{}])[0]
            current_revision = revision.get("revid")
            counts["checked"] += 1
            if current_revision == record.get("revision_id"):
                counts["current"] += 1
            else:
                counts["changed"] += 1
                findings.append(
                    {
                        "kind": "page_revision_changed",
                        "title": record.get("source_title"),
                        "recorded_revision": record.get("revision_id"),
                        "current_revision": current_revision,
                    }
                )

    for page_id, record in by_id.items():
        if page_id not in seen:
            counts["missing"] += 1
            findings.append(
                {
                    "kind": "page_missing",
                    "title": record.get("source_title"),
                    "page_id": page_id,
                }
            )
    return counts, findings


def audit_redirect_records(
    auditor: Auditor, api: str, records: list[dict[str, Any]]
) -> tuple[dict[str, int], list[dict[str, Any]]]:
    counts = {"checked": 0, "current": 0, "changed": 0, "missing": 0}
    findings: list[dict[str, Any]] = []

    for batch in chunks(records, 50):
        wanted = {canonical_title(record["source_title"]): record for record in batch}
        result = auditor.query(
            api,
            titles="|".join(record["source_title"] for record in batch),
            prop="info|revisions",
            rvprop="ids|timestamp",
        )
        normalized = {
            canonical_title(item["to"]): canonical_title(item["from"])
            for item in result.get("query", {}).get("normalized", [])
        }
        found: set[str] = set()
        for page in result.get("query", {}).get("pages", []):
            page_key = canonical_title(page.get("title", ""))
            record_key = normalized.get(page_key, page_key)
            record = wanted.get(record_key)
            if not record or page.get("missing"):
                continue
            found.add(record_key)
            revision = (page.get("revisions") or [{}])[0]
            current_revision = revision.get("revid")
            counts["checked"] += 1
            if current_revision == record.get("revision_id"):
                counts["current"] += 1
            else:
                counts["changed"] += 1
                findings.append(
                    {
                        "kind": "redirect_revision_changed",
                        "title": record.get("source_title"),
                        "recorded_revision": record.get("revision_id"),
                        "current_revision": current_revision,
                    }
                )
        for key, record in wanted.items():
            if key not in found:
                counts["missing"] += 1
                findings.append(
                    {"kind": "redirect_missing", "title": record.get("source_title")}
                )
    return counts, findings


def audit_media_records(
    auditor: Auditor,
    api: str,
    records: list[dict[str, Any]],
) -> tuple[dict[str, int], list[dict[str, Any]]]:
    imported = [record for record in records if record.get("import_status") == "imported"]
    unresolved = [record for record in records if record.get("import_status") != "imported"]
    counts = {
        "checked": 0,
        "current": 0,
        "changed": 0,
        "missing": 0,
        "recorded_unresolved": len(unresolved),
        "unresolved_now_available": 0,
    }
    findings: list[dict[str, Any]] = []
    by_id = {int(record["page_id"]): record for record in imported if record.get("page_id")}
    seen: set[int] = set()

    for batch in chunks(list(by_id), 50):
        result = auditor.query(
            api,
            pageids="|".join(str(page_id) for page_id in batch),
            prop="imageinfo|revisions",
            iiprop="sha1|timestamp|size|mime",
            rvprop="ids|timestamp",
        )
        for page in result.get("query", {}).get("pages", []):
            page_id = page.get("pageid")
            if page_id not in by_id or page.get("missing"):
                continue
            seen.add(page_id)
            record = by_id[page_id]
            image = (page.get("imageinfo") or [{}])[0]
            revision = (page.get("revisions") or [{}])[0]
            current_revision = revision.get("revid")
            current_sha1 = image.get("sha1")
            revision_matches = current_revision == record.get("file_revision_id")
            sha1_matches = current_sha1 == record.get("sha1")
            counts["checked"] += 1
            if revision_matches and sha1_matches:
                counts["current"] += 1
            else:
                counts["changed"] += 1
                findings.append(
                    {
                        "kind": "media_changed",
                        "title": record.get("source_title"),
                        "recorded_revision": record.get("file_revision_id"),
                        "current_revision": current_revision,
                        "recorded_sha1": record.get("sha1"),
                        "current_sha1": current_sha1,
                    }
                )

    for page_id, record in by_id.items():
        if page_id not in seen:
            counts["missing"] += 1
            findings.append(
                {
                    "kind": "media_missing",
                    "title": record.get("source_title"),
                    "page_id": page_id,
                }
            )

    for batch in chunks(unresolved, 20):
        result = auditor.query(
            api,
            titles="|".join(f"File:{record['source_title']}" for record in batch),
            redirects="1",
            prop="imageinfo|revisions",
            iiprop="sha1|url",
            rvprop="ids|timestamp",
        )
        for page in result.get("query", {}).get("pages", []):
            image = (page.get("imageinfo") or [{}])[0]
            if not page.get("missing") and image.get("url"):
                counts["unresolved_now_available"] += 1
                findings.append(
                    {
                        "kind": "unresolved_media_now_available",
                        "title": page.get("title", "").removeprefix("File:"),
                    }
                )
    return counts, findings


def validate_local_records(
    source_name: str,
    source: dict[str, Any],
    page_data: dict[str, Any],
    media_data: dict[str, Any],
) -> tuple[dict[str, int], list[dict[str, Any]]]:
    host = source["host"]
    findings: list[dict[str, Any]] = []
    counts = {"checked": 0, "invalid": 0}
    local_pages: set[str] = set()

    for record in [*page_data.get("pages", []), *page_data.get("skipped_pages", [])]:
        counts["checked"] += 1
        url = str(record.get("source_url", ""))
        errors: list[str] = []
        if not url.startswith(f"https://{host}/wiki/"):
            errors.append("unexpected source URL")
        local_page = record.get("local_page")
        if local_page:
            if local_page in local_pages:
                errors.append("duplicate local page")
            local_pages.add(local_page)
            if not (ROOT / "docs" / local_page).is_file():
                errors.append("local page missing")
        if errors:
            counts["invalid"] += 1
            findings.append(
                {
                    "kind": "local_page_record_invalid",
                    "source": source_name,
                    "title": record.get("source_title"),
                    "errors": errors,
                }
            )

    for record in media_data.get("media", []):
        counts["checked"] += 1
        errors = []
        file_page = str(record.get("source_file_page", ""))
        if not file_page.startswith(f"https://{host}/wiki/File:"):
            errors.append("unexpected File-page URL")
        if record.get("import_status") == "imported":
            local_path = record.get("local_path")
            if not local_path or not (ROOT / "docs" / local_path).is_file():
                errors.append("imported local media missing")
            if not record.get("sha1") or not record.get("file_revision_id"):
                errors.append("incomplete imported provenance")
        if errors:
            counts["invalid"] += 1
            findings.append(
                {
                    "kind": "local_media_record_invalid",
                    "source": source_name,
                    "title": record.get("source_title"),
                    "errors": errors,
                }
            )
    return counts, findings


def audit_mod_source_records() -> tuple[dict[str, int], list[dict[str, Any]]]:
    """Validate the identity and source URL recorded for every current mod."""
    data = load_json(MODLIST)
    records = data.get("mods", [])
    counts = {
        "checked": len(records),
        "published_sources": 0,
        "pack_local_modules": 0,
        "curseforge_identity_matches": 0,
        "invalid": 0,
    }
    findings: list[dict[str, Any]] = []
    seen_filenames: set[str] = set()

    for record in records:
        errors: list[str] = []
        name = str(record.get("name", "")).strip()
        filename = str(record.get("filename", "")).strip()
        raw_url = record.get("source_url")
        url = str(raw_url).strip() if raw_url else ""
        project_id = record.get("curseforge_project_id")
        if not name:
            errors.append("missing name")
        if not filename:
            errors.append("missing filename")
        elif filename.casefold() in seen_filenames:
            errors.append("duplicate filename")
        else:
            seen_filenames.add(filename.casefold())

        if not url:
            counts["pack_local_modules"] += 1
            if project_id is not None:
                errors.append("project ID without a source URL")
        else:
            counts["published_sources"] += 1
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append("source URL is not absolute HTTPS")
            if parsed.hostname == "www.curseforge.com":
                match = re.fullmatch(r"/projects/(\d+)/?", parsed.path)
                if not match:
                    errors.append("unexpected CurseForge project URL")
                elif project_id is None or int(match.group(1)) != int(project_id):
                    errors.append("CurseForge URL and project ID differ")
                else:
                    counts["curseforge_identity_matches"] += 1
            elif parsed.hostname not in {"github.com", "serilum.com"}:
                errors.append("unexpected source host")

        if errors:
            counts["invalid"] += 1
            findings.append(
                {
                    "kind": "mod_source_record_invalid",
                    "name": name or "(unnamed)",
                    "errors": errors,
                }
            )
    return counts, findings


def audit_source(auditor: Auditor, name: str) -> dict[str, Any]:
    source = SOURCES[name]
    pages = load_json(source["pages"])
    media = load_json(source["media"])
    article_records = [*pages.get("pages", []), *pages.get("skipped_pages", [])]

    local_counts, local_findings = validate_local_records(name, source, pages, media)
    page_counts, page_findings = audit_page_records(auditor, source["api"], article_records)
    redirect_counts, redirect_findings = audit_redirect_records(
        auditor, source["api"], pages.get("redirects", [])
    )
    media_counts, media_findings = audit_media_records(
        auditor, source["api"], media.get("media", [])
    )
    return {
        "source": name,
        "api": source["api"],
        "local_records": local_counts,
        "pages": page_counts,
        "redirects": redirect_counts,
        "media": media_counts,
        "findings": [
            *local_findings,
            *page_findings,
            *redirect_findings,
            *media_findings,
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", choices=("all", *SOURCES), default="all", help="source to audit"
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--pace", type=float, default=0.05)
    parser.add_argument("--report", type=Path, help="optional JSON report path")
    args = parser.parse_args()

    names = list(SOURCES) if args.source == "all" else [args.source]
    auditor = Auditor(timeout=args.timeout, pace=args.pace)
    results = []
    for name in names:
        print(f"Auditing {name} source records...", flush=True)
        result = audit_source(auditor, name)
        results.append(result)
        print(
            f"  pages {result['pages']['current']}/{result['pages']['checked']} current; "
            f"redirects {result['redirects']['current']}/{result['redirects']['checked']} current; "
            f"media {result['media']['current']}/{result['media']['checked']} current; "
            f"local invalid {result['local_records']['invalid']}",
            flush=True,
        )

    mod_counts, mod_findings = audit_mod_source_records()
    print(
        f"Mod sources: {mod_counts['published_sources']} published records and "
        f"{mod_counts['pack_local_modules']} pack-local modules checked; "
        f"invalid {mod_counts['invalid']}",
        flush=True,
    )
    report = {
        "schema": 1,
        "sources": results,
        "mod_sources": {"counts": mod_counts, "findings": mod_findings},
        "summary": {
            "findings": sum(len(result["findings"]) for result in results)
            + len(mod_findings),
            "changed": sum(
                result["pages"]["changed"]
                + result["redirects"]["changed"]
                + result["media"]["changed"]
                for result in results
            ),
            "missing": sum(
                result["pages"]["missing"]
                + result["redirects"]["missing"]
                + result["media"]["missing"]
                for result in results
            ),
            "local_invalid": sum(result["local_records"]["invalid"] for result in results),
            "unresolved_now_available": sum(
                result["media"]["unresolved_now_available"] for result in results
            ),
            "mod_source_invalid": mod_counts["invalid"],
        },
    }
    if args.report:
        report_path = args.report if args.report.is_absolute() else ROOT / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Report: {report_path}")

    summary = report["summary"]
    print(json.dumps(summary, indent=2))
    return 1 if any(summary.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
