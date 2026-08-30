#!/usr/bin/env python3
"""Reconcile an exact client runtime inventory into the Packwiz source."""

from __future__ import annotations

import argparse
import json
import tomllib
from datetime import date
from pathlib import Path


EXCLUSIONS = {
    "c2me-neoforge-mc1.21.1-0.4.0-alpha.0.120.jar": (
        "DEFERRED-BLOCKED",
        "Clean dedicated-server shutdown hangs with the tested alpha artifact.",
    ),
    "tensura-trainer-neoforge-2.0.5.jar": (
        "USER-OPTIONAL-NOT-SHIPPED",
        "Player-managed optional mod; excluded from all distributed profiles.",
    ),
    "tensura_fancymenu-neoforge-1.21.1-0.1.1-beta.jar.disabled": (
        "DISABLED-NOT-SHIPPED",
        "The runtime reference has this compatibility addon disabled.",
    ),
}

CLIENT_ONLY = {
    "appleskin-neoforge-mc1.21-3.0.9.jar",
    "athena-neoforge-1.21.1-4.0.6.jar",
    "BetterF3-11.0.3-NeoForge-1.21.1.jar",
    "biomemusic-1.21.1-4.1.jar",
    "cloth-config-15.0.140-neoforge.jar",
    "configured-neoforge-1.21.1-2.6.3.jar",
    "Controlling-neoforge-1.21.1-19.0.4.jar",
    "DistantHorizons-3.2.0-b-1.21.1-fabric-neoforge.jar",
    "drippyloadingscreen_neoforge_3.1.5_MC_1.21.1.jar",
    "dynamic-fps-3.11.3+minecraft-1.21.0-neoforge.jar",
    "enchdesc-neoforge-1.21.1-21.1.11.jar",
    "entity_model_features-3.2.4-1.21-neoforge.jar",
    "entity_texture_features_1.21-neoforge-7.1.jar",
    "entityculling-neoforge-1.10.5-mc1.21.1.jar",
    "EuphoriaPatcher-1.9.3-r5.8.1-neoforge.jar",
    "ExtremeSoundMuffler-3.56_NeoForge-1.21.jar",
    "fancymenu_neoforge_3.9.11_MC_1.21.1.jar",
    "forgematica-0.4.2+mc1.21.1.jar",
    "foxablazeaqzl_wiki-1.0.2.4.jar",
    "ftbxaerocompat-neoforge-1.1.4.jar",
    "ImmediatelyFast-NeoForge-1.6.12+1.21.1.jar",
    "inventoryessentials-neoforge-1.21.1-21.1.17.jar",
    "iris-neoforge-1.8.14-beta.1+mc1.21.1.jar",
    "itempeek-mc1.21.1-1.2.0.jar",
    "jei-1.21.1-neoforge-19.32.0.359.jar",
    "JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar",
    "konkrete_neoforge_1.9.9_MC_1.21.jar",
    "mafglib-0.4.3+mc1.21.1.jar",
    "melody_neoforge_1.0.10_MC_1.21.jar",
    "moreculling-neoforge-1.21.1-1.0.9.jar",
    "MouseTweaks-neoforge-mc1.21-2.26.1.jar",
    "NeoForgematicaPrinter-0.1.0+mc1.21.1.jar",
    "PickUpNotifier-v21.1.1-1.21.1-NeoForge.jar",
    "Searchables-neoforge-1.21.1-1.0.2.jar",
    "sodium-neoforge-0.8.13+mc1.21.1.jar",
    "sound-physics-remastered-neoforge-1.21.1-1.5.1.jar",
    "tensura_trepu-1.0.0.2.jar",
    "xaerominimap-neoforge-1.21.1-26.4.2.jar",
    "xaeroworldmap-neoforge-1.21.1-1.45.0.jar",
}

PACK_OWNED = {
    "tsr-sgear-metalworks-compat-1.0.0.jar",
}

TAB_FILENAME = "TAB v5.5.0 1.20.5 - 1.21.1.jar"
TAB_CURSEFORGE_PROJECT = 1232967
TAB_CURSEFORGE_FILE = 7659430


