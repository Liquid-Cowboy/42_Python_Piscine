def absolute_import() -> str:
    from alchemy.transmutation.basic import (lead_to_gold as lg,
                                             stone_to_gem as sg)
    return ('Testing Absolute Imports (from basic.py):\n'
            f'lead_to_gold(): {lg()}\nstone_to_gem(): {sg()}\n')


def relative_import() -> str:
    from alchemy.transmutation.advanced import (philosophers_stone as ps,
                                                elixir_of_life as el)
    return ('Testing Relative Imports (from advanced.py):\n'
            f'philosophers_stone(): {ps()}\nelixir_of_life(): {el()}\n')


def package_acess() -> str:
    import alchemy as al
    return ('Testing Package Access:\n'
            'alchemy.transmutation.lead_to_gold(): '
            f'{al.transmutation.lead_to_gold()}\n'
            'alchemy.transmutation.philosophers_stone(): '
            f'{al.transmutation.philosophers_stone()}\n')


if __name__ == '__main__':
    print('\n=== Pathway Debate Mastery ===\n')
    print(absolute_import())
    print(relative_import())
    print(package_acess())
    print('Both pathways work! Absolute: clear, Relative: concise')
