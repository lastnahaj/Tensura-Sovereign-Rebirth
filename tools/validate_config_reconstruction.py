#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import tomllib
from pathlib import Path


ALLOWED_RUNTIME_FILES = {
    Path("craftedcore/cache/patreons.txt"),
    Path("fml.toml"),
    Path("neoforge-client.toml"),
    Path("neoforge-common.toml"),
    Path("neoforge-server.toml"),
    Path("stextras/internal/tensura_config_patcher_state.toml"),
}


def parse_json5(text: str) -> object:
    without_comments = re.sub(r"(?m)^\s*//.*(?:\r?\n|$)", "", text)
    without_trailing_commas = re.sub(r",\s*([}\]])", r"\1", without_comments)
    return json.loads(without_trailing_commas)


def semantic_value(path: Path) -> object:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".toml":
        return tomllib.loads(text)
    if path.suffix == ".json":
        return json.loads(text)
    if path.suffix == ".json5":
        return parse_json5(text)
    if path.suffix == ".txt":
        return text.replace("\r\n", "\n")
    return path.read_bytes()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("runtime", type=Path)
    args = parser.parse_args()

    source = args.source.resolve()
    runtime = args.runtime.resolve()
    if not source.is_dir() or not runtime.is_dir():
        raise SystemExit("Both source and runtime config directories must exist")

    source_files = {
        path.relative_to(source): path for path in source.rglob("*") if path.is_file()
    }
    runtime_files = {
        path.relative_to(runtime): path for path in runtime.rglob("*") if path.is_file()
    }
    errors: list[str] = []
    for relative, source_path in source_files.items():
        runtime_path = runtime_files.get(relative)
        if runtime_path is None:
            errors.append(f"missing after reconstruction: {relative}")
            continue
        try:
            if semantic_value(source_path) != semantic_value(runtime_path):
                errors.append(f"semantic setting changed: {relative}")
        except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"could not compare {relative}: {exc}")

    extra = set(runtime_files) - set(source_files) - ALLOWED_RUNTIME_FILES
    errors.extend(f"unexpected generated config: {relative}" for relative in sorted(extra))
    if errors:
        raise SystemExit("Config reconstruction failed:\n- " + "\n- ".join(errors))

    print(
        f"Config reconstruction OK: {len(source_files)}/{len(source_files)} packaged files; "
        f"{len(set(runtime_files) - set(source_files))} approved runtime files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
