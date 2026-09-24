"""Build the unified ability landing page and its lightweight search index."""
import html
import json
import posixpath
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
CATEGORIES = {
    'skills/intrinsic': ('Intrinsic', 'Talents inherent to a race or evolution.', 'assets/upstream/tensura/skills/absorb-and-dissolve-7e27621142.png'),
    'skills/common': ('Common', 'Foundational combat, movement and utility.', 'assets/upstream/tensura/skills/self-regeneration-e5a1e8ed3e.png'),
    'skills/extra': ('Extra', 'Specialized techniques and mastery upgrades.', 'assets/upstream/tensura/skills/analytical-appraisal-bb01737e8d.png'),
    'skills/unique': ('Unique', 'Build-defining powers, modes and passives.', 'assets/upstream/tensura/skills/great-sage-157839d932.png'),
    'skills/ultimate': ('Ultimate', 'Advanced powers and awakening requirements.', 'assets/ascension/ultimates/the_timeless_mage.png'),
    'battlewill': ('Battlewill', 'Aura techniques, training and resource control.', 'assets/ascension/skills/energy_charge.png'),
    'magic': ('Magic', 'Spells, schools and their casting mechanics.', 'assets/upstream/tensura/magic/gate-2ede9e9877.png'),
    'resistances': ('Resistances', 'Defensive effects and nullifications.', 'assets/upstream/tensura/resistances/pain-nullification-404b1c5c4b.png'),
}


def relative(page, target):
    base = page[:-8] if page.endswith('index.md') else page[:-3] + '/'
    result = posixpath.relpath(target, base)
    return result + ('/' if target.endswith('/') and not result.endswith('/') else '')


def style_directory(content, category, page):
    """Keep catalogue cards and source metadata; replace only the banner."""
    soup = BeautifulSoup(content, 'html.parser')
    header = soup.select_one('.reference-directory-hero')
    count = len(soup.select('.reference-card'))
    title = header.h1.get_text(strip=True)
    description = header.select_one('.reference-directory-hero-copy > p:not(.reference-eyebrow)').get_text(' ', strip=True)
    replacement = f'<header class="skill-directory-heading"><p class="reference-eyebrow">Ability directory</p><h1>{html.escape(title)}</h1><p>{html.escape(description)}</p><span class="skill-entry-count">{count} entries</span></header>'
    overview = header.select_one('.reference-directory-overview-link')
    if overview:
        replacement = replacement.replace('</header>', str(overview) + '</header>')
    content = re.sub(r'<header class="reference-directory-hero[^>]*>.*?</header>', lambda _: replacement, content, count=1, flags=re.S)
    nav = ['<nav class="skill-type-nav" aria-label="Ability categories">', f'<a href="{relative(page, "tensura-reference/skills/")}">All abilities</a>']
    for key, (label, _, _) in CATEGORIES.items():
        current = ' aria-current="page"' if key == category else ''
        nav.append(f'<a href="{relative(page, "tensura-reference/" + key + "/")}"{current}>{label}</a>')
    nav.append('</nav>')
    content = content.replace('</header>', '</header>\n' + ''.join(nav), 1)
    content = content.replace('class="reference-directory"', 'class="reference-directory skill-directory"', 1)
    content = content.replace('Open reference <span', 'View ability <span')
    return f'---\ntitle: {json.dumps(title)}\nhide:\n  - navigation\n  - toc\n---\n\n' + content


