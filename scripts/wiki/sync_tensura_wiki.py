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
DATA_ROOT = ROOT / "data"
SOURCE_KEY = "tensura"
REFERENCE_SLUG = "tensura-reference"
DATA_STEM = "upstream_tensura"
SOURCE_WIKI_NAME = "Tensura: Reincarnated Wiki"
SOURCE_REFERENCE_TITLE = "Tensura: Reincarnated Reference"
SOURCE_BADGE = "Base Tensura reference"
SOURCE_CONTEXT_LABEL = "base-mod"
REFERENCE_ROOT = DOCS / REFERENCE_SLUG
ASSET_ROOT = DOCS / "assets" / "upstream" / SOURCE_KEY
ATTRIBUTION_REPORT = DOCS / "project" / "upstream-attribution.md"
COVERAGE_REPORT = DOCS / "project" / "ingestion-coverage.md"
DEFAULT_CACHE = ROOT / ".build" / "wiki-cache"
API_URL = "https://tensura.wiki.gg/api.php"
WIKI_ROOT = "https://tensura.wiki.gg"
SOURCE_EXCLUDED_TITLES: set[str] = set()
TEXT_LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
USER_AGENT = (
    "TSRWikiIngest/1.0 "
    "(+https://github.com/lastnahaj/Tensura-Sovereign-Rebirth)"
)


def configure_source(source: str) -> Path:
    global SOURCE_KEY, REFERENCE_SLUG, DATA_STEM, SOURCE_WIKI_NAME
    global SOURCE_REFERENCE_TITLE, SOURCE_BADGE, SOURCE_CONTEXT_LABEL
    global REFERENCE_ROOT, ASSET_ROOT, ATTRIBUTION_REPORT, COVERAGE_REPORT
    global API_URL, WIKI_ROOT, SOURCE_EXCLUDED_TITLES

    if source == "tensura":
        SOURCE_KEY = "tensura"
        REFERENCE_SLUG = "tensura-reference"
        DATA_STEM = "upstream_tensura"
        SOURCE_WIKI_NAME = "Tensura: Reincarnated Wiki"
        SOURCE_REFERENCE_TITLE = "Tensura: Reincarnated Reference"
        SOURCE_BADGE = "Base Tensura reference"
        SOURCE_CONTEXT_LABEL = "base-mod"
        API_URL = "https://tensura.wiki.gg/api.php"
        WIKI_ROOT = "https://tensura.wiki.gg"
        ATTRIBUTION_REPORT = DOCS / "project" / "upstream-attribution.md"
        COVERAGE_REPORT = DOCS / "project" / "ingestion-coverage.md"
        SOURCE_EXCLUDED_TITLES = set()
        cache = ROOT / ".build" / "wiki-cache"
    elif source == "mysticism":
        SOURCE_KEY = "mysticism"
        REFERENCE_SLUG = "mysticism-reference"
        DATA_STEM = "upstream_mysticism"
        SOURCE_WIKI_NAME = "Tensura Reincarnated: Mysticism Wiki"
        SOURCE_REFERENCE_TITLE = "TR Mysticism Reference"
        SOURCE_BADGE = "TR Mysticism reference"
        SOURCE_CONTEXT_LABEL = "companion add-on"
        API_URL = "https://trmysticism.wiki.gg/api.php"
        WIKI_ROOT = "https://trmysticism.wiki.gg"
        ATTRIBUTION_REPORT = DOCS / "project" / "mysticism-upstream-attribution.md"
        COVERAGE_REPORT = DOCS / "project" / "mysticism-ingestion-coverage.md"
        SOURCE_EXCLUDED_TITLES = {
            "archive/skills/abilities",
            "category",
            "example character",
        }
        cache = ROOT / ".build" / "wiki-cache-mysticism"
    else:
        raise ValueError(f"Unsupported source: {source}")

    REFERENCE_ROOT = DOCS / REFERENCE_SLUG
    ASSET_ROOT = DOCS / "assets" / "upstream" / SOURCE_KEY
    return cache
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
    "mobs": ("Mobs", "Documented entity catalog."),
    "bosses": ("Bosses", "Documented boss encounters."),
    "items": ("Items & Materials", "Materials, consumables, drops, and special items."),
    "weapons": ("Weapons", "Documented weapons and combat equipment."),
    "armor": ("Armor", "Documented armor pieces and sets."),
    "tools": ("Tools", "Tools and utility equipment."),
    "blocks": ("Blocks", "Mechanically relevant blocks and block families."),
    "structures": ("Structures", "Documented structures and generation information."),
    "biomes": ("Biomes", "Documented biomes and biome-specific behavior."),
    "dimensions": ("Dimensions", "Dimensions, portals, access, and world content."),
    "commands": ("Commands", "Player and administrator command reference."),
    "configuration": ("Configuration", "Configuration reference."),
    "gamerules": ("Gamerules", "Tensura-specific gamerules and behavior."),
    "version-history": ("Version History", "Historical releases and upstream change records."),
    "other": ("Other Reference", "Additional maintained reference articles."),
}

CATEGORY_ORDER = list(CATEGORY_INFO)

VISUAL_ASSETS = {
    "evolution": "assets/images/reference-races-evolution.png",
    "abilities": "assets/images/reference-skills-magic.png",
    "bestiary": "assets/images/reference-bestiary.png",
    "world": "assets/images/reference-world-equipment.png",
}

