from ex0 import Card
from enum import Enum

class Deck():
    def add_card(self, card: Card) -> None:
        pass

    def remove_card(self, card_name: str) -> bool:
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        pass


class EffectType(Enum):
    DAMAGE: str = 'damage'
    HEAL: str = 'heal'
    BUFF: str = 'buff'
    DEBUFF: str = 'debuff'

class Rarity(Enum):
    COMMON: str = 'common'
    UNCOMMON: str = 'uncommon'
    RARE: str = 'rare'
    LEGENDARY: str = 'legendary'
