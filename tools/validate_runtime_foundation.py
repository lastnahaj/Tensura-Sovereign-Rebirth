#!/usr/bin/env python3
from __future__ import annotations

import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODS = ROOT / "pack" / "mods"

EXPECTED = {
    "architectury-api.pw.toml": {
        "filename": "architectury-13.0.11-neoforge.jar",
        "hash": "008656a0702801174b8ec245ed7aad1921d6e9f1",
        "source": ("curseforge", 419699, 8492726),
    },
    "geckolib.pw.toml": {
        "filename": "geckolib-neoforge-1.21.1-4.9.2.jar",
        "hash": "14c64013cadee7d28f3685f94350f9a4d2ec6d86",
        "source": ("curseforge", 388172, 8350073),
    },
    "manascore.pw.toml": {
        "filename": "manascore-neoforge-4.0.0.2.jar",
        "hash": "f11a0062d7829e26a8705183762a5e0f2d022dd3",
        "source": ("curseforge", 619025, 8022425),
    },
    "smartbrainlib.pw.toml": {
        "filename": "SmartBrainLib-neoforge-1.21.1-1.16.11.jar",
        "hash": "0310135a01eeceefbc7f1ab017498a65f3ad6836",
        "source": ("curseforge", 661293, 7055149),
    },
    "tensura-reincarnated.pw.toml": {
        "filename": "tensura-neoforge-2.0.1.2.jar",
        "hash": "f6f0c8ce46b77a1996c5986d029411878142112f",
        "source": ("curseforge", 643695, 8665599),
    },
    "terrablender.pw.toml": {
        "filename": "TerraBlender-neoforge-1.21.1-4.1.0.8.jar",
        "hash": (
            "9d4b2a1be5139c0fb2fad92ed21805b17d9e83b6ea48e637e018bb14063c1823"
            "a206390755dbfe8d025c20fd62ac11cdd84db53ddb956dabaeda01bff57bac50"
        ),
        "source": ("modrinth", "kkmrDlKT", "6e8GCrLb"),
    },
}


errors: list[str] = []
for filename, expected in EXPECTED.items():
    path = MODS / filename
    if not path.is_file():
        errors.append(f"Missing runtime foundation metadata: {filename}")
        continue

    try:
        metadata = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"Invalid TOML in {filename}: {exc}")
        continue

    if metadata.get("filename") != expected["filename"]:
        errors.append(f"Unexpected artifact filename in {filename}")
    if metadata.get("side") != "both":
        errors.append(f"Runtime foundation mod is not installed on both sides: {filename}")
    if metadata.get("download", {}).get("hash") != expected["hash"]:
        errors.append(f"Artifact hash changed in {filename}")

    provider, project, version = expected["source"]
    update = metadata.get("update", {}).get(provider, {})
    if provider == "curseforge":
        if update.get("project-id") != project or update.get("file-id") != version:
            errors.append(f"CurseForge identity changed in {filename}")
    elif update.get("mod-id") != project or update.get("version") != version:
        errors.append(f"Modrinth identity changed in {filename}")

if errors:
    raise SystemExit("Runtime foundation validation failed:\n- " + "\n- ".join(errors))

print(f"Runtime foundation OK: {len(EXPECTED)} pinned artifacts")
