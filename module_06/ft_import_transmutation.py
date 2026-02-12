def module_import() -> str:
    import alchemy.elements
    return ('Method 1 - Full module import:\n'
            'alchemy.elements.create_fire(): '
            f'{alchemy.elements.create_fire()}\n')


def function_import() -> str:
    from alchemy.elements import create_water
    return ('Method 2 - Specific function import:\n'
            'create_water(): '
            f'{create_water()}\n')


def alias_import() -> str:
    from alchemy.potions import healing_potion as heal
    return ('Method 3 - Aliased import:\n'
            f'heal(): {heal()}\n')


def multiple_import() -> str:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    return ('Method 4 - Multiple imports:\n'
            f'create_earth(): {create_earth()}\n'
            f'create_fire(): {create_fire()}\n'
            f'strength_potion(): {strength_potion()}\n')


if __name__ == '__main__':
    print('\n=== Import Transmutation Mastery ===\n')

    print(module_import())
    print(function_import())
    print(alias_import())
    print(multiple_import())
    print('All import transmutation methods mastered!')
