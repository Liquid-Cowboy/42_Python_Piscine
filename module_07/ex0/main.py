from ex0 import CreatureCard
from typing import Any

if __name__ == '__main__':
    fire_dragon: CreatureCard = CreatureCard('Fire Dragon', 5, 'Legendary',
                                             7, 5)
    goblin_warrior: CreatureCard = CreatureCard('Goblin Warrior', 4, 'Common',
                                                2, 3)

    game_state: dict[str, Any] = {
        'player_1': {
            'player': fire_dragon,
            'mana_available': 6,
            },
        'player_2': {
            'player': goblin_warrior,
            'mana_available': 3,
        },
    }

    print('\n=== DataDeck Card Foundation ===\n')

    print('Testing Abstract Base Class Design:\n')

    print('CreatureCard Info:')
    print(fire_dragon.get_card_info())

    print(f'\nPlaying {fire_dragon.get_card_info()["name"]} with '
          f'{game_state["player_1"]["mana_available"]} '
          'mana available:')
    print('Playable:',
          fire_dragon.is_playable(game_state["player_1"]["mana_available"]))
    print(f'Play result: {fire_dragon.play(game_state)}\n')

    print('Fire Dragon attacks Goblin Warrior:')
    print(f'Attack result: {fire_dragon.attack_target(goblin_warrior)}\n')

    print('Testing insufficient mana '
          f'({game_state["player_2"]["mana_available"]} available):')
    print('Playable:',
          goblin_warrior.is_playable(game_state["player_2"]["mana_available"]))

    print('\nAbstract pattern successfully demonstrated!')
