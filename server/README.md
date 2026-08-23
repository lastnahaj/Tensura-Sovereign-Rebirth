# Dedicated server source

The dedicated-server distribution is generated from the Packwiz source in
`pack/`. The finished package will install NeoForge and retrieve eligible mods
from their canonical distribution sources; third-party JARs are not stored in
this repository.

Disposable automated server instances belong under `.build/server-test/` and
must never be committed. The EULA may be accepted only inside that disposable
test directory for automated validation.
