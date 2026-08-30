# TSR Runtime Module Listings

The public modpack should reference these two original TSR modules as normal
platform projects instead of embedding them as unlisted override JARs.

## TSR Client Stability

**Project type:** Mod

**Summary:** Preserves player keybind changes when early NeoForge client saves
rewrite an incomplete options state.

**Environment:** Client only

**Minecraft:** 1.21.1

**Loader:** NeoForge

**License:** All Rights Reserved

**Version:** 1.0.0

**Version type:** Release

### Description

TSR Client Stability is a narrowly scoped client compatibility module for
Tensura: Sovereign Rebirth.

During startup, some large NeoForge client stacks can save `options.txt` before
every modded key mapping has been reconstructed. That early save can restore
removed controls to their defaults or overwrite player changes. This module
captures existing keybind values before options load, protects them during the
early-save window, reloads the complete options state after mod loading, and
then releases the guard for normal play.

The module does not set gameplay controls on every launch. It protects the
player's saved choices. TSR's first-install defaults are supplied separately by
the modpack.

### 1.0.0 changelog

- Added startup protection for existing modded keybind values.
- Added a post-construction options reload after all client mappings register.
- Verified changed and unbound controls across two complete client restarts in
  the TSR Version 1 Beta profile.

## TSR Silent Gear Metalworks Compat

**Project type:** Mod

**Summary:** Corrects and verifies Productive Metalworks fluid units when
Silent Gear Metalworks is used without Silent Gems.

**Environment:** Client and server

**Minecraft:** 1.21.1

**Loader:** NeoForge

**License:** All Rights Reserved

**Version:** 1.0.0

**Version type:** Release

### Required dependencies

- Productive Metalworks 1.21.1-1.15.1
- Silent Gear 4.2.1.1
- Silent Gear Metalworks 1.21.1-1.5.0

### Description

TSR Silent Gear Metalworks Compat is a focused data compatibility module for
Tensura: Sovereign Rebirth.

It installs a top-priority built-in datapack that corrects the Productive
Metalworks fluid-unit map for a runtime containing Silent Gear Metalworks but
not Silent Gems. The corrected map keeps Productive Metalworks defaults and
the seven installed Silent Gear molten fluids while excluding 21 unavailable
Silent Gems fluids.

After every data-map update, the module verifies that all required mappings are
present and that unavailable Silent Gems entries did not load. It fails early
with a clear error if the effective mapping becomes inconsistent after a
dependency update.

This module is intentionally specific to the tested dependency versions. It
does not modify the upstream JARs.

### 1.0.0 changelog

- Added the corrected Metalworks fluid-unit data map.
- Added runtime verification for required installed fluid mappings.
- Added validation that unavailable Silent Gems mappings remain excluded.
