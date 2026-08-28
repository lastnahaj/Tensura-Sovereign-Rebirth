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
```

Use `--refresh` to ignore the selected source's response cache. The synchronizer is deliberately
paced and single-threaded. Generated pages are replaced as one owned output
tree; handcrafted TSR pages elsewhere in `docs/` are never rewritten.

The synchronizer verifies the upstream File-page CC BY-SA 4.0 declaration,
then checks every file's metadata and page text for exceptions. Media is
downloaded with its source page and revision recorded unless the file states
fair-use, non-free, or restrictive terms.
