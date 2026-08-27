"""Validate local links and assets in the rendered MkDocs site."""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]


class TargetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name.lower() in {"href", "src"} and value:
                self.targets.append(value)


def configured_base_path() -> str:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    match = re.search(r"^site_url:\s*['\"]?([^'\"\s]+)", config, re.MULTILINE)
    if not match:
        return "/"
    path = urlsplit(match.group(1)).path
    return "/" + path.strip("/") + "/" if path.strip("/") else "/"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", nargs="?", type=Path, default=ROOT / "site")
    args = parser.parse_args()

    site = args.site_dir.resolve()
    if not site.is_dir():
        raise SystemExit(f"Rendered site directory does not exist: {site}")
    base_path = configured_base_path()
    html_files = sorted(site.rglob("*.html"))
    errors: list[str] = []
    checked = 0

    for page in html_files:
        target_parser = TargetParser()
        target_parser.feed(page.read_text(encoding="utf-8"))
        for raw_target in target_parser.targets:
            target = html.unescape(raw_target).strip()
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith(("#", "//")):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if path.lower().endswith(".md"):
                errors.append(f"{page.relative_to(site)} -> rendered source link {path}")
                continue
            if path.startswith(base_path):
                candidate = site / path[len(base_path) :]
            elif path.startswith("/"):
                candidate = site / path.lstrip("/")
            else:
                candidate = page.parent / path
            candidate = candidate.resolve()
            if site not in candidate.parents and candidate != site:
                errors.append(f"{page.relative_to(site)} -> path escapes site: {path}")
                continue
            checked += 1
            if candidate.is_dir():
                candidate = candidate / "index.html"
            if not candidate.exists():
                errors.append(f"{page.relative_to(site)} -> missing rendered target {path}")

    if errors:
        raise SystemExit(
            "Rendered site validation failed:\n- " + "\n- ".join(sorted(set(errors)))
        )
    print(f"Rendered site OK: {len(html_files)} HTML pages and {checked} local targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
