from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from enum import Enum


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            _ = effect_type + ' '
            self._effect_type: EffectType = EffectType(effect_type)
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._effect_type = EffectType.DAMAGE
            print('Effect type defaulted to "Damage"')
        self._used: bool = False

    def play(self, game_state: dict) -> dict:
        try:
            if not isinstance(game_state, dict):
                raise TypeError('game_state must be a dict')
            if not self._used and self.is_playable(
                game_state['available_mana']
            ):
                self._used = True
                game_state['available_mana'] -= self._cost
                res_play: dict = {
                    'card_played': self._name,
                    'mana_used': self._cost,
                }
                res_play.update(self.resolve_effect(game_state['targets']))
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
            'type': CardType.SPELL.value,
            'effect_type': self._effect_type.value,
            'used': self._used
        }

    def resolve_effect(self, targets: list) -> dict:
        if not isinstance(targets, list):
            return {}
        for target in targets:
            if not isinstance(target, (CreatureCard)):
                return {}
        effect_res: dict = {
            'effect': ''
        }
        match self._effect_type:
            case EffectType.DAMAGE:
                for target in targets:
                    target._health -= self._cost
                    effect_res['effect'] = (
                        f'Deal {self._cost} damage to target')
            case EffectType.HEAL:
                for target in targets:
                    target._health += self._cost
                    effect_res['effect'] = (
                        f'Heal target by {self._cost} points')
            case EffectType.BUFF:
                for target in targets:
                    target._attack += self._cost
                    effect_res['effect'] = (
                        f'Buff target damage by {self._cost} points')
            case EffectType.DEBUFF:
                for target in targets:
                    target._attack -= self._cost
                    effect_res['effect'] = (
                        f'Debuff target damage by {self._cost} points')
        return effect_res


class EffectType(Enum):
    DAMAGE = 'Damage'
    HEAL = 'Heal'
    BUFF = 'Buff'
    DEBUFF = 'Debuff'
