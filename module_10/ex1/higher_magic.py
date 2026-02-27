from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    We can define a function inside of another function and then return it
    We also can pass to these new functions, other functions and whatever
    arguments they were called with, by using *args and **kwargs
    *args enables the function to receive an unspecified number of
    positional arguments(arguments following one another)
    **kwargs enables the function to receive an unspecified number of
    keyword arguments"""
    try:
        if not callable(spell1) or not callable(spell2):
            raise TypeError('Function expects two Callables')

        def combined(*args, **kwargs) -> tuple:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        return combined
    except TypeError as e:
        print('[ERROR]:', e)
        return lambda: None


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Check spell_combiner()'s docstring for more info"""
    try:
        if not callable(base_spell):
            raise TypeError('Argument[0] must be a Callable')
        if not isinstance(multiplier, int):
            raise TypeError('Argument[1], must be an int')

        def multiply() -> int:
            return base_spell() * multiplier
        return multiply
    except TypeError as e:
        print('[ERROR]:', e)
        return lambda: None


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Check spell_combiner()'s docstring for more info"""
    try:
        if not callable(condition) or not callable(spell):
            raise TypeError('Function expects two Callables')

        def cast_spell(*args, **kwargs) -> str:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            else:
                return 'Spell fizzled'
        return cast_spell
    except TypeError as e:
        print('[ERROR]:', e)
        return lambda: None


def spell_sequence(spells: list[Callable]) -> Callable:
    """Check spell_combiner()'s docstring for more info"""
    try:
        if not isinstance(spells, list):
            raise TypeError('Argument must be a list')
        for spell in spells:
            if not callable(spell):
                raise TypeError('Spell must be Callable')

        def return_sequence(*args, **kwargs) -> list[Any]:
            return [c(*args, **kwargs) for c in spells]
        return return_sequence

    except TypeError as e:
        print('[ERROR]:', e)
        return lambda: None


if __name__ == '__main__':
    def fireball(target: str) -> str:
        return f'Fireball hits {target}'

    def heal(target: str) -> str:
        return f'Heals {target}'

    combined: tuple[str, str] = spell_combiner(fireball, heal)('Dragon')
    print('\nTesting spell combiner...\n'
          'Combined spell result:',
          f'{combined[0]}, {combined[1]}'
          )

    def power() -> int:
        return 10
    amplified: Callable = power_amplifier(power, 3)
    print('\nTesting power amplifier...\n'
          f'Original: {power()}, Amplified: {amplified()}')

"""    def condition(value: bool) -> bool:
        return value

    def recharge_mana(value: bool) -> str:
        return 'Mana recharged!' if value else 'Recharge failed'

    conditional_spell: str = conditional_caster(condition, recharge_mana)(True)
    print('\nTesting conditional caster...\n', conditional_spell)

    spells: list[Callable] = [
        lambda s: '* ' + s + ' *',
        lambda s: '* ' + s + ' *',
        lambda s: '* ' + s + ' *',
        lambda s: '* ' + s + ' *',
        lambda s: '* ' + s + ' *',
    ]
    multiple_casts: list[str] = spell_sequence(spells)('42')
    print('\nTesting spell sequence...\n', multiple_casts)
"""
