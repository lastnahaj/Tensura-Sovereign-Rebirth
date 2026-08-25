# Storage & Logistics

TSR deliberately uses one storage family for actual storage and Tom's only as an interface layer.

## Personal storage

**Sophisticated Backpacks**
+ **Tensura Backpack Expansion**
+ **Gear Evolution integration**

Backpacks participate in Tensura-style progression rather than being a disconnected inventory upgrade.

## Base storage

**Sophisticated Storage** owns physical base/warehouse storage:
- chests,
- barrels,
- upgrades,
- storage controllers.

## Network access

**Tom's Simple Storage is stripped down.**

Player-facing Tom's functionality is intended to contain only:
- storage terminal,
- crafting terminal,
- wireless terminal(s),
- wireless linking/access items,
- the minimum backend connector/link infrastructure technically required by those terminals.

Everything else from Tom's is removed from recipes and hidden from normal progression where practical.

The beta baseline removes 18 non-terminal recipes and retains the seven recipes required for terminals, wireless access, connectors, and links. Connector reach is 12 blocks with a 256-position scan ceiling. Basic wireless reach is 12 blocks, advanced reach is 64 blocks, and inventory links are limited to 128 blocks. Unlimited beacon access and cross-dimensional wireless access are disabled.

Tom's multithreaded scanning is disabled for the initial server baseline. This favors predictable inventory access and easier profiling while Sophisticated Storage owns the physical inventory graph.

## Progression intent

**Physical storage** → **organized warehouse** → **terminal access** → **crafting terminal** → **wireless access**

Cross-dimensional or effectively unlimited wireless access remains unavailable unless a later progression gate is implemented and passes multiplayer contention and chunk-loading tests.
