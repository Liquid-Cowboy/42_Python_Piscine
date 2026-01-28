from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError('Attack must be higher than or equal to 0')
        if health < 0:
            raise ValueError('Health must be higher than or equal to 0')
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        mana: int = game_state['player_1']['mana_available']
        if (self.health > 0 and
           self.is_playable(mana)):
            mana -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to the battlefield',
            }
        return {
            'card_played': None,
            'mana_used': 0,
            'effect': 'Unable to play card.'
        }

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }

    def attack_target(self, target: Card) -> dict:
        target.health -= self.attack
        resolved: bool = False if target.health > 0 else True
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': resolved,
        }
