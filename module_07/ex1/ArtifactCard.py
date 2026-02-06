from ex0.Card import Card, CardType


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            if durability < 0:
                raise ValueError('Durability must be a positive integer')
            self._durability: int = durability
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._durability: int = 0
            print('Durability defaulted to 0')

        try:
            _ = effect + ' '
            self._effect: str = effect
        except TypeError as e:
            print('[ERROR]:', e)
            self._effect: str = ''
            print('Effect defaulted to ""')

        self._activated: bool = False

    def play(self, game_state: dict) -> dict:
        try:
            if not isinstance(game_state, dict):
                raise TypeError('game_state must be a dict')
            res_play: dict = {
                'card_played': self._name,
                'mana_used': self._cost,
                'effect': self._effect,
            }
            if (self.is_playable(game_state["available_mana"]) and
               self._activated is False):
                game_state['available_mana'] -= self._cost
                self.activate_ability()
                return res_play
            if self._activated:
                return res_play
            return {
                'card_played': None,
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
            'type': CardType.ARTIFACT.value,
            'durability': self._durability,
            'effect': self._effect,
            'activated': self._activated,
        }

    def activate_ability(self) -> dict:
        if self._durability > 0:
            self._activated = True
        else:
            self._activated = False
        if self._activated is True:
            self._durability -= 1
            return {'activated': True}
        return {'activated': False}
