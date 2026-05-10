#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    if not isinstance(artifacts, list):
        raise TypeError('"artifacts" argument is not a list.')
    for i, d in enumerate(artifacts):
        if not isinstance(d, dict):
            raise TypeError('"artifacts" argument must be comprised ' +
                            'of only dictionaries.')
        if set(d.keys()) != {'name', 'power', 'type'}:
            raise KeyError(f'Dictionary {i + 1} in "artifacts" argument ' +
                           'must only have the following keys: ["name", ' +
                           '"power", "type"]')
        if not isinstance(d['name'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"name" is not a str.')
        if not isinstance(d['power'], int):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"power" is not a str.')
        if not isinstance(d['type'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"type" is not a str.')

    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    if not isinstance(mages, list):
        raise TypeError('"mages" argument is not a list.')
    for i, d in enumerate(mages):
        if not isinstance(d, dict):
            raise TypeError('"mages" argument must be comprised ' +
                            'of only dictionaries.')
        if set(d.keys()) != {'name', 'power', 'element'}:
            raise KeyError(f'Dictionary {i + 1} in "mages" argument ' +
                           'must only have the following keys: ["name", ' +
                           '"power", "element"]')
        if not isinstance(d['name'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"name" is not a str.')
        if not isinstance(d['power'], int):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"power" is not a str.')
        if not isinstance(d['element'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"element" is not a str.')
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    if not isinstance(spells, list):
        raise TypeError('"spells" argument is not a list.')
    for i, s in enumerate(spells):
        if not isinstance(s, str):
            raise TypeError(f'Element {i + 1} of "spells" ' +
                            'argument is not a str.')
    return list(map(lambda x: '*' + x + '*', spells))


def mage_stats(mages: list[dict]) -> dict:
    if not isinstance(mages, list):
        raise TypeError('"mages" argument is not a list.')
    for i, d in enumerate(mages):
        if not isinstance(d, dict):
            raise TypeError('"mages" argument must be comprised ' +
                            'of only dictionaries.')
        if set(d.keys()) != {'name', 'power', 'element'}:
            raise KeyError(f'Dictionary {i + 1} in "mages" argument ' +
                           'must only have the following keys: ["name", ' +
                           '"power", "element"]')
        if not isinstance(d['name'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"name" is not a str.')
        if not isinstance(d['power'], int):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"power" is not a str.')
        if not isinstance(d['element'], str):
            raise TypeError(f'Dictionary {i + 1} key ' +
                            '"element" is not a str.')
    return {
        'max_power': max(mages, key=lambda x: x['power']),
        'min_power': min(mages, key=lambda x: x['power']),
        'avg_power': round(sum(map(lambda x: x['power'], mages)) /
                           len(mages), 2),
    }


if __name__ == '__main__':

    artifacts: list[dict] = [
        {'name': 'Sorcerer\'s Stone', 'power': 4, 'type': 'mystic'},
        {'name': 'Goblin Dagger', 'power': 2, 'type': 'melee'},
        {'name': 'Merlin\'s Sword', 'power': 10, 'type': 'melee'}
                           ]

    mages: list[dict] = [
        {'name': 'Azkhaban', 'power': 5, 'element': 'dark'},
        {'name': 'Harry Poter', 'power': 10, 'element': 'light'},
        {'name': 'Hermione', 'power': 2, 'element': 'fire'}
                        ]

    spells: list[str] = ['avrakedabra', 'fireball', 'frostbite']

    try:
        print('\nTesting artifact sorter...')
        for i, item in enumerate(artifact_sorter(artifacts)):
            print(f'\tItem {i + 1}: ', end='')
            print(f'{item["name"]} ({item["power"]} power)')
    except (TypeError, KeyError) as e:
        print('Error in artifact_sorter(artifacts: list[dict]) ' +
              f'-> list[dict]: {e}')
    try:
        print('\nTesting power filter (min 3)...')
        for i, item in enumerate(power_filter(mages, 3)):
            print(f'\tItem {i + 1}: ', end='')
            print(f'{item["name"]} ({item["power"]} power)')
    except (TypeError, KeyError) as e:
        print('Error in power_filter(mages: list[dict],' +
              f' min_power: int) -> list[dict]:  {e}')
    try:
        print('\nTesting spell transformer...')
        print('\tBefore:')
        print(f'\t\t{spells}')
        print('\tAfter:')
        print(f'\t\t{spell_transformer(spells)}')
    except (TypeError, KeyError) as e:
        print('Error in spell_transformer(spells: list[str]) ' +
              f'-> list[str]: {e}')
    try:
        print('\nTesting mage stats...')
        print('\tMax power mage:')
        max_mage: dict[str, str | int] = mage_stats(mages)['max_power']
        min_mage: dict[str, str | int] = mage_stats(mages)['min_power']

        print(f'\t\t{max_mage["name"]} ({max_mage["power"]} power) ' +
              f'({max_mage["element"]} element)')
        print('\tMin power mage:')
        print(f'\t\t{min_mage["name"]} ({min_mage["power"]} power) ' +
              f'({min_mage["element"]} element)')
        print('\tAverage power:')
        print(f'\t\t{mage_stats(mages)["avg_power"]}')
    except (TypeError, KeyError) as e:
        print('Error in spell_transformer(spells: list[str]) ' +
              f'-> list[str]: {e}')
