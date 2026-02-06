from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import shuffle as shu


class Deck():
    def __init__(self):
        self._total_cards: int = 0
        self._creatures: int = 0
        self._spells: int = 0
        self._artifacts: int = 0
        self._total_cost: int = 0
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self._cards.append(card)
            self._total_cards += 1
            self._total_cost += card._cost

            if isinstance(card, CreatureCard):
                self._creatures += 1
            if isinstance(card, SpellCard):
                self._spells += 1
            if isinstance(card, ArtifactCard):
                self._artifacts += 1

    def remove_card(self, card_name: str) -> bool:
        try:
            _ = card_name + ' '
        except TypeError as e:
            print('[ERROR]:', e)
            return False
        new_deck: list[Card] = [c for c in self._cards if c._name != card_name]
        if new_deck == self._cards:
            return False

        for card in self._cards:
            if card not in new_deck:
                self._total_cards -= 1
                self._total_cost -= card._cost
                if isinstance(card, CreatureCard):
                    self._creatures -= 1
                if isinstance(card, SpellCard):
                    self._spells -= 1
                if isinstance(card, ArtifactCard):
                    self._artifacts -= 1
        self._cards = new_deck
        return True

    def shuffle(self) -> None:
        shu(self._cards)

    def draw_card(self) -> Card:
        self._total_cards -= 1
        self._total_cost -= self._cards[0]._cost
        if isinstance(self._cards[0], CreatureCard):
            self._creatures -= 1
        if isinstance(self._cards[0], SpellCard):
            self._spells -= 1
        if isinstance(self._cards[0], ArtifactCard):
            self._artifacts -= 1
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        return {
            'total_cards': self._total_cards,
            'creatures': self._creatures,
            'spells': self._spells,
            'artifacts': self._artifacts,
            'avg_cost': round(self._total_cost / self._total_cards, 1) if (
                self._total_cards > 0) else 0.0
        }
