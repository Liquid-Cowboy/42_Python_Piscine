#! /usr/bin/env python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1):
        raise TypeError('First argument "spell1" is not a valid Callable.')
    if not callable(spell2):
        raise TypeError('Second argument "spell2" is not a valid Callable.')

    def wrapper(*args, **kwargs) -> tuple[str, str]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return wrapper


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError('First argument "base_spell" is not a valid Callable.')
    if not isinstance(multiplier, int) or multiplier <= 0:
        raise TypeError('Second argument "multiplier" is not a positive int.')

    def wrapper(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return wrapper


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise TypeError('First argument "condition" is not a valid Callable.')
    if not callable(spell):
        raise TypeError('Second argument "spell" is not a valid Callable.')

    def wrapper(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return 'Spell fizzled'
    return wrapper


def spell_sequence(spells: list[Callable]) -> Callable:
    if not isinstance(spells, list):
        raise TypeError('First argument "spells" is not a valid list.')
    for x in spells:
        if not callable(x):
            raise TypeError('First argument "spells" ' +
                            'must be a list of Callables.')

    def wrapper(*args, **kwargs) -> list[str]:
        res: list[str] = []
        for s in spells:
            res.append(s(*args, **kwargs))
        return res
    return wrapper


if __name__ == '__main__':

    def fireball(target: str, power: int) -> str:
        return f'Fireball hits {target} for {power} HP.'

    def frostbite(target: str, power: int) -> str:
        return f'Frostbite hits {target} for {power} HP.'

    def condition(target: str, power: int) -> bool:
        return True if power % 2 == 0 else False
    try:
        print('Testing spell combiner...')
        print(spell_combiner(fireball, frostbite)('goblin', 13))
    except Exception as e:
        print(f'Error in spell_combiner: {e}')

    try:
        print('\nTesting power amplifier...')
        print(fireball('goblin', 5))
        print('Now with amplified power...')
        print(power_amplifier(fireball, 3)('goblin', 5))
    except Exception as e:
        print(f'Error in power_amplifier: {e}')

    try:
        print('\nTesting conditional caster...')
        print('Testing with even power number...')
        print(conditional_caster(condition, fireball)('goblin', 4))
        print('Testing with uneven power number...')
        print(conditional_caster(condition, fireball)('goblin', 5))
    except Exception as e:
        print(f'Error in conditional_caster: {e}')

    try:
        print('\nTesting spell sequence...')
        for s in spell_sequence([fireball, frostbite])('goblin', 3):
            print(f'\t{s}')
    except Exception as e:
        print(f'Error in spell_sequence: {e}')
