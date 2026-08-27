#!/usr/bin/env python3
import re
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors = []
link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
html_target_re = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']", re.IGNORECASE)

markdown_files = sorted(ROOT.glob("*.md")) + sorted(DOCS.rglob("*.md"))


def validate_candidate(md: Path, target: str, candidate: Path) -> None:
    candidate = candidate.resolve()
    if ROOT not in candidate.parents and candidate != ROOT:
        errors.append(f"{md.relative_to(ROOT)} -> path escapes repository: {target}")
    elif not candidate.exists():
        errors.append(f"{md.relative_to(ROOT)} -> missing {target}")


for md in markdown_files:
    text = md.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        target = target.strip().split()[0].strip('<>')
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        candidate = (ROOT / target.lstrip("/")) if target.startswith("/") else (md.parent / target)
        validate_candidate(md, target, candidate)
    for target in html_target_re.findall(text):
        target = target.strip().split()[0].strip('<>')
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = unquote(target.split("#", 1)[0])
        is_generated = DOCS in md.parents and md.relative_to(DOCS).as_posix().startswith(
            "tensura-reference/"
        )
        is_rendered_route = (
            DOCS in md.parents and target.endswith("/") and not target.startswith("/")
        )
        if not target.startswith("/") and (is_generated or is_rendered_route):
            rendered_dir = md.parent if md.name == "index.md" else md.with_suffix("")
            candidate = (rendered_dir / target).resolve()
            if target.endswith("/"):
                candidate = (
                    candidate / "index.md"
                    if candidate.is_dir()
                    else Path(str(candidate).rstrip("\\/") + ".md")
                )
        else:
            candidate = (ROOT / target.lstrip("/")) if target.startswith("/") else (md.parent / target)
        validate_candidate(md, target, candidate)

try:
    mkdocs = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
except (OSError, yaml.YAMLError) as exc:
    errors.append(f"mkdocs.yml -> invalid YAML: {exc}")
    mkdocs = {}

nav_targets = set()


def collect_nav(node):
    if isinstance(node, str):
        nav_targets.add(node)
    elif isinstance(node, list):
        for item in node:
            collect_nav(item)
    elif isinstance(node, dict):
        for item in node.values():
            collect_nav(item)


collect_nav(mkdocs.get("nav", []))
for target in sorted(nav_targets):
    if not (DOCS / target).is_file():
        errors.append(f"mkdocs.yml -> missing nav target {target}")

document_paths = {str(path.relative_to(DOCS)).replace("\\", "/") for path in DOCS.rglob("*.md")}
handcrafted_paths = {
    path for path in document_paths if not path.startswith("tensura-reference/")
}
missing_from_nav = handcrafted_paths - nav_targets
if missing_from_nav:
    errors.append("mkdocs.yml -> documents missing from nav: " + ", ".join(sorted(missing_from_nav)))

asset_targets = list(mkdocs.get("extra_css", []))
asset_targets.extend(mkdocs.get("extra_javascript", []))
theme = mkdocs.get("theme", {})
asset_targets.extend(theme.get(key) for key in ("logo", "favicon") if theme.get(key))
for target in asset_targets:
    if not (DOCS / target).is_file():
        errors.append(f"mkdocs.yml -> missing asset {target}")

yaml_files = sorted((ROOT / ".github").rglob("*.yml")) + sorted((ROOT / ".github").rglob("*.yaml"))
for yaml_path in yaml_files:
    try:
        parsed = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"{yaml_path.relative_to(ROOT)} -> invalid YAML: {exc}")
        continue
    if not isinstance(parsed, dict):
        errors.append(f"{yaml_path.relative_to(ROOT)} -> expected a YAML mapping")

issue_forms = sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml"))
for form in issue_forms:
    if form.name == "config.yml":
        continue
    parsed = yaml.safe_load(form.read_text(encoding="utf-8"))
    for field in ("name", "description", "body"):
        if not parsed.get(field):
            errors.append(f"{form.relative_to(ROOT)} -> missing {field}")
    if not isinstance(parsed.get("body"), list):
        errors.append(f"{form.relative_to(ROOT)} -> body must be a list")

forbidden_patterns = {
    "Windows home path": re.compile(r"[A-Za-z]:[\\/]Users[\\/]", re.IGNORECASE),
    "Unix home path": re.compile(r"/(?:home|Users)/[^/\s]+/"),
    "temporary data path": re.compile(r"/mnt/" + r"data/|AppData[\\/]Local[\\/]Temp", re.IGNORECASE),
    "private archive path": re.compile("PRIVATE_REFERENCE_" + r"DO_NOT_COMMIT|Tempest-Protocol-" + r"ftbquests\.rar", re.IGNORECASE),
    "AI-related metadata": re.compile(
        r"\b(?:Code" + r"x|Chat" + r"GPT|Open" + r"AI)\b|generated by " + r"AI|co-authored" + r"-by:",
        re.IGNORECASE,
    ),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "private IPv4 address": re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"),
}
text_suffixes = {".md", ".yml", ".yaml", ".json", ".py", ".css", ".txt"}
special_text_names = {"Makefile", ".gitignore", ".gitattributes", "CODEOWNERS"}
for path in ROOT.rglob("*"):
    if not path.is_file() or any(
        part in {".build", ".git", ".venv", "site"} for part in path.parts
    ):
        continue
    if path.suffix not in text_suffixes and path.name not in special_text_names:
        continue
    text = path.read_text(encoding="utf-8")
    for label, pattern in forbidden_patterns.items():
        if pattern.search(text):
            errors.append(f"{path.relative_to(ROOT)} -> contains {label}")

if errors:
    raise SystemExit("Repository documentation validation failed:\n- " + "\n- ".join(sorted(set(errors))))

print(
    f"Repository documentation OK across {len(markdown_files)} Markdown files, "
    f"{len(nav_targets)} navigation entries, {len(document_paths) - len(handcrafted_paths)} "
    f"generated reference pages, and {len(yaml_files)} YAML files"
)
