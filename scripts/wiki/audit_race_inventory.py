"""Match Base and Mysticism race articles to the pinned 1.21.1 registries.

This read-only review writes an ignored audit report, not wiki eligibility rules.
Registry presence does not verify evolution gates, stats, or server overrides.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tomllib
import zipfile
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[2]
BUILDS = {
    "tensura": {"class": "io.github.manasmods.tensura.registry.race.TensuraRaces", "sha1": "f6f0c8ce46b77a1996c5986d029411878142112f", "version": "2.0.1.2", "source_url": "https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599"},
    "mysticism": {"class": "io.github.Memoires.mysticism.registry.race.MysticismRaces", "sha1": "cca1bd878b46c21ddbbf507bd4489fbb217899c7", "version": "2.1.2", "source_url": "https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529"},
}


def normalized(value):
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def disassemble(jar, javap, class_name, artifact_hash, verbose=False):
    key = hashlib.sha256((class_name + str(verbose)).encode()).hexdigest()[:24]
    cache = ROOT / ".build/race-bytecode" / artifact_hash / (key + ".txt")
    if cache.exists():
        return cache.read_text(encoding="utf-8")
    command = [javap, "-classpath", str(jar), "-c", "-p"] + (["-v"] if verbose else []) + [class_name]
    output = subprocess.run(command, check=True, capture_output=True, text=True).stdout
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(output, encoding="utf-8", newline="\n")
    return output


def inspect(source, jar, javap):
    build = BUILDS[source]
    if hashlib.sha1(jar.read_bytes()).hexdigest() != build["sha1"]:
        raise ValueError(f"Pinned artifact hash mismatch for {source}")
    output = disassemble(jar, javap, build["class"], build["sha1"], verbose=True)
    fields = set(re.findall(r"RegistrySupplier<[^>]+> (\w+);", output))
    initializer = output.split("  static {};", 1)[1].split("BootstrapMethods:", 1)[0]
    entries = re.findall(r"// String ([a-z0-9_./-]+)\s*\n(?:(?!// String).)*?// InvokeDynamic #(\d+):get:(?:(?!// String).)*?// Field (\w+):Ldev/architectury/registry/registries/RegistrySupplier;", initializer, re.S)
    if fields != {field for _, _, field in entries}:
        raise ValueError(f"Incomplete race registry extraction: {source}")
    constructors = dict(re.findall(r'^  (\d+): #[^\n]+\n(?:(?!^  \d+:).)*?REF_newInvokeSpecial ([\w/$]+)\."<init>"', output.split("BootstrapMethods:", 1)[1], re.S | re.M))
    with zipfile.ZipFile(jar) as archive:
        language = json.loads(archive.read(f"assets/{source}/lang/en_us.json"))
    registry = {}
    for name, bootstrap, field in entries:
        identifier = source + ":" + name
        title = language.get(source + ".race." + name) or language.get("race." + source + "." + name) or name.replace("_", " ").title()
        if bootstrap not in constructors:
            raise ValueError(f"Unresolved race constructor: {identifier}")
        registry[identifier] = {"id": identifier, "title": re.sub(r"§[0-9a-fk-or]", "", title, flags=re.I), "field": field, "implementation": constructors[bootstrap].replace("/", ".")}
    manifest = json.loads((ROOT / f"data/upstream_{source}_pages.json").read_text(encoding="utf-8"))
    pages = []
    for record in manifest["pages"]:
        if record["category"] != "races":
            continue
        names = {normalized(record["display_title"]), normalized(record["source_title"].split("/")[-1])}
        matches = [key for key in registry if normalized(key.split(":")[1]) in names]
        if not matches:
            matches = [key for key, value in registry.items() if normalized(value["title"]) in names]
        pages.append({"local_page": record["local_page"], "title": record["display_title"], "source_url": record["source_url"], "revision_id": record["revision_id"], "registry_id": matches[0] if len(matches) == 1 else None, "candidates": matches})
    matched = {page["registry_id"] for page in pages if page["registry_id"]}
    return {"build": build, "registry": registry, "pages": pages, "registry_without_article": sorted(registry.keys() - matched)}


def inspect_methods(source, jar, javap, inventory):
    configs = {}
    for path in (ROOT / f"pack/config/{source}/race").rglob("*.toml"):
        for section, values in tomllib.loads(path.read_text(encoding="utf-8")).items():
            if isinstance(values, dict):
                configs.setdefault(section, []).append({"path": path.relative_to(ROOT).as_posix(), "section": section, "values": values})

    def inspect_one(entry):
        output = disassemble(jar, javap, entry["implementation"], inventory["build"]["sha1"])
        superclass = re.search(r" extends ([\w.$]+)", output)
        methods = {}
        for declaration, body in re.findall(r"^  ((?:public|protected|private) [^\n]+);\n    Code:\n(.*?)(?=^  (?:public|protected|private|static)|^\})", output, re.S | re.M):
            name = re.search(r"([\w$]+)\(", declaration)
            if name and ("Evolution" in name[1] or name[1] in {"getIntrinsicSkills", "getDefaultConfig", "isDivine", "isSpiritual", "getDifficulty"}):
                methods[name[1]] = body.strip()
        config_classes = set(re.findall(r"(?:protected|public|private) static final [\w.]+\$(\w+) CONFIG;", output))
        if not config_classes:
            config_classes = set(re.findall(r"// Field [\w/]+\.\w+:L[\w/]+\$(\w+);", methods.get("getDefaultConfig", "")))
        associated = [config for section in config_classes for config in configs.get(section, [])]
        return entry["id"], {"superclass": superclass[1] if superclass else None, "config": associated, "methods": methods}

    with ThreadPoolExecutor(max_workers=4) as executor:
        return dict(executor.map(inspect_one, inventory["registry"].values()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tensura-jar", type=Path, required=True)
    parser.add_argument("--mysticism-jar", type=Path, required=True)
    parser.add_argument("--javap", required=True)
    parser.add_argument("--methods", action="store_true", help="Also review evolution methods and matching tracked configuration")
    args = parser.parse_args()
    results = {source: inspect(source, getattr(args, source + "_jar"), args.javap) for source in BUILDS}
    if args.methods:
        for source, inventory in results.items():
            inventory["implementation_review"] = inspect_methods(source, getattr(args, source + "_jar"), args.javap, inventory)
            print(f"Reviewed {len(inventory['implementation_review'])} {source} race implementations", flush=True)
    destination = ROOT / ".build/race-inventory-audit.json"
    destination.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    for source, result in results.items():
        print(f"{source}: {len(result['registry'])} registered races, {len(result['pages'])} articles, {sum(bool(page['registry_id']) for page in result['pages'])} exact matches")
        print("Unresolved articles: " + ", ".join(page["title"] for page in result["pages"] if not page["registry_id"]))


if __name__ == "__main__":
    main()
