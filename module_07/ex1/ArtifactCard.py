from ex0 import Card
from ex1.Deck import EffectType


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect_type: str):

        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect_type: str = EffectType(effect_type)

    def play(self, game_state: str) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
