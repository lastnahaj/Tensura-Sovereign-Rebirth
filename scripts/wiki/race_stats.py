"""Render recorded race configuration without confusing bonuses with totals."""
import html


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


def configuration_details(decision):
    config = decision['configuration']
    values = config['values']
    source = 'https://github.com/lastnahaj/Tensura-Sovereign-Rebirth/blob/main/' + config['path']
    requirements = []
    if 'epRequirement' in values:
        requirements.append(number(values['epRequirement']) + ' EP')
    if 'bossRequirement' in values:
        requirements.append('boss-count setting: ' + number(values['bossRequirement']))
    requirement = '; '.join(requirements) if requirements else 'No EP or boss-count threshold is declared in this configuration section.'
    return ('<dt>Configured evolution thresholds</dt><dd>' + html.escape(requirement)
            + ' Other route, skill, naming, or awakening conditions can still apply.</dd>'
            + '<dt>Stat source</dt><dd><a href="' + source + '">Recorded race configuration</a> · '
            + html.escape(config['section']) + '. Bonuses are not total character stats; live server overrides may differ.</dd>')
