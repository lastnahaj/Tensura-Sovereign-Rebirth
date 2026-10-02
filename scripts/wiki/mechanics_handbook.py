"""Build a task-oriented handbook without editorial placeholder media."""
from __future__ import annotations

import html
from pathlib import Path

PAGE = 'tensura-reference/core-mechanics/mechanics.md'
ASSET = 'assets/images/items/magic-tome.webp'
SUMMARY = 'Choose a guide for character growth, skill learning, casting, crafting, or prestige; check each system’s source and verification scope.'
GUIDES = [
    ('Character', 'Start your first hour', 'Join the realm, read your reincarnation, and follow a practical opening route.', '../../../getting-started/', 'assets/images/onboarding-realm-arrival.webp'),
    ('Evolution', 'Plan a race route', 'Browse separate race families and open each evolution for its documented requirements.', '../../races/', 'assets/images/onboarding-character-paths.webp'),
    ('Spellcraft', 'Learn before you cast', 'Compare spell schools and distinguish tome acquisition, learning, mastery, and casting costs.', '../../../magic-learning/', 'assets/images/items/magic-tome.webp'),
    ('Casting', 'Bind a working loadout', 'Check tool slots, spell exclusions, binding, selection controls, and resource costs.', '../../tools/caster-tools-tutorial/', 'assets/images/items/low-magic-staff.webp'),
    ('Crafting', 'Build from a schematic', 'Browse packaged Smithing Bench recipes and their required learned schematics.', '../../blocks/blocks-smithing-bench/', 'assets/images/blocks/smithing-bench.webp'),
    ('Prestige', 'Prepare before resetting', 'Read the SlimeThrone Extras guide for prestige conditions, Soul Grade, and eligible skill locks.', '../../../prestige-and-soul-grade/', 'assets/images/guides/prestige-progression.webp'),
]
TOPICS = [
    ('Combat & character', [('Ability usage', '../mechanics-ability-usage/'), ('Dodging', '../dodging/'), ('EP, Magicules & Aura', '../ep-magicule-aura/'), ('Gear evolution', '../gear-evolution/'), ('Engravings', '../engravings/'), ('Battlewill training', '../../../battlewill-training/')]),
    ('World & community', [('Naming', '../naming/'), ('Trading', '../trading/'), ('Dwarf reputation', '../../mobs/mobs-dwarf/#Reputation_System'), ('Praying & Labyrinth Tree', '../../structures/structures-labyrinth-tree/'), ('Hipokute farming', '../mechanics-hipokute-farming/')]),
    ('Reset & server rules', [('Reset scrolls', '../mechanics-reset-scrolls/'), ('Reset counter reference', '../mechanics-reset-counter/'), ('Rimuru Mode reference', '../mechanics-rimuru-mode/'), ('Hardcore Race reference', '../mechanics-hardcore-race/'), ('Current gamerule catalogue', '../../gamerules/'), ('Commands by source', '../../commands/'), ('Configuration reference', '../../configuration/')]),
]


def apply(records):
    for record in records:
        if record['local_page'] == PAGE:
            record['display_title'] = 'Mechanics Handbook'
            record['_summary_override'] = SUMMARY
            record['_primary_media'] = {'local_path': ASSET, 'kind': 'original'}


def generate():
    lines = [
        '---', 'title: Mechanics Handbook', f'description: {SUMMARY}', '---', '', '# Mechanics Handbook', '',
        '<section data-reference-section="core-mechanics" class="reference-overview reference-theme-evolution staff-guide-hero smithing-guide-hero">',
        f'<figure class="reference-overview-media"><img src="../../../{ASSET}" alt="Original navy and gold field-guide book illustration" loading="eager" decoding="async"><figcaption>Original TSR book illustration · handbook artwork</figcaption></figure>',
        '<div class="reference-overview-copy"><p class="reference-eyebrow">Player systems · Minecraft 1.21.1</p><h2>Understand the system behind your next step.</h2><p>Choose a practical guide, then open the detailed reference. Character resources, learning conditions, equipment, and server rules answer different questions.</p><nav class="reference-quick-jumps" aria-label="Handbook sections"><a href="#choose-your-next-step">Choose a guide</a><a href="#browse-the-reference">Browse topics</a><a href="#read-the-evidence">Check evidence</a></nav></div></section>', '',
        '## Choose your next step', '',
        '<div class="tensura-reference-article"><div class="chilled-crafting-grid mechanics-guide-grid">',
    ]
    for category, title, description, destination, asset in GUIDES:
        lines.append(f'<article class="smithing-recipe mechanics-guide-card"><a href="{destination}"><img src="../../../{asset}" alt="" loading="lazy" decoding="async"><p class="reference-eyebrow">{category}</p><h3>{title}</h3><p>{description}</p><span class="reference-card-action">Open guide <span aria-hidden="true">→</span></span></a></article>')
    lines.extend(['</div></div>', '', '<span id="Ingame_Mechanics"></span>', '', '## Browse the reference', '',
                  'These topic links preserve the upstream index while separating player actions from server-controlled rules. A reference page is not proof that its optional system is enabled or its behavior has been tested on the server.', '',
                  '<div class="tensura-reference-article"><div class="chilled-crafting-grid mechanics-topic-grid">'])
    for category, topics in TOPICS:
        links = ''.join(f'<li><a href="{url}">{html.escape(title)}</a></li>' for title, url in topics)
        anchor = '<span id="Gamerule_Mechanics"></span>' if category == 'Reset & server rules' else ''
        lines.append(f'<article class="smithing-recipe">{anchor}<h3>{html.escape(category)}</h3><ul>{links}</ul></article>')
    lines.extend([
        '</div></div>', '', '## Read the evidence', '',
        '<div class="skill-reading-guide"><div><span>01</span><h3>Find the source</h3><p>Check the named mod, selected version, source revision, and attribution. Similar names can belong to different systems.</p></div><div><span>02</span><h3>Check the method</h3><p>A registry ID, cost, or configuration value alone does not establish a survival obtainment route. Read the prerequisites and implementation scope.</p></div><div><span>03</span><h3>Respect the limits</h3><p>Artifact checks are not live gameplay tests. Server overrides, optional rules, and untested retention remain explicit where applicable.</p></div></div>', '',
        '??? info "What this handbook verifies"', '',
        '    This page organizes existing guides and preserves the source index’s topic destinations. Its links, artwork, rendered panels, and disclosures are checked as site content. It does not certify every linked mechanic, enable a gamerule, or establish live progression and reset outcomes. Each guide carries its own evidence and limits.', '',
        '## Source and licensing', '',
        '[Mechanics](https://tensura.wiki.gg/wiki/Mechanics?oldid=12765), recorded revision `12765`, on the Tensura: Reincarnated Wiki supplied the retained topic index. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). TSR-specific learning, crafting, and prestige guides cite their own artifact, configuration, and upstream sources.', '',
        'The book and guide-card illustrations are original TSR artwork, not screenshots or evidence of game interfaces. The source’s WIP2 editor portrait is omitted; its File page did not establish reusable image permission. See [Sources and attribution](../../project/sources-and-attribution.md).', '',
        '[Browse all mechanics](index.md) · [Progression overview](../../progression-overview.md)', '',
    ])
    return '\n'.join(lines)
