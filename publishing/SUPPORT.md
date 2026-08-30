# Installation and Support Copy

## Client installation

### CurseForge

Download the CurseForge release through the CurseForge App. If testing a direct
beta file, use **Create Custom Profile → Import** and select the TSR ZIP. Do not
extract the ZIP into an existing instance.

### Modrinth

Download the Modrinth release through the Modrinth App. For a direct private
beta file, use **Create instance → From file** and select the `.mrpack`.

Use 64-bit Java 21 and allocate 8 GB of memory. Do not allocate all available
system memory to Minecraft.

## Dedicated server

Use only the server file that matches the client version. Follow
`SERVER_FILE.md`, accept the EULA only after reading it, and keep an offline
backup before updates.

## Updating

1. Back up worlds and any launcher instance being replaced.
2. Install the new client version as a fresh profile.
3. Copy only personal files that the release notes say are safe to migrate.
4. Do not copy an old `mods` directory over a new release.
5. Stop and back up dedicated servers before applying the matching server
   update.

## Known beta limitations

- Progression and reward balance is still being tuned.
- Long-duration world generation and large multiplayer populations need wider
  beta coverage.
- Non-OP permission and claim-protection behavior remains under audit.
- TR Addon, Unique Monsters, and the tested C2ME alpha are deferred because of
  reproduced runtime failures.
- Tensura Skill Trainer is not part of the supported distribution.

## Bug reports

Include all of the following:

- TSR version and platform used to install it;
- client, dedicated server, or both;
- Java version and allocated memory;
- exact steps that reproduce the problem;
- whether it also happens in a new world;
- `latest.log` and the relevant crash report;
- a mod list if anything was added, removed, or updated manually.

Remove access tokens, IP addresses, usernames, and other private information
before attaching logs. Issues from modified instances should be reproduced in
an unmodified TSR profile before they are treated as pack defects.

## Common questions

**Can I add my own mods?**

Yes, but the resulting instance is unsupported until the issue is reproduced
with the unmodified pack. Never add a client-only mod to a dedicated server.

**Is Tensura Skill Trainer included?**

No. It is intentionally player-managed and is not distributed in any TSR
client or server file.

**Can I use Fabric or Forge?**

No. This release requires Minecraft 1.21.1 and NeoForge 21.1.248.

**Why did a mod disappear from the planned list?**

Frozen content is not silently replaced. Mods with reproduced startup or
shutdown failures are documented and deferred until an official compatible
release passes the required tests.
