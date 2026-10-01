"""Render recorded race configuration without confusing bonuses with totals."""
import html
from race_requirements import requirement_label, family_details


def number(value):
    return f'{value:,.4f}'.rstrip('0').rstrip('.') if isinstance(value, float) else f'{value:,}'


def configured_stats(decision):
    values = decision['configuration']['values']
    result = []
    for field, label in (('maxHealth', 'HP bonus'), ('maxSpiritualHealth', 'SHP bonus'), ('attack', 'Attack bonus'), ('movementSpeed', 'Speed bonus')):
        if field in values:
            value = values[field]
            result.append((label, ('+' if value >= 0 else '') + number(value)))
    for low, high, label in (('minAura', 'maxAura', 'AP range'), ('minMagicule', 'maxMagicule', 'MP range')):
        if low in values and high in values:
            result.append((label, number(values[low]) if values[low] == values[high] else number(values[low]) + '–' + number(values[high])))
    return result


def configuration_details(decision, current_route=None):
    config = decision['configuration']
    values = config['values']
    source = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/' + config['path']
    requirements = []
    reviewed = requirement_label(decision)
    if reviewed:
        requirements.append(reviewed)
    if 'epRequirement' in values:
        requirements.append(number(values['epRequirement']) + ' EP')
    if 'bossRequirement' in values:
        requirements.append('boss-count setting: ' + number(values['bossRequirement']))
    requirement = '; '.join(requirements) if requirements else 'No EP or boss-count threshold is declared in this configuration section.'
    if reviewed:
        requirement = requirement.rstrip('.') + '.'
    return ('<dt>Configured evolution thresholds</dt><dd>' + html.escape(requirement)
            + ' Other route, skill, naming, or awakening conditions can still apply.</dd>'
            + (family_details(decision, current_route) if current_route else '')
            + '<dt>Stat source</dt><dd><a href="' + source + '">Recorded race configuration</a> · '
            + html.escape(config['section']) + '. Bonuses are not total character stats; live server overrides may differ.</dd>')
