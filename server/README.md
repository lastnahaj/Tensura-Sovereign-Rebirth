# Dedicated server

The beta server archive is generated from the validated runtime and tracked
configuration source. It includes NeoForge 21.1.248, the 175-JAR playable
server profile, stability defaults, KubeJS data, and nine quest chapters
containing 140 loaded FTB Quests entries.

Use Java 21. Before the first start, read the Minecraft EULA and set
`eula=true` in `eula.txt` if you accept it. Start with `run.bat` on Windows or
`run.sh` on Linux. The default heap is 2-8 GB; leave at least 2 GB available for
the operating system.

The generated archive remains a private beta-testing artifact until it is
attached to an approved public client release. Public distribution remains
gated on the platform and licensing audit.

Disposable automated server instances belong under `.build/server-test/` and
must never be committed. The EULA may be accepted only inside that disposable
test directory for automated validation.
