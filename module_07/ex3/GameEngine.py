from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy
from random import randint


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        try:
            if not isinstance(factory, CardFactory):
                raise TypeError('factory must be a CardFactory')
            if not isinstance(strategy, GameStrategy):
                raise TypeError('strategy must be a GameStrategy')
        except TypeError as e:
            print('[ERROR]:', e)
            return

        self._cards_created: int = 0

        if not factory._cards:
            factory.create_themed_deck(randint(0, 100))
            self._cards_created += len(factory._cards)
        enemy: FantasyCardFactory = FantasyCardFactory()
        enemy.create_themed_deck(len(factory._cards))
        self._cards_created += len(enemy._cards)
        self._player1: CardFactory = factory
        self._player2: CardFactory = enemy
        self._turn_count: int = 0
        self._strategy: GameStrategy = strategy
        self._total_damage: int = 0

    def simulate_turn(self) -> dict:
        try:
            self._turn_count += 1
            turn: dict = (self._strategy.execute_turn(
                        self._player1._cards, self._player2._cards))
            self._total_damage += turn['damage_dealt']
            return turn
        except AttributeError as e:
            print('[ERROR]:', e)
            return {}

    def get_engine_status(self) -> dict:
        try:
            return {
                'turns_simulated': 1,
                'strategy_used': self._strategy.get_strategy_name(),
                'total_damage': self._total_damage,
                'cards_created': self._cards_created,
            }
        except AttributeError as e:
            print('[ERROR]:', e)
            return {}
