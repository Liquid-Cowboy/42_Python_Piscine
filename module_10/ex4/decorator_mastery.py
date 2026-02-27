from typing import Callable, Any
from functools import wraps
from time import perf_counter as clock


def spell_timer(func: Callable) -> Callable:
    """Wrapping a function makes it so it's reusable
      a wrapper function makes so we can preserve
    operations "around it" and metadata from the function we
    will wrap with it (docstrings for ex.)"""
    try:
        if not callable(func):
            raise TypeError('spell_timer() argument[0]("func") '
                            'is not Callable')
    except TypeError as e:
        print(f'[ERROR]: {e}')
        return lambda: None

    @wraps(func)
    def timer(*args, **kwargs) -> Any:
        print(f'Casting {func.__name__}...')
        start: float = clock()
        result: Any = func(*args, **kwargs)
        end: float = clock()
        print(f'Spell completed in {end - start:.2f} seconds')
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    """Since we're passing an argument to this function
    a decorator receiving the function has to be defined inside"""
    try:
        if not isinstance(min_power, int):
            raise TypeError('power_validator() argument[0](min_power) '
                            'must be an int')
    except TypeError as e:
        print(f'[ERROR]: {e}')
        return lambda: None

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if len(args) > 0 and isinstance(args[0], int):
                return (func(*args, **kwargs) if args[0] > min_power
                        else 'Insufficient power for this spell')
            try:
                if 'power' not in kwargs:
                    raise KeyError('wrapper() argument[0] or '
                                   '"power" not found')
                if not isinstance(kwargs['power'], int):
                    raise TypeError('power must be an int')
                return (func(*args, **kwargs) if kwargs['power'] > min_power
                        else 'Insufficient power for this spell')
            except (KeyError, TypeError) as e:
                print(f'[ERROR]: {e}')
                return None
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    try:
        if not isinstance(max_attempts, int):
            raise TypeError('retry_spell() argument[0] must be an int')
    except TypeError as e:
        print(f'[ERROR]: {e}')
        return lambda: None

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f'Spell failed, retrying...'
                              f'(attempt {attempt}/{max_attempts})')
                    else:
                        return ('Spell casting failed after '
                                f'{max_attempts} attempts')
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        try:
            if not isinstance(name, str):
                raise TypeError('MageGuild.validate_mage_name() '
                                'must take a str')
        except TypeError as e:
            print(f'[ERROR]: {e}')
            return False
        if len(name) < 3:
            return False
        for chr in name:
            if (not (chr >= '\t' and chr <= '\r') and
                    not chr == ' ' and not
                    (chr >= 'a' and chr <= 'z')):
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        try:
            if not isinstance(spell_name, str):
                raise TypeError('MageGuild.cast_spell() '
                                'argument[0] (spell_name) '
                                'must be a str')
        except TypeError as e:
            print(f'[ERROR]: {e}')
            return ''
        return f'Successfully cast {spell_name} with {power} power'


if __name__ == '__main__':
    @spell_timer
    def fireball() -> str:
        return 'Fireball cast!'
    print('\nTesting spell timer...')
    print(fireball())
    guild: MageGuild = MageGuild()
    print('\nTesting MageGuild...\n'
          f'{MageGuild.validate_mage_name("*Supreme Mage*")}\n'
          f'{MageGuild.validate_mage_name("Supreme Mage")}\n'
          f'{guild.cast_spell("Lightning", power=15)}')
