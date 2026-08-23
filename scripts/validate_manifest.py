#!/usr/bin/env python3
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "data" / "mod-manifest.json"
data = json.loads(path.read_text(encoding="utf-8"))

required_project = ["name", "short_name", "minecraft", "loader", "freeze"]
missing = [k for k in required_project if not data.get("project", {}).get(k)]
if missing:
    raise SystemExit(f"Missing project fields: {', '.join(missing)}")

try:
    date.fromisoformat(data["project"]["freeze_date"])
except (KeyError, TypeError, ValueError):
    raise SystemExit("Project freeze_date must use ISO YYYY-MM-DD format") from None

seen = {}
errors = []
categories = data.get("categories", {})
if not isinstance(categories, dict) or not categories:
    raise SystemExit("Manifest categories must be a non-empty object")

status_counts = {}
category_counts = {}
for category, entries in categories.items():
    if not isinstance(entries, list):
        errors.append(f"Category {category!r} must contain a list of entries")
        continue
    category_counts[category] = len(entries)
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(f"Invalid non-object entry in {category}")
            continue
        name = entry.get("name", "").strip()
        if not name:
            errors.append(f"Unnamed mod entry in {category}")
            continue
        key = name.casefold()
        if key in seen:
            errors.append(f"Duplicate mod entry: {name!r} in {category} and {seen[key]}")
        else:
            seen[key] = category
        if category != "Rejected":
            if not entry.get("version"):
                errors.append(f"Missing version for {name}")
            if not entry.get("status"):
                errors.append(f"Missing status for {name}")
            else:
                status = entry["status"]
                status_counts[status] = status_counts.get(status, 0) + 1
        else:
            if not entry.get("reason"):
                errors.append(f"Missing rejection reason for {name}")

declared = data.get("counts", {})
rejected = category_counts.get("Rejected", 0)
non_rejected = len(seen) - rejected
test_candidates = sum(
    count for status, count in status_counts.items() if status.startswith("TEST")
)
optional = status_counts.get("OPTIONAL", 0)
calculated = {
    "baseline_frozen_entries": non_rejected - test_candidates - optional,
    "test_candidates": test_candidates,
    "optional_entries": optional,
    "rejected_entries_tracked": rejected,
    "total_non_rejected_entries": non_rejected,
}
for key, value in calculated.items():
    if declared.get(key) != value:
        errors.append(
            f"Count {key!r} is {declared.get(key)!r}; calculated value is {value}"
        )

if errors:
    raise SystemExit("Manifest validation failed:\n- " + "\n- ".join(errors))

print(
    f"Manifest OK: {len(seen)} unique entries across {len(categories)} categories; "
    "declared counts match"
)
