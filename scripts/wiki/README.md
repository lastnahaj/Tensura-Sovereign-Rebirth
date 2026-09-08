# Tensura Wiki Synchronizer

The synchronizer builds the generated base-mod and TR Mysticism references from
their official MediaWiki APIs. It keeps raw responses in ignored `.build/`
caches and records source revisions, local destinations, redirects, media
licensing, and coverage in `data/`.

```powershell
python -m pip install -r requirements.txt -r requirements-wiki.txt
python scripts/wiki/sync_tensura_wiki.py --source tensura
python scripts/wiki/sync_tensura_wiki.py --source mysticism
python scripts/wiki/check_reference.py
python -m mkdocs build --strict
python scripts/wiki/check_built_site.py
python scripts/wiki/check_progression.py
python scripts/wiki/check_skill_catalogue.py
```

Use `--refresh` to ignore the selected source's response cache. The synchronizer is deliberately
paced and single-threaded. Only pages owned by the previous source manifest are
replaced; maintained TSR and Ascension pages are preserved.

`data/ascension_reference.json` registers maintained Ascension entries in the
combined category indexes. Rebuild those indexes without fetching the upstream
wikis with `--rebuild-indexes-only`. Both synchronization and index rebuilding
refresh the race and skill progression graph in `docs/assets/data/progression.json`.

Run `python scripts/wiki/sync_progression.py --check` to verify that the graph
matches the current articles. Connections use documented progression fields and
explicit Ascension requirements; alphabetical neighbors are not progression paths.

Race families group connected forms from the documented graph and preserve each
stage's original reference link. `python scripts/wiki/sync_race_families.py --check`
verifies the generated family maps and directory. Rebuilding indexes also refreshes
these maps. Maintained skills live in their ordinary type directories; legacy
collection links redirect to the corresponding individual skill pages.

`python scripts/wiki/sync_skill_catalogue.py` rebuilds only the ability directories,
version-scoped skill metadata, acquisition panels, and Mysticism SVG emblems. It
does not rebuild race families. Both full synchronization and index rebuilding
apply the same catalogue gate automatically.

The catalogue uses the pinned Skill Books registry export for formal skill types;
that export is not evidence of a gameplay obtainment route. Historical entries
and collection guides are excluded from current skill cards, progression, and
site search. Maintained implementation-backed additions are registered in
`data/skill_reference.json`. Acquisition summaries distinguish upstream methods,
pinned implementation checks, and incomplete or unknown routes.

Run `python scripts/wiki/check_skill_catalogue.py --source-only` before a build,
then run it without the flag after building to check rendered acquisition links
and search exclusions as well. The check also guards against spell/effect name
collisions, incorrect formal types, duplicate cards, stale generated output, and
editorial placeholders.

Nightmares skill imports use a separate reference-build audit. Run
`audit_nightmares_skills.py --jar <reference-artifact> --javap <java-disassembler>`
to verify the recorded artifact hash, read registry identifiers, and match the
1.21.1 source articles. Then run `import_nightmares_skills.py` to regenerate those
articles from the ignored audit cache, followed by `sync_progression.py`.
`data/nightmares_skill_reference.json` records revisions, registered names,
unresolved sources, and the reference release. An artifact match is not a server
installation check. Nightmares entries stay marked as reference-build-only in
directories, obtainment panels, and progression cards until that match is known.
Explicitly non-gameplay variants are excluded. Original interface emblems avoid
assuming the article text license also covers game artwork.

Normal catalogue and progression checks work from the committed manifests and
articles; they do not download or require the reference artifact in CI.

The synchronizer verifies the upstream File-page CC BY-SA 4.0 declaration,
then checks every file's metadata and page text for exceptions. Media is
downloaded with its source page and revision recorded unless the file states
fair-use, non-free, or restrictive terms.
