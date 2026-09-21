"""Keep unverified race imports out of current recommendations and search."""
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from race_catalogue import family_partition, race_reference

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'
BEGIN, END = '<!-- race-reference:start -->', '<!-- race-reference:end -->'
UNAVAILABLE_BEGIN, UNAVAILABLE_END = '<!-- race-unavailable:start -->', '<!-- race-unavailable:end -->'
MAINTENANCE_BLOCK = re.compile(r'<div>\s*<table\b.*?</table>\s*</div>\s*', re.I | re.S)
MAINTENANCE_CREDIT = re.compile(
    r'(?im)^<li><a\b[^>]*File:(?:Mysticism_WIP|Placeholder)\.png[^>]*>.*?</li>\s*\r?\n?'
)

HISTORICAL_MEDIA = (
    (('spider', 'silk-soul'), 'assets/upstream/tensura/mobs/black-spider-yellow-c2fa32a0c0.gif'),
    (('wasp',), 'assets/upstream/tensura/mobs/army-wasp-751af321e0.gif'),
    (('centipede',), 'assets/upstream/tensura/mobs/evil-centipede-2bc8cccc6a.png'),
    (('scorpion',), 'assets/images/races/scorpion.webp'),
    (('mantis',), 'assets/images/races/mantis.webp'),
    (('beetle',), 'assets/images/races/beetle.webp'),
    (('ant', 'hardshell'), 'assets/upstream/tensura/mobs/giant-ant-4e3b228173.gif'),
    (('wolf', 'fang'), 'assets/upstream/mysticism/races/direwolf-9251a4c081.jpg'),
    (('dryad', 'foliaris', 'pixie', 'verdant'), 'assets/upstream/mysticism/races/fairy-b898cd83c7.jpg'),
    (('fallen',), 'assets/upstream/mysticism/races/fallenangel-f6645f3aed.jpg'),
    (('loong', 'wyrm', 'dragon'), 'assets/upstream/mysticism/races/attuneddragon-e7451a91d7.jpg'),
)


def relative(page: str, asset: str) -> str:
    rendered_route = page[:-8] if page.endswith('index.md') else page[:-3] + '/'
    return posixpath.relpath(asset, rendered_route)


def strip_maintenance_markup(text: str) -> str:
    """Remove imported source-wiki editing notices from player-facing pages."""
    text = MAINTENANCE_BLOCK.sub(
        lambda match: '' if 'work in progress' in BeautifulSoup(match.group(0), 'html.parser').get_text(' ', strip=True).casefold() else match.group(0),
        text,
    )
    text = re.sub(r'(?m)^- Work_in_Progress\s*\r?\n', '', text)
    text = re.sub(r'<p>\s*(?:Actually\s+)?WIP\s*</p>\s*', '', text, flags=re.I | re.S)
    text = re.sub(r'(?im)^\s*WIP\s*\r?\n?', '', text)
    text = text.replace('(Remove this once finalized)', '')
    text = MAINTENANCE_CREDIT.sub('', text)
    text = re.sub(r'(?m)^description:[ \t]+tags:', "description: ''\ntags:", text)
    text = re.sub(r'(?m)^(description:[ \t]*[\'\"])[ \t]+', r'\1', text)
    text = re.sub(r'(?m)^description:(?![ \t])', 'description: ', text)
    text = re.sub(r'<small>\s*</small>', '', text)

    def tidy_credits(match: re.Match[str]) -> str:
        block = match.group(0)
        count = len(re.findall(r'<li\b', block, flags=re.I))
        if not count:
            return ''
        noun = 'file' if count == 1 else 'files'
        return re.sub(r'Media credits \(\d+ source files?\)', f'Media credits ({count} source {noun})', block)

    return re.sub(r'<details class="reference-media-credits">.*?</details>', tidy_credits, text, flags=re.I | re.S)


def family_media(page: str, media_overrides: dict[str, str]) -> str | None:
    family = family_partition(page)
    if family and family in media_overrides:
        return media_overrides[family]
    slug = Path(page).stem.casefold()
    return next((asset for terms, asset in HISTORICAL_MEDIA if any(term in slug for term in terms)), None)


def normalize_known_skill_links(text: str, page: str) -> str:
    target = relative(page, 'tensura-reference/skills/extra/analytical-appraisal/').rstrip('/') + '/'
    return re.sub(
        r'<a\b[^>]*href="(?:https://(?:tensura|tensurareincarnated)\.wiki\.gg/wiki/Analytical_Appraisal(?:Analytical)?|(?:\.\./)+tensura-reference/skills/extra/analytical-appraisal/?)"[^>]*>.*?</a>',
        f'<a href="{target}" title="Analytical Appraisal">Analytical Appraisal</a>',
        text,
        flags=re.I | re.S,
    )


def replace_placeholder_figure(text: str, page: str, decision: dict, asset: str, credits: dict[str, dict]) -> str:
    if asset in credits:
        credit = credits[asset]
        caption = f'<a href="{html.escape(credit["source_file_page"], quote=True)}">{html.escape(credit["source_title"])} · {html.escape(credit["license"])}</a>'
        source_class = ' reference-overview-media--source'
    else:
        caption = 'Original TSR family illustration'
        source_class = ''
    figure = (
        f'<figure class="reference-overview-media{source_class}">\n'
        f'<img src="{relative(page, asset)}" alt="{html.escape(decision["title"])} family reference artwork" loading="eager" decoding="async">\n'
        f'<figcaption>{caption}</figcaption>\n'
        '</figure>'
    )
    return re.sub(
        r'<figure class="reference-overview-media[^>]*>.*?(?:wip|placeholder|family reference artwork|Original TSR family illustration).*?</figure>',
        lambda _match: figure,
        text,
        count=1,
        flags=re.I | re.S,
    )


