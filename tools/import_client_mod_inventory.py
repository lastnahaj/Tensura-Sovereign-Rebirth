#!/usr/bin/env python3
"""Convert a launcher HTML mod list into a reproducible runtime inventory."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ITEM_PATTERN = re.compile(r"<li>(.*?)</li>", re.IGNORECASE | re.DOTALL)
LINK_PATTERN = re.compile(
    r'<a\s+href="([^"]+)">(.*?)</a>', re.IGNORECASE | re.DOTALL
)
VERSION_PATTERN = re.compile(r"\[([^]]+)]")
FILENAME_PATTERN = re.compile(r"\(([^()]+\.jar(?:\.disabled)?)\)\s*$", re.IGNORECASE)
TAG_PATTERN = re.compile(r"<[^>]+>")
CURSEFORGE_PROJECT_PATTERN = re.compile(r"/projects/(\d+)(?:/|$)")
MODRINTH_PROJECT_PATTERN = re.compile(r"/mod/([^/?#]+)(?:/|$)")


def clean(value: str) -> str:
    return " ".join(html.unescape(TAG_PATTERN.sub("", value)).split())


def parse_item(fragment: str) -> dict[str, object]:
    link = LINK_PATTERN.search(fragment)
    url = html.unescape(link.group(1)) if link else None
    name = clean(link.group(2)) if link else clean(fragment.split("[", 1)[0])

    version_match = VERSION_PATTERN.search(fragment)
    filename_match = FILENAME_PATTERN.search(clean(fragment))
    if not filename_match:
        raise ValueError(f"Could not locate JAR filename in inventory entry: {clean(fragment)}")

    filename = filename_match.group(1)
    entry: dict[str, object] = {
        "name": name,
        "version": clean(version_match.group(1)) if version_match else None,
        "filename": filename,
        "enabled": not filename.lower().endswith(".disabled"),
        "source_url": url,
    }

    if url:
        host = (urlparse(url).hostname or "").lower()
        if host.endswith("curseforge.com"):
            project = CURSEFORGE_PROJECT_PATTERN.search(urlparse(url).path)
            entry["curseforge_project_id"] = int(project.group(1)) if project else None
        elif host.endswith("modrinth.com"):
            project = MODRINTH_PROJECT_PATTERN.search(urlparse(url).path)
            entry["modrinth_project_id"] = project.group(1) if project else None

    return entry


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--mods-dir",
        type=Path,
        help="Optional runtime mods directory used to record exact size and SHA-256",
    )
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    mods = [parse_item(match.group(1)) for match in ITEM_PATTERN.finditer(source)]
    if not mods:
        raise SystemExit("No launcher mod entries were found")

    duplicate_filenames = sorted(
        filename
        for filename in {str(mod["filename"]) for mod in mods}
        if sum(mod["filename"] == filename for mod in mods) > 1
    )
    if duplicate_filenames:
        raise SystemExit("Duplicate filenames: " + ", ".join(duplicate_filenames))

    if args.mods_dir:
        mods_dir = args.mods_dir.resolve()
        if not mods_dir.is_dir():
            raise SystemExit(f"Runtime mods directory does not exist: {mods_dir}")
        missing: list[str] = []
        for mod in mods:
            runtime_path = mods_dir / str(mod["filename"])
            if not runtime_path.is_file():
                missing.append(str(mod["filename"]))
                continue
            digest = hashlib.sha256()
            with runtime_path.open("rb") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
            mod["size"] = runtime_path.stat().st_size
            mod["sha256"] = digest.hexdigest()
        if missing:
            raise SystemExit("Inventory files missing from runtime: " + ", ".join(missing))

    inventory = {
        "schema_version": 1,
        "captured_on": date.today().isoformat(),
        "minecraft": "1.21.1",
        "loader": "NeoForge",
        "profile": "client-runtime-reference",
        "mod_count": len(mods),
        "mods": mods,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(mods)} client entries to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
