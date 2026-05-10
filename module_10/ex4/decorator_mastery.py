#! /usr/bin/env python3

from functools import wraps
from collections.abc import Callable
from time import perf_counter as now, sleep
from typing import Any


def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError('First argument "func" is not a valid Callable.')

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """This is a wrapper."""
        start: float = now()
        print(f'Casting {func.__name__}...')
        sleep(1)
        res: Any = func(*args, **kwargs)
        print(f'Spell completed in {now()-start:.3f} seconds')
        print('Result: ', end='')
        return res

    return wrapper


def power_validator(min_power: int) -> Callable:

    if not isinstance(min_power, int):
        raise TypeError('First argument "min_power" is not a valid int.')

    def wrapper(func: Callable) -> Callable:

        if not callable(func):
            raise TypeError('First argument "func" is not a valid Callable.')

        @wraps(func)
        def validator(*args, **kwargs) -> Any:
            """This is a validator"""

            if not isinstance(args[0], int):
                raise TypeError('First argument "power" is not a valid int.')

            if args[0] < min_power:
                return 'Insufficient power for this spell'
            else:
                return func(*args, **kwargs)
        return validator
    return wrapper


def retry_spell(max_attempts: int) -> Callable:

    if not isinstance(max_attempts, int):
        raise TypeError('First argument "max_attempts" is not a valid int.')

    def wrapper(func: Callable) -> Callable:
        if not callable(func):
            raise TypeError('First argument "func" is not a valid Callable.')

        @wraps(func)
        def try_func(*args, **kwargs) -> Any:
            """This is a function tester"""

            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if i < max_attempts:
                        print('Spell failed, retrying... ' +
                              f'(attempt {i}/{max_attempts})')

            return f'Spell casting failed after {max_attempts} attempts'

        return try_func
    return wrapper


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        if not isinstance(name, str):
            raise TypeError('First argument "name" is not a valid str.')
        if len(name) < 3 or not ''.join(name.split()).isalpha():
            return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        if not isinstance(spell_name, str):
            raise TypeError('First argument "spell_name" is not a valid str.')
        if not isinstance(power, int):
            raise TypeError('Second argument "power" is not a valid int.')

        @power_validator(10)
        def check_power(power: int) -> str:
            return f'Successfully cast {spell_name} with {power} power'
        return check_power(power)


if __name__ == '__main__':
    @spell_timer
    def activate_spell() -> str:
        """Activates a spell."""
        return 'Avrakedabra!!!'

    guild: MageGuild = MageGuild()

    def difficult_spell(power: int, effect: str):
        """Casts a difficult spell."""
        if not isinstance(power, int) or not isinstance(effect, str):
            raise TypeError()
        match effect:
            case 'heal':
                return f'Target is healed with {power} points'
            case 'damage':
                return f'Target is damaged with {power} points'
            case 'buff':
                return f'Target is buffed with {power} points'
            case 'debuff':
                return f'Target is debuffed with {power} points'
            case _:
                raise ValueError()
    try:
        print('Testing spell timer...')
        print(activate_spell())
        print(f'Getting function docstring -> "{activate_spell.__doc__}"')
    except Exception as e:
        print(f'Error in spell_timer: {e}')

    try:
        try_spell = retry_spell(3)(difficult_spell)
        try_spell_again = retry_spell(1)(difficult_spell)
        print('\nTesting retrying spell...')
        print(try_spell('tree', 'true'))
        print(try_spell_again(3, 'heal'))
        print(f'Getting function docstring -> "{try_spell_again.__doc__}"')
    except Exception as e:
        print(f'Error in retry_spell: {e}')

    try:
        print('\nTesting MageGuild...')
        print(guild.validate_mage_name('Mary poppins'))
        print(guild.validate_mage_name(' 4 '))
    except Exception as e:
        print(f'Error in MageGuild.validate_mage_name: {e}')

    try:
        print(guild.cast_spell('Alakazaam', 15))
        print(guild.cast_spell('Fireball', 1))
    except Exception as e:
        print(f'Error in MageGuild.cast_spell: {e}')
