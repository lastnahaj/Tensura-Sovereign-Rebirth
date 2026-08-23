# Contributing

Thanks for helping improve Tensura: Sovereign Rebirth.

## Before opening a pull request

1. Open or reference an issue for compatibility or behavioral changes.
2. Do not add a mod that duplicates an already-authoritative progression system without explaining why.
3. Never invent registry IDs, permission nodes, config keys, or custom FTB task types. Verify them from the assembled pack or source.
4. Keep player-facing documentation synchronized with any configuration or progression change.
5. Run the repository validation scripts and a strict MkDocs build.

## Validation

```bash
python scripts/validate_manifest.py
python scripts/validate_docs.py
mkdocs build --strict
```

## Quest work

Quest changes must be based on the exact assembled mod versions. If an intended objective cannot be detected reliably, document the gap instead of faking it with unrelated item turn-ins.
