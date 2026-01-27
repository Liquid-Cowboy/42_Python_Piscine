def healing_potion() -> str:
    from .elements import create_fire as f, create_water as w
    return f'Healing potion brewed with {f()} and {w()}'


def strength_potion() -> str:
    from .elements import create_earth as e, create_fire as f
    return f'Strength potion brewed with {e()} and {f()}'


def invisibility_potion() -> str:
    from .elements import create_air as a, create_water as w
    return f'Invisibility potion brewed with {a()} and {w()}'


def wisdom_potion() -> str:
    from .elements import (create_air as a, create_fire as f,
                           create_earth as e, create_water as w)
    return (f'Wisdom potion brewed with all elements: '
            f'{f()}, {w()}, {e()}, {a()}')
