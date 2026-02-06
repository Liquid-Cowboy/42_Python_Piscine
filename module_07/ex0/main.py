from ex0.CreatureCard import CreatureCard

print('\n=== DataDeck Card Foundation ===\n')

print('Testing Abstract Base Class Design:\n')

fire_dragon: CreatureCard = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
goblin_warrior: CreatureCard = CreatureCard('Goblin Warrior',
                                            2, 'Common', 2, 3)
player1 = {
    'available_mana': 6,
    'target': goblin_warrior,
}

print('CreatureCard Info:')
print(fire_dragon.get_card_info())

print('\nPlaying', fire_dragon.get_card_info()["name"],
      'with', player1['available_mana'], 'mana available:')
print('Playable:', fire_dragon.is_playable(player1['available_mana']))
print('Play result:', fire_dragon.play(player1))

print()

print(fire_dragon.get_card_info()['name'], 'attacks',
      player1['target'].get_card_info()['name'], ':')
print('Attack result:', fire_dragon.attack_target(goblin_warrior))

print(f'\nTesting insufficient mana ({player1["available_mana"]} available):')
print('Playable:', fire_dragon.is_playable(player1['available_mana']))

print('\nAbstract pattern successfully demonstrated!')
