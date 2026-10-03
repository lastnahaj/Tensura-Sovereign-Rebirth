"""Replace legacy acquisition claims and an empty source onboarding page."""
from __future__ import annotations

PAGE = 'mysticism-reference/skills/ultimate/ultimate-skill-aquisition.md'
START_PAGE = 'mysticism-reference/core-mechanics/getting-started.md'
EVIDENCE = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/ultimate_acquisition_reference.json'


def apply(records):
    for record in records:
        if record['local_page'] == START_PAGE:
            record['_catalogue_entry'] = False


def generate_all():
    from skill_catalogue import catalogue
    from sync_skill_catalogue import prepare_page
    lines = [
        '---', 'search:', '  exclude: true', 'title: Ultimate Skill Acquisition',
        'description: Read skill-specific unlock conditions and distinguish current abilities from Mysticism’s historical acquisition guide.',
        '---', '', '# Ultimate Skill Acquisition', '',
        '<section class="reference-overview reference-theme-abilities staff-guide-hero smithing-guide-hero">',
        '<figure class="reference-overview-media"><img src="../../../../assets/images/guides/soul-energy.webp" alt="Original soul-flame illustration" loading="eager" decoding="async"><figcaption>Original TSR soul-system artwork · not a skill icon</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Acquisition reference · Minecraft 1.21.1</p><h2>Follow the skill’s route, not a universal checklist.</h2><p>This legacy Mysticism address explains the limits of the old requirements. Current abilities remain together in the normal Ultimate directory.</p><nav class="reference-quick-jumps" aria-label="Acquisition guide"><a href="#Requirements">Find requirements</a><a href="#selected-mysticism-build">Selected build</a><a href="#Notes">Historical source</a></nav></div></section>', '',
        '<div class="tensura-reference-article" markdown="1">', '',
        '!!! warning "Historical requirements are not current unlock instructions"',
        '    The upstream guide’s generic awakening, mastery, MP, and Soul Quality requirements have not been verified for Mysticism **2.1.2**. They do not establish requirements for Tensura, Ascension, or Nightmares abilities.', '',
        '<span id="Requirements"></span>', '', '## Find the right requirements', '',
        '<div class="skill-reading-guide"><div><span>01</span><h3>Identify the ability</h3><p>Open the current Ultimate directory and check the owning mod and version. A similar name or a registered ID is not a player acquisition route.</p></div><div><span>02</span><h3>Read How to obtain</h3><p>Use the ability’s documented prerequisites, mastery conditions, and complete acquisition method. Missing conditions remain unverified rather than being filled from this historical guide.</p></div><div><span>03</span><h3>Check separate limits</h3><p>Distinguish learning costs, casting resources, server rules, and prestige locks. A cost or slot limit does not itself unlock an ability.</p></div></div>', '',
        '[Browse current Ultimate Skills](../../../tensura-reference/skills/ultimate/index.md) · [Understand Soul Energy](../../other/soul-energy.md) · [Prestige and Soul Grade](../../../prestige-and-soul-grade.md)', '',
        '## Selected Mysticism build', '',
        'The reviewed **2.1.2** Ultimate registry registers **`mysticism:embryo`**, with Ultimate type and Lord tier. This is a concrete exception to treating the old removal note as proof that the selected artifact has no Ultimate registration.', '',
        'Embryo’s own class declares its title, icon, and description methods but no completed active-effect or acquisition implementation. Its inherited behavior has not been fully audited. It remains **held out of the playable ability catalogue**: neither a working survival obtainment route nor a completed effect has been verified. The exported skill-book inventory entry is not proof that a random book successfully grants it.', '',
        'No Embryo game texture is redistributed here. An icon path in an artifact does not establish reusable image permission.', '',
        '<span id="Notes"></span>', '', '## Historical source limits', '',
        '??? info "Why the old checklist is not a current route"', '',
        '    The imported article combines older progression requirements with a later note about removal in the 1.21 update. Neither statement has been established as a universal rule for the selected pack. The historical [Soul Quality](../../core-mechanics/soul-quality.md) system is not interchangeable with current Soul Energy or SlimeThrone Extras’ Soul Grade.', '',
        '    Artifact registration, a skill-book inventory entry, and an upstream article describe different evidence. Successful acquisition, event ordering, add-on interactions, and active server rules still require separate checks.', '',
        '## Source and licensing', '',
        f'[Ultimate Skill Aquisition](https://trmysticism.wiki.gg/wiki/Ultimate_Skill_Aquisition), recorded revision `3427`, Mysticism Wiki, supplies the historical topic. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The [selected 2.1.2 artifact](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529) and [implementation review]({EVIDENCE}) support the limited registry and class findings above; these are **not live gameplay tests**.', '',
        'The illustration is original TSR thematic artwork, not Embryo’s icon or an official franchise image. [Sources and attribution](../../../project/sources-and-attribution.md).', '', '</div>', '',
    ]
    text, _ = prepare_page(PAGE, catalogue()['pages'][PAGE], '\n'.join(lines))
    start = [
        '---', 'title: Mysticism — Start Here', 'description: Use the TSR first-hour guide, selected Soul Energy reference, and prestige guide instead of an empty source import.', '---', '', '# Mysticism — Start Here', '',
        '<section class="reference-overview reference-theme-evolution staff-guide-hero smithing-guide-hero"><figure class="reference-overview-media"><img src="../../../assets/images/onboarding-realm-arrival.webp" alt="Original illustration of an adventurer arriving above a fantasy settlement" loading="eager" decoding="async"><figcaption>Original TSR onboarding artwork · not a screenshot</figcaption></figure><div class="reference-overview-copy"><p class="reference-eyebrow">Player guide · Minecraft 1.21.1</p><h2>Start with the realm. Then learn the system.</h2><p>The source onboarding page contains only an editorial maintenance banner. These TSR guides provide useful starting points without inventing Mysticism-specific beginner instructions.</p><nav class="reference-quick-jumps" aria-label="Starting guides"><a href="../../../getting-started/">First-hour route</a><a href="../../other/soul-energy/">Soul Energy</a><a href="../../../prestige-and-soul-grade/">Prestige</a></nav></div></section>', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid mechanics-guide-grid">',
    ]
    cards = [
        ('Start', 'Follow the first-hour route', 'Read your reincarnation, establish a foothold, and use the local field checklist.', '../../../getting-started/', 'assets/images/onboarding-realm-arrival.webp'),
        ('Learn', 'Understand Soul Energy', 'Separate current balance, maximum capacity, acquisition costs, and checked reset callbacks.', '../../other/soul-energy/', 'assets/images/guides/soul-energy.webp'),
        ('Plan', 'Prepare for prestige', 'Read the separate SlimeThrone Extras system before committing to reset or skill-lock decisions.', '../../../prestige-and-soul-grade/', 'assets/images/guides/prestige-progression.webp'),
    ]
    for category, title, summary, url, asset in cards:
        start.append(f'<article class="smithing-recipe mechanics-guide-card"><a href="{url}"><img src="../../../{asset}" alt="" loading="lazy" decoding="async"><p class="reference-eyebrow">{category}</p><h3>{title}</h3><p>{summary}</p><span class="reference-card-action">Open guide <span aria-hidden="true">→</span></span></a></article>')
    start += ['</div></div>', '', '## Scope', '', 'This preserved source address is a navigation guide, not an additional race, ability, or independent player progression system. Each linked guide carries its own evidence and verification limits.', '', '## Source and licensing', '', '[Getting Started](https://trmysticism.wiki.gg/wiki/Getting_Started), recorded revision `656`, Mysticism Wiki, contains no player instructions beyond an editorial maintenance banner. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The linked guides cite their own implementation and upstream sources.', '', f'[Source and artifact review]({EVIDENCE}). The three illustrations are original TSR thematic artwork, not in-game interfaces. The unrelated editorial portrait is omitted. [Sources and attribution](../../project/sources-and-attribution.md).', '']
    return {PAGE: text, START_PAGE: '\n'.join(start)}
