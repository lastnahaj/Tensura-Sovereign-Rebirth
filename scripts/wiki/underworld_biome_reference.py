"""Render pinned Underworld biomes while preserving their legacy routes."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAMES = {
    'underworld_barrens': 'Underworld Barrens',
    'underworld_red_sands': 'Underworld Red Sands',
    'underworld_sands': 'Underworld Sands',
    'underworld_spikes': 'Underworld Spikes',
}
REVISIONS = {'underworld_barrens': 11826, 'underworld_red_sands': 11825, 'underworld_sands': 11823, 'underworld_spikes': 11824}
HEADLINES = {
    'underworld_barrens': 'Daemon territory. Open your route carefully.',
    'underworld_red_sands': 'Red sands. Ruins worth investigating.',
    'underworld_sands': 'Survey the sands. Watch for Megalodons.',
    'underworld_spikes': 'Rock spikes. Hostile ground.',
}


def manifest():
    return json.loads((ROOT / 'data/underworld_biome_reference.json').read_text(encoding='utf-8'))


def page(slug):
    return f'tensura-reference/blocks/{slug.replace("_", "-")}.md'


def definition(data, path):
    return data['resources'][path]['definition']


def baseline(data, slug):
    # An additive reference baseline, not a measured or guaranteed chunk value.
    biome = definition(data, f'data/tensura/biome_magicule/{slug}.json')['modifiers'][0]['value']
    level = definition(data, 'data/tensura/level_magicule/hell.json')['modifiers'][0]['value']
    return data['area_configuration']['baseMagicule'] + level + biome


def mob_name(registry_id):
    return registry_id.split(':', 1)[1].replace('_', ' ').title()


def spawn_entries(data, slug):
    base = definition(data, f'data/tensura/worldgen/biome/{slug}.json')['spawners']['monster']
    additions = [definition(data, f'data/tensura/neoforge/biome_modifier/{mob}_spawn.json')['spawners'] for mob in ('arch_daemon', 'greater_daemon', 'lesser_daemon')]
    return [(item, 'Biome definition') for item in base] + [(item, 'Hell-tag spawn addition') for item in additions]


def apply(records):
    data = manifest()
    by_page = {page(slug): slug for slug in NAMES}
    for record in records:
        slug = by_page.get(record.get('local_page'))
        if not slug:
            continue
        record['category'] = 'biomes'
        mobs = list(dict.fromkeys(mob_name(item['type']) for item, _ in spawn_entries(data, slug)))
        record['_card_stats'] = {'Magicule baseline': f'{baseline(data, slug):,.0f}', 'Mobs': ', '.join(mobs)}
        record['_stat_source_note'] = 'Pinned artifact and tracked configuration; live spawning and chunk values untested.'


def generate():
    data = manifest()
    overrides = json.loads((ROOT / 'data/reference_card_media.json').read_text(encoding='utf-8'))
    outputs = {}
    for slug, title in NAMES.items():
        local_page = page(slug)
        summary = overrides[local_page]['summary']
        biome = definition(data, f'data/tensura/worldgen/biome/{slug}.json')
        magicule = definition(data, f'data/tensura/biome_magicule/{slug}.json')
        rows = []
        for item, route in spawn_entries(data, slug):
            link = f'../mobs/mobs-{item["type"].split(":", 1)[1].replace("_", "-")}.md'
            rows.append(f'| [{mob_name(item["type"])}]({link}) | {item["weight"]} | {item["minCount"]}–{item["maxCount"]} | {route} |')
        terrain = ', '.join('`' + feature + '`' for step in biome['features'] for feature in step)
        has_ruin = slug in {'underworld_sands', 'underworld_red_sands'}
        ruin = 'red_sand_ruin' if slug == 'underworld_red_sands' else 'sand_ruin'
        ruin_title = 'Big Ruins' if slug == 'underworld_red_sands' else 'Ruins'
        ruin_page = 'structures-big-ruins' if slug == 'underworld_red_sands' else 'structures-ruins'
        structure_text = (
            f'The packaged `tensura:hell/{ruin}` structure targets a biome tag containing `{ "tensura:" + slug }`. Its placement set uses spacing **5 chunks** and separation **4 chunks**. Eligibility and placement parameters do not promise a ruin at a particular location or in already-generated chunks.\n\n[{ruin_title} reference](../structures/{ruin_page}.md)'
            if has_ruin else
            'No dedicated ruin association is asserted here. The upstream article does not establish one, and the checked sand-ruin tags select the two sand biomes instead. Use the [Structures directory](../structures/index.md) for separately verified locations.'
        )
        related = []
        for other_slug, other_title in NAMES.items():
            if other_slug == slug:
                continue
            asset = overrides[page(other_slug)]['asset']
            related.append(f'<a class="reference-related-card" href="../{other_slug.replace("_", "-")}/"><img src="../../../{asset}" alt="" loading="lazy" decoding="async"><span class="reference-related-copy"><strong>{other_title}</strong><small>{html.escape(overrides[page(other_slug)]["summary"])}</small></span></a>')
        content = [
            '---', f'title: {title}', 'description: ' + json.dumps(summary), '---', '', f'# {title}', '',
            '<span class="reference-badge">Tensura · Minecraft 1.21.1</span> <span class="reference-category">Biomes</span>', '',
            '<section data-reference-section="biomes" class="reference-overview reference-theme-world">',
            f'<figure class="reference-overview-media reference-overview-media--theme"><img src="../../../{overrides[local_page]["asset"]}" alt="{title} conceptual landscape" loading="eager" decoding="async"><figcaption>Original TSR landscape · not an in-game screenshot</figcaption></figure>',
            f'<div class="reference-overview-copy"><p class="reference-eyebrow">Underworld field reference</p><h2>{HEADLINES[slug]}</h2><p>{html.escape(summary)}</p><nav class="reference-quick-jumps" aria-label="Biome guide"><a href="#spawns">Spawn entries</a><a href="#magicules">Magicules</a><a href="#terrain-and-structures">Terrain &amp; structures</a></nav></div></section>', '',
            '!!! note "Artifact and configuration checked · live world untested"',
            '    This is a biome, not a collectible terrain block. The guide checks Tensura 2.0.1.2 resources and the tracked TSR configuration. Actual spawning, generated terrain, structure locations, and chunk Magicules have not been measured on the server.', '',
            '<div class="tensura-reference-article" markdown="1">', '', '<span id="Description"></span>', '', '## Spawns', '',
            'The base biome list and the tagged NeoForge additions are shown separately. **Arch Daemon is added through a biome modifier**, rather than appearing in the base biome JSON. Greater and Lesser Daemons also have Hell-tag additions; those entries are not collapsed into invented percentage chances.', '',
            '| Mob | Weight | Group range | Resource route |', '| --- | ---: | --- | --- |', *rows, '',
            'Weights are relative selection inputs, not spawn percentages or measured encounter rates. Group bounds, spawn costs, placement rules, area Magicules, other add-ons, and server data packs can affect the final result. The checked Hound Dog biome modifier targets Overworld tags; its presence in Barrens and Spikes instead comes from their own base biome lists.', '',
            '## Magicules', '',
            f'<div class="kiln-tier-grid"><article class="smithing-recipe"><p class="reference-eyebrow">Tracked base</p><h3>{data["area_configuration"]["baseMagicule"]:,.0f}</h3><p>Base chunk Magicules in the tracked area configuration.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Hell level modifier</p><h3>+100,000</h3><p>Packaged ADD modifier for <code>tensura:hell</code>.</p></article><article class="smithing-recipe"><p class="reference-eyebrow">Biome modifier</p><h3>+{magicule["modifiers"][0]["value"]:,.0f}</h3><p>Packaged ADD modifier for this biome.</p></article></div>', '',
            f'These three additive inputs give a **{baseline(data, slug):,.0f} reference baseline** before other modifiers. It is not a guaranteed current chunk reading or a personal MP grant. Generation, regeneration, magic engines, and server overrides can change the area value.', '',
            '??? info "Regeneration inputs"', '',
            '    The tracked base regeneration is **10**; the Hell resource has a **MULTIPLY 2** regeneration modifier, and this biome has an **ADD 50** regeneration modifier. No final rate or modifier-order result is asserted without checking the applying implementation and live server.', '',
            '<span id="Notes"></span>', '', '## Terrain and structures', '',
            f'The packaged biome feature list includes {terrain}. Precipitation is disabled in its definition. Landscape artwork is atmospheric illustration, not evidence of a particular castle, landmark, or terrain shape in game.', '',
            structure_text, '', '</div>', '',
            '<section class="reference-related"><div class="reference-related-heading"><h2>Compare Underworld biomes</h2><a href="../../biomes/">Browse all Biomes</a></div><div class="reference-related-grid">', *related, '</div></section>', '',
            '## Source and licensing', '',
            f'Adapted from [{title}](https://tensura.wiki.gg/wiki/{title.replace(" ", "_")}?oldid={REVISIONS[slug]}) on the Tensura: Reincarnated Wiki, recorded revision `{REVISIONS[slug]}`. Adapted text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The upstream spawn list is supplemented by the checked base biome and tagged additions.', '',
            f'Implementation: [Tensura {data["version"]}]({data["source_url"]}) · [Underworld evidence register](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/data/underworld_biome_reference.json) · [tracked area configuration](https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/{data["area_configuration"]["path"]}). Artifact SHA-1: `{data["artifact_sha1"]}`.', '',
            'The original TSR landscape is conceptual artwork. The source articles show missing image-file links; those upload links are not usable media and are not included here. See [Sources and attribution](../../project/sources-and-attribution.md).', '',
            '[Back to Biomes](../biomes/index.md) · [Hell dimension](../dimensions/hell.md)', '',
        ]
        outputs[local_page] = '\n'.join(content)
    return outputs