def load_metadata(directory: Path) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for path in sorted(directory.glob("*.pw.toml")):
        entry = tomllib.loads(path.read_text(encoding="utf-8"))
        entry["_path"] = path
        result.append(entry)
    return result


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_metadata(entry: dict[str, object]) -> str:
    lines = [
        f'name = {toml_string(str(entry["name"]))}',
        f'filename = {toml_string(str(entry["filename"]))}',
        f'side = {toml_string(str(entry.get("side", "both")))}',
        "",
        "[download]",
    ]
    download = entry["download"]
    assert isinstance(download, dict)
    for key in ("url", "hash-format", "hash", "mode"):
        if key in download:
            lines.append(f"{key} = {toml_string(str(download[key]))}")

    update = entry.get("update", {})
    assert isinstance(update, dict)
    if update:
        lines.extend(("", "[update]"))
        modrinth = update.get("modrinth")
        if isinstance(modrinth, dict):
            lines.extend(("[update.modrinth]", f'mod-id = {toml_string(str(modrinth["mod-id"]))}', f'version = {toml_string(str(modrinth["version"]))}'))
        curseforge = update.get("curseforge")
        if isinstance(curseforge, dict):
            lines.extend(("[update.curseforge]", f'file-id = {int(curseforge["file-id"])}', f'project-id = {int(curseforge["project-id"])}'))
    return "\n".join(lines) + "\n"


def with_modrinth(entry: dict[str, object], modrinth: dict[str, object]) -> dict[str, object]:
    update = dict(entry.get("update", {}))
    update["modrinth"] = {
        "mod-id": modrinth["project_id"],
        "version": modrinth["version_id"],
    }
    return {
        "name": entry["name"],
        "filename": entry["filename"],
        "side": entry.get("side", "both"),
        "download": {
            "url": modrinth["url"],
            "hash-format": "sha512",
            "hash": modrinth["sha512"],
        },
        "update": update,
    }


