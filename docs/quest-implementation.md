# Quest Implementation

The actual FTB Quest files should be generated/reviewed against the **assembled TSR instance**, not from guessed registry names.

## Implementation workflow

1. Freeze the installed mod/version set.
2. Enumerate real item/block/entity/skill/race registries.
3. Inspect Tensura Compat: FTB custom task and reward serializers.
4. Inspect the exact FTB Quests SNBT format used by the installed version.
5. Verify events/state for MineColonies, Guild, Gear Evolution, SlimeThrone, Ascension, and Great Sage.
6. Build quests using only verified task types and identifiers.
7. Where FTB cannot observe a desired event, document the gap.
8. Add a minimal KubeJS or server-side bridge only when a real event/API exists and the solution is reliable.
9. Validate every quest with a clean non-OP test character.
