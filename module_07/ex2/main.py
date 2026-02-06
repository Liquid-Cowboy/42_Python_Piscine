from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

print('\n=== DataDeck Ability System ===\n')

card_m = [
    m for m in dir(Card)
    if callable(getattr(Card, m)) and not m.startswith('__')
        ]

combat_m = [
    m for m in dir(Combatable)
    if callable(getattr(Combatable, m)) and not m.startswith('__')
        ]

magic_m = [
    m for m in dir(Magical)
    if callable(getattr(Magical, m)) and not m.startswith('__')
        ]

print('EliteCard capabilities:')
print('- Card:', card_m)
print('- Combatable:', combat_m)
print('- Magical:', magic_m)

arcane_warrior: EliteCard = EliteCard('Arcane Warrior', 5, 'Ancient',
                                      5, 5, 'melee', 8)
targets: list[EliteCard] = [
    EliteCard('Enemy1', 2, 'Uncommon', 3, 5, 'ranged', 3),
    EliteCard('Enemy2', 2, 'Uncommon', 3, 5, 'ranged', 3)
]

print('\nPlaying', arcane_warrior.get_card_info()['name'],
      f'({arcane_warrior.get_card_info()["type"]} Card):\n')

print('Combat phase:')
print('Attack result:', arcane_warrior.attack(targets[0]))
print('Defense result:', arcane_warrior.defend(5))

print('\nMagic phase:')
print('Spell cast:', arcane_warrior.cast_spell('Fireball', targets))
print('Mana channel:', arcane_warrior.channel_mana(3))

print('\nMultiple interface implementation successful!')
