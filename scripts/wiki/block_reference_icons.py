"""Generate compact, code-native symbols for implementation-only block records."""
from __future__ import annotations

import argparse
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "docs/assets/icons/blocks"

ICONS = {
    "mysticism-elemental-realm-portal": ("Elemental Realm Portal", "#74ddec", '<ellipse cx="48" cy="48" rx="25" ry="32"/><ellipse cx="48" cy="48" rx="14" ry="23"/><path d="M48 16v64M23 48h50M29 29l38 38M67 29 29 67"/>'),
    "nightmares-cadence-acceleration-glass": ("Cadence Acceleration Glass", "#d0aeff", '<rect x="19" y="19" width="58" height="58" rx="5"/><path d="M19 38h58M19 58h58M38 19v58M58 19v58M48 28v20l14 8"/><circle cx="48" cy="48" r="25"/>'),
    "nightmares-domicile-door": ("Domicile Door", "#f3d397", '<path d="M25 78V25q0-7 7-7h32q7 0 7 7v53ZM34 78V29h28v49"/><circle cx="56" cy="53" r="2.5"/><path d="M18 78h60M40 18v-7h16v7"/>'),
    "nightmares-domicile-trapdoor": ("Domicile Trapdoor", "#f3d397", '<path d="m20 35 28-17 28 17-28 17Zm0 0v29l28 17V52m28-17v29L48 81"/><path d="M30 40v21l18 11M66 40v21L48 72"/><circle cx="48" cy="45" r="2.5"/>'),
    "nightmares-gabriel-snow-crystal": ("Gabriel Snow Crystal", "#8be5ff", '<path d="M48 15v66M20 32l56 32M20 64l56-32M37 21l11 10 11-10M37 75l11-10 11 10M22 46l15-2-2-14M74 50l-15 2 2 14"/><path d="m48 32 14 8v16l-14 8-14-8V40Z"/>'),
    "nightmares-stasis-lattice": ("Stasis Lattice", "#aeb8ff", '<path d="M18 22h60v52H18Z M18 39h60M18 57h60M38 22v52M58 22v52"/><circle cx="48" cy="48" r="17"/><path d="M48 38v20M38 48h20"/>'),
}


def render(title: str, color: str, glyph: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" role="img"><title>{html.escape(title)} symbol</title><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0b172a"/><stop offset="1" stop-color="#111b38"/></linearGradient></defs><rect x="1" y="1" width="94" height="94" rx="18" fill="url(#g)" stroke="{color}" stroke-opacity=".45"/><g fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{glyph}</g></svg>\n'


def generate() -> dict[Path, str]:
    return {OUTPUT / f"{name}.svg": render(*spec) for name, spec in ICONS.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, content in generate().items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale block symbol: {path.relative_to(ROOT)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f'Block symbols {"checked" if args.check else "generated"}: {len(ICONS)}')


if __name__ == "__main__":
    main()