def provider_summary(entry: dict[str, object] | None, modrinth: dict[str, object] | None) -> tuple[dict[str, object] | None, dict[str, object] | None, str]:
    curseforge = None
    if entry:
        provider = entry.get("update", {}).get("curseforge")
        if provider:
            curseforge = {
                "project_id": provider["project-id"],
                "file_id": provider["file-id"],
            }
    mr = None
    if modrinth:
        mr = {
            "project_id": modrinth["project_id"],
            "version_id": modrinth["version_id"],
        }
    if curseforge and mr:
        status = "BOTH-PINNED"
    elif curseforge:
        status = "CURSEFORGE-ONLY"
    elif mr:
        status = "MODRINTH-ONLY"
    else:
        status = "PACK-OWNED-OR-UNRESOLVED"
    return curseforge, mr, status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", type=Path, required=True)
    parser.add_argument("--detected-pack", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--modrinth-files", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    mods_dir = (args.pack / "mods").resolve()
    detected_mods_dir = (args.detected_pack / "mods").resolve()
    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    modrinth_files = json.loads(args.modrinth_files.read_text(encoding="utf-8"))
    modrinth_by_filename = {entry["filename"]: entry for entry in modrinth_files}

    current_entries = load_metadata(mods_dir)
    detected_entries = load_metadata(detected_mods_dir)
    current_by_filename = {str(entry["filename"]): entry for entry in current_entries}
    current_by_cf_project = {
        int(entry["update"]["curseforge"]["project-id"]): entry
        for entry in current_entries
        if entry.get("update", {}).get("curseforge")
    }
    detected_by_filename = {str(entry["filename"]): entry for entry in detected_entries}

    report_entries: list[dict[str, object]] = []
    imported = 0
    updated = 0
    for item in inventory["mods"]:
        filename = str(item["filename"])
        exclusion = EXCLUSIONS.get(filename)
        detected = detected_by_filename.get(filename)
        current = current_by_filename.get(filename)
        modrinth = modrinth_by_filename.get(filename)

        if exclusion:
            status, reason = exclusion
            provider_entry = detected or current
            curseforge, mr, platform = provider_summary(provider_entry, modrinth)
            report_entries.append(
                {
                    "name": item["name"],
                    "filename": filename,
                    "pack_status": status,
                    "reason": reason,
                    "side": None,
                    "platform_status": platform,
                    "curseforge": curseforge,
                    "modrinth": mr,
                }
            )
            continue

        if filename in PACK_OWNED:
            report_entries.append(
                {
                    "name": item["name"],
                    "filename": filename,
                    "pack_status": "ACTIVE-PACK-OWNED",
                    "side": "both",
                    "platform_status": "PACK-OWNED",
                    "curseforge": None,
                    "modrinth": None,
                }
            )
            continue

        selected = current or detected
        if not selected:
            raise SystemExit(f"No Packwiz identity found for active runtime file: {filename}")

        target_path = Path(selected["_path"])
        if not current:
            project = selected.get("update", {}).get("curseforge", {}).get("project-id")
            replaced = current_by_cf_project.get(int(project)) if project else None
            if replaced:
                target_path = Path(replaced["_path"])
                updated += 1
            else:
                target_path = mods_dir / Path(selected["_path"]).name
                imported += 1

        output_entry = {
            key: value for key, value in selected.items() if not key.startswith("_")
        }
        output_entry["side"] = "client" if filename in CLIENT_ONLY else "both"
        if modrinth:
            output_entry = with_modrinth(output_entry, modrinth)
        target_path.write_text(render_metadata(output_entry), encoding="utf-8")
        current_by_filename[filename] = output_entry

        curseforge, mr, platform = provider_summary(output_entry, modrinth)
        report_entries.append(
            {
                "name": item["name"],
                "filename": filename,
                "pack_status": "ACTIVE",
                "side": output_entry["side"],
                "platform_status": platform,
                "curseforge": curseforge,
                "modrinth": mr,
            }
        )

    tab_modrinth = modrinth_by_filename[TAB_FILENAME]
    tab_entry = with_modrinth(
        {
            "name": "TAB",
            "filename": TAB_FILENAME,
            "side": "server",
            "download": {},
            "update": {
                "curseforge": {
                    "project-id": TAB_CURSEFORGE_PROJECT,
                    "file-id": TAB_CURSEFORGE_FILE,
                }
            },
        },
        tab_modrinth,
    )
    (mods_dir / "tab.pw.toml").write_text(render_metadata(tab_entry), encoding="utf-8")

    active = [entry for entry in report_entries if entry["pack_status"].startswith("ACTIVE")]
    exceptions = [entry for entry in active if entry["platform_status"] != "BOTH-PINNED"]
    report = {
        "schema_version": 1,
        "generated_on": date.today().isoformat(),
        "runtime_reference_count": inventory["mod_count"],
        "active_reference_count": len(active),
        "excluded_reference_count": len(report_entries) - len(active),
        "imported_metadata_count": imported,
        "updated_metadata_count": updated,
        "active_cross_platform_exception_count": len(exceptions),
        "server_requirements": [
            {
                "name": "FTB Essentials",
                "filename": "ftb-essentials-neoforge-2101.1.10.jar",
                "side": "both",
            },
            {
                "name": "TAB",
                "filename": TAB_FILENAME,
                "side": "server",
                "curseforge": {
                    "project_id": TAB_CURSEFORGE_PROJECT,
                    "file_id": TAB_CURSEFORGE_FILE,
                },
                "modrinth": {
                    "project_id": tab_modrinth["project_id"],
                    "version_id": tab_modrinth["version_id"],
                },
            },
        ],
        "required_pack_additions": [
            {
                "name": "TSR Client Stability",
                "filename": "tsr-client-stability-1.0.0.jar",
                "side": "client",
                "sha256": "e044e888ca8169681c02453daa5969771a519e8c169cd1ed990edea71f2d251e",
            }
        ],
        "entries": report_entries,
    }
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Runtime inventory synchronized: {len(active)} active reference files, "
        f"{len(report_entries) - len(active)} excluded, {len(exceptions)} platform exceptions, "
        f"{imported} metadata imports, {updated} metadata updates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
