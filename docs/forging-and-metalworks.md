# Forging & Metalworks

TSR's advanced crafting layer is built around:

- Tensura Metalworks
- Silent Gear
- Productive Metalworks
- Silent Gear Metalworks
- Almost Unified
- KubeJS

The goal is to make Tensura materials part of a real progression path while avoiding duplicated ores/ingots/recipes.

## Stability defaults

Productive Metalworks foundries are capped at 256 blocks of volume, 96 blocks of circumference, and 12 blocks of height. Inventory rendering inside the multiblock is disabled to reduce client rendering load around large foundries.

Silent Gear starter blueprints and the starter material book are not granted automatically. The authored quest path introduces blueprints, materials, and forging in the intended order.

TSR Silent Gear Metalworks Compat supplies the effective Productive Metalworks fluid-unit map when Silent Gems is absent. It preserves the seven molten Silent Gear materials installed by the pack, excludes only unavailable Silent Gems fluids, and verifies the active mappings every time data maps reload. No upstream mod JAR is modified.

## Almost Unified

Almost Unified is used to keep duplicate metal/material recipes sane across compatible mods.

## KubeJS

KubeJS is the pack-level integration tool for:
- recipe removal,
- hiding disabled content,
- progression gating,
- small compatibility scripts,
- removing redundant Tom's Storage content.

Exact scripts are created against the assembled registry set.

The current integration contains eleven guarded data-recipe overrides for optional mods that are not installed. This keeps the active recipes valid without creating phantom item or fluid dependencies.
