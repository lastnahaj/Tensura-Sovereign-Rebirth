"""Render the checked casting-tool walkthrough at its existing address."""
import html


def generate(data):
    caster = data['caster_tools']
    lines = ['---', 'title: Caster Tools Tutorial', 'description: Bind compatible spells, select a stored spell, and understand casting costs and learning exclusions for Minecraft 1.21.1.', '---', '',
             '<span class="reference-badge">Tensura: Reincarnated</span> <span class="reference-category">Casting equipment</span>', '',
             '<section data-reference-section="items" class="reference-overview reference-theme-abilities staff-guide-hero">',
             '<figure class="reference-overview-media"><img src="../../../assets/images/items/low-magic-staff.webp" alt="Original wooden casting staff illustration with a cyan crystal" loading="eager" decoding="async"><figcaption>TSR illustration · casting staff example</figcaption></figure>',
             '<div class="reference-overview-copy"><p class="reference-eyebrow">Casting field guide · Minecraft 1.21.1</p><h1>Bind. Select. Cast.</h1><p>Turn a compatible casting tool into a spell loadout. Keep stored spells separate from character learning, and budget for the extra cost of casting magic you have not learned.</p>',
             '<nav class="reference-quick-jumps" aria-label="Casting guide"><a href="#prepare-your-loadout">Prepare a loadout</a><a href="#budget-for-unlearned-casting">Casting costs</a><a href="#learning-required">Learning required</a></nav></div></section>', '',
             '<span id="Caster_Tools"></span><span id="What_are_Caster_Tools.3F"></span><span id="What_are_Caster_Tools?"></span>', '',
             '## Prepare your loadout', '', '<div class="tensura-reference-article"><section class="potion-guide caster-guide"><div class="potion-guide-grid">',
             '<article class="potion-guide-card caster-step"><p class="reference-eyebrow">01 · Bind</p><h2>Build the loadout</h2><p>Place a compatible item in the <a href="../../resistances/spellbinding-table/">Spellbinding Table</a> and choose an eligible spell from its list.</p><details><summary>Check binding requirements</summary><p>The spell must be magic, outside the unbindable tag, and have nonnegative mastery. The tool needs a free spell slot; slot and equip hooks can reject it.</p><p>Ordinary staff binding does not require full mastery. Copying a spell into an Unbound Tome is a separate branch with mastery and copy-exclusion checks.</p></details></article>',
             '<article class="potion-guide-card caster-step"><p class="reference-eyebrow">02 · Select</p><h2>Choose the spell</h2><p>Hold the casting tool in your main hand. Hold <strong>Next Ability Mode</strong> or <strong>Previous Ability Mode</strong> while scrolling to change the stored spell.</p><details><summary>Spell versus mode</summary><p>Holding Next Ability Mode while using the tool requests a mode change for the current spell. It does not select another stored spell. A spell without extra modes cannot gain one this way.</p><p>Check Minecraft Controls for your assigned keys; these control names do not assume a default keyboard layout.</p></details></article>',
             '<article class="potion-guide-card caster-step"><p class="reference-eyebrow">03 · Cast</p><h2>Use the selected spell</h2><p>Use the tool without the mode modifier. An empty stored spell list fails the staff use check. Watch the selected spell, resource messages, and cooldown.</p><details><summary>Stored is not learned</summary><p>A tool can supply an eligible unlearned spell instance without teaching the spell to your character. Excluded spells still require learning; possession of a tool is not a bypass.</p><p>Spell-specific conditions, modes, and add-on restrictions can still prevent casting.</p></details></article>',
             '</div></section></div>', '',
             'For base slots, crafting materials, and learned-schematic requirements, use the [staff comparison guide](../items/magic-staves.md). Low / Medium / High staffs start at **3 / 4 / 5 slots**, plus the Magic Capacity enchantment level.', '',
             '<span id="How_do_Caster_Tools_work.3F"></span><span id="How_do_Caster_Tools_work?"></span>', '',
             '## Budget for unlearned casting', '',
             '<section class="caster-cost-grid" aria-label="Unlearned casting modifiers">',
             '<article><p class="reference-eyebrow">Resource inputs</p><strong>×' + str(caster['unlearned_cost_multiplier']).removesuffix('.0') + '</strong><h3>Aura and Magicules</h3><p>The shared resource check multiplies both cost inputs before later adjustments. This is not a universal final-cost quote.</p></article>',
             '<article><p class="reference-eyebrow">Normal chant input</p><strong>×' + str(caster['unlearned_chant_multiplier']).removesuffix('.0') + '</strong><h3>Before Chant Speed</h3><p>The normal path applies the multiplier before Chant Speed. An allowed instant-cast path returns one tick first.</p></article>', '</section>', '',
             'Magicule cost also uses the character’s Magic Cost Multiplier attribute. On the normal chant path, a nonzero Chant Speed divides the adjusted input; integer conversion and a one-tick minimum apply. Staff cooldown and chant duration are different values. These implementation inputs do not guarantee elapsed server time.', '',
             '??? info "What stored gear EP can pay for"', '',
             '    A qualifying casting weapon in use, with nonnegative spell mastery and an `EP_DURABILITY` component, can contribute stored EP toward the **Magicule** cost. That pool is separate from the item’s ordinary durability bar and does not replace the **Aura** check. Do not assume unlimited fuel or a refund on every failed cast; live fuel behavior is untested.', '',
             '<span id="Magics_that_require_learning_to_use"></span>', '', '## Learning required', '',
             'The selected artifact’s unlearned-cast exclusion tag contains the following entries. This is a restriction on casting **without learning**, not a list of every spell that can or cannot be bound.', '',
             '<ul class="caster-exclusions">']
    for entry in caster['unlearned_exclusions']:
        route = '../../' + entry['page'].removeprefix('../').removesuffix('.md')
        if route.endswith('/index'):
            route = route.removesuffix('index')
        else:
            route += '/'
        lines.append('<li><a href="' + route + '">' + html.escape(entry['label']) + '</a></li>')
    lines.extend(['</ul>', '',
                  '## Troubleshoot a cast', '',
                  '??? question "The spell will not bind"', '    Check the table’s eligible list, available capacity, nonnegative mastery, and spell-specific slot/equip conditions. A listing in the wiki is not proof of binding compatibility.', '',
                  '??? question "The tool will not cast"', '    Check that it contains a spell, the selected spell is correct, and no mode modifier is held. If the spell is unlearned, check the exclusions above. Resource, cooldown, and spell-specific checks still apply.', '',
                  '??? question "Changing modes does not change spells"', '    Use the modifier **with scrolling** to select another stored spell. Modifier **with item use** requests a mode change within the current spell.', '',
                  '??? question "Will the loadout survive a reset or prestige?"', '    Reset-scroll and SlimeThrone Extras prestige retention have not been verified. Do not rely on a guaranteed stored-spell or learned-spell retention rule here.', '',
                  '!!! note "Verification scope"', '    ' + caster['verification_limits'], '',
                  '## Source and licensing', '',
                  'Adapted from [Caster Tools Tutorial](' + caster['source_url'] + ') on the Tensura: Reincarnated Wiki, recorded revision `12819`; the live article was reviewed on ' + data['reviewed_on'] + '. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The original staff illustration is not an in-game appearance guarantee.', '',
                  'Implementation: [Tensura 2.0.1.2 release](https://www.curseforge.com/minecraft/mc-mods/tensura-reincarnated/files/8665599) · [casting evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/magic_reference.json) · [TSR magic configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/tensura/ability/magic_config.toml). The checked artifact SHA-256 is `' + data['reference_build']['artifact_sha256'] + '`.', '',
                  '??? info "Artifact evidence"', ''])
    lines.extend('    - `' + path + '`' for path in caster['evidence_paths'])
    lines.extend(['', '[Compare casting staves](../items/magic-staves.md) · [Learn magic](../../magic-learning.md) · [Browse Tools](index.md)', ''])
    return '\n'.join(lines)
