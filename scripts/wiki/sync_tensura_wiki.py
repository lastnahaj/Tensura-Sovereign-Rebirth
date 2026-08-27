#!/usr/bin/env python3
"""Synchronize the official Tensura wiki into the generated TSR reference."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import quote, unquote, urlparse

import requests
import yaml
from bs4 import BeautifulSoup, Comment, Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
REFERENCE_ROOT = DOCS / "tensura-reference"
ASSET_ROOT = DOCS / "assets" / "upstream" / "tensura"
DATA_ROOT = ROOT / "data"
DEFAULT_CACHE = ROOT / ".build" / "wiki-cache"
API_URL = "https://tensura.wiki.gg/api.php"
WIKI_ROOT = "https://tensura.wiki.gg"
TEXT_LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
USER_AGENT = (
    "TSRWikiIngest/1.0 "
    "(+https://github.com/lastnahaj/Tensura-Sovereign-Rebirth)"
)
SYNCED_AT = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
    "+00:00", "Z"
)


CATEGORY_INFO: dict[str, tuple[str, str]] = {
    "core-mechanics": ("Core Mechanics", "Foundational resources and progression mechanics."),
    "races": ("Races", "Playable and documented race forms and their evolution data."),
    "skills/intrinsic": ("Intrinsic Skills", "Intrinsic racial and species-linked skills."),
    "skills/common": ("Common Skills", "Common skills and broadly available abilities."),
    "skills/extra": ("Extra Skills", "Extra-class skills and their documented progressions."),
    "skills/unique": ("Unique Skills", "Unique-class skills and their documented mechanics."),
    "skills/ultimate": ("Ultimate Skills", "Ultimate-class skills and related evolutions."),
    "skills/other": ("Other Skills", "Skills outside the primary class directories."),
    "resistances": ("Resistances", "Resistance, immunity, nullification, and cancellation abilities."),
    "magic": ("Magic", "Magic systems, aspects, and individual spells."),
    "battlewill": ("Battlewill", "Aura-powered Battlewill techniques and manuals."),
    "arts": ("Arts", "Documented Arts and their acquisition or mastery."),
    "mobs": ("Mobs", "The base mod's documented entity catalog."),
    "bosses": ("Bosses", "Boss encounters documented by the base mod."),
    "items": ("Items & Materials", "Materials, consumables, drops, and special items."),
    "weapons": ("Weapons", "Documented weapons and combat equipment."),
    "armor": ("Armor", "Documented armor pieces and sets."),
    "tools": ("Tools", "Tools and utility equipment."),
    "blocks": ("Blocks", "Mechanically relevant blocks and block families."),
    "structures": ("Structures", "Base Tensura structures and generation information."),
    "biomes": ("Biomes", "Base Tensura biomes and biome-specific behavior."),
    "dimensions": ("Dimensions", "Dimensions, portals, access, and world content."),
    "commands": ("Commands", "Player and administrator command reference."),
    "configuration": ("Configuration", "Base Tensura configuration reference."),
    "gamerules": ("Gamerules", "Tensura-specific gamerules and behavior."),
    "version-history": ("Version History", "Historical releases and upstream change records."),
    "other": ("Other Reference", "Additional maintained base-mod reference articles."),
}

CATEGORY_ORDER = list(CATEGORY_INFO)
MEDIA_CATEGORY_MAP = {
    "core-mechanics": "misc",
    "races": "races",
    "skills/intrinsic": "skills",
    "skills/common": "skills",
    "skills/extra": "skills",
    "skills/unique": "skills",
    "skills/ultimate": "skills",
    "skills/other": "skills",
    "resistances": "resistances",
    "magic": "magic",
    "battlewill": "battlewill",
    "arts": "arts",
    "mobs": "mobs",
    "bosses": "bosses",
    "items": "items",
    "weapons": "weapons",
    "armor": "armor",
    "tools": "items",
    "blocks": "items",
    "structures": "structures",
    "biomes": "biomes",
    "dimensions": "dimensions",
    "commands": "misc",
    "configuration": "misc",
    "gamerules": "misc",
    "version-history": "misc",
    "other": "misc",
}

CORE_MECHANIC_TERMS = {
    "alignment",
    "aura",
    "awakening",
    "demon lord",
    "demon lord seed",
    "ep",
    "existence points",
    "hero",
    "harvest festival",
    "magicules",
    "naming",
    "reincarnation",
    "souls",
    "spiritual health",
    "true demon lord",
    "true hero",
}

NON_CONTENT_CATEGORIES = {
    "Crafting_Table_templates",
    "Lua-based_templates",
    "Main_page_boxes",
    "Table_templates",
    "Templates_with_no_documentation",
    "Tensura:_Reincarnated_Wiki",
}

ALLOWED_LICENSE_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bcc[- ]?by[- ]?sa[- ]?4(?:\.0)?\b", re.I), "CC BY-SA 4.0"),
    (re.compile(r"creative commons attribution-sharealike 4(?:\.0)?", re.I), "CC BY-SA 4.0"),
    (re.compile(r"\bcc[- ]?by[- ]?4(?:\.0)?\b", re.I), "CC BY 4.0"),
    (re.compile(r"creative commons attribution 4(?:\.0)?", re.I), "CC BY 4.0"),
    (re.compile(r"\bcc0\b|creative commons zero", re.I), "CC0"),
    (re.compile(r"public domain|\{\{\s*pd(?:[-|}])", re.I), "Public domain"),
)

RESTRICTIVE_LICENSE_RE = re.compile(
    r"fair use|non[- ]?free|all rights reserved|copyrighted|no redistribution|"
    r"permission only|proprietary",
    re.I,
)


@dataclass
class ApiClient:
    cache_root: Path
    refresh: bool = False
    pace: float = 0.18

    def __post_init__(self) -> None:
        retry = Retry(
            total=6,
            connect=6,
            read=6,
            backoff_factor=0.8,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset({"GET"}),
            respect_retry_after_header=True,
        )
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
        self.last_request = 0.0

    def get_json(self, params: dict[str, Any], cache_name: str) -> dict[str, Any]:
        cache_path = self.cache_root / "api" / cache_name
        if cache_path.exists() and not self.refresh:
            return json.loads(cache_path.read_text(encoding="utf-8"))

        elapsed = time.monotonic() - self.last_request
        if elapsed < self.pace:
            time.sleep(self.pace - elapsed)
        response = self.session.get(API_URL, params=params, timeout=(15, 90))
        self.last_request = time.monotonic()
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise RuntimeError(f"MediaWiki API error: {data['error']}")
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        return data

    def download(self, url: str, destination: Path) -> None:
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.hostname or not parsed.hostname.endswith(
            "wiki.gg"
        ):
            raise RuntimeError(f"Refusing unexpected media host: {url}")
        elapsed = time.monotonic() - self.last_request
        if elapsed < self.pace:
            time.sleep(self.pace - elapsed)
        response = self.session.get(url, timeout=(15, 120), stream=True)
        self.last_request = time.monotonic()
        response.raise_for_status()
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(destination.suffix + ".part")
        with temporary.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=128 * 1024):
                if chunk:
                    handle.write(chunk)
        temporary.replace(destination)

    def get_text(self, url: str, cache_name: str) -> str:
        cache_path = self.cache_root / cache_name
        if cache_path.exists() and not self.refresh:
            return cache_path.read_text(encoding="utf-8")
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "tensura.wiki.gg":
            raise RuntimeError(f"Refusing unexpected page host: {url}")
        elapsed = time.monotonic() - self.last_request
        if elapsed < self.pace:
            time.sleep(self.pace - elapsed)
        response = self.session.get(url, timeout=(15, 90))
        self.last_request = time.monotonic()
        response.raise_for_status()
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(response.text, encoding="utf-8")
        return response.text


def chunks(values: list[Any], size: int) -> Iterable[list[Any]]:
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def normalize_title(value: str) -> str:
    return unicodedata.normalize("NFC", value.replace("_", " ").strip()).casefold()


def slugify(value: str, max_length: int = 110) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = value.replace("/", "-")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return (value[:max_length].rstrip("-") or "article")


def wiki_url(title: str) -> str:
    return f"{WIKI_ROOT}/wiki/{quote(title.replace(' ', '_'), safe='/:()!,.\'')}"


def strip_html(value: str | None) -> str:
    if not value:
        return ""
    return BeautifulSoup(value, "html.parser").get_text(" ", strip=True)


def metadata_value(metadata: dict[str, Any], key: str) -> str:
    value = metadata.get(key, "")
    if isinstance(value, dict):
        value = value.get("value", "")
    return strip_html(str(value))


def enumerate_pages(client: ApiClient, redirect_filter: str) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    continuation: dict[str, Any] = {}
    batch = 0
    while True:
        params: dict[str, Any] = {
            "action": "query",
            "list": "allpages",
            "apnamespace": 0,
            "aplimit": "max",
            "apfilterredir": redirect_filter,
            "format": "json",
            "formatversion": 2,
            **continuation,
        }
        data = client.get_json(params, f"allpages/{redirect_filter}-{batch:03d}.json")
        pages.extend(data["query"]["allpages"])
        if "continue" not in data:
            break
        continuation = data["continue"]
        batch += 1
    return pages


def fetch_siteinfo(client: ApiClient) -> dict[str, Any]:
    data = client.get_json(
        {
            "action": "query",
            "meta": "siteinfo",
            "siprop": "general|statistics|rightsinfo",
            "format": "json",
            "formatversion": 2,
        },
        "siteinfo.json",
    )
    return data["query"]


def fetch_revision_metadata(
    client: ApiClient, pages: list[dict[str, Any]]
) -> dict[int, dict[str, Any]]:
    output: dict[int, dict[str, Any]] = {}
    for batch_number, page_batch in enumerate(chunks(pages, 50)):
        data = client.get_json(
            {
                "action": "query",
                "pageids": "|".join(str(page["pageid"]) for page in page_batch),
                "prop": "info|revisions",
                "rvprop": "ids|timestamp",
                "format": "json",
                "formatversion": 2,
            },
            f"revisions/canonical-{batch_number:03d}.json",
        )
        for page in data["query"]["pages"]:
            revision = (page.get("revisions") or [{}])[0]
            output[page["pageid"]] = {
                "revision_id": revision.get("revid") or page.get("lastrevid"),
                "modified": revision.get("timestamp") or page.get("touched"),
                "length": page.get("length"),
            }
    return output


def fetch_redirect_map(
    client: ApiClient, redirects: list[dict[str, Any]]
) -> tuple[dict[str, str], list[dict[str, Any]]]:
    redirect_map: dict[str, str] = {}
    records: list[dict[str, Any]] = []
    redirect_re = re.compile(r"^\s*#redirect\s*\[\[([^\]#]+)(?:#[^\]]*)?\]\]", re.I)
    for batch_number, page_batch in enumerate(chunks(redirects, 50)):
        data = client.get_json(
            {
                "action": "query",
                "pageids": "|".join(str(page["pageid"]) for page in page_batch),
                "prop": "revisions",
                "rvprop": "ids|timestamp|content",
                "rvslots": "main",
                "format": "json",
                "formatversion": 2,
            },
            f"redirects/batch-{batch_number:03d}.json",
        )
        for page in data["query"]["pages"]:
            revision = (page.get("revisions") or [{}])[0]
            content = revision.get("slots", {}).get("main", {}).get("content", "")
            match = redirect_re.search(content)
            target = match.group(1).strip() if match else ""
            status = "processed" if target else "failed"
            if target:
                redirect_map[normalize_title(page["title"])] = target
            records.append(
                {
                    "source_title": page["title"],
                    "target_title": target or None,
                    "revision_id": revision.get("revid"),
                    "modified": revision.get("timestamp"),
                    "status": status,
                }
            )
    return redirect_map, records


def parse_articles(
    client: ApiClient,
    pages: list[dict[str, Any]],
    revisions: dict[int, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    parsed: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    total = len(pages)
    for index, page in enumerate(pages, start=1):
        revision_id = revisions.get(page["pageid"], {}).get("revision_id") or "unknown"
        try:
            data = client.get_json(
                {
                    "action": "parse",
                    "pageid": page["pageid"],
                    "prop": "displaytitle|revid|text|links|images|categories|properties",
                    "format": "json",
                    "formatversion": 2,
                },
                f"parse/{page['pageid']}-{revision_id}.json",
            )
            parsed.append({"listing": page, "parse": data["parse"]})
        except Exception as exc:  # continue to produce an explicit failure report
            failed.append(
                {
                    "source_title": page["title"],
                    "page_id": page["pageid"],
                    "reason": str(exc),
                }
            )
        if index % 50 == 0 or index == total:
            print(f"Parsed {index}/{total} canonical articles", flush=True)
    return parsed, failed


def category_names(parse_data: dict[str, Any]) -> list[str]:
    return [
        entry.get("category", "")
        for entry in parse_data.get("categories", [])
        if entry.get("category") and not entry.get("hidden")
    ]


def classify_article(title: str, categories: list[str]) -> str:
    normalized_title = normalize_title(title)
    title_parts = [normalize_title(part) for part in title.split("/")]
    category_text = " ".join(normalize_title(category) for category in categories)
    combined = f"{normalized_title} {category_text}"
    leaf = title_parts[-1]

    if re.match(r"^\d+\.\d+(?:\.\d+)?\s", title) or "version history" in combined:
        return "version-history"
    if (
        leaf in CORE_MECHANIC_TERMS
        or normalized_title in {"ep, magicule, aura", "getting started"}
        or leaf in {"chantspeed", "damage types", "dodging", "engravings", "gear evolution", "trading"}
        or title_parts[0] in {"mechanics", "effects", "effect"}
        or any(term in category_text for term in ("mechanic", "progression"))
    ):
        return "core-mechanics"
    if title_parts[0] in {"races", "race"} or re.search(r"\braces?\b", category_text):
        return "races"
    if title_parts[0] in {"mobs", "entities"}:
        return "bosses" if "boss" in combined else "mobs"
    if title_parts[0] in {"weapons", "weapon"}:
        return "weapons"
    if title_parts[0] in {"armor", "armour"}:
        return "armor"
    if title_parts[0] == "tools":
        return "tools"
    if title_parts[0] == "blocks":
        return "blocks"
    if leaf in {"underworld barrens", "underworld red sands", "underworld sands", "underworld spikes"}:
        return "blocks"
    if title_parts[0] == "structures":
        return "structures"
    if leaf == "ruins":
        return "structures"
    if title_parts[0] == "biomes":
        return "biomes"
    if title_parts[0] == "dimensions":
        return "dimensions"
    if "battlewill" in combined:
        return "battlewill"
    if re.search(r"\barts?\b", combined) and "artifact" not in combined:
        return "arts"
    if re.search(r"\bmagics?\b|\bspells?\b", combined):
        return "magic"
    if "resistance" in combined or "nullification" in combined or "immunity" in combined:
        return "resistances"
    if "ultimate skill" in combined or "ultimate skills" in combined:
        return "skills/ultimate"
    if "unique skill" in combined or "unique skills" in combined:
        return "skills/unique"
    if "intrinsic skill" in combined or "intrinsic skills" in combined:
        return "skills/intrinsic"
    if "common skill" in combined or "common skills" in combined:
        return "skills/common"
    if "extra skill" in combined or "extra skills" in combined:
        return "skills/extra"
    if "skill" in combined or title_parts[0] in {"abilities", "skills"}:
        return "skills/other"
    if "boss" in combined:
        return "bosses"
    if title_parts[0] in {"mobs", "entities"} or re.search(r"\bmobs?\b|\bentities\b", category_text):
        return "mobs"
    if re.search(r"\b(?:boots|chestplate|helmet|leggings|scalemail|greaves|cuirass)\b$", leaf):
        return "armor"
    if re.search(r"\b(?:axe|hoe|pickaxe|shovel)\b$", leaf) and not re.search(
        r"\b(?:battle|great|war)\s+axe\b$", leaf
    ):
        return "tools"
    if re.search(
        r"\b(?:battle axe|bow|dagger|great sword|greatsword|halberd|katana|kodachi|"
        r"lance|long sword|longsword|mace|odachi|rapier|scythe|short sword|shortsword|"
        r"sickle|spear|staff|sword|tachi|war axe|wand)\b$",
        leaf,
    ):
        return "weapons"
    if "weapon" in combined or title_parts[0] == "weapons":
        return "weapons"
    if re.search(r"\b(?:armor|armour)\b", combined) or title_parts[0] == "armor":
        return "armor"
    if "tool" in combined or title_parts[0] == "tools":
        return "tools"
    if "block" in combined or title_parts[0] == "blocks":
        return "blocks"
    if "structure" in combined or title_parts[0] == "structures":
        return "structures"
    if "biome" in combined or title_parts[0] == "biomes":
        return "biomes"
    if "dimension" in combined or title_parts[0] == "dimensions":
        return "dimensions"
    if "command" in combined or title_parts[0] == "commands":
        return "commands"
    if "gamerule" in combined or "game rule" in combined:
        return "gamerules"
    if "config" in combined or "configuration" in combined:
        return "configuration"
    if (
        "item" in combined
        or "material" in combined
        or "ore" in combined
        or any(
            category in categories
            for category in ("Stackable_resources", "Non-stackable_resources", "Has_crafting")
        )
    ):
        return "items"
    if leaf in {
        "bat glider",
        "bulldeer milk bucket",
        "cargotest",
        "greater holy water",
        "holy milk",
        "holy milk bucket",
        "holy water",
        "monster saddle",
        "revival elixir",
        "unbound tome",
    }:
        return "items"
    return "other"


def non_content_reason(title: str, categories: list[str], description: str) -> str | None:
    if normalize_title(title) == "crafting/doc":
        return "Template documentation rather than player-facing mod information"
    matched = sorted(NON_CONTENT_CATEGORIES.intersection(categories))
    if matched:
        return "Wiki-management or template-support article (" + ", ".join(matched) + ")"
    if description.startswith("Documentation Edit this documentation at Template:"):
        return "Template documentation rather than player-facing mod information"
    return None


def build_page_records(
    parsed_articles: list[dict[str, Any]], revisions: dict[int, dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    occupied: dict[tuple[str, str], int] = {}
    for article in parsed_articles:
        listing = article["listing"]
        parse_data = article["parse"]
        categories = category_names(parse_data)
        properties = parse_data.get("properties", {})
        description = " ".join(strip_html(properties.get("description")).split())
        reason = non_content_reason(listing["title"], categories, description)
        if reason:
            revision = revisions.get(listing["pageid"], {})
            skipped.append(
                {
                    "source_title": listing["title"],
                    "source_url": wiki_url(listing["title"]),
                    "page_id": listing["pageid"],
                    "revision_id": parse_data.get("revid") or revision.get("revision_id"),
                    "upstream_modified": revision.get("modified"),
                    "upstream_categories": categories,
                    "import_status": "skipped",
                    "reason": reason,
                }
            )
            continue
        primary_category = classify_article(listing["title"], categories)
        slug = slugify(listing["title"])
        key = (primary_category, slug)
        if key in occupied:
            slug = f"{slug}-{listing['pageid']}"
        occupied[(primary_category, slug)] = listing["pageid"]
        local_page = PurePosixPath("tensura-reference") / primary_category / f"{slug}.md"
        display_title = strip_html(parse_data.get("displaytitle")) or listing["title"].split("/")[-1]
        revision = revisions.get(listing["pageid"], {})
        records.append(
            {
                "source_title": listing["title"],
                "display_title": display_title,
                "source_url": wiki_url(listing["title"]),
                "page_id": listing["pageid"],
                "revision_id": parse_data.get("revid") or revision.get("revision_id"),
                "upstream_modified": revision.get("modified"),
                "upstream_length": revision.get("length"),
                "local_page": local_page.as_posix(),
                "category": primary_category,
                "upstream_categories": categories,
                "description": description[:500],
                "image_titles": parse_data.get("images", []),
                "import_status": "imported",
                "last_synchronized": SYNCED_AT,
                "_html": parse_data.get("text", ""),
                "_properties": properties,
            }
        )
    return records, skipped


def resolve_redirects(
    redirect_map: dict[str, str],
    records: list[dict[str, Any]],
    redirect_records: list[dict[str, Any]],
    skipped_pages: list[dict[str, Any]],
) -> tuple[dict[str, str], dict[str, list[str]]]:
    canonical_lookup = {normalize_title(record["source_title"]): record["source_title"] for record in records}
    aliases_by_target: dict[str, list[str]] = defaultdict(list)
    resolved: dict[str, str] = {}

    def chase(target: str) -> str | None:
        seen: set[str] = set()
        current = target
        while normalize_title(current) not in canonical_lookup:
            key = normalize_title(current)
            if key in seen or key not in redirect_map:
                return None
            seen.add(key)
            current = redirect_map[key]
        return canonical_lookup[normalize_title(current)]

    skipped_lookup = {normalize_title(record["source_title"]) for record in skipped_pages}
    for alias_key, target in redirect_map.items():
        canonical = chase(target)
        source_record = next(
            (record for record in redirect_records if normalize_title(record["source_title"]) == alias_key),
            None,
        )
        if canonical:
            resolved[alias_key] = canonical
            alias_title = source_record["source_title"] if source_record else alias_key
            aliases_by_target[canonical].append(alias_title)
            if source_record:
                source_record["resolved_target"] = canonical
        elif source_record:
            target_key = normalize_title(target).lstrip(":")
            if (
                target_key.startswith(("category:", "template:"))
                or normalize_title(target) in skipped_lookup
            ):
                source_record["status"] = "skipped"
                source_record["reason"] = "Alias targets a category, template, or excluded wiki-maintenance page"
            else:
                source_record["status"] = "failed"
                source_record["reason"] = "Target did not resolve to a canonical main-namespace article"
    for record in redirect_records:
        record.setdefault("resolved_target", None)
    return resolved, aliases_by_target


def fetch_media_metadata(
    client: ApiClient, image_titles: list[str]
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for batch_number, title_batch in enumerate(chunks(image_titles, 20)):
        data = client.get_json(
            {
                "action": "query",
                "titles": "|".join(f"File:{title}" for title in title_batch),
                "redirects": 1,
                "prop": "imageinfo|revisions",
                "iiprop": "url|size|mime|sha1|extmetadata|timestamp|user|comment",
                "iiurlwidth": 1200,
                "rvprop": "ids|timestamp|content",
                "rvslots": "main",
                "format": "json",
                "formatversion": 2,
            },
            f"media/batch-{batch_number:04d}.json",
        )
        for page in data.get("query", {}).get("pages", []):
            title = page.get("title", "")
            if title.lower().startswith("file:"):
                title = title[5:]
            image_info = (page.get("imageinfo") or [{}])[0]
            revision = (page.get("revisions") or [{}])[0]
            content = revision.get("slots", {}).get("main", {}).get("content", "")
            records.append(
                {
                    "source_title": title,
                    "page_id": page.get("pageid"),
                    "source_file_page": wiki_url(f"File:{title}"),
                    "source_url": image_info.get("url"),
                    "thumbnail_url": image_info.get("thumburl"),
                    "width": image_info.get("width"),
                    "height": image_info.get("height"),
                    "size": image_info.get("size"),
                    "mime": image_info.get("mime"),
                    "sha1": image_info.get("sha1"),
                    "file_timestamp": image_info.get("timestamp"),
                    "uploaded_by": image_info.get("user"),
                    "upload_comment": image_info.get("comment"),
                    "file_revision_id": revision.get("revid"),
                    "file_modified": revision.get("timestamp"),
                    "extmetadata": image_info.get("extmetadata", {}),
                    "_wikitext": content,
                }
            )
        if (batch_number + 1) % 10 == 0 or (batch_number + 1) * 20 >= len(image_titles):
            print(
                f"Audited media metadata for {min((batch_number + 1) * 20, len(image_titles))}/"
                f"{len(image_titles)} files",
                flush=True,
            )
    return records


def verify_file_page_license(client: ApiClient, media_records: list[dict[str, Any]]) -> dict[str, str]:
    candidates = sorted(
        (record for record in media_records if record.get("source_url") and record.get("source_file_page")),
        key=lambda record: (record.get("source_title") != "Skillicon.png", record.get("source_title", "")),
    )
    if not candidates:
        raise RuntimeError("Cannot verify the upstream File-page media license")
    page_html = ""
    for sample in candidates[:20]:
        try:
            page_html = client.get_text(
                sample["source_file_page"], "policy/file-page-license.html"
            )
            break
        except requests.HTTPError as exc:
            if exc.response is None or exc.response.status_code != 404:
                raise
    if not page_html:
        raise RuntimeError("Could not load a live upstream File page to verify its media license")
    soup = BeautifulSoup(page_html, "html.parser")
    license_link = soup.select_one('link[rel="license"]')
    footer = soup.select_one("#footer-info-copyright")
    license_url = license_link.get("href", "") if license_link else ""
    footer_text = " ".join(footer.get_text(" ", strip=True).split()) if footer else ""
    if license_url.rstrip("/") != TEXT_LICENSE_URL.rstrip("/"):
        raise RuntimeError("Upstream File pages do not expose the expected CC BY-SA 4.0 license link")
    if not re.search(r"page content is under.+unless otherwise noted", footer_text, re.I):
        raise RuntimeError("Upstream File-page license footer could not be verified")
    return {
        "name": "CC BY-SA 4.0",
        "url": TEXT_LICENSE_URL,
        "evidence": (
            "Upstream File page declares CC BY-SA 4.0 for page content unless otherwise noted"
        ),
    }


def determine_license(
    record: dict[str, Any], file_page_license: dict[str, str]
) -> tuple[str | None, str | None, str]:
    metadata = record.get("extmetadata", {})
    candidates = " ".join(
        filter(
            None,
            (
                metadata_value(metadata, "LicenseShortName"),
                metadata_value(metadata, "UsageTerms"),
                metadata_value(metadata, "License"),
                record.get("_wikitext", ""),
            ),
        )
    )
    if RESTRICTIVE_LICENSE_RE.search(candidates):
        return None, None, "File page identifies restrictive or non-free terms"
    for pattern, canonical in ALLOWED_LICENSE_PATTERNS:
        if pattern.search(candidates):
            license_url = metadata_value(metadata, "LicenseUrl")
            if not license_url:
                license_url = {
                    "CC BY-SA 4.0": TEXT_LICENSE_URL,
                    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/",
                    "CC0": "https://creativecommons.org/publicdomain/zero/1.0/",
                    "Public domain": "https://creativecommons.org/publicdomain/mark/1.0/",
                }.get(canonical, "")
            return canonical, license_url or None, "Explicit reusable license on File page"
    return (
        file_page_license["name"],
        file_page_license["url"],
        file_page_license["evidence"],
    )


def safe_media_filename(title: str, sha1: str | None) -> str:
    suffix = Path(title).suffix.lower()
    if not re.fullmatch(r"\.[a-z0-9]{1,8}", suffix):
        suffix = ".bin"
    stem = title[: -len(Path(title).suffix)] if Path(title).suffix else title
    slug = slugify(stem, max_length=82)
    digest = (sha1 or hashlib.sha1(title.encode("utf-8")).hexdigest())[:10]
    return f"{slug}-{digest}{suffix}"


def prepare_media(
    client: ApiClient,
    media_records: list[dict[str, Any]],
    page_records: list[dict[str, Any]],
    file_page_license: dict[str, str],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, int]]:
    used_on: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for page in page_records:
        for image_title in page["image_titles"]:
            used_on[normalize_title(image_title)].append(page)

    media_lookup: dict[str, dict[str, Any]] = {}
    category_counts: Counter[str] = Counter()
    for record in media_records:
        key = normalize_title(record["source_title"])
        pages = used_on.get(key, [])
        record["used_on"] = sorted({page["local_page"] for page in pages})
        article_categories = Counter(page["category"] for page in pages)
        primary_article_category = article_categories.most_common(1)[0][0] if article_categories else "other"
        media_category = MEDIA_CATEGORY_MAP.get(primary_article_category, "misc")
        record["category"] = media_category
        license_name, license_url, license_reason = determine_license(record, file_page_license)
        record["license"] = license_name
        record["license_url"] = license_url
        record["license_evidence"] = license_reason
        metadata = record.get("extmetadata", {})
        record["artist"] = metadata_value(metadata, "Artist") or None
        record["credit"] = metadata_value(metadata, "Credit") or None
        record["attribution"] = metadata_value(metadata, "Attribution") or None
        record["last_synchronized"] = SYNCED_AT

        if not record.get("source_url"):
            record["import_status"] = "failed"
            record["reason"] = "No downloadable file URL returned by MediaWiki"
        elif not license_name:
            record["import_status"] = "skipped-license"
            record["reason"] = license_reason
        else:
            filename = safe_media_filename(record["source_title"], record.get("sha1"))
            local_path = PurePosixPath("assets") / "upstream" / "tensura" / media_category / filename
            destination = DOCS / Path(local_path.as_posix())
            source_url = record["source_url"]
            if (
                record.get("thumbnail_url")
                and record.get("mime") not in {"image/gif", "image/svg+xml"}
                and ((record.get("size") or 0) > 2_000_000 or (record.get("width") or 0) > 1600)
            ):
                source_url = record["thumbnail_url"]
                record["optimized_to_width"] = 1200
            try:
                if not destination.exists() or client.refresh:
                    client.download(source_url, destination)
                record["local_path"] = local_path.as_posix()
                record["download_url"] = source_url
                record["import_status"] = "imported"
                record["reason"] = "Reusable File-page media imported with attribution"
            except Exception as exc:
                record["import_status"] = "failed"
                record["reason"] = str(exc)
        category_counts[media_category] += 1
        record.pop("extmetadata", None)
        record.pop("_wikitext", None)
        media_lookup[key] = record

    return media_records, media_lookup, dict(sorted(category_counts.items()))


def local_relative_url(current_page: str, target_page: str) -> str:
    current_dir = PurePosixPath(current_page).parent
    return os.path.relpath(target_page, current_dir.as_posix()).replace("\\", "/")


def rendered_page_relative_url(current_page: str, target_page: str) -> str:
    """Return a directory URL relative to the rendered current page URL."""
    current_url_dir = PurePosixPath(current_page).with_suffix("")
    target_url_dir = PurePosixPath(target_page).with_suffix("")
    relative = os.path.relpath(
        target_url_dir.as_posix(), current_url_dir.as_posix()
    ).replace("\\", "/")
    return relative.rstrip("/") + "/"


def rendered_asset_relative_url(current_page: str, target_path: str) -> str:
    """Return an asset URL relative to the rendered current page URL."""
    current_url_dir = PurePosixPath(current_page).with_suffix("")
    return os.path.relpath(target_path, current_url_dir.as_posix()).replace("\\", "/")


def media_key_from_img(img: Tag) -> str:
    parent = img.parent if isinstance(img.parent, Tag) else None
    if parent and parent.name == "a":
        href = parent.get("href", "")
        parsed = urlparse(href)
        if parsed.path.startswith("/wiki/File:"):
            return normalize_title(unquote(parsed.path[len("/wiki/File:") :]))
    alt = img.get("alt", "")
    return normalize_title(alt)


def clean_article_html(
    record: dict[str, Any],
    canonical_lookup: dict[str, dict[str, Any]],
    redirect_lookup: dict[str, str],
    media_lookup: dict[str, dict[str, Any]],
) -> tuple[str, int, int, int]:
    soup = BeautifulSoup(record["_html"], "html.parser")
    root = soup.select_one(".mw-parser-output") or soup
    for comment in root.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()
    for selector in (
        "script",
        "style",
        "noscript",
        ".mw-editsection",
        ".toc",
        ".navbox",
        ".navbar",
        ".ranger-navbox",
        ".navigation-not-searchable",
        ".noprint",
        ".mw-empty-elt",
        "[role='navigation']",
    ):
        for element in root.select(selector):
            element.decompose()
    for element in root.find_all(True):
        for attribute in ("style", "onclick", "onload", "data-mw", "about", "typeof"):
            element.attrs.pop(attribute, None)

    links_converted = 0
    for anchor in root.find_all("a", href=True):
        href = html.unescape(str(anchor["href"]))
        parsed = urlparse(href)
        if href.startswith("//"):
            anchor["href"] = "https:" + href
            continue
        if parsed.path.startswith("/wiki/") and parsed.netloc in {"", urlparse(WIKI_ROOT).netloc}:
            source_title = unquote(parsed.path[len("/wiki/") :]).replace("_", " ")
            source_title = source_title.split("|", 1)[0]
            key = normalize_title(source_title)
            if key.startswith("file:") or key.startswith("category:"):
                anchor["href"] = wiki_url(source_title) + (
                    f"#{parsed.fragment}" if parsed.fragment else ""
                )
                continue
            if key in redirect_lookup:
                key = normalize_title(redirect_lookup[key])
            target = canonical_lookup.get(key)
            if target:
                anchor["href"] = rendered_page_relative_url(
                    record["local_page"], target["local_page"]
                )
                if parsed.fragment:
                    anchor["href"] += f"#{parsed.fragment}"
                links_converted += 1
            else:
                anchor["href"] = href if parsed.netloc else WIKI_ROOT + href
        elif href.startswith("/"):
            anchor["href"] = WIKI_ROOT + href

    imported_placements = 0
    skipped_placements = 0
    for img in list(root.find_all("img")):
        key = media_key_from_img(img)
        media = media_lookup.get(key)
        parent = img.parent if isinstance(img.parent, Tag) else None
        if media and media.get("import_status") == "imported":
            img["src"] = rendered_asset_relative_url(
                record["local_page"], media["local_path"]
            )
            for attribute in ("srcset", "data-src", "data-srcset", "loading"):
                img.attrs.pop(attribute, None)
            imported_placements += 1
        else:
            skipped_placements += 1
            if parent and parent.name == "a" and "image" in parent.get("class", []):
                parent.decompose()
            else:
                img.decompose()

    return str(root), links_converted, imported_placements, skipped_placements


def yaml_front_matter(record: dict[str, Any], aliases: list[str]) -> str:
    tags = list(dict.fromkeys(record["upstream_categories"] + aliases))
    metadata = {
        "title": record["display_title"],
        "description": record["description"] or f"Base Tensura reference for {record['display_title']}.",
        "tags": tags[:80],
    }
    return "---\n" + yaml.safe_dump(
        metadata, allow_unicode=True, sort_keys=False, width=1000
    ).strip() + "\n---\n"


def render_page(
    record: dict[str, Any],
    body_html: str,
    aliases: list[str],
    overlay: dict[str, Any] | None,
    skipped_placements: int,
) -> str:
    lines = [yaml_front_matter(record, aliases), f"# {record['display_title']}", ""]
    lines.append(
        '<span class="reference-badge">Base Tensura reference</span> '
        f'<span class="reference-category">{CATEGORY_INFO[record["category"]][0]}</span>'
    )
    lines.append("")
    if aliases:
        lines.append(f"**Also known as:** {', '.join(sorted(aliases, key=str.casefold))}")
        lines.append("")
    if record["category"] == "version-history":
        lines.extend(
            [
                "!!! info \"Historical upstream version\"",
                "    This article records upstream history and does not identify TSR's Minecraft runtime.",
                "",
            ]
        )
    lines.append('<div class="tensura-reference-article">')
    lines.append(body_html)
    lines.append("</div>")
    lines.append("")
    if skipped_placements:
        lines.extend(
            [
                "!!! note \"Upstream media\"",
                "    Some media shown by the source article is not redistributed here because its File page does not document a clearly reusable license. The exact source article remains linked below.",
                "",
            ]
        )
    if overlay:
        lines.extend(["## In Tensura: Sovereign Rebirth", ""])
        status = overlay.get("status")
        if status:
            lines.append(f'<span class="tsr-status">{status}</span>')
            lines.append("")
        text = overlay.get("content", "").strip()
        if text:
            lines.extend([text, ""])
        links = overlay.get("links", [])
        if links:
            rendered_links = []
            for item in links:
                target = item.get("target")
                url = local_relative_url(record["local_page"], target) if target else item["url"]
                rendered_links.append(f"[{item['label']}]({url})")
            lines.append("**TSR guides:** " + " · ".join(rendered_links))
            lines.append("")
    lines.extend(["---", "", "## Source and licensing", ""])
    revision_text = f"revision `{record['revision_id']}`" if record.get("revision_id") else "current recorded revision"
    modified_text = f", modified `{record['upstream_modified']}`" if record.get("upstream_modified") else ""
    lines.append(
        f"Base Tensura reference adapted from [{record['source_title']}]({record['source_url']}) "
        f"on the Tensura: Reincarnated Wiki ({revision_text}{modified_text}). "
        f"Adapted text is available under [CC BY-SA 4.0]({TEXT_LICENSE_URL})."
    )
    lines.append("")
    return "\n".join(lines)


def load_overlays() -> dict[str, dict[str, Any]]:
    path = DATA_ROOT / "tsr-wiki-overlays.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {normalize_title(title): value for title, value in data.get("overlays", {}).items()}


def extract_race_evolution(record: dict[str, Any]) -> dict[str, list[str]]:
    soup = BeautifulSoup(record["_html"], "html.parser")
    output: dict[str, list[str]] = {}
    for row in soup.select(".druid-row"):
        label_node = row.select_one(".druid-label")
        data_node = row.select_one(".druid-data")
        if not label_node or not data_node:
            continue
        label = " ".join(label_node.get_text(" ", strip=True).split())
        if not re.search(r"evolution|evolves|previous|predecessor|successor|harvest|awakening|naming", label, re.I):
            continue
        values = [" ".join(anchor.get_text(" ", strip=True).split()) for anchor in data_node.find_all("a")]
        if not values:
            text = " ".join(data_node.get_text(" ", strip=True).split())
            values = [text] if text else []
        if values:
            output[label] = list(dict.fromkeys(values))
    return output


def generate_evolution_index(records: list[dict[str, Any]]) -> str:
    race_records = [record for record in records if record["category"] == "races"]
    sections = [
        "# Race Evolution Relationships",
        "",
        "This directory reproduces only evolution relationships explicitly exposed by the upstream race infoboxes. It does not infer branches from similar names.",
        "",
    ]
    relationship_count = 0
    for record in sorted(race_records, key=lambda item: item["display_title"].casefold()):
        relationships = extract_race_evolution(record)
        if not relationships:
            continue
        relationship_count += sum(len(values) for values in relationships.values())
        relative = os.path.relpath(
            record["local_page"], "tensura-reference/races"
        ).replace("\\", "/")
        sections.extend([f"## [{record['display_title']}]({relative})", ""])
        for label, values in relationships.items():
            sections.append(f"- **{label}:** {', '.join(values)}")
        sections.append("")
    if relationship_count == 0:
        sections.extend(
            [
                "No structured evolution fields were exposed by the current upstream race infoboxes. Consult individual race pages for prose requirements.",
                "",
            ]
        )
    sections.extend(
        [
            "---",
            "",
            f"Generated from `{len(race_records)}` imported race articles; `{relationship_count}` explicit relationship values indexed.",
            "",
        ]
    )
    return "\n".join(sections)


def generate_category_index(category: str, records: list[dict[str, Any]]) -> str:
    title, description = CATEGORY_INFO[category]
    category_records = [record for record in records if record["category"] == category]
    lines = [f"# {title}", "", description, ""]
    lines.append(f"**{len(category_records)} upstream articles indexed.**")
    lines.append("")
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in category_records:
        first = record["display_title"][:1].upper()
        buckets[first if first.isalnum() else "#"].append(record)
    for bucket in sorted(buckets, key=lambda value: (value == "#", value)):
        lines.extend([f"## {bucket}", ""])
        for record in sorted(buckets[bucket], key=lambda item: item["display_title"].casefold()):
            relative = PurePosixPath(record["local_page"]).name
            summary = record["description"].replace("\n", " ").strip()
            if len(summary) > 160:
                summary = summary[:157].rstrip() + "…"
            suffix = f" — {summary}" if summary else ""
            lines.append(f"- [{record['display_title']}]({relative}){suffix}")
        lines.append("")
    return "\n".join(lines)


def generate_reference_index(
    siteinfo: dict[str, Any], records: list[dict[str, Any]], redirects: list[dict[str, Any]], media: list[dict[str, Any]]
) -> str:
    category_counts = Counter(record["category"] for record in records)
    imported_media = sum(record.get("import_status") == "imported" for record in media)
    lines = [
        "# Tensura: Reincarnated Reference",
        "",
        "This generated library is the base-mod layer of the TSR wiki. It preserves the live upstream article corpus as a searchable local reference while TSR-specific behavior remains clearly separated in dedicated notes and guides.",
        "",
        "!!! warning \"Version context\"",
        "    Upstream articles may describe historical Minecraft or mod versions. TSR targets **Minecraft 1.21.1**, **NeoForge 21.1.248**, and **Java 21**. A base article is not proof that a historical feature is active in TSR's frozen runtime.",
        "",
        "## Snapshot coverage",
        "",
        f"- **Canonical articles imported:** {len(records)}",
        f"- **Redirect aliases processed:** {sum(item.get('status') == 'processed' for item in redirects)}",
        f"- **Media files discovered:** {len(media)}",
        f"- **Explicitly reusable media imported:** {imported_media}",
        f"- **Upstream synchronization:** {SYNCED_AT}",
        f"- **Upstream MediaWiki:** {siteinfo['general'].get('generator', 'MediaWiki')}",
        "",
        "## Browse the reference",
        "",
    ]
    for category in CATEGORY_ORDER:
        title, description = CATEGORY_INFO[category]
        index_path = PurePosixPath(category) / "index.md"
        lines.append(
            f"- **[{title}]({index_path.as_posix()})** — {category_counts.get(category, 0)} articles. {description}"
        )
    lines.extend(
        [
            "",
            "## TSR layer",
            "",
            "Use the main TSR guides for installed-mod status, configured values, compatibility, quests, progression, world generation, storage, and server behavior. Generated base pages include a TSR section only when a verified project-specific overlay exists.",
            "",
            "See [Upstream Attribution](../project/upstream-attribution.md) and [Ingestion Coverage](../project/ingestion-coverage.md) for licensing and audit details.",
            "",
        ]
    )
    return "\n".join(lines)


def public_page_record(record: dict[str, Any], aliases: list[str]) -> dict[str, Any]:
    return {
        key: value
        for key, value in {**record, "redirect_aliases": sorted(aliases, key=str.casefold)}.items()
        if not key.startswith("_")
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_reports(
    siteinfo: dict[str, Any],
    page_records: list[dict[str, Any]],
    skipped_pages: list[dict[str, Any]],
    redirect_records: list[dict[str, Any]],
    failed_pages: list[dict[str, Any]],
    media_records: list[dict[str, Any]],
    aliases_by_target: dict[str, list[str]],
    counters: Counter[str],
    media_category_counts: dict[str, int],
    discovered_image_titles: int,
) -> dict[str, Any]:
    public_pages = [
        public_page_record(record, aliases_by_target.get(record["source_title"], []))
        for record in page_records
    ]
    write_json(
        DATA_ROOT / "upstream_tensura_pages.json",
        {
            "source": WIKI_ROOT + "/",
            "text_license": "CC BY-SA 4.0",
            "text_license_url": TEXT_LICENSE_URL,
            "synchronized_at": SYNCED_AT,
            "pages": public_pages,
            "skipped_pages": skipped_pages,
            "redirects": redirect_records,
            "failed_pages": failed_pages,
        },
    )
    write_json(
        DATA_ROOT / "upstream_tensura_media.json",
        {
            "source": WIKI_ROOT + "/",
            "synchronized_at": SYNCED_AT,
            "policy": (
                "Media is imported under the upstream File-page CC BY-SA 4.0 declaration unless "
                "the individual File page states restrictive or non-free terms."
            ),
            "media": media_records,
        },
    )

    category_counts = Counter(record["category"] for record in page_records)
    media_status_counts = Counter(record.get("import_status", "unknown") for record in media_records)
    coverage = {
        "source": WIKI_ROOT + "/",
        "synchronized_at": SYNCED_AT,
        "site_statistics": siteinfo.get("statistics", {}),
        "upstream_pages_discovered": len(page_records) + len(skipped_pages) + len(failed_pages),
        "pages_considered_relevant": len(page_records) + len(failed_pages),
        "pages_imported": len(page_records),
        "redirects_discovered": len(redirect_records),
        "redirects_processed": sum(item.get("status") == "processed" for item in redirect_records),
        "redirects_skipped": sum(item.get("status") == "skipped" for item in redirect_records),
        "redirects_failed": sum(item.get("status") == "failed" for item in redirect_records),
        "pages_skipped": len(skipped_pages),
        "pages_failed": len(failed_pages),
        "images_discovered": discovered_image_titles,
        "image_file_records_resolved": len(media_records),
        "images_imported": media_status_counts.get("imported", 0),
        "images_skipped_due_to_licensing": media_status_counts.get("skipped-license", 0),
        "images_failed": media_status_counts.get("failed", 0),
        "media_placements_imported": counters.get("media_placements_imported", 0),
        "media_placements_omitted": counters.get("media_placements_omitted", 0),
        "internal_links_converted": counters.get("internal_links_converted", 0),
        "broken_links_remaining": counters.get("broken_links_remaining", 0),
        "content_categories": dict(sorted(category_counts.items())),
        "media_categories": media_category_counts,
        "media_statuses": dict(sorted(media_status_counts.items())),
        "failures": failed_pages,
    }
    write_json(DATA_ROOT / "upstream_tensura_coverage.json", coverage)
    return coverage


def render_coverage_report(coverage: dict[str, Any]) -> str:
    lines = [
        "# Tensura Wiki Ingestion Coverage",
        "",
        f"**Snapshot:** `{coverage['synchronized_at']}`  ",
        f"**Source:** [{coverage['source']}]({coverage['source']})",
        "",
        "## Article coverage",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Canonical pages discovered | {coverage['upstream_pages_discovered']} |",
        f"| Pages considered relevant | {coverage['pages_considered_relevant']} |",
        f"| Pages imported/adapted | {coverage['pages_imported']} |",
        f"| Redirects processed | {coverage['redirects_processed']} |",
        f"| Redirects skipped as non-content | {coverage['redirects_skipped']} |",
        f"| Redirects failed | {coverage['redirects_failed']} |",
        f"| Pages skipped | {coverage['pages_skipped']} |",
        f"| Pages failed | {coverage['pages_failed']} |",
        "",
        "## Media coverage",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Images discovered | {coverage['images_discovered']} |",
        f"| Distinct File records resolved | {coverage['image_file_records_resolved']} |",
        f"| Images imported | {coverage['images_imported']} |",
        f"| Imported image placements | {coverage['media_placements_imported']} |",
        f"| Images skipped due to licensing | {coverage['images_skipped_due_to_licensing']} |",
        f"| Images failed | {coverage['images_failed']} |",
        "",
        "The upstream File pages declare page content under CC BY-SA 4.0 unless otherwise noted. The synchronizer preserves source and revision records, imports media under that declaration, and rejects any file whose metadata or page text states restrictive or non-free terms.",
        "",
        "## Link conversion",
        "",
        f"- Internal links converted to local TSR reference pages: **{coverage['internal_links_converted']}**",
        f"- Broken local links remaining: **{coverage['broken_links_remaining']}**",
        "",
        "## Content categories",
        "",
        "| Category | Imported pages |",
        "|---|---:|",
    ]
    for category, count in coverage["content_categories"].items():
        lines.append(f"| {CATEGORY_INFO.get(category, (category, ''))[0]} | {count} |")
    lines.extend(["", "## Media categories", "", "| Category | Discovered files |", "|---|---:|"])
    for category, count in coverage["media_categories"].items():
        lines.append(f"| {category.replace('-', ' ').title()} | {count} |")
    lines.extend(
        [
            "",
            "## Machine-readable reports",
            "",
            "- `data/upstream_tensura_pages.json`",
            "- `data/upstream_tensura_media.json`",
            "- `data/upstream_tensura_coverage.json`",
            "",
        ]
    )
    return "\n".join(lines)


def render_attribution(siteinfo: dict[str, Any]) -> str:
    rights = siteinfo.get("rightsinfo", {})
    license_text = rights.get("text", "Creative Commons Attribution-ShareAlike 4.0 License")
    license_url = rights.get("url", TEXT_LICENSE_URL)
    return f"""# Upstream Attribution

