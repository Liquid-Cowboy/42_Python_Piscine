from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """reduce() from functools receives a function and an iterable
    and applies that function in pairs to the elements of said
    iterable until there's only one element. It then returns that
    element.
    Instead of raising a ValueError for an empty list, we could
    provide a third argument, the initializer, which sets that as
    a starting value."""
    try:
        if not isinstance(spells, list):
            raise TypeError('Argument[0] must be a list')
        if not spells:
            raise ValueError('List must be comprised of ints')
        for spell in spells:
            if not isinstance(spell, int):
                raise TypeError('Spells must be ints')
        match operation:
            case 'add':
                return reduce(add, spells)
            case 'multiply':
                return reduce(mul, spells)
            case 'max':
                return max(spells)
            case 'min':
                return min(spells)
            case _:
                raise ValueError('Invalid argument[2]')
    except (TypeError, ValueError) as e:
        print('[ERROR]:', e)
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Partial function converts the passed function to a function that
    can be preset with some defaults parameters and leave out other parameters
    to later be filled. This is valid for both *args and **kwargs.
        Here we set the function, being base_enchantment, the power (set to 50)
        and the element, set to the corresponding keys."""
    try:
        if not callable(base_enchantment):
            raise TypeError('Argument[0] must be Callable')
        return {
            'fire_enchant': partial(base_enchantment, power=50,
                                    element='Fire'),
            'ice_enchant': partial(base_enchantment, power=50,
                                   element='Ice'),
            'lightning_enchant': partial(base_enchantment, power=50,
                                         element='Lightning'),
        }
    except TypeError as e:
        print('[ERROR]:', e)
        return {'None': lambda: None}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """The lru_cache decorator enables you to store results from previous
    calls
    In this example, if n is set to 10 in a first call, and in a second
    call we set it to 5, the program will not calculate these resultes
    again since they're already stored via the @lru_cache decorator.
    Can set the cache size with maxsize.
    This decorator works great with recursive functions"""
    try:
        if not isinstance(n, int):
            raise TypeError('Argument[0] must be an int')
        if n < 0:
            raise ValueError('Int must be positive')
        return n if n < 2 else (memoized_fibonacci(n - 1) +
                                memoized_fibonacci(n - 2))

    except (TypeError, ValueError) as e:
        print('[ERROR]:', e)
        return 0


def spell_dispatcher() -> Callable:
    """The singledispatch decorator enables you to create generic
    functions that may accept a variable amount of data types and
    act accordingly to each of them"""
    @singledispatch
    def cast_spell(spell: (int | str | list[str])) -> str:
        raise NotImplementedError('Argument[0] must be an int, '
                                  'a str or a list of str')

    @cast_spell.register
    def _(spell: int) -> str:
        return f'Spell power: {spell}'

    @cast_spell.register
    def _(spell: str) -> str:
        return f'Spell name: {spell}'

    @cast_spell.register
    def _(spell: list) -> str:
        try:
            spell_list: str = ''
            for s in spell:
                if not isinstance(s, str):
                    raise ValueError('Spell must be a str')
                spell_list += (s + ', ')
            return 'Multi cast: ' + spell_list[:-2]
        except ValueError as e:
            print('[ERROR]:', e)
            return ''

    return cast_spell


if __name__ == '__main__':
    s_powers: list[int] = [40, 20, 30, 10]
    print('\nTesting spell reducer...\n'
          f'Sum: {spell_reducer(s_powers, "add")}\n'
          f'Product: {spell_reducer(s_powers, "multiply")}\n'
          f'Max: {spell_reducer(s_powers, "max")}\n'
          # f'Min: {spell_reducer(s_powers, "min")}\n'
          )

    print('Testing memoized fibonacci...\n'
          f'Fib(10): {memoized_fibonacci(10)}\n'
          f'Fib(15): {memoized_fibonacci(15)}')
"""
    enchantment: Callable = (lambda *, power, element, target:
                             f'{target} enchanted with {element} '
                             f'({power} power)')
    print('\nTesting partial enchanter...\n'
          'Enchanting Sword with Fire:',
          partial_enchanter(enchantment)['fire_enchant'](target='Sword'),
          'Enchanting Shield with Ice:',
          partial_enchanter(enchantment)['ice_enchant'](target='Shield'),
          'Enchanting Mjolnir:',
          partial_enchanter(enchantment)['lightning_enchant'](target='Hammer'),
          sep='\n')

    print('\nTesting spell dispatcher...',
          spell_dispatcher()(42),
          spell_dispatcher()('Fireball'),
          spell_dispatcher()(['Fireball',
                              'Frostbite', 'Avrakedabra']),
          sep='\n'
          )
"""
