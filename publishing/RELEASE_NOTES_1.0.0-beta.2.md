# Tensura: Sovereign Rebirth 1.0.0 Beta 2

Beta 2 reduces excessive natural mob density while preserving every active
progression species and encounter.

## Changes

- Reduced the shared natural monster cap from 70 to 48 and slowed natural
  monster spawn attempts from every tick to every two ticks.
- Reduced passive, ambient, aquatic, and Aether category caps.
- Shortened non-persistent mob despawn ranges so distant natural mobs release
  capacity sooner.
- Bounded zombie reinforcement, Nether portal, monster-spawner, and infested
  silverfish pressure through ServerCore mobcaps.
- Reduced natural Tensura creature frequency across the full active spawn
  table, with larger reductions for Direwolves, Armorsaurus, Orcs, and Slimes.
- Reduced Mysticism Okami natural spawn frequency from 1-in-8 to 1-in-24.
- Retained the client keybinding persistence fix and all Beta 1 quests,
  branding, client defaults, and server defaults.

## Updating

Back up the server before replacing files. Existing mobs are not removed by
this update; the new density becomes visible as old natural mobs despawn and
new spawn cycles use the updated settings.

## Known beta targets

Live multiplayer density, long-duration world generation, late-game boss
scaling, non-operator permissions, and claim protection still require extended
playtesting.
