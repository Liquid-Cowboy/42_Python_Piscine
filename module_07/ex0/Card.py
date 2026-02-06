from abc import ABC, abstractmethod
from enum import Enum


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        try:
            _ = name + ' '
            self._name: str = name
        except TypeError as e:
            print('[ERROR]:', e)
            self._name: str = ''
            print('Name defaulted to ""')

        try:
            _ = cost + 1
            if cost < 0:
                raise ValueError('Cost cannot be a negative value')
            self._cost: int = cost
        except (ValueError, TypeError) as e:
            print('[ERROR:]', e)
            self._cost: int = 0
            print('Cost defaulted to 0')

        try:
            self._rarity: Rarity = Rarity(rarity)
        except ValueError as e:
            print('[ERROR]:', e)
            self._rarity = Rarity.COMMON
            print('Rarity defaulted to "Common"')

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity.value,
        }

    def is_playable(self, avaiable_mana: int) -> bool:
        try:
            _ = avaiable_mana + 1
        except TypeError as e:
            print('[ERROR]:', e)
            print('Avaiable_mana defaulted to 0')
            return True if self._cost == 0 else False
        return True if avaiable_mana >= self._cost else False


class Rarity(Enum):
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    PRIMAL = 'Primal'
    LEGENDARY = 'Legendary'


class CardType(Enum):
    CREATURE = 'Creature'
    SPELL = 'Spell'
    ARTIFACT = 'Artifact'
    ELITE = 'Elite'
