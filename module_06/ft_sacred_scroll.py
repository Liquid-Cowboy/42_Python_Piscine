import alchemy.elements
import alchemy
from typing import Callable


def test_modules(c: str, f: str) -> Callable | str:
    try:
        if c == 'direct':
            func: Callable = getattr(alchemy.elements, f)
            return func()
        if c == 'package':
            func: Callable = getattr(alchemy, f)
            return func()
        return 'Uknown module access mode'
    except AttributeError:
        return 'AttributeError - not exposed'


if __name__ == '__main__':
    functions: list[str] = [
        'create_fire', 'create_water', 'create_earth', 'create_air'
        ]

    print('\n=== Sacred Scroll Mastery ===\n')
    print('Testing direct module access:')
    for f in functions:
        print(f'alchemy.elements.{f}(): ', end='')
        print(test_modules('direct', f))
    print('\nTesting package-level access (controlled by __init__.py):')
    for f in functions:
        print(f'alchemy.{f}(): ', end='')
        print(test_modules('package', f))

    print('\nPackage metadata:')
    print('Version:', alchemy.__version__)
    print('Author:', alchemy.__author__)
