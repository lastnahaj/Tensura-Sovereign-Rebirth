#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import zipfile
from pathlib import Path


FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def normalize(archive_path: Path) -> None:
    archive_path = archive_path.resolve()
    temporary_path = archive_path.with_name(archive_path.name + ".normalized")
    with zipfile.ZipFile(archive_path, "r") as source:
        with zipfile.ZipFile(
            temporary_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as target:
            for name in sorted(source.namelist()):
                data = source.read(name)
                info = zipfile.ZipInfo(name, FIXED_TIMESTAMP)
                info.create_system = 3
                info.external_attr = (0o755 if name.endswith("/") else 0o644) << 16
                info.compress_type = zipfile.ZIP_STORED if name.endswith("/") else zipfile.ZIP_DEFLATED
                target.writestr(info, data, compresslevel=9)
    try:
        os.replace(temporary_path, archive_path)
    except PermissionError:
        # Some Windows scanners briefly prevent replace-in-place on large archives.
        backup_path = archive_path.with_name(archive_path.name + ".replace-backup")
        if backup_path.exists():
            raise
        os.replace(archive_path, backup_path)
        try:
            os.replace(temporary_path, archive_path)
        except Exception:
            os.replace(backup_path, archive_path)
            raise
        backup_path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archives", type=Path, nargs="+")
    args = parser.parse_args()
    for archive in args.archives:
        normalize(archive)
        print(f"Normalized archive: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
