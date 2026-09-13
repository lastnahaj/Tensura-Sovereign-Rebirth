"""Extract registered gamerules and defaults from the reviewed 1.21.1 mod jars."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "tensura": {
        "jar": ".build/tensura-neoforge-2.0.1.2.jar",
        "class": "io.github.manasmods.tensura.world.TensuraGameRules",
    },
    "mysticism": {
        "jar": ".build/mysticism-neoforge-2.1.2.jar",
        "class": "io.github.Memoires.mysticism.world.MysticismGameRules",
    },
    "ascension": {
        "jar": ".build/ascension-2.1.2.jar",
        "class": "com.simplygray.tensuraaddon.AddonGameRules",
    },
    "nightmares": {
        "jar": ".build/trnightmare-1.0.3.2.8-neoforge-1.21.1.jar",
        "class": "com.github.hvnbael.trnightmare.world.TRNightmareGamerules",
    },
}


def javap_path(override: str | None = None) -> Path:
    if override:
        return Path(override)
    discovered = shutil.which("javap")
    if discovered:
        return Path(discovered)
    java_home = os.environ.get("JAVA_HOME")
    if java_home:
        candidate = Path(java_home) / "bin" / ("javap.exe" if os.name == "nt" else "javap")
        if candidate.exists():
            return candidate
    raise SystemExit("javap was not found; add a JDK bin directory to PATH or pass --javap")


def disassemble(jar: Path, class_name: str, javap: Path) -> str:
    result = subprocess.run(
        [str(javap), "-classpath", str(jar), "-c", "-p", class_name],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    # On this Windows host javap can report an AccessDeniedException after it has
    # emitted a complete disassembly. Treat stdout as authoritative when present.
    if "Compiled from" not in result.stdout:
        raise SystemExit(result.stderr.strip() or f"Unable to inspect {jar}")
    return result.stdout


def pushed_value(line: str) -> int | None:
    match = re.search(r"\biconst_m1\b", line)
    if match:
        return -1
    match = re.search(r"\biconst_([0-5])\b", line)
    if match:
        return int(match.group(1))
    match = re.search(r"\b(?:bipush|sipush)\s+(-?\d+)\b", line)
    if match:
        return int(match.group(1))
    match = re.search(r"\bldc(?:_w)?\s+#\d+\s+//\s+(?:int|long)\s+(-?\d+)\b", line)
    if match:
        return int(match.group(1))
    return None


def extract(text: str) -> list[dict]:
    rules: list[dict] = []
    static_defaults: dict[str, bool] = {}
    static_match = re.search(r"\n  static \{\};\n    Code:\n(?P<body>.*?)(?:\n\}|\Z)", text, re.DOTALL)
    if static_match:
        pending: int | None = None
        for candidate in static_match.group("body").splitlines():
            value = pushed_value(candidate)
            if value is not None:
                pending = value
            field = re.search(r"putstatic\s+#\d+\s+// Field ([A-Za-z0-9_]+):Z", candidate)
            if field and pending is not None:
                static_defaults[field.group(1)] = bool(pending)
                pending = None
    block: list[str] = []
    for line in text.splitlines():
        if re.search(r"// String [A-Za-z]", line):
            block = [line]
            continue
        if not block:
            continue
        block.append(line)
        if "GameRules.register:" not in line:
            continue
        joined = "\n".join(block)
        name_match = re.search(r"// String ([^\s]+)", block[0])
        category_match = re.search(
            r"// Field (?:(?:net/minecraft/world/level/GameRules\$Category\.)?)([A-Z][A-Z0-9_]*):Lnet/minecraft/world/level/GameRules\$Category;",
            joined,
        )
        type_match = re.search(r"GameRules\$(BooleanValue|IntegerValue)\.create", joined)
        values = [value for value in (pushed_value(candidate) for candidate in block) if value is not None]
        if type_match and type_match.group(1) == "BooleanValue" and not values:
            default_field = re.search(r"// Field ([A-Za-z0-9_]+):Z", joined)
            if default_field and default_field.group(1) in static_defaults:
                values = [int(static_defaults[default_field.group(1)])]
        if not (name_match and category_match and type_match and values):
            raise ValueError(f"Could not parse gamerule registration:\n{joined}")
        kind = "boolean" if type_match.group(1) == "BooleanValue" else "integer"
        default: bool | int = bool(values[-1]) if kind == "boolean" else values[-1]
        rules.append({
            "name": name_match.group(1),
            "category": category_match.group(1).lower(),
            "type": kind,
            "default": default,
        })
        block = []
    return rules


def audit(javap_override: str | None = None) -> dict[str, list[dict]]:
    output: dict[str, list[dict]] = {}
    javap = javap_path(javap_override)
    for source, spec in SOURCES.items():
        jar = ROOT / spec["jar"]
        if not jar.exists():
            raise SystemExit(f"Missing audited artifact: {jar}")
        output[source] = extract(disassemble(jar, spec["class"], javap))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    parser.add_argument("--javap")
    args = parser.parse_args()
    print(json.dumps(audit(args.javap), indent=None if args.compact else 2, sort_keys=True))


if __name__ == "__main__":
    main()
