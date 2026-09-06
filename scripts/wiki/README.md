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

The synchronizer verifies the upstream File-page CC BY-SA 4.0 declaration,
then checks every file's metadata and page text for exceptions. Media is
downloaded with its source page and revision recorded unless the file states
fair-use, non-free, or restrictive terms.
