# Project Owner Checklist

Complete these items before either public project is submitted.

## Identity and rights

- [ ] Confirm the final project title and slug are available on both platforms.
- [ ] Confirm the license for TSR-owned configuration, quest, code, and artwork.
- [ ] Confirm the right to publish the chosen avatar, banner, logo, menu
      background, and quest backgrounds.
- [ ] Confirm the franchise disclaimer in the storefront description is
      acceptable.

## Public links

- [ ] Open the player wiki in a signed-out browser and confirm every in-game
      quest link reaches it.
- [ ] Provide a public support or issue-report URL. A private repository issue
      tracker is not usable by ordinary players.
- [ ] Remove or replace any storefront link that is not publicly accessible.

## Platform projects

- [ ] Publish TSR Client Stability on CurseForge and Modrinth.
- [ ] Publish TSR Silent Gear Metalworks Compat on CurseForge and Modrinth.
- [ ] Record the approved project/file or project/version IDs in Packwiz.
- [ ] Regenerate the client files without unlisted copies of those modules.

## CurseForge

- [ ] Reconfirm the exact Ponder artifact qualifies under the approved
      non-CurseForge content rules.
- [ ] Import the regenerated ZIP in a clean CurseForge profile.
- [ ] Upload the client as a Beta.
- [ ] Upload the matching server ZIP as the client's Additional File.
- [ ] Add real release-candidate screenshots and the final avatar.

## Modrinth

- [ ] Resolve every non-Modrinth artifact in
      `data/client-runtime-reconciliation.json` with an exact hosted version or
      documented redistribution permission.
- [ ] Attach author permission evidence to the moderation area where required.
- [ ] Run the strict publishable export and retain its clean output.
- [ ] Import the regenerated `.mrpack` in a clean Modrinth App profile.
- [ ] Submit the project and version as Beta only after the permission gate
      passes.

## Final release check

- [ ] Run the graphical client to the main menu from both downloaded platform
      files.
- [ ] Start the matching extracted server, create a clean world, save, stop,
      and restart it.
- [ ] Verify all 140 quests load and the wiki buttons open the public site.
- [ ] Change and remove at least one modded keybind, restart twice, and confirm
      both changes persist.
- [ ] Confirm Skill Trainer, TR Addon, Unique Monsters, C2ME, and all diagnostic
      JARs are absent.
- [ ] Publish SHA-256 hashes with the beta announcement.