VISUAL_GROUPS = {
    "core-mechanics": "evolution",
    "races": "evolution",
    "skills/intrinsic": "abilities",
    "skills/common": "abilities",
    "skills/extra": "abilities",
    "skills/unique": "abilities",
    "skills/ultimate": "abilities",
    "skills/other": "abilities",
    "resistances": "abilities",
    "magic": "abilities",
    "battlewill": "abilities",
    "arts": "abilities",
    "mobs": "bestiary",
    "bosses": "bestiary",
    "items": "world",
    "weapons": "world",
    "armor": "world",
    "tools": "world",
    "blocks": "world",
    "structures": "world",
    "biomes": "world",
    "dimensions": "world",
    "commands": "world",
    "configuration": "world",
    "gamerules": "world",
    "version-history": "world",
    "other": "world",
}

REFERENCE_PATHS = (
    (
        "evolution",
        "Reincarnation & Evolution",
        "Choose a form, understand its requirements, and follow explicit race branches.",
        ("core-mechanics", "races"),
    ),
    (
        "abilities",
        "Skills & Arcana",
        "Explore abilities by class, magical system, resistance, and combat discipline.",
        (
            "skills/intrinsic",
            "skills/common",
            "skills/extra",
            "skills/unique",
            "skills/ultimate",
            "skills/other",
            "resistances",
            "magic",
            "battlewill",
            "arts",
        ),
    ),
    (
        "bestiary",
        "Bestiary & Bosses",
        "Meet the creatures, named threats, and major encounters documented upstream.",
        ("mobs", "bosses"),
    ),
    (
        "world",
        "World & Equipment",
        "Browse gear, materials, structures, terrain, and the technical reference.",
        (
            "items",
            "weapons",
            "armor",
            "tools",
            "blocks",
            "structures",
            "biomes",
            "dimensions",
            "commands",
            "configuration",
            "gamerules",
            "version-history",
            "other",
        ),
    ),
)
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
    "Candidates_for_deletion",
    "Crafting_Table_templates",
    "Lua-based_templates",
    "Main_page_boxes",
    "Table_templates",
    "Templates_with_no_documentation",
    "Tensura:_Reincarnated_Wiki",
    "Tensura_Reincarnated:_Mysticism_Wiki",
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
        if parsed.scheme != "https" or parsed.hostname != urlparse(WIKI_ROOT).hostname:
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

    if (
        re.match(r"^\d+\.\d+(?:\.\d+)?\s", title)
        or "version history" in combined
        or title_parts[0] == "version"
    ):
        return "version-history"
    if (
        leaf in CORE_MECHANIC_TERMS
        or normalized_title
        in {
            "compatibility system",
            "ep, magicule, aura",
            "getting started",
            "soul quality",
        }
        or leaf in {"chantspeed", "damage types", "dodging", "engravings", "gear evolution", "trading"}
        or title_parts[0] in {"mechanics", "effects", "effect"}
        or any(term in category_text for term in ("mechanic", "progression"))
    ):
        return "core-mechanics"
    if (
        title_parts[0] in {"races", "race"}
        or normalized_title in {"angel", "insect"}
        or re.search(r"\braces?\b", category_text)
    ):
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
    if title_parts[0] == "structures and biomes":
        return "biomes" if "biome" in leaf else "structures"
    if leaf == "ruins":
        return "structures"
    if title_parts[0] == "biomes":
        return "biomes"
    if title_parts[0] == "dimensions":
        return "dimensions"
    if normalized_title == "spirit realm":
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
    if normalize_title(title) in SOURCE_EXCLUDED_TITLES:
        return "Wiki-management, archive, or example content rather than maintained mod reference"
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
    preferred_case_variant: dict[str, tuple[str, int]] = {}
    for article in parsed_articles:
        listing = article["listing"]
        revision = revisions.get(listing["pageid"], {})
        rank = (revision.get("modified") or "", listing["pageid"])
        key = normalize_title(listing["title"])
        if key not in preferred_case_variant or rank > preferred_case_variant[key]:
            preferred_case_variant[key] = rank

    for article in parsed_articles:
        listing = article["listing"]
        parse_data = article["parse"]
        categories = category_names(parse_data)
        properties = parse_data.get("properties", {})
        description = " ".join(strip_html(properties.get("description")).split())
        revision = revisions.get(listing["pageid"], {})
        preferred_rank = preferred_case_variant[normalize_title(listing["title"])]
        current_rank = (revision.get("modified") or "", listing["pageid"])
        if current_rank != preferred_rank:
            skipped.append(
                {
                    "source_title": listing["title"],
                    "source_url": wiki_url(listing["title"]),
                    "page_id": listing["pageid"],
                    "revision_id": parse_data.get("revid") or revision.get("revision_id"),
                    "upstream_modified": revision.get("modified"),
                    "upstream_categories": categories,
                    "import_status": "skipped",
                    "reason": "Older case-only duplicate of another canonical article",
                }
            )
            continue
        reason = non_content_reason(listing["title"], categories, description)
        if reason:
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
        local_page = PurePosixPath(REFERENCE_SLUG) / primary_category / f"{slug}.md"
        display_title = strip_html(parse_data.get("displaytitle")) or listing["title"].split("/")[-1]
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
    source_title_owners = {
        (record["category"], normalize_title(record["source_title"].split("/")[-1])): record[
            "page_id"
        ]
        for record in records
    }
    for record in records:
        source_leaf = record["source_title"].split("/")[-1]
        display_key = (record["category"], normalize_title(record["display_title"]))
        if (
            normalize_title(record["display_title"]) != normalize_title(source_leaf)
            and source_title_owners.get(display_key) not in {None, record["page_id"]}
        ):
            record["display_title"] = source_leaf

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
    seen_files: set[tuple[str, Any]] = set()
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
            identity = (
                ("page", page.get("pageid"))
                if page.get("pageid")
                else ("title", normalize_title(title))
            )
            # Multiple requested aliases can resolve to the same File page. Keep
            # one provenance record and one local asset for that upstream file.
            if identity in seen_files:
                continue
            seen_files.add(identity)
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
            local_path = PurePosixPath("assets") / "upstream" / SOURCE_KEY / media_category / filename
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
    current_path = PurePosixPath(current_page)
    target_path = PurePosixPath(target_page)
    current_url_dir = current_path.parent if current_path.name == "index.md" else current_path.with_suffix("")
    target_url_dir = target_path.parent if target_path.name == "index.md" else target_path.with_suffix("")
    relative = os.path.relpath(
        target_url_dir.as_posix(), current_url_dir.as_posix()
    ).replace("\\", "/")
    return "./" if relative == "." else relative.rstrip("/") + "/"


