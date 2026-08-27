# Configuration Specification

Every runtime subsystem must ship with reviewed defaults rather than relying on whatever a mod generates on first launch. Configuration changes are accepted only after a clean instance reconstructs the packaged tree semantically and passes the subsystem's client and dedicated-server gates.

## Ownership

- `pack/config` contains reviewed client, common, and globally loaded server settings.
- `pack/defaultconfigs` contains world-scoped server defaults when a mod uses NeoForge's per-world configuration path.
- `pack/kubejs` contains pack-owned recipes, removals, tags, and small data integrations.
- Machine-local NeoForge files, caches, migration state, logs, and discovered runtime state are not distributable configuration.

## Stability policy

Defaults must bound expensive scans, multiblock sizes, entity populations, pathfinding, chunk loading, world operations, and background network work. Parallel or asynchronous behavior stays disabled where an owning mod's thread-safety has not been demonstrated in the complete runtime. Terrain griefing and experimental faction/warfare systems remain off until their recovery and permission behavior is validated.

## Progression policy

Free starter kits, natural high-tier reward injection, unrestricted cross-dimensional travel, and overlapping equipment paths remain disabled when they bypass authored progression. KubeJS removals must name exact recipes and preserve the minimum infrastructure required by retained features.

## Validation contract

The repository validator locks critical values and direct dependency hashes. A clean runtime must reproduce every packaged file without semantic changes; only explicitly listed machine-local files may appear. Client validation must reject fatal or broken mod states even if rendering reaches the main menu. Dedicated-server validation must include new-world creation, flushed save, clean shutdown, and restart.

The current reviewed values and phase-specific evidence are recorded in `configuration-baseline.md` and `phase-reports.md`.
