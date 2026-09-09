"""Keep unverified race imports out of current recommendations and search."""
from __future__ import annotations

import argparse
import html
import posixpath
import re
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
from race_catalogue import race_reference

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'
BEGIN, END = '<!-- race-reference:start -->', '<!-- race-reference:end -->'


def generate():
    policy = race_reference()
    outputs = {}
    for page, decision in policy['pages'].items():
        text = (DOCS / page).read_text(encoding='utf-8')
        text = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END) + r'\s*', '', text, flags=re.S)
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
            for card in soup.select('.reference-related-card[href]'):
                link = urlsplit(card['href'])
                if link.scheme or link.netloc:
                    continue
                destination = posixpath.normpath(posixpath.join(page.removesuffix('.md') + '/', link.path)).rstrip('/') + '.md'
                if policy['pages'].get(destination, {}).get('status', 'registered') != 'registered':
                    card.decompose()
            return re.sub(r'\n[ \t]*\n+', '\n', str(soup)) if soup.select('.reference-related-card') else ''
        text = re.sub(r'<section class="reference-related">.*?</section>', related, text, flags=re.S)
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
