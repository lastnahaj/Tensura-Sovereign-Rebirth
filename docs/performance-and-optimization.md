# Performance & Optimization

TSR uses a conservative optimization stack because MineColonies citizen AI, Tensura mobs/subordinates, bosses, dimensions, and worldgen are all sensitive to aggressive server tuning.

## Baseline

- ModernFix
- FerriteCore
- ServerCore
- ImmediatelyFast
- Entity Culling
- Dynamic FPS
- Clumps
- Chunky
- spark

## Test-only rendering option

Embeddium remains a controlled client test until Tensura effects, entities, MineColonies previews, boss rendering, and UI are validated.

## ServerCore policy

Begin conservatively. Do **not** immediately enable aggressive entity activation, AI throttling, or simulation changes.

## Profiling order

1. Establish baseline.
2. Pregenerate the final world with Chunky after worldgen is frozen.
3. Profile with spark.
4. Identify real tick/memory/render bottlenecks.
5. Tune one subsystem at a time.
6. Re-test Tensura combat, MineColonies AI, bosses, and subordinates.
