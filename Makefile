.PHONY: docs validate

docs:
	mkdocs serve

validate:
	python scripts/validate_manifest.py
	python scripts/validate_docs.py
	python scripts/wiki/check_reference.py
	python tools/validate_pack.py
	python tools/validate_runtime_foundation.py
	mkdocs build --strict
	python scripts/wiki/check_built_site.py
