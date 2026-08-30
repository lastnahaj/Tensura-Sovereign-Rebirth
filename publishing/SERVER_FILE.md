# Server File Copy

## Short additional-file description

Ready-to-run dedicated server for Tensura: Sovereign Rebirth 1.0.0 Beta 1.
Requires 64-bit Java 21 and acceptance of the Minecraft EULA. This is the
matching server package for the 1.0.0-beta.1 client.

## Installation

1. Extract the ZIP into a new, empty directory.
2. Install 64-bit Java 21.
3. Read Mojang's Minecraft EULA. Change `eula=false` to `eula=true` only if you
   accept it.
4. Run `run.bat` on Windows or `run.sh` on Linux.
5. Allow startup to finish before joining. The first world creation takes
   longer than a restart.

The supplied JVM settings permit up to 8 GB of heap. Leave enough memory for
the operating system and hosting panel. Back up the world, configuration,
KubeJS, quest, and backup directories before every pack update.

Do not install the client ZIP on a dedicated server. Do not add client-only
mods to the server unless a later release explicitly requires them.

## Update notice

Stop the server cleanly and make an offline backup before replacing files.
Preserve the existing world and server-specific administration data. Review
the new release notes for configuration migrations before the next start.
