"""Render individually reviewed evolution gates from the pinned race configuration."""
from functools import lru_cache
import html
import json
import posixpath
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[2]
BEGIN = '<!-- verified-race-requirement:start -->'
END = '<!-- verified-race-requirement:end -->'


@lru_cache(maxsize=1)
def manifest():
    return json.loads((ROOT / 'data/race_evolution_requirements.json').read_text(encoding='utf-8'))


def reviewed_requirement(decision):
    entry = manifest()['races'].get(decision.get('registry_id'))
    if not entry:
        return None
    config = tomllib.loads((ROOT / entry['config_path']).read_text(encoding='utf-8'))
    return {**entry, 'count': config[entry['config_section']][entry['config_key']]}


def link(page, current_route):
    return posixpath.relpath(page.removesuffix('.md') + '/', current_route).rstrip('/') + '/'


def requirement_label(decision):
    entry = reviewed_requirement(decision)
    return f"{entry['count']:,} {entry['item_title']} uses" if entry else None


def family_details(decision, current_route):
    entry = reviewed_requirement(decision)
    if not entry:
        return ''
    return ('<dt>Complete the consumption gate</dt><dd>Consume <a href="' + link(entry['item_page'], current_route)
            + '">' + html.escape(entry['item_title']) + '</a> with <a href="' + link(entry['ability_page'], current_route)
            + '">Absorb &amp; Dissolve</a>. The requirement counts item uses, not inventory holdings. '
            + '<a href="' + link(entry['local_page'], current_route) + '#verified-evolution-requirement">Read the verified route and evidence</a>.</dd>')


def article_panel(decision, page):
    entry = reviewed_requirement(decision)
    if not entry:
        return ''
    current_route = page.removesuffix('.md') + '/'
    item_link = link(entry['item_page'], current_route)
    ability_link = link(entry['ability_page'], current_route)
    config_link = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/' + entry['config_path']
    build = manifest()['build']
    return (BEGIN + '\n<section class="skill-availability">'
            + '<h2 id="verified-evolution-requirement">Evolve from Slime</h2>'
            + '<p>The checked-in consumption gate is <strong>' + f"{entry['count']:,}"
            + ' <a href="' + item_link + '">Magic Ore Shard uses</a></strong>.</p>'
            + '<ol><li>Slime is the recorded predecessor for this route.</li>'
            + '<li>Hold an ore shard in your main hand and activate <a href="' + ability_link
            + '">Absorb &amp; Dissolve</a>. Each consumed shard records one item use.</li>'
            + '<li>Check the in-game evolution menu for the completed consumption gate and any remaining conditions.</li></ol>'
            + '<p>Carrying shards, crafting their storage block, or mining ore is not the documented consumption action. '
            + 'The requirement reads the item-use statistic; this check does not establish how add-ons or prestige resets affect that statistic.</p>'
            + '<p>Evidence: <a href="' + config_link + '">MetalSlime.oreRequirement configuration</a> · '
            + '<a href="' + build['source_url'] + '">Tensura ' + build['version'] + ' artifact</a>. '
            + 'Code and configuration checks are not live-server gameplay tests.</p>'
            + '<details><summary>Artifact evidence</summary><ul>'
            + ''.join('<li><code>' + html.escape(path) + '</code></li>' for path in entry['evidence_paths'])
            + '</ul></details></section>\n' + END + '\n\n')
