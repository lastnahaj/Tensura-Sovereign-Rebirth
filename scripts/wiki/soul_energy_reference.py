"""Render current Soul Energy guidance with explicit legacy-system boundaries."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = 'mysticism-reference/other/soul-energy.md'
ASSET = 'assets/images/guides/soul-energy.webp'
MECHANICS = 'mysticism-reference/core-mechanics/mechanics.md'
LEGACY = {'mysticism-reference/core-mechanics/soul-quality.md': ('Soul Quality', 'https://trmysticism.wiki.gg/wiki/Soul_Quality', '2158'), 'mysticism-reference/core-mechanics/compatibility-system.md': ('Compatibility System', 'https://trmysticism.wiki.gg/wiki/Compatibility_System', '2439')}
SUMMARY = 'Read current and maximum Soul Energy, Unique Skill costs, naming gains, awakening bonuses, and the selected reset hooks.'

def apply(records):
    for record in records:
        page = record['local_page']
        if not record.get('_primary_media') and any(title.replace('_', ' ').casefold() == 'mysticism wip.png' for title in record.get('image_titles', [])):
            record['_omit_media'] = True
        if page == PAGE:
            record['_summary_override'] = SUMMARY
            record['_primary_media'] = {'local_path': ASSET, 'kind': 'original'}
        elif page == MECHANICS:
            record['display_title'] = 'Mysticism Soul Systems'
            record['_summary_override'] = 'Start with the selected Soul Energy implementation; distinguish historical source systems from current player guidance.'
            record['_primary_media'] = {'local_path': ASSET, 'kind': 'original'}
        elif page in LEGACY:
            record['_omit_media'] = True
            record['display_title'] = LEGACY[page][0] + ' · historical reference'
            record['_summary_override'] = 'Historical upstream system; not verified for the selected Mysticism 2.1.2 build. Use current Soul Energy and TSR Soul Grade guides.'

def source():
    return '\n'.join(['## Source and licensing', '', '[Soul Energy](https://trmysticism.wiki.gg/wiki/Soul_Energy) on the Mysticism Wiki supplies the source topic. Its imported revision `2892` describes an earlier behavior snapshot; the figures and hook distinctions below follow the [selected 2.1.2 artifact](https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529), the [implementation review](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/soul_energy_reference.json), and the tracked configuration. Adapted source text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).', '', 'The soul-flame illustration is original TSR thematic artwork, not an in-game icon or interface. The editor portrait is omitted because its File page did not establish reusable image permission. See [Sources and attribution](../../project/sources-and-attribution.md).', ''])

def generate():
    data = json.loads((ROOT / 'data/soul_energy_reference.json').read_text(encoding='utf-8'))
    lines = ['---', 'title: Soul Energy', f'description: {SUMMARY}', '---', '', '# Soul Energy', '',
        '<section data-reference-section="other" class="reference-overview reference-theme-evolution staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original cyan and violet soul-flame illustration" loading="eager" decoding="async"><figcaption>Original TSR thematic artwork · not an in-game icon</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Mysticism 2.1.2 · Minecraft 1.21.1</p><h2>Know your balance before learning another Unique Skill.</h2><p>Soul Energy has a spendable balance and a maximum. Its acquisition cost is separate from casting resources and SlimeThrone Extras’ Soul Grade.</p><nav class="reference-quick-jumps" aria-label="Soul Energy guide"><a href="#learning-cost">Learning cost</a><a href="#grow-your-capacity">Capacity gains</a><a href="#reset-behavior">Reset behavior</a></nav></div></section>', '',
        '!!! note "Selected implementation · not a live-server test"', '    The handlers, mixin targets, and tracked configuration were reviewed for Mysticism **2.1.2**. The active world gamerule, successful skill acquisition, naming eligibility, and complete reset interactions with other mods have not been tested on the server.', '',
        '<span id="Functionality"></span>', '', '## Three different values', '',
        '<div class="skill-reading-guide"><div><span>01</span><h3>Current Soul Energy</h3><p>The balance used by applicable acquisition checks. A cost can reduce this without lowering your maximum.</p></div><div><span>02</span><h3>Maximum Soul Energy</h3><p>Your capacity attribute. The checked gains increase both this value and the current balance.</p></div><div><span>03</span><h3>TSR Soul Grade</h3><p>A separate SlimeThrone Extras prestige system. Soul Energy is not a grade, Ultimate Skill slot count, or skill-lock limit.</p></div></div>', '',
        '## Learning cost', '',
        'The selected Unique Skill handler is controlled by **`uniqueSECost`**, registered with a default of **true**. This is the packaged default, not confirmation of the current world setting. The tracked `General.seCostMultiplier` is **4**.', '',
        '**Soul Energy cost = the skill instance’s acquisition Magicule cost × 4.** Use the acquisition value, not the MP spent when casting or activating a mode. A calculated acquisition cost of 100,000 would require 400,000 Soul Energy; this is a formula example, not a particular skill’s requirement.', '',
        'For this handler, a balance **equal to the cost is sufficient**. A lower balance blocks the unlock; an accepted branch subtracts the cost and marks the instance for its removal/refund handler. This does not bypass the skill’s other learning requirements or establish a survival obtainment route.', '',
        '??? info "Checked bypasses and separate handlers"', '',
        '    This Unique Skill branch skips sub-instances, temporary skills, instances tagged `vicSkill`, an explicit `NoSoulEnergyCost` exemption, infinite-material players, a disabled `uniqueSECost` rule, non-Unique skills, and negative mastery. The explicit exemption tag is removed after bypass. The separate `MysticSkill` handler has its own cost method and stricter balance comparison; do not apply the Unique Skill formula to every ability class.', '',
        '    A removal hook can refund a tagged acquisition cost, but complete event ordering and reset/add-on combinations were not gameplay-tested. Do not treat removing or resetting a skill as a guaranteed refund strategy.', '',
        '## Starting capacity', '',
        'The first-login hook initializes current and maximum energy when the player has **no registered race**. Its weighted roll spans **500,000–7,000,000** and rounds to the nearest 100. The Rimuru Mode branch instead initializes **3,000,000**. These initialization conditions are not proof that every reset rerolls your balance or that every first Unique Skill is free.', '',
        '??? info "Initial-roll distribution"', '', '    | Selected band | Probability |', '    | --- | --- |']
    for band in data['initial_roll']['bands']:
        lines.append(f'    | {band["minimum"]:,}–{band["maximum"]:,} | {band["probability_percent"]:g}% |')
    lines += ['', '    The band probabilities total 100%. Adjacent ranges share endpoints; values are rounded after the integer draw. These are branch probabilities, not a measured distribution from player accounts.', '',
        '## Grow your capacity', '',
        '| Checked event branch | Capacity and current-balance increase |', '| --- | --- |',
        '| Naming with no player namer | Random **100,000–249,999** |',
        '| Naming by a player with a higher maximum | The maximum-energy difference, capped at **1,000,000**; requires the recipient’s naming-boost flag to be false |',
        '| Player awakening event | Random **500,000–999,999** |', '',
        'The player-namer branch sets the naming-boost flag after a successful gain; a namer with an equal or lower maximum grants no increase through that branch. The no-player-namer branch uses a different random gain and does not set that flag. Neither result proves that repeated naming is available: the underlying naming system still decides whether the event can occur.', '',
        'The awakening hook does not establish a repeatable farming route. Awakening prerequisites, naming costs, event eligibility, world persistence, and other mods’ progression restrictions remain separate checks.', '',
        '## Reset behavior', '',
        '| Selected Mysticism hook | Direct Soul Energy behavior |', '| --- | --- |',
        '| Skill reset, at the start of `resetSkill` | Sets the current balance to the maximum |',
        '| Character reset, at the start of `resetEverything` | Refills the current balance to the maximum; if the base `isFullReset` condition is true, first adds **500,000–999,999** to capacity |',
        '| Race reset, on return from `resetRace` | Does not directly refill Soul Energy in this hook |',
        '| Administrative Soul Energy reset command | Rerolls current and maximum energy; not a normal player progression route |', '',
        '!!! warning "A refill hook is not a complete reset outcome"', '    These are direct add-on callbacks. Subsequent learning can spend energy, and base reset behavior or other add-ons can alter the final result. This review does not establish a free reroll, guaranteed skill retention, repeated bonus, or compatibility with TSR prestige. Read the [TSR prestige guide](../../prestige-and-soul-grade.md) before committing to a reset.', '',
        '## Historical systems are not current requirements', '',
        'The upstream [Soul Quality](../core-mechanics/soul-quality.md) slot probabilities and [Compatibility System](../core-mechanics/compatibility-system.md) drop claims are not verified for the selected build. Searches of the packaged classes found no constants under those legacy system names. That negative search is limited evidence, not proof that no differently named implementation can exist. Neither system is presented here as a current progression requirement.', '',
        source(), '[Browse abilities](../../tensura-reference/skills/index.md) · [Prestige and Soul Grade](../../prestige-and-soul-grade.md) · [Commands by source](../../tensura-reference/commands/index.md)', '']
    content = '\n'.join(lines)
    content = content.replace('!!! note "Selected implementation', '<div class="tensura-reference-article" markdown="1">\n\n!!! note "Selected implementation', 1)
    return content + '\n</div>\n'

def generate_all():
    pages = {PAGE: generate()}
    pages[MECHANICS] = '\n'.join(['---','title: Mysticism Soul Systems','description: Current Soul Energy guidance and the boundary between selected-build mechanics and historical upstream systems.','---','','# Mysticism Soul Systems','','<span class="reference-badge">Mysticism 2.1.2 · Minecraft 1.21.1</span>', '', '## Start with the current guide', '', '[Soul Energy](../other/soul-energy.md) explains spendable energy, maximum capacity, acquisition costs, naming and awakening gains, and the checked reset hooks. [TSR prestige and Soul Grade](../../prestige-and-soul-grade.md) covers the separate SlimeThrone Extras system.', '', '## Historical upstream topics', '', 'The source index links [Soul Quality](soul-quality.md) and [Compatibility System](compatibility-system.md). Their older slot probabilities and skill-drop claims are **not verified for the selected Mysticism build**. They remain source-history references, not current player requirements.', '', '## Source and licensing', '', '[Mysticism Mechanics](https://trmysticism.wiki.gg/wiki/Mechanics), recorded revision `2948`, supplies the original topic index. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Selected-build checks are recorded in the [Soul Energy implementation review](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/soul_energy_reference.json).', ''])
    for page, (title, url, revision) in LEGACY.items():
        pages[page] = '\n'.join(['---',f'title: {title} — Historical Reference',f'description: Historical {title} source topic; not verified as a current Mysticism 2.1.2 player system.','---','',f'# {title}', '', '!!! warning "Historical reference · not a current requirement"', '    The imported source describes an older system. Its probabilities, slot limits, and obtainment claims have not been verified for Mysticism **2.1.2** on Minecraft **1.21.1**, so they are not supplied as current progression instructions.', '', '<span id="Functionality"></span>', '', '## Use the selected-build guides', '', '[Soul Energy](../other/soul-energy.md) documents the checked current and maximum-energy model. [TSR prestige and Soul Grade](../../prestige-and-soul-grade.md) explains the separate SlimeThrone Extras system. Neither should be interpreted through this historical topic.', '', 'The packaged-class scan found no constants named `soulQuality`, `SoulQuality`, `compatibilitySystem`, or `CompatibilitySystem`. This does not exclude an implementation with another name or an external add-on; it is not enough to certify these historical claims.', '', '## Source and licensing', '', f'Original topic: [{title}]({url}), recorded revision `{revision}`, Mysticism Wiki. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). [Selected artifact review](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/soul_energy_reference.json).', ''])
    for page in [MECHANICS, *LEGACY]:
        title = 'Mysticism Soul Systems' if page == MECHANICS else LEGACY[page][0]
        if page == MECHANICS:
            figure = f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original cyan and violet soul-flame illustration" loading="eager" decoding="async"><figcaption>Original TSR thematic artwork</figcaption></figure>'
            copy = 'Start with the selected Soul Energy implementation.'
        else:
            figure = ''
            copy = 'Historical source topic · not a verified current requirement.'
        hero = f'<section class="reference-overview reference-theme-evolution">{figure}<div class="reference-overview-copy"><p class="reference-eyebrow">Mysticism 2.1.2 · Minecraft 1.21.1</p><h2>{copy}</h2><nav class="reference-quick-jumps" aria-label="Current soul-system guides"><a href="../../other/soul-energy/">Read Soul Energy</a><a href="../../../prestige-and-soul-grade/">TSR Soul Grade</a></nav></div></section>'
        pages[page] = pages[page].replace('# '+title+'\n', '# '+title+'\n\n'+hero+'\n\n<div class="tensura-reference-article" markdown="1">\n', 1) + '\n</div>\n'
    return pages