The generated **Tensura: Reincarnated Reference** is adapted from the
[Tensura: Reincarnated Wiki]({WIKI_ROOT}/), synchronized on `{SYNCED_AT}`.
Each generated article links to its exact source page and records the upstream
revision ID and modified timestamp used by the synchronizer.

## Text license

The upstream site's MediaWiki rights metadata identifies its reusable text as
[{license_text}]({license_url}). Adapted upstream text in
`docs/tensura-reference/` remains available under the same license. TSR-specific
guidance is layered separately and identified by the **In Tensura: Sovereign
Rebirth** heading.

## Media license policy

The upstream File pages declare page content under
[Creative Commons Attribution-ShareAlike 4.0]({TEXT_LICENSE_URL}) unless otherwise
noted. The synchronizer verifies that File-page declaration, records each
file's source page and revision, and checks its metadata and page text for
exceptions. Fair-use claims, non-free terms, and restrictive notices cause the
file to be skipped.

The complete decision record, source URL, File page, license evidence, local
path, and page associations are stored in
`data/upstream_tensura_media.json`.

## Separation from TSR

Tensura: Sovereign Rebirth did not create Tensura: Reincarnated or the upstream
wiki. Base-mod facts retain their upstream version context. TSR runtime claims
come from the frozen manifest, installed artifacts, tracked configuration, and
recorded validation evidence in this repository.
"""


def ensure_generated_roots_clean() -> None:
    reference_resolved = REFERENCE_ROOT.resolve()
    docs_resolved = DOCS.resolve()
    if docs_resolved not in reference_resolved.parents:
        raise RuntimeError(f"Unsafe generated reference path: {reference_resolved}")
    if REFERENCE_ROOT.exists():
        shutil.rmtree(REFERENCE_ROOT)
    REFERENCE_ROOT.mkdir(parents=True, exist_ok=True)


def ensure_asset_root_clean() -> None:
    asset_resolved = ASSET_ROOT.resolve()
    docs_resolved = DOCS.resolve()
    if docs_resolved not in asset_resolved.parents:
        raise RuntimeError(f"Unsafe generated asset path: {asset_resolved}")
    if ASSET_ROOT.exists():
        shutil.rmtree(ASSET_ROOT)


def normalize_generated_text(value: str) -> str:
    """Remove source-line whitespace without changing rendered content."""
    return "\n".join(line.rstrip() for line in value.splitlines()).rstrip() + "\n"


def audit_generated_links(root: Path) -> list[str]:
    errors: list[str] = []
    markdown_link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    html_link_re = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)
    for page in sorted(root.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        for raw_target in markdown_link_re.findall(text):
            target = html.unescape(raw_target).strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (page.parent / target).resolve()
            if not candidate.exists():
                errors.append(f"{page.relative_to(ROOT)} -> missing {target}")
        for raw_target in html_link_re.findall(text):
            target = html.unescape(raw_target).strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (page.with_suffix("") / target).resolve()
            source_candidate = Path(str(candidate).rstrip("\\/") + ".md") if target.endswith("/") else candidate
            if not source_candidate.exists():
                errors.append(f"{page.relative_to(ROOT)} -> missing rendered target {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Ignore cached API responses and media")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--pace", type=float, default=0.18, help="Minimum seconds between requests")
    parser.add_argument("--limit", type=int, help="Development-only canonical article limit")
    args = parser.parse_args()

    client = ApiClient(args.cache_dir, refresh=args.refresh, pace=max(args.pace, 0.05))
    siteinfo = fetch_siteinfo(client)
    canonical = enumerate_pages(client, "nonredirects")
    redirects = enumerate_pages(client, "redirects")
    if args.limit:
        canonical = canonical[: args.limit]
    print(
        f"Discovered {len(canonical)} canonical articles and {len(redirects)} redirects",
        flush=True,
    )

    revisions = fetch_revision_metadata(client, canonical)
    redirect_map, redirect_records = fetch_redirect_map(client, redirects)
    parsed_articles, failed_pages = parse_articles(client, canonical, revisions)
    page_records, skipped_pages = build_page_records(parsed_articles, revisions)
    resolved_redirects, aliases_by_target = resolve_redirects(
        redirect_map, page_records, redirect_records, skipped_pages
    )

    image_titles = sorted(
        {image for record in page_records for image in record["image_titles"]},
        key=str.casefold,
    )
    media_records = fetch_media_metadata(client, image_titles)
    file_page_license = verify_file_page_license(client, media_records)
    ensure_asset_root_clean()
    media_records, media_lookup, media_category_counts = prepare_media(
        client, media_records, page_records, file_page_license
    )

    canonical_lookup = {
        normalize_title(record["source_title"]): record for record in page_records
    }
    overlays = load_overlays()
    ensure_generated_roots_clean()
    counters: Counter[str] = Counter()
    for record in page_records:
        body_html, links, imported_placements, skipped_placements = clean_article_html(
            record, canonical_lookup, resolved_redirects, media_lookup
        )
        counters["internal_links_converted"] += links
        counters["media_placements_imported"] += imported_placements
        counters["media_placements_omitted"] += skipped_placements
        aliases = aliases_by_target.get(record["source_title"], [])
        overlay = overlays.get(normalize_title(record["source_title"]))
        output = DOCS / Path(record["local_page"])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            normalize_generated_text(
                render_page(record, body_html, aliases, overlay, skipped_placements)
            ),
            encoding="utf-8",
        )

    for category in CATEGORY_ORDER:
        index = REFERENCE_ROOT / Path(category) / "index.md"
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text(
            normalize_generated_text(generate_category_index(category, page_records)),
            encoding="utf-8",
        )
    evolution_path = REFERENCE_ROOT / "races" / "evolution-trees.md"
    evolution_path.write_text(
        normalize_generated_text(generate_evolution_index(page_records)), encoding="utf-8"
    )
    (REFERENCE_ROOT / "index.md").write_text(
        normalize_generated_text(
            generate_reference_index(siteinfo, page_records, redirect_records, media_records)
        ),
        encoding="utf-8",
    )
    generated_link_errors = audit_generated_links(REFERENCE_ROOT)
    counters["broken_links_remaining"] = len(generated_link_errors)

    coverage = write_reports(
        siteinfo,
        page_records,
        skipped_pages,
        redirect_records,
        failed_pages,
        media_records,
        aliases_by_target,
        counters,
        media_category_counts,
        len(image_titles),
    )
    project_root = DOCS / "project"
    project_root.mkdir(parents=True, exist_ok=True)
    (project_root / "upstream-attribution.md").write_text(
        normalize_generated_text(render_attribution(siteinfo)), encoding="utf-8"
    )
    (project_root / "ingestion-coverage.md").write_text(
        normalize_generated_text(render_coverage_report(coverage)), encoding="utf-8"
    )

    print(
        "Generated reference: "
        f"{coverage['pages_imported']} pages, {coverage['redirects_processed']} redirects, "
        f"{coverage['images_discovered']} media discovered, "
        f"{coverage['images_imported']} media imported, "
        f"{coverage['images_skipped_due_to_licensing']} skipped for licensing",
        flush=True,
    )
    if failed_pages:
        print(f"WARNING: {len(failed_pages)} pages failed; inspect the coverage report", file=sys.stderr)
        return 2
    if generated_link_errors:
        print(
            f"WARNING: {len(generated_link_errors)} generated links are broken; inspect the checker output",
            file=sys.stderr,
        )
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
