.PHONY: docs validate

docs:
	mkdocs serve

validate:
	python scripts/validate_manifest.py
	python scripts/validate_docs.py
	mkdocs build --strict