def mark_unavailable_links(text: str, page: str, policy: dict) -> str:
    """Keep historical names readable without presenting them as usable routes."""
    marked = 'reference-unavailable-link' in text

    def replace(match: re.Match[str]) -> str:
        nonlocal marked
        parsed = urlsplit(match.group(1))
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        destination = posixpath.normpath(
            posixpath.join(page.removesuffix('.md') + '/', unquote(parsed.path))
        ).rstrip('/') + '.md'
        decision = policy['pages'].get(destination)
        if not decision or decision.get('status') == 'registered':
            return match.group(0)
        marked = True
        label = BeautifulSoup(match.group(0), 'html.parser').get_text(' ', strip=True)
        return (
            f'<span class="reference-unavailable-link" title="Not registered in the recorded Minecraft 1.21.1 build">'
            f'{html.escape(label)} <small>not in recorded 1.21.1 build</small></span>'
        )

    text = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>.*?</a>', replace, text, flags=re.I | re.S)
    if not marked:
        return text
    note = (
        f'{UNAVAILABLE_BEGIN}\n'
        '<aside class="skill-evidence-note"><strong>1.21.1 route notice:</strong> '
        'This source article names one or more evolution routes that are not registered in the recorded 1.21.1 build. '
        'Those names are marked below and are excluded from the current family map.</aside>\n'
        f'{UNAVAILABLE_END}'
    )
    return re.sub(r'</section>', '</section>\n\n' + note, text, count=1)


def generate():
    policy = race_reference()
    media_overrides = json.loads((ROOT / 'data/race_family_media.json').read_text(encoding='utf-8'))
    media_credits = {
        item['local_path']: item
        for source in ('tensura', 'mysticism')
        for item in json.loads((ROOT / f'data/upstream_{source}_media.json').read_text(encoding='utf-8'))['media']
        if item.get('local_path')
    }
    outputs = {}
    for page, decision in policy['pages'].items():
        text = (DOCS / page).read_text(encoding='utf-8')
        text = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END) + r'\s*', '', text, flags=re.S)
        text = re.sub(re.escape(UNAVAILABLE_BEGIN) + r'.*?' + re.escape(UNAVAILABLE_END) + r'\s*', '', text, flags=re.S)
        text = strip_maintenance_markup(text)
        text = normalize_known_skill_links(text, page)
        asset = family_media(page, media_overrides)
        if asset:
            text = replace_placeholder_figure(text, page, decision, asset, media_credits)
        if decision['status'] != 'registered':
            front, rest = text[4:].split('\n---\n', 1)
            if not re.search(r'^search:', front, re.M):
                front += '\nsearch:\n  exclude: true'
            text = '---\n' + front + '\n---\n' + rest
            build = policy['builds'][decision['source']]
            if decision['status'] == 'guide':
                note = 'This source page is an overview, not an individual race or evolution stage.'
            elif decision['status'] == 'incomplete':
                note = 'This registered template lacks a verified standalone progression guide. It is not presented as a selectable starting race or an independent evolution family.'
            else:
                note = f'This article has not been matched to a registered race in the recorded {html.escape(decision["source"].title())} {html.escape(build["version"])} build for Minecraft 1.21.1. It may describe an older name or unavailable content. It is excluded from current race families and progression; do not use its stats or requirements as current TSR guidance.'
            target = posixpath.relpath('tensura-reference/races/', page.removesuffix('.md') + '/') + '/'
            panel = f'{BEGIN}\n<section class="skill-availability skill-availability--historical"><h2>Reference status</h2><p>{note}</p><p><a href="{target}">Browse current race families</a> · <a href="{build["source_url"]}">Recorded release</a></p></section>\n{END}\n\n'
            marker = '<section class="reference-overview '
            index = text.find(marker)
            if index < 0:
                raise ValueError(f'Missing race overview: {page}')
            text = text[:index] + panel + text[index:]

        def related(match):
            soup = BeautifulSoup(match[0], 'html.parser')
            current_family = family_partition(page)
            for card in soup.select('.reference-related-card[href]'):
                link = urlsplit(card['href'])
                if link.scheme or link.netloc:
                    continue
                destination = posixpath.normpath(posixpath.join(page.removesuffix('.md') + '/', link.path)).rstrip('/') + '.md'
                destination_family = family_partition(destination)
                if (
                    decision['status'] != 'registered'
                    or policy['pages'].get(destination, {}).get('status', 'registered') != 'registered'
                    or destination_family != current_family
                ):
                    card.decompose()
                    continue
                related_asset = family_media(destination, media_overrides)
                image = card.select_one('img')
                if related_asset and image:
                    image['src'] = relative(page, related_asset)
                    image['alt'] = ''
            return re.sub(r'\n[ \t]*\n+', '\n', str(soup)) if soup.select('.reference-related-card') else ''
        text = re.sub(r'<section class="reference-related">.*?</section>', related, text, flags=re.S)
        if decision['status'] == 'registered':
            text = mark_unavailable_links(text, page, policy)
        text = re.sub(r'[ \t]+(?=\r?$)', '', text, flags=re.M)
        text = text.rstrip() + '\n'
        outputs[page] = text
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for page, text in generate().items():
        destination = DOCS / page
        if args.check:
            if destination.read_text(encoding='utf-8') != text:
                raise SystemExit(f'Stale race reference status: {page}')
        else:
            destination.write_text(text, encoding='utf-8', newline='\n')
    print('Race reference status and related-card checks passed')


if __name__ == '__main__':
    main()
