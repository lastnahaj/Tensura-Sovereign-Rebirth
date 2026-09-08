"""Build version-scoped skill directories and consistent acquisition summaries."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import tomllib
from urllib.parse import unquote, urlsplit, urlunsplit

from bs4 import BeautifulSoup

from skill_catalogue import ROOT, POOL, ACTIVE, catalogue

DOCS = ROOT / "docs"
BEGIN, END = "<!-- skill-catalogue:start -->", "<!-- skill-catalogue:end -->"
LABELS = {"skills/common": "Common Skills", "skills/extra": "Extra Skills", "skills/intrinsic": "Intrinsic Skills", "skills/unique": "Unique Skills", "skills/ultimate": "Ultimate Skills", "skills/other": "Other Skills", "magic": "Magic", "battlewill": "Battlewill", "resistances": "Resistances"}


def pinned_learning_requirement(page, decision):
    identifier = decision.get("id", "")
    if identifier in {"mysticism:ice_domination", "mysticism:light_domination", "mysticism:darkness_domination"}:
        element = identifier.split(":")[1].split("_")[0]
        config = tomllib.loads((ROOT / "pack/config/mysticism/ability/skill/extra_config.toml").read_text(encoding="utf-8"))
        threshold = config[element.title() + "Manipulation"]["dominationEpAcquirement"]
        title = element.title() + " Manipulation"
        url = relative(page, "mysticism-reference/skills/extra/" + element + "-manipulation/") + "/"
        return f'<p><strong>Pinned build learning requirements:</strong> Fully master <a href="{url}">{title}</a> and exceed <strong>{threshold:,.0f} EP</strong>. The implementation uses a strict greater-than check; exactly {threshold:,.0f} EP is not enough.</p><p class="skill-evidence-note">These are the skill’s acquisition checks, not a promise of an automatic grant. They supersede the older upstream EP threshold. See the <a href="https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/pack/config/mysticism/ability/skill/extra_config.toml">pinned configuration</a> and <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529">Mysticism 2.1.2</a>.</p>'
    if identifier == "mysticism:melancholy":
        thrower = relative(page, "tensura-reference/skills/unique/thrower/") + "/"
        molecular = relative(page, "tensura-reference/skills/extra/molecular-manipulation/") + "/"
        return f'<p><strong>Pinned build learning requirements:</strong> Fully master both <a href="{thrower}">Thrower</a> and <a href="{molecular}">Molecular Manipulation</a>. The acquisition check requires both skills; it does not establish an automatic grant.</p><p class="skill-evidence-note">Checked against <a href="https://www.curseforge.com/minecraft/mc-mods/tensura-mysticism/files/8379529">Mysticism 2.1.2</a>. That implementation also sets Melancholy’s maximum mastery to <strong>1,500</strong>, replacing the older upstream value of 1,000.</p>'
    return ""


def route(page):
    return page[:-8] if page.endswith("index.md") else page[:-3] + "/"


def relative(page, destination):
    return posixpath.relpath(destination, route(page))


def render_acquisition_markdown(content, page):
    """Raw HTML links need rendered routes; MkDocs cannot rewrite them later."""
    import markdown
    soup = BeautifulSoup(markdown.markdown(content), "html.parser")
    for anchor in soup.select("a[href]"):
        url = urlsplit(anchor["href"])
        if not url.scheme and not url.netloc and url.path.endswith(".md"):
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(page), url.path))
            target = relative(page, route(destination)) + "/"
            anchor["href"] = urlunsplit(("", "", target, url.query, url.fragment))
    return str(soup)


def localize_skill_links(text, page, policy, records):
    """Keep reading links local and recommendations limited to current entries."""
    hosts = {"tensura.wiki.gg", "tensurareincarnated.wiki.gg", "trmysticism.wiki.gg", "tensuranightmares.wiki.gg"}
    sources = {unquote(r["source_url"]).replace("_", " "): r["local_page"] for r in records if urlsplit(r.get("source_url", "")).netloc in hosts}
    for record in records:
        if urlsplit(record.get("source_url", "")).netloc in {"tensura.wiki.gg", "tensurareincarnated.wiki.gg"}:
            for host in ("tensura.wiki.gg", "tensurareincarnated.wiki.gg"):
                sources[f'https://{host}/wiki/{record["source_title"]}'.replace("_", " ")] = record["local_page"]
    def rewrite(match):
        url = urlsplit(html.unescape(match[1]))
        if url.query:
            return match[0]
        key = unquote(urlunsplit((url.scheme, url.netloc, url.path, "", ""))).replace("_", " ")
        destination = sources.get(key)
        if not destination:
            return match[0]
        return 'href="' + html.escape(relative(page, route(destination)) + "/" + ("#" + url.fragment if url.fragment else ""), quote=True) + '"'
    # Attribution links always retain the upstream destination.
    body, separator, credits = text.partition("\n## Source and licensing")
    body = re.sub(r'href="([^"]+)"', rewrite, body)
    def related(match):
        soup = BeautifulSoup(match[0], "html.parser")
        browse = soup.select_one(".reference-related-heading a")
        if browse:
            browse["href"] = relative(page, "tensura-reference/" + policy["pages"][page]["category"] + "/") + "/"
            browse.string = "Browse all " + LABELS[policy["pages"][page]["category"]]
        for anchor in soup.select("a.reference-related-card[href]"):
            url = urlsplit(anchor["href"])
            target = posixpath.normpath(posixpath.join(route(page), url.path)).rstrip("/") + ".md"
            decision = policy["pages"].get(target)
            if decision and decision["status"] not in ACTIVE:
                anchor.decompose()
            elif decision and decision["namespace"] == "mysticism":
                preview = anchor.find("img")
                if preview:
                    preview["src"] = relative(page, "assets/icons/skills/" + decision["id"].replace(":", "-") + ".svg")
        if not soup.select("a.reference-related-card"):
            return ""
        return re.sub(r"\n[ \t]*\n+", "\n", str(soup))
    body = re.sub(r'<section class="reference-related">.*?</section>', related, body, flags=re.S)
    return body + separator + credits


def icon(identifier, title=""):
    """Small, code-native emblems with a subject glyph and distinct constellation."""
    if identifier.startswith("trnightmare:"):
        from nightmares_skill_icons import icon as nightmares_icon
        return nightmares_icon(identifier, title)
    name = identifier.split(":")[-1]
    color = "#52d5ef"
    glyph = '<path d="M48 21 66 39 48 75 30 39Z M30 39h36 M48 21v54"/>'
    if any(word in name for word in ("lightning", "spark", "discharge", "dissonance", "zekrom", "paralysis")):
        color = "#ffd36b"; glyph = '<path d="m54 17-26 35h18l-5 27 28-39H51Z"/>'
    elif any(word in name for word in ("ice", "cryogenic", "kyurem")):
        glyph = '<path d="M48 19v58M23 34l50 28M23 62l50-28M38 25l10 9 10-9M38 71l10-9 10 9M25 44l12-1-1-12M71 52l-12 1 1 12"/>'
    elif any(word in name for word in ("poison", "corro", "toxic", "lethal")):
        color = "#a4e16e"; glyph = '<path d="M38 22h20M42 22v23L28 68q-3 7 7 7h26q10 0 7-7L54 45V22M35 57h26"/><circle cx="44" cy="63" r="2"/><circle cx="54" cy="68" r="2"/>'
    elif any(word in name for word in ("gravity", "void", "phaser", "fourth_wall")):
        color = "#b79bff"; glyph = '<ellipse cx="48" cy="48" rx="30" ry="12" transform="rotate(-30 48 48)"/><ellipse cx="48" cy="48" rx="30" ry="12" transform="rotate(30 48 48)"/><circle cx="48" cy="48" r="8"/>'
    elif any(word in name for word in ("butcher", "blood", "crasher")):
        color = "#ff9bab"; glyph = '<path d="M48 19C39 33 27 43 27 56a21 21 0 0 0 42 0C69 43 57 33 48 19Z M36 56q0 13 12 13"/>'
    elif any(word in name for word in ("gardener", "cultivator", "provider")):
        color = "#9de7b7"; glyph = '<path d="M29 68C18 42 36 23 70 23c0 35-17 50-41 45Zm0 0 33-35M42 55V38M42 55h18"/>'
    elif any(word in name for word in ("dreamer", "schrodinger", "melancholy", "hidden")):
        color = "#a9baff"; glyph = '<path d="M22 48q26-31 52 0-26 31-52 0Z"/><circle cx="48" cy="48" r="10"/><path d="M48 38v20"/>'
    elif "darkness" in name:
        color = "#b79bff"; glyph = '<path d="M58 20a29 29 0 1 0 16 45C42 77 28 40 58 20Z"/>'
    elif name.startswith("light_"):
        color = "#ffe5a0"; glyph = '<circle cx="48" cy="48" r="15"/><path d="M48 18v9M48 69v9M18 48h9M69 48h9M27 27l7 7M62 62l7 7M27 69l7-7M62 34l7-7"/>'
    elif any(word in name for word in ("hell", "reshiram", "profaned")):
        color = "#ffd48e"; glyph = '<path d="M50 19c8 23-8 26-1 36 3-8 11-12 13-18 20 34-5 47-21 38-22-12-7-36 9-56Z"/>'
    elif any(word in name for word in ("exoskeleton", "mithril", "magisteel", "tenacity", "constant", "restricted")):
        color = "#b6dce8"; glyph = '<path d="m48 19 25 10-4 28q-5 14-21 22-16-8-21-22l-4-28Z M48 28v38M35 45h26"/>'
    elif any(word in name for word in ("soul", "spiritual", "relapse")):
        color = "#9ef5e6"; glyph = '<path d="M48 20c-22 12-25 31-16 47l10-8 6 15 6-15 10 8c9-16 6-35-16-47Z"/><circle cx="41" cy="44" r="2"/><circle cx="55" cy="44" r="2"/>'
    elif "scholar" in name:
        glyph = '<path d="M48 30q-13-10-28-6v45q15-4 28 6 13-10 28-6V24q-15-4-28 6Zm0 0v45M28 36l12 4M28 46l12 4M56 40l12-4M56 50l12-4"/>'
    elif "engineer" in name:
        glyph = '<path d="m39 20-3 11-11 3-7 14 8 9v14l14 7 9-8 14 1 10-12-5-11 4-13-13-11-11 5Z"/><circle cx="47" cy="49" r="12"/>'
    elif "malleable" in name:
        color = "#efbd9b"; glyph = '<path d="M29 28h38l-5 13q13 28-4 34H38q-17-6-4-34Zm5 13h28M29 61h38M38 75l4-27M58 75l-4-27"/>'
    elif "stagnator" in name:
        color = "#b79bff"; glyph = '<circle cx="48" cy="48" r="28"/><path d="M48 20v8M48 68v8M20 48h8M68 48h8M42 34v28M54 34v28"/>'
    elif any(word in name for word in ("subjugator", "victorious")):
        color = "#ffd36b"; glyph = '<path d="m22 32 14 12 12-23 12 23 14-12-8 35H30Zm8 43h36M48 49v10"/>'
    elif "repeater" in name:
        glyph = '<path d="M22 40a28 28 0 0 1 49-10l4 9H59M74 56a28 28 0 0 1-49 10l-4-9h16M75 39V23M21 57v16"/>'
    elif "reducer" in name:
        glyph = '<path d="M22 22h15M22 22v15M74 22H59M74 22v15M22 74h15M22 74V59M74 74H59M74 74V59M24 24l16 16M72 24 56 40M24 72l16-16M72 72 56 56"/>'
    elif "coalescence" in name:
        glyph = '<circle cx="37" cy="48" r="21"/><circle cx="59" cy="48" r="21"/><path d="M48 30v36"/>'
    elif "captivator" in name:
        color = "#ff9bab"; glyph = '<path d="M27 24v30a21 21 0 0 0 42 0V24H56v30a8 8 0 0 1-16 0V24Zm0 15h13M56 39h13"/>'
    elif "bullet_punch" in name:
        glyph = '<path d="M34 64V35q0-7 7-7h7q7 0 7 7v10h9q7 0 7 7v12l-9 12H43Zm10-20V26M55 45v10M22 32h-7M24 46H12M24 60h-9"/>'
    if name.endswith("_domination"):
        glyph = '<g transform="translate(12 10) scale(.75)">' + glyph + '</g><path d="m30 73 10 7 8-13 8 13 10-7-3 15H33Z" stroke="#ffd36b" fill="#0b172a"/>'
    digest = hashlib.sha256(identifier.encode()).digest()
    dots = "".join(f'<circle cx="{20 + digest[i] % 58}" cy="{12 if i % 2 else 84}" r="1.5" fill="{color}" stroke="none"/>' for i in range(4))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" role="img"><title>{html.escape(name.replace("_", " ").title())} emblem</title><rect x="1" y="1" width="94" height="94" rx="20" fill="#0b172a" stroke="{color}" stroke-opacity=".35"/><g fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{glyph}{dots}</g></svg>\n'


def acquisition(text, page, decision):
    requirement = pinned_learning_requirement(page, decision)
    if requirement:
        return requirement, True
    soup = BeautifulSoup(text, "html.parser")
    items = []
    for row in soup.select('.druid-row[data-druid-section-row="Obtaining"]'):
        label, value = row.select_one(".druid-label"), row.select_one(".druid-data")
        if not label or not value:
            continue
        clean = value.get_text(" ", strip=True)
        if clean in {"", "None", "NA", "N/A", "[[]]"}:
            continue
        caption = label.get_text(" ", strip=True)
        prefix = f'<strong>{html.escape(caption)}:</strong> ' if caption else ""
        items.append(f'<li>{prefix}{value.decode_contents()}</li>')
    if items:
        return '<p>Source-described obtainment methods:</p><ul>' + "".join(items) + '</ul><p class="skill-evidence-note">An obtainment method is separate from a skill’s MP cost. Check all conditions; a listed route is not a guaranteed starting roll.</p>', True
    if decision["namespace"] == "ascension" and decision["category"] == "skills/ultimate":
        previous = re.search(r"\*\*Previous:\*\*\s*(\[[^\]]+\]\([^)]+\))", text)
        gate = re.search(r"\*\*Extra gate:\*\*\s*(.*?)(?:\*\*Previous:|\n)", text)
        if previous:
            content = f"1. Learn and fully master {previous[1]}.\n2. Reach **5,000,000 Max EP** and complete **True Hero** or **True Demon Lord** awakening.\n3. " + (gate[1].strip() if gate else "No additional skill-specific gate is documented.") + "\n4. Complete the [Ultimate Altar ritual](../../../ascension-and-awakening.md#ritual-readiness) with a catalyst and a clear ritual cooldown."
            return render_acquisition_markdown(content, page), True
    if decision.get("id") in {"ascension:angel_wings", "ascension:sharpened_claws"}:
        family = "angel" if decision["id"].endswith("angel_wings") else "kitsune"
        return f'<p>Granted by the <a href="{relative(page, "tensura-reference/races/" + family + "/")}/">{family.title()} race line</a>. This describes the racial grant, not a separate reincarnation chance for the skill.</p>', True
    # Maintained Markdown already supplies explicit obtainment instructions.
    lines = [line.lstrip("- ") for line in text.splitlines() if re.match(r"\s*-?\s*\*\*(?:Obtainment|Obtaining|How to obtain|Requirement|Requirements|Prerequisite|Prerequisites):", line, re.I)]
    if lines:
        return render_acquisition_markdown("\n\n".join(lines), page), True
    # Some source articles describe acquisition under a prose heading.
    for heading in soup.find_all(["h2", "h3"]):
        if not re.fullmatch(r"Obtaining|Obtainment|Acquisition|How to obtain", heading.get_text(" ", strip=True), re.I):
            continue
        parts = []
        for node in heading.next_siblings:
            if getattr(node, "name", None) in {"h2", "h3"}:
                break
            if getattr(node, "name", None) in {"p", "ul", "ol"}:
                parts.append(str(node))
        if parts:
            return "".join(parts), True
    previous = soup.select_one(".druid-row-Previous .druid-data")
    if previous and previous.get_text(" ", strip=True) not in {"", "None", "[[]]"}:
        return '<p><strong>Documented prerequisite:</strong> ' + previous.decode_contents() + '</p><p>The source identifies this prerequisite but does not provide a complete obtainment method. Do not assume mastery alone unlocks the skill.</p>', False
    return '<p>No verified obtainment method is documented for this entry yet. Registration does not establish a reincarnation, mastery, crafting, or reward route.</p>', False


def prepare_page(page, decision, text):
    text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
    label = LABELS[decision["category"]]
    registered = decision["status"] in ACTIVE
    if not registered:
        if text.startswith("---\n") and "search:\n  exclude: true" not in text.split("\n---", 1)[0]:
            text = text.replace("---\n", "---\nsearch:\n  exclude: true\n", 1)
        message = ("This is a guide, not an individual skill." if decision["status"] == "guide" else "This entry is not part of the current registered skill catalogue. Its upstream mechanics are historical reference, not an available TSR progression path.")
        section = f'<aside class="skill-availability skill-availability--historical"><h2>Reference status</h2><p>{message}</p><a href="{relative(page, "tensura-reference/skills/")}/">Browse current skills →</a></aside>'
        documented = False
    else:
        obtain, documented = acquisition(text, page, decision)
        evidence = "Pinned pack inventory"
        notice = ""
        if decision["status"] == "reference":
            reference = decision["reference_build"]
            evidence = "1.21.1 reference build"
            notice = f'<p class="skill-evidence-note"><strong>Server build match pending.</strong> Reference: <a href="{reference["source_url"]}">Nightmares {reference["version"]}</a>.</p><details class="skill-source-limits"><summary>Version and source limits</summary><p>This skill is registered in the reference release. The installed version and server configuration have not yet been matched. Requirements and effects describe the cited wiki revision, not verified server behavior.</p>'
            if decision.get("source_partial"):
                notice += '<p class="skill-evidence-note">The upstream article is incomplete; missing effects or unlock conditions are not assumed.</p>'
            notice += '</details>'
        section = f'<section class="skill-obtainment" aria-labelledby="how-to-obtain"><p class="reference-eyebrow">{html.escape(label)} · {evidence}</p><h2 id="how-to-obtain">How to obtain</h2>{notice}{obtain}</section>'
        if not decision.get("maintained"):
            browse = relative(page, "tensura-reference/" + decision["category"] + "/") + "/"
            section = f'<nav class="skill-category-nav" aria-label="Skill directory"><a href="{browse}">← Browse {html.escape(label)}</a></nav>\n' + section
        text = re.sub(r'(<span class="reference-category">)[^<]*(</span>)', lambda m: m[1] + label + m[2], text)
        if decision["category"].startswith("skills/"):
            text = re.sub(r'(<div class="druid-data druid-data-Type[^>]*>).*?(</div>)', lambda m: m[1] + label.removesuffix("s") + m[2], text, count=1, flags=re.S)
        # Apply verified learning corrections to the infobox consumed by the graph.
        requirement = pinned_learning_requirement(page, decision)
        if requirement:
            soup = BeautifulSoup(requirement, "html.parser")
            first = soup.find("p").decode_contents()
            text = re.sub(r'(<div class="druid-data druid-data-Previous[^>]*>).*?(</div>)', lambda m: m[1] + first + m[2], text, count=1, flags=re.S)
        if decision.get("id") == "mysticism:melancholy":
            text = re.sub(r'(<div class="druid-data druid-data-PointstoMaster[^>]*>).*?(</div>)', lambda m: m[1] + "1,500" + m[2], text, count=1, flags=re.S)
        if decision.get("maintained"):
            text = re.sub(r'(<p class="reference-eyebrow">)[^<]*(</p>)', lambda m: m[1] + label + m[2], text, count=1)
            text = re.sub(r'\[Browse [^\]]+\]\([^)]*\)', f'[Browse {label}]({posixpath.relpath("tensura-reference/" + decision["category"] + "/index.md", posixpath.dirname(page))})', text, count=1)
    if registered and not decision.get("maintained") and '<a href="#how-to-obtain">How to obtain</a>' not in text:
        if '<nav class="reference-quick-jumps"' in text:
            text = re.sub(r'(<nav class="reference-quick-jumps"[^>]*>)', r'\1\n<a href="#how-to-obtain">How to obtain</a>', text, count=1)
        else:
            text = text.replace('<div class="reference-reading-controls"', '<nav class="reference-quick-jumps" aria-label="Article sections"><a href="#how-to-obtain">How to obtain</a></nav>\n<div class="reference-reading-controls"', 1)
    marker = '<div class="maintained-skill-article"' if decision.get("maintained") else ('<div class="tensura-reference-article">' if registered else '<section class="reference-overview ')
    offset = text.find(marker)
    if offset < 0:
        raise ValueError(f"Missing article insertion target: {page}")
    section = "\n".join(line.rstrip() for line in section.splitlines())
    text = text[:offset] + BEGIN + "\n" + section + "\n" + END + "\n\n" + text[offset:]
    # Remove editorial instructions from player-facing summaries.
    text = text.replace("(Remove this once finalized)", "")
    text = re.sub(r"(?<=>)[ \t]+$", "", text, flags=re.M)
    return text, documented


def generate():
    from sync_tensura_wiki import configure_source, load_reference_snapshot, supplementary_records, generate_category_index
    policy = catalogue()
    configure_source("tensura")
    records = []
    for source in ("tensura", "mysticism"):
        records.extend(load_reference_snapshot(source)[0])
    records.extend(supplementary_records())
    outputs = {}
    previous_path = DOCS / "assets/data/skill-catalogue.json"
    if previous_path.exists():
        previous = json.loads(previous_path.read_text(encoding="utf-8"))["pages"]
        for page in previous.keys() - policy["pages"].keys():
            text = (DOCS / page).read_text(encoding="utf-8")
            text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
            category = "Magic" if "/magic/" in page else "Core Mechanics"
            outputs[page] = re.sub(r'(<span class="reference-category">)[^<]*(</span>)', lambda m: m[1] + category + m[2], text)
    for page, decision in policy["pages"].items():
        original = localize_skill_links((DOCS / page).read_text(encoding="utf-8"), page, policy, records)
        text, documented = prepare_page(page, decision, original)
        decision["obtainment_documented"] = documented
        if decision["namespace"] in {"mysticism", "trnightmare"} and decision["status"] in ACTIVE:
            asset = "assets/icons/skills/" + decision["id"].replace(":", "-") + ".svg"
            outputs[asset] = icon(decision["id"], decision["title"])
            decision["asset"] = asset
            # Replace the preview, including its credit: these are TSR emblems.
            text = re.sub(r'(<figure class="reference-overview-media[^>]*>).*?(</figure>)', lambda m: m[1] + f'<img src="{relative(page, asset)}" alt="{html.escape(decision["title"])} emblem" width="96" height="96"><figcaption>TSR skill emblem</figcaption>' + m[2], text, count=1, flags=re.S)
            text = re.sub(r'<img\b[^>]*src="[^"]*(?:wip|placeholder)[^"]*"[^>]*>', "", text, flags=re.I)
        outputs[page] = text
    active = []
    seen = set()
    for record in records:
        if record["local_page"] in outputs:
            record = {**record, "_html": outputs[record["local_page"]]}
        decision = policy["pages"].get(record["local_page"])
        if decision:
            if decision["status"] not in ACTIVE or decision["id"] in seen:
                continue
            seen.add(decision["id"])
            record = {**record, "category": decision["category"], "registry_id": decision["id"]}
            record["reference_build_only"] = decision["status"] == "reference"
            if decision.get("asset"):
                record["_primary_media"] = {"local_path": decision["asset"], "kind": "emblem"}
            record["_html"] = outputs[record["local_page"]]
        active.append(record)
    for category in LABELS:
        outputs[f"tensura-reference/{category}/index.md"] = generate_category_index(category, active)
    # Source-specific directory URLs remain usable but obey the same eligibility gate.
    configure_source("mysticism")
    for category in ("skills/extra", "skills/intrinsic", "skills/unique", "skills/ultimate", "skills/other"):
        outputs[f"mysticism-reference/{category}/index.md"] = generate_category_index(category, [r for r in active if r["local_page"].startswith("mysticism-reference/")])
    configure_source("tensura")
    exported = {"schema": 1, "minecraft": "1.21.1", "inventory_sha256": hashlib.sha256(POOL.read_bytes()).hexdigest(), "pages": policy["pages"]}
    outputs["assets/data/skill-catalogue.json"] = json.dumps(exported, indent=2, ensure_ascii=False) + "\n"
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = generate()
    for name, content in outputs.items():
        path = DOCS / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale skill output: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Skill catalogue OK: {len(outputs)} outputs")


if __name__ == "__main__":
    main()
