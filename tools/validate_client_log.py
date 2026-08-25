#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


READY_MARKERS = (
    "Sound engine started",
    "Created: 1024x512x0 minecraft:textures/atlas/blocks.png-atlas",
)
FATAL_MARKERS = (
    "/FATAL]",
    "broken mod state",
    "Failed to wait for future Common setup",
    "Caught exception during event",
    "Failed to load service",
    "ModLoadingException",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reject Minecraft client logs that reached rendering with a broken mod state."
    )
    parser.add_argument("logs", type=Path, nargs="+")
    args = parser.parse_args()

    combined = ""
    for path in args.logs:
        if not path.is_file():
            raise SystemExit(f"Missing client log: {path}")
        combined += path.read_text(encoding="utf-8", errors="replace")

    ready = [marker for marker in READY_MARKERS if marker in combined]
    fatal = [marker for marker in FATAL_MARKERS if marker in combined]
    if not ready:
        raise SystemExit("Client log validation failed: no menu-ready marker found")
    if fatal:
        raise SystemExit(
            "Client log validation failed: fatal mod-loading marker(s): " + ", ".join(fatal)
        )

    print(f"Client log OK: {len(args.logs)} file(s), ready marker present, no fatal mod-loading marker")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
