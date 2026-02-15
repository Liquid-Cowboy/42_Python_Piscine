def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Validates input and uses a simple sorted() with the key
    being a lambda function (which returns the power of each artifact).
    Because we want the sorted list in descending order and sorted(),
    by default, returns the list in ascending order, the flag reverse=
    needs to be set to True"""
    try:
        if not isinstance(artifacts, list):
            raise TypeError('Argument[0] must be a list of dicts')
        for af in artifacts:
            if not isinstance(af, dict):
                raise TypeError('List must be comprised of only dicts')
            if list(af.keys()) != ['name', 'power', 'type']:
                raise KeyError('Dict keys must be '
                               '["name", "power", "type"]')
            if not isinstance(af['name'], str):
                raise TypeError('Artifact name must be a str')
            if not isinstance(af['power'], int):
                raise TypeError('Artifact power must be an int')
            if not isinstance(af['type'], str):
                raise TypeError('Artifact type must be a str')

    except (TypeError, KeyError) as e:
        print('[ERROR]:', e)
        return [{}]

    return sorted(artifacts, key=lambda af: af['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Validates input and uses filter(), which takes in a function
    with a boolean return type and an iterable, passes the iterable's
    elements through the function and returns them if the return
    value is True.
    If no function is given, filtered() will assume that each of
    the iterable's elements is a boolean value and will return every
    True element."""

    try:
        if not isinstance(mages, list):
            raise TypeError('Argument[0] must be a list of dicts')
        for mage in mages:
            if not isinstance(mage, dict):
                raise TypeError('List must be comprised of only dicts')
            if list(mage.keys()) != ['name', 'power', 'element']:
                raise KeyError('Dict keys must be '
                               '["name", "power", "element"]')
            if not isinstance(mage['name'], str):
                raise TypeError('Mage name must be a str')
            if not isinstance(mage['power'], int):
                raise TypeError('Mage power must be an int')
            if not isinstance(mage['element'], str):
                raise TypeError('Mage element must be a str')
        if not isinstance(min_power, int):
            raise TypeError('Argument[1] must be an int')
    except (TypeError, KeyError) as e:
        print('[ERROR]:', e)
        return [{}]
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Validates input and uses map(), which applies our lambda function
    to all elements of the iterable, which in this case is out list input.
    The lambda function returns the string concatenated in between "*  *".
    Map takes an unspecified amount of iterables, stoping execution when the
    first one is exhausted, or (by using the flag strict=) raises a ValueError
    if one iterable is exhausted before all others"""
    try:
        if not isinstance(spells, list):
            raise TypeError('Argument[0] must be a list of strs')
        for spell in spells:
            if not isinstance(spell, str):
                raise TypeError('List must be comprised of only strs')
    except TypeError as e:
        print('[ERROR]:', e)
        return ['']
    return list(map(lambda s: '* ' + s + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    """Validates input and returns a dict with statistics.
    Lambda functions are used as keys in max() and min() accessing
    each dict's "power" key"""
    try:
        if not isinstance(mages, list):
            raise TypeError('Argument[0] must be a list of dicts')
        for mage in mages:
            if not isinstance(mage, dict):
                raise TypeError('List must be comprised of only dicts')
            if list(mage.keys()) != ['name', 'power', 'element']:
                raise KeyError('Dict keys must be '
                               '["name", "power", "element"]')
            if not isinstance(mage['name'], str):
                raise TypeError('Mage name must be a str')
            if not isinstance(mage['power'], int):
                raise TypeError('Mage power must be an int')
            if not isinstance(mage['element'], str):
                raise TypeError('Mage element must be a str')
    except (TypeError, KeyError) as e:
        print('[ERROR]:', e)
        return {}
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(m['power'] for m in mages) / len(mages), 2)
    }


if __name__ == '__main__':

    print('\nTesting artifact sorter...')

    artifacts: list[
                    dict[str, (str | int)]
                   ] = [
                        {'name': 'Staff', 'power': 92, 'type': 'Fire'},
                        {'name': 'Orb', 'power': 85, 'type': 'Crystal'},
                       ]
    spells: list[str] = ['fireball', 'heal', 'shield']
    mages: list[
                dict[str, (str | int)]
               ] = [
                    {'name': 'Gandalf', 'power': 9000, 'element': 'Air'},
                    {'name': 'Saruman', 'power': 8500, 'element': 'Fire'},
                    {'name': 'Merlin', 'power': 500, 'element': 'Earth'},
                    {'name': 'Dumbledore', 'power': 100, 'element': 'Water'},
                   ]

    artifacts = artifact_sorter(artifacts)
    print(artifacts[0]['type'], artifacts[0]['name'],
          f'({artifacts[0]["power"]} power)',
          'comes before',
          artifacts[1]['type'], artifacts[1]['name'],
          f'({artifacts[1]["power"]} power)')

    print('\nTesting spell transformer...')
    spells = spell_transformer(spells)
    print(spells[0], spells[1], spells[2])

"""    print('\nTesting power filter...')
    powerful_mages: list[
                dict[str, (str | int)]
               ] = power_filter(mages, 501)
    print('Powerful mages (>= 501 power)')
    for mage in powerful_mages:
        print(mage)

    print('\nTesting mage stats...')
    print(mage_stats(mages))"""