def rendered_asset_relative_url(current_page: str, target_path: str) -> str:
    """Return an asset URL relative to the rendered current page URL."""
    current_path = PurePosixPath(current_page)
    current_url_dir = current_path.parent if current_path.name == "index.md" else current_path.with_suffix("")
    return os.path.relpath(target_path, current_url_dir.as_posix()).replace("\\", "/")


def visual_group(category: str) -> str:
    return VISUAL_GROUPS.get(category, "world")


def visual_asset(category: str) -> str:
    return VISUAL_ASSETS[visual_group(category)]


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
    primary_key = normalize_title((record.get("_primary_media") or {}).get("source_title", ""))
    primary_marked = False
    for img in list(root.find_all("img")):
        key = media_key_from_img(img)
        media = media_lookup.get(key)
        parent = img.parent if isinstance(img.parent, Tag) else None
        if media and media.get("import_status") == "imported":
            img["src"] = rendered_asset_relative_url(
                record["local_page"], media["local_path"]
            )
            for attribute in ("srcset", "data-src", "data-srcset"):
                img.attrs.pop(attribute, None)
            img["loading"] = "lazy"
            img["decoding"] = "async"
            if key == primary_key and not primary_marked and not img.find_parent(class_="druid-container"):
                duplicate = parent if parent and parent.name == "a" else img
                duplicate["class"] = list(duplicate.get("class", [])) + ["reference-overview-duplicate"]
                primary_marked = True
            imported_placements += 1
        else:
            skipped_placements += 1
            if parent and parent.name == "a" and "image" in parent.get("class", []):
                parent.decompose()
            else:
                img.decompose()

    return str(root), links_converted, imported_placements, skipped_placements


def attach_page_media(
    page_records: list[dict[str, Any]], media_lookup: dict[str, dict[str, Any]]
) -> None:
    for record in page_records:
        media = []
        for order, image_title in enumerate(record["image_titles"]):
            item = media_lookup.get(normalize_title(image_title))
            if not item or item.get("import_status") != "imported":
                continue
            if item not in media:
                item_copy = dict(item)
                item_copy["_placement_order"] = order
                media.append(item_copy)
        record["_media"] = media
        if not media:
            record["_primary_media"] = None
            continue

        display = normalize_title(record["display_title"])

        def media_score(item: dict[str, Any]) -> tuple[int, int]:
            source = normalize_title(Path(item["source_title"]).stem)
            width = item.get("width") or 0
            height = item.get("height") or 0
            area = width * height
            score = 0
            if display and (display in source or source in display):
                score += 120
            if "invicon" in source or "icon" in source:
                score += 28 if record["category"] in {"items", "weapons", "armor", "tools"} else 8
            if area >= 40_000:
                score += 24
            if width and height and 0.55 <= width / height <= 1.8:
                score += 10
            if item.get("mime") == "image/gif":
                score += 4
            if re.search(r"\bwip\d*\b|placeholder|missing", source):
                score -= 200
            return score, -item["_placement_order"]

        record["_primary_media"] = max(media, key=media_score)


def article_summary(record: dict[str, Any], body_html: str, max_length: int = 360) -> str:
    soup = BeautifulSoup(body_html, "html.parser")
    candidate = ""
    for heading in soup.find_all(["h2", "h3"]):
        if normalize_title(heading.get_text(" ", strip=True)) not in {"description", "overview", "summary"}:
            continue
        node = heading.find_next_sibling()
        while node and getattr(node, "name", None) not in {"h2", "h3"}:
            text = " ".join(node.get_text(" ", strip=True).split()) if isinstance(node, Tag) else ""
            if len(text) >= 24:
                candidate = text
                break
            node = node.find_next_sibling()
        if candidate:
            break
    if not candidate:
        for paragraph in soup.find_all("p"):
            if paragraph.find_parent(class_="druid-container"):
                continue
            text = " ".join(paragraph.get_text(" ", strip=True).split())
            if len(text) >= 20:
                candidate = text
                break
    if not candidate:
        candidate = " ".join((record.get("description") or "").split())
    candidate = re.sub(r"View or edit this template.*$", "", candidate, flags=re.I).strip()
    if not candidate:
        candidate = f"Upstream reference information for {record['display_title']}."
    if len(candidate) > max_length:
        candidate = candidate[: max_length - 1].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return candidate


