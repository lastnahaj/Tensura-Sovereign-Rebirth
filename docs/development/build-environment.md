# Build Environment

Version 1 (Beta) uses a reproducible Packwiz source. Third-party JARs are
downloaded only into ignored test instances from their canonical sources.

## Locked baseline

| Component | Version | Verification |
|---|---:|---|
| Minecraft | 1.21.1 | v0.1 design freeze |
| Java | 21 | Runtime requirement |
| NeoForge | 21.1.248 | Official NeoForge Maven catalog |
| Packwiz | `dfd8b68a4796` | Packwiz source revision used to initialize the pack |
| Pack format | `packwiz:1.1.0` | Generated pack metadata |

Tensura: Reincarnated 2.0.1.2 declares NeoForge `[21.1,)`, so the selected
runtime satisfies its loader range. Every frozen mod is still checked against
this runtime as its exact file is added.

## Local directories

- `.build/client-test/` — disposable client validation instance
- `.build/server-test/` — disposable dedicated-server instance
- `.build/packwiz-cache/` — Packwiz download cache
- `.build/tools/` — local build tools

All four paths are ignored by Git.
