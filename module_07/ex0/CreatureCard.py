from ex0.Card import Card, CardType


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)

        try:
            _ = attack + 1
            if attack < 0:
                raise ValueError('Attack must be a positive integer')
            self._attack = attack
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._attack = 0
            print('Attack defaulted to 0')

        try:
            _ = health + 1
            if health < 0:
                raise ValueError('Health must be a positive integer')
            self._health = health
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._health = 0
            print('Health defaulted to 0')

    def play(self, game_state: dict) -> dict:
        try:
            if not isinstance(game_state, dict):
                raise TypeError('game_state must be a dict')
            if self.is_playable(game_state['available_mana']):
                game_state['available_mana'] -= self._cost
                return {
                    'card_played': self._name,
                    'mana_used': self._cost,
                    'effect': 'Creature summoned to battlefield'
                }

        except (TypeError, KeyError) as e:
            print('[ERROR]:', e)
            return {
                'card_played': None,
            }

    def get_card_info(self) -> dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity.value,
            'type': CardType.CREATURE.value,
            'attack': self._attack,
            'health': self._health,
        }

    def attack_target(self, target) -> dict:
        if isinstance(target, (CreatureCard)):
            target._health -= self._attack
            return {
                'attacker': self._name,
                'target': target._name,
                'damage_dealt': self._attack,
                'combat_resolved': True if target._health <= 0 else False,
            }
