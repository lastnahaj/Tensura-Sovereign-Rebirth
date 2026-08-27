# Unique Monsters Compatibility

Tensura: Unique Monsters 1.0.2 remains a required Version 1 (Beta) component. TSR uses the official CurseForge project 1489273, file 7844220 without modifying it.

| Artifact | Verification |
|---|---|
| `tensurauniquemonsters-neoforge-1.0.2.jar` | SHA-1 `bb7e4098c776fd4d8eccaafd5d84c0e0520c57db`; SHA-256 `db73f98391ae96d9a267d2ee63c128e497b887ac00c74da9618cd6e0a271eea3` |
| `tsr-unique-monsters-compat-1.0.0.jar` | 8,151 bytes; SHA-256 `e5b9799bb648d1933c7e50b980ecbfc4a8bc24e91008f46380133d49a85a5a65` |

## Root cause and correction

Unique Monsters calls `ExtraSkills.init()` from `TRUniqueMobsRegistry.injectInit()` during parallel mod construction. That call can reach Architectury before ManasCore has made the `manascore_skill:skills` registrar reliably available, producing a construction-order failure.

The TSR compatibility mod applies three narrow, required Mixins:

1. Redirect the single premature `ExtraSkills.init()` call in `TRUniqueMobsRegistry.injectInit()`.
2. Capture ManasCore's real skill registrar and registry key at the tail of `SkillRegistry` class initialization, then invoke the original `ExtraSkills.init()` method exactly once.
3. Return the captured registrar only for the `tr_unique_monsters` Architectury provider and the exact captured skill-registry key.

The compatibility mod does not duplicate skill definitions. Common setup fails closed if either lifecycle hook changes or if the real registry does not contain `tr_unique_monsters:appraisal_eye`.

## Validation

| Test | Result |
|---|---|
| Isolated foundation + Unique Monsters + compatibility mod, clean world | PASS |
| Complete Phase 2A runtime, clean cold starts | PASS, 20/20 |
| Complete Phase 2A runtime, new-world creation and Labyrinth generation | PASS |
| Flushed save and clean shutdown | PASS, every cold run |
| Warm restart of generated world | PASS |
| Restart of existing Phase 2 world | PASS |
| Appraisal Eye present in the real ManasCore skill registry | PASS, every cold run |
| Registry-order, duplicate-registration, Mixin, and lifecycle exceptions | 0 in the final 20-run log set |

Earlier lifecycle-only hooks were rejected because registry construction and Architectury's shared custom-registry lookup could still race. A NewRegistryEvent hook was also rejected because the builder was not guaranteed to be initialized at that point. The final exact-provider bridge removes that remaining lookup race without sleeps, retries, or changes to either upstream JAR.

Any official Unique Monsters update must be tested first without the compatibility mod. The compatibility layer remains required until upstream registration ordering is corrected and the updated artifact passes the complete cold-start, world, shutdown, and restart matrix.
