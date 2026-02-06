from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, EffectType
from random import randint, choice


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        try:
            if not isinstance(name_or_power, (str, int, None)):
                raise TypeError('name_or_power must be either a str, a'
                                ' positive integer or None')
            if isinstance(name_or_power, int):
                if name_or_power < 0:
                    raise ValueError('name_or_power must be either a str, a'
                                     ' positive integer or None')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            name_or_power = ""
            print('name_or_power defaulted to ""')

        def_names: list[str] = [
            'Fire Dragon', 'Goblin Warrior', 'Ancient Warrior',
            'Dark Sorceress', 'Rabid Vaewolf', 'Hydra',
            'Cerberus', 'Manticore', 'Berserker Uruk'
        ]

        name: str = choice(def_names)
        cost: int = 0
        health: int = 0
        rarity: Rarity = choice(list(Rarity))
        attack: int = 0

        match rarity:
            case Rarity.COMMON:
                cost = 1
                health = 2
                attack = 2
            case Rarity.UNCOMMON:
                cost = 2
                health = 2
                attack = 3
            case Rarity.RARE:
                cost = 3
                health = 3
                attack = 4
            case Rarity.PRIMAL:
                cost = 4
                health = 4
                attack = 4
            case Rarity.LEGENDARY:
                cost = 5
                health = 5
                attack = 5

        if isinstance(name_or_power, str) and name_or_power != "":
            name = name_or_power
        if isinstance(name_or_power, int):
            attack = name_or_power

        return CreatureCard(name, cost, rarity.value, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        try:
            if not isinstance(name_or_power, (str, int, None)):
                raise TypeError('name_or_power must be either a str, a'
                                ' positive integer or None')
            if isinstance(name_or_power, int):
                if name_or_power < 0:
                    raise ValueError('name_or_power must be either a str, a'
                                     ' positive integer or None')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            name_or_power = ""
            print('name_or_power defaulted to ""')

        damage_n: list[str] = [
            'Lightning Bolt', 'Fireball', 'Frostbite'
        ]

        heal_n: list[str] = [
            'Amara\'s blessing', 'Rejuvinate', 'Life drain'
        ]

        buff_n: list[str] = [
            'Mida\'s touch', 'Odin\'s blessing', 'Berserk rage'
        ]

        debuff_n: list[str] = [
            'Slime ball', 'Poison sting', 'Blunt weapon'
        ]

        name: str = ''
        cost: int = 0
        rarity: Rarity = choice(list(Rarity))
        effect_type: EffectType = choice(list(EffectType))

        match rarity:
            case Rarity.COMMON:
                cost = 1
            case Rarity.UNCOMMON:
                cost = 2
            case Rarity.RARE:
                cost = 3
            case Rarity.PRIMAL:
                cost = 4
            case Rarity.LEGENDARY:
                cost = 5

        match effect_type:
            case EffectType.DAMAGE:
                name = choice(damage_n)
            case EffectType.HEAL:
                name = choice(heal_n)
            case EffectType.BUFF:
                name = choice(buff_n)
            case EffectType.DEBUFF:
                name = choice(debuff_n)

        if isinstance(name_or_power, str) and name_or_power != "":
            name = name_or_power
        if isinstance(name_or_power, int):
            cost = name_or_power

        return SpellCard(name, cost, rarity.value, effect_type.value)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        try:
            if not isinstance(name_or_power, (str, int, None)):
                raise TypeError('name_or_power must be either a str, a'
                                ' positive integer or None')
            if isinstance(name_or_power, int):
                if name_or_power < 0:
                    raise ValueError('name_or_power must be either a str, a'
                                     ' positive integer or None')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            name_or_power = ""
            print('name_or_power defaulted to ""')

        def_names: dict = {
            'mana_ring': ('Permanent: +1 mana per turn', 3),
            'bear_hide': ('Permanent: +1 proctection per turn', 4),
            'invisibility_cloak': ('Permanent: deflects first attack '
                                   'per turn', 5),
            'golden_compass': ('Permanent: player can avoid 1 attack '
                               'per turn', 7),
            'ceremonial_dagger': ('Permanent: +1 poison damage per turn', 3),
            'giant_toe': ('Permanent: 25% chance of '
                          '+1 health upon each incoming attack', 2),
        }

        name: str = choice(list(def_names.keys()))
        cost: int = def_names[name][1]
        rarity: Rarity = choice(list(Rarity))
        durability: int = 0
        effect: str = def_names[name][0]

        match rarity:
            case Rarity.COMMON:
                durability = 2
            case Rarity.UNCOMMON:
                durability = 3
            case Rarity.RARE:
                durability = 4
            case Rarity.PRIMAL:
                durability = 5
            case Rarity.LEGENDARY:
                durability = 7

        if isinstance(name_or_power, str) and name_or_power != "":
            name = name_or_power
        if isinstance(name_or_power, int):
            durability = name_or_power

        return ArtifactCard(name, cost, rarity.value, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        try:
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            if size < 0:
                raise ValueError('size must be a positive integer')
        except (TypeError, ValueError) as e:
            print('[ERROR]:', e)
            return {}
        creature_count: int = randint(0, size)
        spell_count: int = randint(0, (size - creature_count))
        artifact_count: int = spell_count - creature_count
        creatures: list[CreatureCard] = []
        spells: list[SpellCard] = []
        artifacts: list[ArtifactCard] = []

        for _ in range(creature_count):
            creature: CreatureCard = self.create_creature('')
            self._cards.append(creature)
            creatures.append(creature)
        for _ in range(spell_count):
            spell: SpellCard = self.create_spell('')
            self._cards.append(spell)
            spells.append(spell)
        for _ in range(artifact_count):
            artifact: ArtifactCard = self.create_artifact('')
            self._cards.append(artifact)
            artifacts.append(artifact)
        return {
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': [
                c._name for c in self._cards if isinstance(c, CreatureCard)
            ],
            'spells': [
                c._name for c in self._cards if isinstance(c, SpellCard)
            ],
            'artifacts': [
                c._name for c in self._cards if isinstance(c, ArtifactCard)
            ]
        }
