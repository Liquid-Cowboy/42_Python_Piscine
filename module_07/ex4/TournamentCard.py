from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard, CombatTypes
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from random import randint


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, damage: int, defense: int,
                 combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            if not isinstance(health, int):
                raise TypeError(f'{health} is not a valid integer')
            if health < 0:
                raise TypeError('health must be a positive integer')
            self._health: int = health
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._health: int = 0
            print('health defaulted to 0')

        try:
            if not isinstance(damage, int):
                raise TypeError(f'{damage} is not a valid integer')
            if damage < 0:
                raise TypeError('damage must be a positive integer')
            self._damage: int = damage
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._damage: int = 0
            print('damage defaulted to 0')

        try:
            if not isinstance(defense, int):
                raise TypeError(f'{defense} is not a valid integer')
            if defense < 0:
                raise TypeError('defense must be a positive integer')
            self._defense: int = defense
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._defense: int = 0
            print('defense defaulted to 0')

        try:
            if not isinstance(combat_type, str):
                raise TypeError(f'{combat_type} is not a valid string')
            self._combat_type: CombatTypes = CombatTypes(combat_type)
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._combat_type: CombatTypes = CombatTypes.MELEE
            print('Combat type defaulted to "melee"')

        self._interfaces: list = [Card, Combatable, Rankable]
        self._rating: int = randint(1000, 2000)
        self._record: tuple = (0, 0)

    def play(self, game_state: dict) -> dict:
        try:
            if not isinstance(game_state, dict):
                raise TypeError('game_state must be a dict')
            if self.is_playable(game_state['available_mana']):
                game_state['available_mana'] -= self._cost
                return {
                    'card_played': self._name,
                    'mana_used': self._cost,
                }
            return {'card_played': None}
        except (TypeError, KeyError) as e:
            print('[ERROR]:', e)
            return {}

    def attack(self, target) -> dict:
        try:
            if not isinstance(target, (CreatureCard, EliteCard,
                                       TournamentCard)):
                raise TypeError('Target is neither a CreatureCard, '
                                'an EliteCard, nor a TournamentCard')
            target._health -= self._damage
            return {
                'attacker': self._name,
                'target': target._name,
                'damage': self._damage,
                'combat_type': self._combat_type.value
            }
        except TypeError as e:
            print('[ERROR]:', e)
            return {}

    def defend(self, incoming_damage: int) -> dict:
        try:
            if not isinstance(incoming_damage, int):
                raise TypeError(f'{incoming_damage} is not a valid integer')
            if incoming_damage < 0:
                raise ValueError('incoming_damage must be a positive integer')
            damage_taken: int = int(incoming_damage - self._defense)
            defended_damage: int = incoming_damage - damage_taken
            self._health -= damage_taken

            return {
                'defender': self._name,
                'damage_taken': damage_taken,
                'damage_blocked': defended_damage,
                'still_alive': True if self._health > 0 else False
            }
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            return {
                'defender': self._name,
                'damage_taken': 0,
                'damage_blocked': 0,
                'still_alive': True if self._health > 0 else False
            }

    def get_combat_stats(self) -> dict:
        return {
            'name': self._name,
            'health': self._health,
            'attack': self._damage,
            'defense': self._defense,
        }

    def calculate_rating(self) -> int:
        self._rating += (self._record[0] * 16)
        self._rating -= (self._record[1] * 16)
        return self._rating

    def update_wins(self, wins: int) -> None:
        try:
            if not isinstance(wins, int):
                raise TypeError(f'{wins} is not a valid integer')
            if wins < 0:
                raise ValueError('wins must be a positive integer')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            return
        self._record = (wins, self._record[1])

    def update_losses(self, losses: int) -> None:
        try:
            if not isinstance(losses, int):
                raise TypeError(f'{losses} is not a valid integer')
            if losses < 0:
                raise ValueError('losses must be a positive integer')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            return
        self._record = (self._record[0], losses)

    def get_rank_info(self) -> dict:
        return {
            'interfaces': ['Card', 'Combatabele', 'Rankable'],
            'rating': self._rating,
            'record': str(self._record[0]) + '-' + str(self._record[1]),
        }
