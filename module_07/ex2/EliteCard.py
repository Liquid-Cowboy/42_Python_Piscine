from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, damage: int, combat_type: str, mana: int):
        super().__init__(name, cost, rarity)
        try:
            if not isinstance(health, int):
                raise TypeError(f'{health} is not a valid integer')
            if health < 0:
                raise ValueError('Health must be a positive integer')
            self._health: int = health
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._health: int = 0
            print('Health defaulted to 0')

        try:
            if not isinstance(damage, int):
                raise TypeError(f'{damage} is not a valid integer')
            if damage < 0:
                raise ValueError('Damage must be a positive integer')
            self._damage: int = damage
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._damage: int = 0
            print('Damage defaulted to 0')

        try:
            if not isinstance(combat_type, str):
                raise TypeError(f'{combat_type} is not a valid string')
            self._combat_type: CombatTypes = CombatTypes(combat_type)
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._combat_type: CombatTypes = CombatTypes.MELEE
            print('Combat type defaulted to "melee"')

        try:
            if not isinstance(mana, int):
                raise TypeError(f'{mana} is not a valid integer')
            if mana < 0:
                raise ValueError('Mana must be a positive integer')
            self._mana = mana
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            self._mana = 0
            print('Mana defaulted to 0')

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

    def get_card_info(self) -> dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity.value,
            'type': CardType.ELITE.value,
        }

    def attack(self, target) -> dict:
        try:
            if not isinstance(target, (CreatureCard, EliteCard)):
                raise TypeError('Target is neither a CreatureCard, '
                                'nor an EliteCard')
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
            damage_taken: int = int(incoming_damage * 0.4)
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
            'damage': self._damage,
            'combat_type': self._combat_type,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        try:
            if not isinstance(spell_name, str):
                raise TypeError(f'{spell_name} is not a valid string')
            spell: SpellTypes = SpellTypes(spell_name)
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            spell: SpellTypes = SpellTypes.FIREBALL
            print('spell defaulted to "Fireball"')
        spell_cost: int = 0
        match spell:
            case SpellTypes.FIREBALL:
                spell_cost = 4
            case SpellTypes.FROSTBITE:
                spell_cost = 4
            case SpellTypes.INVISIBILITY:
                spell_cost = 3
            case SpellTypes.CLAREVOYANCE:
                spell_cost = 1
            case SpellTypes.TELEKINESIS:
                spell_cost = 7
            case SpellTypes.AVRAKEDABRA:
                spell_cost = 10

        try:
            if not isinstance(targets, list):
                raise TypeError('targets is not a valid list')
            for target in targets:
                if not isinstance(target, (CreatureCard, EliteCard)):
                    raise TypeError('target is neither a CreatureCard, '
                                    'nor an EliteCard')
            if self._mana >= spell_cost:
                for target in targets:
                    target._health -= self._damage
                self._mana -= spell_cost
                targets_names: list[str] = [
                    t._name for t in targets
                ]
                return {
                    'caster': self._name,
                    'spell': spell.value,
                    'targets': targets_names,
                    'mana_used': spell_cost,
                }
            return {}
        except TypeError as e:
            print('[ERROR]:', e)
            return {}

    def channel_mana(self, amount: int) -> dict:
        try:
            if not isinstance(amount, int):
                raise TypeError(f'{amount} is not a valid integer')
            if amount < 0:
                raise ValueError('amount must be a positive integer')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            amount = 0
            print('amount defaulted to 0')
        self._mana += amount
        return {'channeled': amount, 'total_mana': self._mana}

    def get_magic_stats(self) -> dict:
        return {
            'name': self._name,
            'available_mana': self._mana
        }


class CombatTypes(Enum):
    MELEE = 'melee'
    RANGED = 'ranged'
    MAGIC = 'magic'


class SpellTypes(Enum):
    FIREBALL = 'Fireball'
    FROSTBITE = 'Frostbite'
    INVISIBILITY = 'Invisibility'
    CLAREVOYANCE = 'Clarevoyance'
    TELEKINESIS = 'Telekinesis'
    AVRAKEDABRA = 'Avrakedabra'
