#! /usr/bin/env python3

import functools
from collections.abc import Callable
from typing import Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not isinstance(spells, list):
        raise TypeError('First argument "spells" is not a valid list.')
    for x in spells:
        if not isinstance(x, int):
            raise TypeError('First argument "spells" must be a ' +
                            'list comprised of only ints.')
    if not isinstance(operation, str):
        raise TypeError('Second argument "operation" is not a valid str.')
    if spells == []:
        return 0
    match operation:
        case 'add':
            return (functools.reduce(add, spells))
        case 'multiply':
            return functools.reduce(mul, spells)
        case 'max':
            return functools.reduce(max, spells)
        case 'min':
            return functools.reduce(min, spells)
        case _:
            raise ValueError('Uknown operation.')


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise TypeError('First argument "base_enchantment" ' +
                        'is not a valid Callable.')
    return {
            'fire': functools.partial(base_enchantment,
                                      power=50, element='fire'),
            'water': functools.partial(base_enchantment,
                                       power=50, element='water'),
            'ice': functools.partial(base_enchantment,
                                     power=50, element='ice')
           }


@functools.lru_cache(maxsize=5)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('First argument "n" is not a valid int.')
    return n if n < 2 else (memoized_fibonacci(n - 1) +
                            memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(spell: Any) -> Any:
        return 'Uknown spell type'

    @cast_spell.register
    def damage_spell(spell: int) -> str:
        return f'Damage spell: {spell} damage'

    @cast_spell.register
    def enchantment(spell: str) -> str:
        return f'Enchantment: {spell}'

    @cast_spell.register
    def multi_cast(spell: list) -> str:
        return f'Multi-cast: {len(spell)} spells'

    return cast_spell


if __name__ == '__main__':

    try:
        spells: list[int] = [13, 22, 40, 12]
        print('Testing spell reducer...')
        print(f'Sum: {spell_reducer( spells, "add")}')
        print(f'Product: {spell_reducer( spells, "multiply")}')
        print(f'Max: {spell_reducer( spells, "max")}')
    except Exception as e:
        print(f'Error in spell_reducer: {e}')

    try:
        print('\nTesting partial enchanter...')

        def enchantment(power: int, element: str, target: str) -> str:
            element = element.title()
            return (f'{element} enchantment does {power} ' +
                    f'points of damage to {target}.')

        enchant_book = partial_enchanter(enchantment)
        print(enchant_book['fire'](target='goblin'))
    except Exception as e:
        print(f'Error in partial_enchanter: {e}')

    try:
        print('\nTesting memoized fibonacci...')
        print(memoized_fibonacci(2))
        print(memoized_fibonacci.cache_info())
        print(memoized_fibonacci(1))
        print(memoized_fibonacci.cache_info())
        print(memoized_fibonacci(1))
        print(memoized_fibonacci.cache_info())
        print(memoized_fibonacci(1))
        print(memoized_fibonacci.cache_info())
    except Exception as e:
        print(f'Error in memoized_fibonacci: {e}')

    try:
        print('\nTesting spell dispatcher...')
        print(spell_dispatcher()(['hello', 'fireball', 'frostbite']))
    except Exception as e:
        print(f'Error in spell_dispatcher: {e}')
