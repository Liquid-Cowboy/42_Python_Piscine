from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex1.SpellCard import SpellCard, EffectType


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        turn_res: dict = {
            'cards_played': [],
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0,
        }
        try:
            if not isinstance(hand, list):
                raise TypeError('hand must be a list')
            for card in hand:
                if not isinstance(card, Card):
                    raise TypeError('hand must be comprised of Cards')
        except TypeError as e:
            print('[ERROR]:', e)
            return turn_res

        sorted_hand: list[Card] = sorted(hand, key=lambda card: card._cost)
        targets: list[(CreatureCard, EliteCard)] = (
            self.prioritize_targets(battlefield))
        for card in sorted_hand:
            if card.is_playable(self._mana) and targets:
                targets = [
                        t for t in targets if t._health > 0
                    ]
                if not targets:
                    return turn_res

                if isinstance(card, CreatureCard):
                    self._mana -= card._cost
                    turn_res['mana_used'] += card._cost
                    turn_res['cards_played'].append(card._name)
                    turn_res['targets_attacked'].append(targets[0]._name)
                    turn_res['damage_dealt'] += card._attack
                    card.attack_target(targets[0])

                elif (isinstance(card, SpellCard) and
                      card._effect_type == EffectType.DAMAGE):
                    self._mana -= card._cost
                    turn_res['mana_used'] += card._cost
                    turn_res['cards_played'].append(card._name)
                    turn_res['targets_attacked'].extend([
                        c._name for c in targets
                    ])
                    turn_res['damage_dealt'] += (card._cost * len(targets))
                    card.resolve_effect(targets)

                elif (isinstance(card, EliteCard)):
                    self._mana -= card._cost
                    turn_res['mana_used'] += card._cost
                    turn_res['cards_played'].append(card._name)
                    turn_res['targets_attacked'].append(targets[0]._name)
                    turn_res['damage_dealt'] += card._damage
                    card.attack(targets[0])
        return turn_res

    def get_strategy_name(self) -> str:
        return 'AgressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        try:
            if not isinstance(available_targets, list):
                raise TypeError('avaiable_targets must be a list')
        except TypeError as e:
            print('[ERROR]:', e)
            return []
        return [
            c for c in available_targets if isinstance(c, (CreatureCard,
                                                           EliteCard))
            and c._health > 0
        ]
