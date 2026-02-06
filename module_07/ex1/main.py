from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

print('\n=== DataDeck Deck Builder ===\n')

print('Building deck with different card types...')
my_deck: Deck = Deck()
cards: list[Card] = [
    SpellCard('Lightning Bolt', 3, 'Uncommon', 'Damage'),
    ArtifactCard('Mana Crystal', 2, 'Uncommon', 3,
                 'Permanent: +1 mana per turn'),
    CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5),
]
for card in cards:
    my_deck.add_card(card)
print('Deck stats:', my_deck.get_deck_stats())

print('\nDrawing and playing cards:\n')

my_deck.shuffle()

game_state: dict = {
    'available_mana': 12,
    'targets': [
        CreatureCard('Goblin Warrior',
                     2, 'Common', 2, 3)
    ]
}

while my_deck._cards:
    drawn_card: Card = my_deck.draw_card()

    print('Drew:', drawn_card.get_card_info()['name'],
          f'({drawn_card.get_card_info()["type"]})')
    print('Play result:', drawn_card.play(game_state))

print('\nPolymorphism in action: Same interface, different card behaviors!')
