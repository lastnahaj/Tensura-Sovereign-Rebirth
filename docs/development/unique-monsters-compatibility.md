# Unique Monsters Compatibility Blocker

## Disposition

Tensura: Unique Monsters 1.0.2 is `DEFERRED-BLOCKED` and is removed from the
active Phase 2 runtime. It is not permanently rejected and has no replacement.
The official CurseForge artifact remains preserved as a re-entry reference:

| Field | Value |
|---|---|
| CurseForge project | `1489273` |
| CurseForge file | `7844220` |
| Version | `1.0.2` |
| SHA-1 | `0cbb72baaf6a7c7008043b99b299326417a53bce` |
| SHA-256 | `38def0f47748e11a5d153a9dde57892c53f396a78dff97c9aaebf3ba631ece83` |

## Reproducible failure

During parallel NeoForge construction, Unique Monsters can invoke
`ExtraSkills.init()` before ManasCore has created the `manascore_skill:skills`
registry. The result is a startup-order exception even though a warm or
repeated start may appear to succeed. Those starts are not considered a fix.

The previously tested TSR lifecycle bridge was diagnostic only. Its JAR is not
part of the release manifest and is not distributed.

### Preserved diagnostic findings

The development bridge redirected the premature `ExtraSkills.init()` call,
captured ManasCore's real skill registrar after `SkillRegistry` initialization,
and returned that registrar only for the Unique Monsters provider. A diagnostic
run with that bridge reached a clean world and restart, but this does not prove
the published artifact is safe: the upstream constructor can still race before
the bridge is available. The experiment therefore remains evidence for the
blocker analysis, not a release fix. No patched upstream JAR or fork is
published.

## Re-entry criteria

An official Unique Monsters artifact may be reconsidered only after it corrects
the registration lifecycle/dependency ordering and passes all of the following
without a diagnostic patch:

1. isolated construction testing;
2. repeated clean/cold complete Phase 2 starts;
3. new-world creation;
4. clean shutdown and restart; and
5. verification that no registry-order exceptions occur.

Until then, the active pack contains neither Unique Monsters 1.0.2 nor the
diagnostic compatibility JAR.