def article_sections(body_html: str, limit: int = 8) -> list[tuple[str, str]]:
    soup = BeautifulSoup(body_html, "html.parser")
    sections: list[tuple[str, str]] = []
    for heading in soup.find_all("h2"):
        title = " ".join(heading.get_text(" ", strip=True).split())
        anchor = heading.get("id")
        if not anchor:
            marker = heading.select_one("[id]")
            anchor = marker.get("id") if marker else None
        if title and anchor:
            sections.append((str(anchor), title))
        if len(sections) >= limit:
            break
    return sections


def build_related_map(records: list[dict[str, Any]], limit: int = 4) -> dict[int, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["category"]].append(record)
    related: dict[int, list[dict[str, Any]]] = {}
    for category_records in grouped.values():
        ordered = sorted(category_records, key=lambda item: item["display_title"].casefold())
        for index, record in enumerate(ordered):
            candidates: list[dict[str, Any]] = []
            distance = 1
            while len(candidates) < limit and (index - distance >= 0 or index + distance < len(ordered)):
                if index - distance >= 0:
                    candidates.append(ordered[index - distance])
                if len(candidates) < limit and index + distance < len(ordered):
                    candidates.append(ordered[index + distance])
                distance += 1
            related[record["page_id"]] = candidates
    return related