def generate_hub(records, policy, directories):
    page = 'tensura-reference/skills/index.md'
    counts = {key: len(BeautifulSoup(directories[f'tensura-reference/{key}/index.md'], 'html.parser').select('.reference-card')) for key in CATEGORIES}
    icons = {}
    for category, (_, _, asset) in CATEGORIES.items():
        if asset.endswith('-'):
            matches = sorted((ROOT / 'docs').glob(asset + '*'))
            if len(matches) != 1:
                raise ValueError(f'Ambiguous category artwork: {category}')
            asset = matches[0].relative_to(ROOT / 'docs').as_posix()
        if not (ROOT / 'docs' / asset).is_file():
            raise ValueError(f'Missing category artwork: {asset}')
        icons[category] = asset
    lookup = {r['local_page']: r for r in records}
    entries = []
    for route, decision in policy['pages'].items():
        if decision['status'] not in {'registered', 'reference'}:
            continue
        record = lookup[route]
        asset = decision.get('asset') or (record.get('_primary_media') or {}).get('local_path', '')
        entries.append({'title': decision['title'], 'route': route.removesuffix('.md') + '/', 'category': decision['category'], 'status': decision['status'], 'image': asset})
    lines = ['---', 'title: Skills & Abilities', 'description: Find abilities, check how to obtain them, and follow documented unlock paths.', 'hide:', '  - navigation', '  - toc', '---', '', '<div class="skill-hub">',
        '<section class="skill-hub-hero"><div><p class="reference-eyebrow">The ability index</p><h1>Skills &amp; <span>abilities.</span></h1><p>Find your next skill. Learn how to obtain it. See what it unlocks.</p><a class="skill-hub-guide" href="../../skills-ep-and-magicules/">Understand EP, mastery &amp; Magicules <span aria-hidden="true">↗</span></a></div>',
        '<aside class="skill-feature"><p class="reference-eyebrow">Follow a mastery path</p><div class="skill-feature-path">',
        '<a href="../../mysticism-reference/skills/extra/ice-manipulation/"><img src="../../assets/upstream/mysticism/skills/ice-manipulation-50c941825a.png" alt=""><strong>Ice Manipulation</strong></a><span aria-hidden="true">→</span><a href="../../mysticism-reference/skills/extra/ice-domination/"><img src="../../assets/upstream/mysticism/skills/ice-domination-cb1ae5000d.png" alt=""><strong>Ice Domination</strong></a>',
        '</div><p>Mastery is one step. Open the next skill to check every acquisition requirement.</p></aside></section>',
        '<section class="skill-finder" aria-labelledby="skill-finder-title"><h2 id="skill-finder-title">Find an ability</h2><label for="skill-hub-search">Search across all skill types</label><div class="skill-finder-input"><input id="skill-hub-search" type="search" autocomplete="off" placeholder="Try Great Sage, Ice Domination, Energy Charge…"><button type="button" data-clear-skill-search>Clear</button></div><p class="skill-finder-status" role="status">Search skills and Battlewill from the unified catalogue. Browse Magic and Resistances below.</p><div class="skill-finder-results" hidden></div><noscript><p>Use the category links below to browse without JavaScript.</p></noscript></section>',
        '<div class="skill-hub-section-heading"><h2>Browse by type</h2><p>One catalogue. Every source kept in context.</p></div><div class="skill-category-grid">']
    for category, (label, description, _) in CATEGORIES.items():
        lines.append(f'<a class="skill-category-tile" href="{relative(page, "tensura-reference/" + category + "/")}"><img src="{relative(page, icons[category])}" alt="" loading="lazy"><span class="skill-category-count">{counts[category]} entries</span><h3>{label}</h3><p>{description}</p><span class="skill-category-open">Browse {label.lower()} <span aria-hidden="true">↗</span></span></a>')
    lines.extend(['</div>', '<section class="skill-reading-guide"><div><span>01</span><h3>Check how to obtain it</h3><p>A cost is not an unlock method. Look for the route, prerequisites, and build-specific conditions.</p></div><div><span>02</span><h3>Read the active modes</h3><p>Separate passives, toggles and active effects before planning how to use a skill.</p></div><div><span>03</span><h3>Follow the next unlock</h3><p>Use the progression cards to explore mastery, combination and awakening connections.</p></div></section>',
        '<details class="skill-coverage"><summary>Build coverage &amp; source notes</summary><p>The directories combine recorded pack entries with Nightmares’ 1.21.1 reference build. Nightmares entries retain <strong>Server build match pending</strong> until the installed release and configuration are confirmed. Historical and explicitly non-gameplay entries are excluded from current skill directories. A race-granted skill can still be Extra-class: obtainment does not change its type.</p><p>Source-described obtainment is distinguished from pinned-build checks, partial prerequisites and unknown methods. A registry entry does not prove a normal gameplay unlock. <a href="../../project/sources-and-attribution/">Browse the source directory</a>.</p></details>',
        '<details class="reference-media-credits"><summary>Ability index image credits</summary><ul>'])
    media = {r['local_path']: r for source in ('tensura', 'mysticism') for r in json.loads((ROOT / f'data/upstream_{source}_media.json').read_text(encoding='utf-8'))['media'] if r.get('local_path')}
    for asset in list(icons.values()) + ['assets/upstream/mysticism/skills/ice-manipulation-50c941825a.png', 'assets/upstream/mysticism/skills/ice-domination-cb1ae5000d.png']:
        if asset in media:
            credit = media[asset]
            lines.append(f'<li><a href="{html.escape(credit["source_file_page"], quote=True)}">{html.escape(credit["source_title"])}</a> · {html.escape(credit["license"])}</li>')
    lines.extend(['<li>Energy Charge and The Timeless Mage: <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-ascensions">Tensura: Ascension</a>.</li></ul></details>', '</div>', ''])
    return {page: '\n'.join(lines), 'assets/data/skill-search.json': json.dumps(sorted(entries, key=lambda e: e['title'].casefold()), ensure_ascii=False, separators=(',', ':')) + '\n'}