def yaml_front_matter(record: dict[str, Any], aliases: list[str]) -> str:
    tags = list(dict.fromkeys(record["upstream_categories"] + aliases))
    metadata = {
        "title": record["display_title"],
        "description": record["description"] or f"{SOURCE_BADGE} for {record['display_title']}.",
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
    related: list[dict[str, Any]],
) -> str:
    lines = [yaml_front_matter(record, aliases), f"# {record['display_title']}", ""]
    lines.append(
        f'<span class="reference-badge">{html.escape(SOURCE_BADGE)}</span> '
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

    summary = article_summary(record, body_html)
    sections = article_sections(body_html)
    primary_media = record.get("_primary_media")
    if primary_media:
        overview_asset = rendered_asset_relative_url(
            record["local_page"], primary_media["local_path"]
        )
        overview_alt = f"{record['display_title']} source reference"
        media_caption = (
            f'<a href="{html.escape(primary_media["source_file_page"], quote=True)}">'
            f'{html.escape(primary_media["source_title"])} · CC BY-SA 4.0</a>'
        )
        media_class = "reference-overview-media--source"
    else:
        overview_asset = rendered_asset_relative_url(
            record["local_page"], visual_asset(record["category"])
        )
        overview_alt = ""
        media_caption = "Original TSR section artwork"
        media_class = "reference-overview-media--theme"

    lines.extend(
        [
            f'<section class="reference-overview reference-theme-{visual_group(record["category"])}">',
            f'<figure class="reference-overview-media {media_class}">',
            f'<img src="{html.escape(overview_asset, quote=True)}" alt="{html.escape(overview_alt, quote=True)}" loading="eager" decoding="async">',
            f"<figcaption>{media_caption}</figcaption>",
            "</figure>",
            '<div class="reference-overview-copy">',
            '<p class="reference-eyebrow">At a glance</p>',
            f"<p>{html.escape(summary)}</p>",
        ]
    )
    if sections:
        lines.append('<nav class="reference-quick-jumps" aria-label="Article sections">')
        for anchor, title in sections:
            lines.append(
                f'<a href="#{html.escape(anchor, quote=True)}">{html.escape(title)}</a>'
            )
        lines.append("</nav>")
    lines.extend(
        [
            '<div class="reference-reading-controls" role="group" aria-label="Article reading mode">',
            '<button type="button" class="reference-mode-button is-active" data-reference-mode="overview" aria-pressed="true">Overview</button>',
            '<button type="button" class="reference-mode-button" data-reference-mode="full" aria-pressed="false">Expand all</button>',
            "</div>",
            "</div>",
            "</section>",
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
                "!!! note \"Unavailable upstream media\"",
                "    Some source placements could not be mirrored because the referenced File record is missing, deleted, or could not be resolved to an auditable source file. The exact source article remains linked below.",
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

    if related:
        category_index = (
            PurePosixPath(REFERENCE_SLUG) / record["category"] / "index.md"
        ).as_posix()
        lines.extend(
            [
                '<section class="reference-related">',
                '<div class="reference-related-heading">',
                "<h2>Continue exploring</h2>",
                f'<a href="{rendered_page_relative_url(record["local_page"], category_index)}">Browse all {html.escape(CATEGORY_INFO[record["category"]][0])}</a>',
                "</div>",
                '<div class="reference-related-grid">',
            ]
        )
        for item in related:
            item_media = item.get("_primary_media")
            item_asset = (
                item_media["local_path"] if item_media else visual_asset(item["category"])
            )
            item_summary = article_summary(item, item.get("_clean_html", item.get("_html", "")), 120)
            lines.extend(
                [
                    f'<a class="reference-related-card" href="{rendered_page_relative_url(record["local_page"], item["local_page"])}">',
                    f'<img src="{html.escape(rendered_asset_relative_url(record["local_page"], item_asset), quote=True)}" alt="" loading="lazy" decoding="async">',
                    '<span class="reference-related-copy">',
                    f"<strong>{html.escape(item['display_title'])}</strong>",
                    f"<small>{html.escape(item_summary)}</small>",
                    "</span>",
                    "</a>",
                ]
            )
        lines.extend(["</div>", "</section>", ""])

    lines.extend(["---", "", "## Source and licensing", ""])
    revision_text = f"revision `{record['revision_id']}`" if record.get("revision_id") else "current recorded revision"
    modified_text = f", modified `{record['upstream_modified']}`" if record.get("upstream_modified") else ""
    lines.append(
        f"{SOURCE_BADGE} adapted from [{record['source_title']}]({record['source_url']}) "
        f"on the {SOURCE_WIKI_NAME} ({revision_text}{modified_text}). "
        f"Adapted text is available under [CC BY-SA 4.0]({TEXT_LICENSE_URL})."
    )
    lines.append("")
    page_media = record.get("_media", [])
    if page_media:
        lines.extend(
            [
                '<details class="reference-media-credits">',
                f"<summary>Media credits ({len(page_media)} source files)</summary>",
                "<ul>",
            ]
        )
        for item in page_media:
            uploader = f"; uploaded by {html.escape(item['uploaded_by'])}" if item.get("uploaded_by") else ""
            revision = f"; revision {item['file_revision_id']}" if item.get("file_revision_id") else ""
            lines.append(
                f'<li><a href="{html.escape(item["source_file_page"], quote=True)}">{html.escape(item["source_title"])}</a>'
                f" — {html.escape(item.get('license') or 'CC BY-SA 4.0')}{uploader}{revision}</li>"
            )
        lines.extend(["</ul>", "</details>", ""])
    return "\n".join(lines)


def load_overlays() -> dict[str, dict[str, Any]]:
    if SOURCE_KEY != "tensura":
        return {}
    path = DATA_ROOT / "tsr-wiki-overlays.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {normalize_title(title): value for title, value in data.get("overlays", {}).items()}


def load_reference_snapshot(source_key: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    data_stem = f"upstream_{source_key}"
    pages_path = DATA_ROOT / f"{data_stem}_pages.json"
    media_path = DATA_ROOT / f"{data_stem}_media.json"
    coverage_path = DATA_ROOT / f"{data_stem}_coverage.json"
    if not pages_path.exists():
        return [], [], {}

    records = json.loads(pages_path.read_text(encoding="utf-8")).get("pages", [])
    media = json.loads(media_path.read_text(encoding="utf-8")).get("media", []) if media_path.exists() else []
    coverage = json.loads(coverage_path.read_text(encoding="utf-8")) if coverage_path.exists() else {}
    media_lookup = {
        normalize_title(item["source_title"]): item
        for item in media
        if item.get("source_title")
    }
    attach_page_media(records, media_lookup)
    for record in records:
        local_page = DOCS / record["local_page"]
        record["_html"] = local_page.read_text(encoding="utf-8") if local_page.exists() else ""
    return records, media, coverage


def combined_reference_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if SOURCE_KEY != "tensura":
        return records
    companion_records, _, _ = load_reference_snapshot("mysticism")
    return records + companion_records


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
    race_title = normalize_title(CATEGORY_INFO["races"][0]).casefold()
    race_records = [
        record
        for record in records
        if record["category"] == "races"
        and normalize_title(record["display_title"]).casefold() != race_title
    ]
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
            record["local_page"], f"{REFERENCE_SLUG}/races"
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
    source_title_overviews = [
        record
        for record in category_records
        if normalize_title(record["source_title"].split("/")[-1]).casefold()
        == normalize_title(title).casefold()
    ]
    display_title_overviews = [
        record
        for record in category_records
        if normalize_title(record["display_title"]).casefold()
        == normalize_title(title).casefold()
    ]
    overview_records: list[dict[str, Any]] = []
    seen_overview_pages: set[str] = set()
    for record in source_title_overviews + display_title_overviews:
        if record["local_page"] in seen_overview_pages:
            continue
        seen_overview_pages.add(record["local_page"])
        overview_records.append(record)
    overview_local_pages = {
        record["local_page"] for record in overview_records
    }
    index_page = (PurePosixPath(REFERENCE_SLUG) / category / "index.md").as_posix()
    hero_asset = rendered_asset_relative_url(index_page, visual_asset(category))
    source_roots = {PurePosixPath(record["local_page"]).parts[0] for record in category_records}
    combined_directory = len(source_roots) > 1
    ordered = sorted(
        [record for record in category_records if record["local_page"] not in overview_local_pages],
        key=lambda item: item["display_title"].casefold(),
    )
    letters = sorted(
        {
            record["display_title"][:1].upper()
            if record["display_title"][:1].isalnum()
            else "#"
            for record in ordered
        },
        key=lambda value: (value == "#", value),
    )
    lines = [
        f'<section class="reference-directory" data-reference-directory="{html.escape(category, quote=True)}">',
        f'<header class="reference-directory-hero reference-theme-{visual_group(category)}">',
        f'<img src="{html.escape(hero_asset, quote=True)}" alt="" loading="eager" decoding="async">',
        '<div class="reference-directory-hero-copy">',
        '<p class="reference-eyebrow">Tensura reference collection</p>',
        f"<h1>{html.escape(title)}</h1>",
        f"<p>{html.escape(description)}</p>",
        '<div class="reference-directory-hero-actions">',
        f'<span class="reference-count"><strong>{len(ordered)}</strong> articles</span>',
    ]
    visible_overviews = (
        overview_records if combined_directory and not ordered else overview_records[:1]
    )
    if not combined_directory or not ordered:
        for position, overview_record in enumerate(visible_overviews):
            label = "Read collection overview" if position == 0 else "Read additional overview"
            lines.append(
                f'<a class="reference-directory-overview-link" href="{rendered_page_relative_url(index_page, overview_record["local_page"])}">{label} <span aria-hidden="true">→</span></a>'
            )
    lines.extend(
        [
        "</div>",
        "</div>",
        "</header>",
        '<div class="reference-directory-tools">',
        '<label class="reference-filter-label">',
        '<span>Filter this collection</span>',
        '<input type="search" class="reference-filter-input" placeholder="Search titles and summaries…" autocomplete="off">',
        "</label>",
        '<div class="reference-letter-filters" aria-label="Filter by first letter">',
        '<button type="button" class="is-active" data-letter="all" aria-pressed="true">All</button>',
        ]
    )
    for letter in letters:
        lines.append(
            f'<button type="button" data-letter="{html.escape(letter, quote=True)}" aria-pressed="false">{html.escape(letter)}</button>'
        )
    lines.extend(
        [
            "</div>",
            f'<p class="reference-filter-status" aria-live="polite">Showing {len(ordered)} of {len(ordered)} articles</p>',
            "</div>",
            '<div class="reference-card-grid">',
        ]
    )
    for record in ordered:
        summary = article_summary(record, record.get("_html", ""), 170)
        letter = record["display_title"][:1].upper()
        if not letter.isalnum():
            letter = "#"
        primary_media = record.get("_primary_media")
        card_asset = primary_media["local_path"] if primary_media else visual_asset(category)
        card_asset_url = rendered_asset_relative_url(index_page, card_asset)
        media_class = "reference-card-media--source" if primary_media else "reference-card-media--theme"
        source_label = "Source media" if primary_media else "TSR artwork"
        lines.extend(
            [
                f'<article class="reference-card" data-letter="{html.escape(letter, quote=True)}" data-search="{html.escape((record["display_title"] + " " + summary).casefold(), quote=True)}">',
                f'<a href="{rendered_page_relative_url(index_page, record["local_page"])}" aria-label="Open {html.escape(record["display_title"], quote=True)}">',
                f'<figure class="reference-card-media {media_class}">',
                f'<img src="{html.escape(card_asset_url, quote=True)}" alt="" loading="lazy" decoding="async">',
                f"<figcaption>{source_label}</figcaption>",
                "</figure>",
                '<div class="reference-card-copy">',
                f"<h2>{html.escape(record['display_title'])}</h2>",
                f"<p>{html.escape(summary)}</p>",
                '<span class="reference-card-action">Open reference <span aria-hidden="true">→</span></span>',
                "</div>",
                "</a>",
                "</article>",
            ]
        )
    lines.extend(
        [
            "</div>",
            '<p class="reference-no-results" hidden>No matching articles. Try a broader search.</p>',
            "</section>",
            "",
        ]
    )
    return "\n".join(lines)


def generate_reference_index(
    siteinfo: dict[str, Any], records: list[dict[str, Any]], redirects: list[dict[str, Any]], media: list[dict[str, Any]]
) -> str:
    category_totals = Counter(record["category"] for record in records)
    category_counts = Counter(
        record["category"]
        for record in records
        if normalize_title(record["display_title"]).casefold()
        != normalize_title(CATEGORY_INFO[record["category"]][0]).casefold()
    )
    imported_media = sum(record.get("import_status") == "imported" for record in media)

    companion_records: list[dict[str, Any]] = []
    companion_media: list[dict[str, Any]] = []
    companion_coverage: dict[str, Any] = {}
    if SOURCE_KEY == "tensura":
        companion_records, companion_media, companion_coverage = load_reference_snapshot("mysticism")

    combined_reference = SOURCE_KEY == "tensura" and bool(companion_records)
    all_records = records + companion_records
    all_category_totals = Counter(record["category"] for record in all_records)
    all_category_counts = Counter(
        record["category"]
        for record in all_records
        if normalize_title(record["display_title"]).casefold()
        != normalize_title(CATEGORY_INFO[record["category"]][0]).casefold()
    )
    total_articles = len(records) + len(companion_records)
    total_aliases = sum(item.get("status") == "processed" for item in redirects) + int(
        companion_coverage.get("redirects_processed", 0)
    )
    total_media = imported_media + sum(item.get("import_status") == "imported" for item in companion_media)

    reference_title = "Tensura Reference" if combined_reference else SOURCE_REFERENCE_TITLE
    if combined_reference:
        reference_intro = (
            "This visual library presents every imported Tensura article in one reference experience. "
            "Start with a path below, filter the collection, then open an article for its "
            "source imagery, at-a-glance summary, infobox, and expandable details."
        )
    elif SOURCE_KEY == "mysticism":
        reference_intro = (
            "This source view is part of the combined [Tensura Reference](../tensura-reference/index.md) and is adapted "
            f"from the {SOURCE_WIKI_NAME}. Start with a path below, filter a collection, then open an article for its "
            "source imagery, at-a-glance summary, infobox, and expandable details."
        )
    else:
        reference_intro = (
            f"This visual library is the {SOURCE_CONTEXT_LABEL} layer of the TSR wiki, adapted from the "
            f"{SOURCE_WIKI_NAME}. Start with a path below, filter a collection, then open an article for its source "
            "imagery, at-a-glance summary, infobox, and expandable details."
        )

    lines = [
        f"# {reference_title}",
        "",
        reference_intro,
        "",
        "!!! warning \"Version context\"",
        "    Upstream articles may describe historical Minecraft or mod versions. TSR targets **Minecraft 1.21.1**, **NeoForge 21.1.248**, and **Java 21**. An upstream article is not proof that a historical feature is active in TSR's frozen runtime.",
        "",
        '<div class="reference-metric-grid">',
        f'<div><strong>{total_articles}</strong><span>articles</span></div>',
        f'<div><strong>{total_aliases}</strong><span>local aliases</span></div>',
        f'<div><strong>{total_media}</strong><span>source images</span></div>',
        (
            '<div><strong>2</strong><span>audited sources</span></div>'
            if combined_reference
            else f'<div><strong>{len(category_totals)}</strong><span>collections</span></div>'
        ),
        "</div>",
        "",
        "## Choose a path",
        "",
        '<div class="reference-path-grid">',
    ]
    index_page = f"{REFERENCE_SLUG}/index.md"
    for group, path_title, path_description, categories in REFERENCE_PATHS:
        group_asset = rendered_asset_relative_url(index_page, VISUAL_ASSETS[group])
        lines.extend(
            [
                f'<article class="reference-path-card reference-theme-{group}">',
                f'<img src="{html.escape(group_asset, quote=True)}" alt="" loading="lazy" decoding="async">',
                '<div class="reference-path-copy">',
                f"<h2>{html.escape(path_title)}</h2>",
                f"<p>{html.escape(path_description)}</p>",
                '<div class="reference-path-links">',
            ]
        )
        for category in categories:
            if not all_category_totals.get(category):
                continue
            category_title = CATEGORY_INFO[category][0]
            target = (PurePosixPath(category) / "index.md").as_posix()
            category_count = all_category_counts.get(category, 0)
            count_label = str(category_count) if category_count else "Overview"
            lines.append(
                f'<a href="{rendered_page_relative_url(index_page, PurePosixPath(REFERENCE_SLUG) / target)}">'
                f"{html.escape(category_title)} <span>{count_label}</span></a>"
            )
        lines.extend(["</div>", "</div>", "</article>"])
    lines.extend(
        [
            "</div>",
            "",
            "## TSR layer",
            "",
            "Use the main TSR guides for installed-mod status, configured values, compatibility, quests, progression, world generation, storage, and server behavior. Generated upstream pages include a TSR section only when a verified project-specific overlay exists.",
            "",
            (
                "See the Tensura: Reincarnated [Upstream Attribution](../project/upstream-attribution.md) and "
                "[Ingestion Coverage](../project/ingestion-coverage.md), plus the Mysticism "
                "[Upstream Attribution](../project/mysticism-upstream-attribution.md) and "
                "[Ingestion Coverage](../project/mysticism-ingestion-coverage.md), for licensing and audit details."
                if combined_reference
                else f"See [Upstream Attribution](../project/{ATTRIBUTION_REPORT.name}) and "
                f"[Ingestion Coverage](../project/{COVERAGE_REPORT.name}) for licensing and audit details."
            ),
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
        DATA_ROOT / f"{DATA_STEM}_pages.json",
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
        DATA_ROOT / f"{DATA_STEM}_media.json",
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
        "media_failures": [
            {
                "source_title": record.get("source_title"),
                "source_file_page": record.get("source_file_page"),
                "reason": record.get("reason"),
            }
            for record in media_records
            if record.get("import_status") == "failed"
        ],
        "failures": failed_pages,
    }
    write_json(DATA_ROOT / f"{DATA_STEM}_coverage.json", coverage)
    return coverage


def render_coverage_report(coverage: dict[str, Any]) -> str:
    lines = [
        f"# {SOURCE_WIKI_NAME} Ingestion Coverage",
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
    media_failures = coverage.get("media_failures", [])
    if media_failures:
        lines.extend(["", "## Media exceptions", ""])
        for record in media_failures:
            source_title = record.get("source_title") or "Unknown File record"
            source_page = record.get("source_file_page")
            label = f"[{source_title}]({source_page})" if source_page else f"`{source_title}`"
            lines.append(f"- {label} — {record.get('reason') or 'Import failed'}")
    lines.extend(
        [
            "",
            "## Machine-readable reports",
            "",
            f"- `data/{DATA_STEM}_pages.json`",
            f"- `data/{DATA_STEM}_media.json`",
            f"- `data/{DATA_STEM}_coverage.json`",
            "",
        ]
    )
    return "\n".join(lines)


def render_attribution(siteinfo: dict[str, Any]) -> str:
    rights = siteinfo.get("rightsinfo", {})
    license_text = rights.get("text", "Creative Commons Attribution-ShareAlike 4.0 License")
    license_url = rights.get("url", TEXT_LICENSE_URL)
    return f"""# {SOURCE_WIKI_NAME} Attribution

The generated **{SOURCE_REFERENCE_TITLE}** is adapted from the
[{SOURCE_WIKI_NAME}]({WIKI_ROOT}/), synchronized on `{SYNCED_AT}`.
Each generated article links to its exact source page and records the upstream
revision ID and modified timestamp used by the synchronizer.

## Text license

The upstream site's MediaWiki rights metadata identifies its reusable text as
[{license_text}]({license_url}). Adapted upstream text in
`docs/{REFERENCE_SLUG}/` remains available under the same license. TSR-specific
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
`data/{DATA_STEM}_media.json`.

## Separation from TSR

Tensura: Sovereign Rebirth did not create the upstream mod or wiki. Upstream
facts retain their original version context. TSR runtime claims
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


def ensure_asset_root_ready() -> None:
    asset_resolved = ASSET_ROOT.resolve()
    docs_resolved = DOCS.resolve()
    if docs_resolved not in asset_resolved.parents:
        raise RuntimeError(f"Unsafe generated asset path: {asset_resolved}")
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)


def prune_stale_assets(media_records: list[dict[str, Any]]) -> None:
    expected = {
        (DOCS / Path(record["local_path"])).resolve()
        for record in media_records
        if record.get("import_status") == "imported" and record.get("local_path")
    }
    root = ASSET_ROOT.resolve()
    for path in ASSET_ROOT.rglob("*"):
        if path.is_file() and path.resolve() not in expected:
            if root not in path.resolve().parents:
                raise RuntimeError(f"Unsafe stale asset path: {path}")
            path.unlink()
    for directory in sorted(
        (path for path in ASSET_ROOT.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        if not any(directory.iterdir()):
            directory.rmdir()


def normalize_generated_text(value: str) -> str:
    """Remove source-line whitespace without changing rendered content."""
    return "\n".join(line.rstrip() for line in value.splitlines()).rstrip() + "\n"


def write_reference_indexes(
    siteinfo: dict[str, Any],
    page_records: list[dict[str, Any]],
    redirect_records: list[dict[str, Any]],
    media_records: list[dict[str, Any]],
) -> None:
    index_records = combined_reference_records(page_records)
    for category in CATEGORY_ORDER:
        index = REFERENCE_ROOT / Path(category) / "index.md"
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text(
            normalize_generated_text(generate_category_index(category, index_records)),
            encoding="utf-8",
        )
    evolution_path = REFERENCE_ROOT / "races" / "evolution-trees.md"
    evolution_path.write_text(
        normalize_generated_text(generate_evolution_index(index_records)), encoding="utf-8"
    )
    (REFERENCE_ROOT / "index.md").write_text(
        normalize_generated_text(
            generate_reference_index(siteinfo, page_records, redirect_records, media_records)
        ),
        encoding="utf-8",
    )


def audit_generated_links(root: Path) -> list[str]:
    errors: list[str] = []
    markdown_link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    html_link_re = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.I)
    for page in sorted(root.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        markdown_source = "\n".join(
            line
            for line in text.splitlines()
            if not (line.lstrip().startswith("<") and line.rstrip().endswith(">"))
        )
        for raw_target in markdown_link_re.findall(markdown_source):
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
                errors.append(f"{page.relative_to(ROOT)} -> missing rendered target {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        choices=("tensura", "mysticism"),
        default="tensura",
        help="Upstream wiki collection to synchronize",
    )
    parser.add_argument("--refresh", action="store_true", help="Ignore cached API responses and media")
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--pace", type=float, default=0.18, help="Minimum seconds between requests")
    parser.add_argument("--limit", type=int, help="Development-only canonical article limit")
    parser.add_argument(
        "--rebuild-indexes-only",
        action="store_true",
        help="Rebuild generated collection indexes from the checked-in snapshots without network access",
    )
    args = parser.parse_args()

    default_cache = configure_source(args.source)
    if args.rebuild_indexes_only:
        page_records, media_records, coverage = load_reference_snapshot(SOURCE_KEY)
        if not page_records:
            raise RuntimeError(f"No checked-in {SOURCE_KEY} reference snapshot is available")
        redirect_records = [
            {"status": "processed"}
            for _ in range(int(coverage.get("redirects_processed", 0)))
        ]
        write_reference_indexes(
            coverage.get("site_statistics", {}), page_records, redirect_records, media_records
        )
        generated_link_errors = audit_generated_links(REFERENCE_ROOT)
        if generated_link_errors:
            raise RuntimeError("\n".join(generated_link_errors[:40]))
        print(
            f"Rebuilt {SOURCE_KEY} reference indexes from {len(page_records)} checked-in articles",
            flush=True,
        )
        return 0

    client = ApiClient(args.cache_dir or default_cache, refresh=args.refresh, pace=max(args.pace, 0.05))
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
    ensure_asset_root_ready()
    media_records, media_lookup, media_category_counts = prepare_media(
        client, media_records, page_records, file_page_license
    )
    prune_stale_assets(media_records)
    attach_page_media(page_records, media_lookup)
    related_map = build_related_map(page_records)

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
        record["_clean_html"] = body_html
        counters["internal_links_converted"] += links
        counters["media_placements_imported"] += imported_placements
        counters["media_placements_omitted"] += skipped_placements
        aliases = aliases_by_target.get(record["source_title"], [])
        overlay = overlays.get(normalize_title(record["source_title"]))
        output = DOCS / Path(record["local_page"])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            normalize_generated_text(
                render_page(
                    record,
                    body_html,
                    aliases,
                    overlay,
                    skipped_placements,
                    related_map.get(record["page_id"], []),
                )
            ),
            encoding="utf-8",
        )

    write_reference_indexes(siteinfo, page_records, redirect_records, media_records)
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
    ATTRIBUTION_REPORT.parent.mkdir(parents=True, exist_ok=True)
    ATTRIBUTION_REPORT.write_text(
        normalize_generated_text(render_attribution(siteinfo)), encoding="utf-8"
    )
    COVERAGE_REPORT.write_text(
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
