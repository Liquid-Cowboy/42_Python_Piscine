from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine

print('\n=== DataDeck Game Engine ===\n')

factory: FantasyCardFactory = FantasyCardFactory()
strategy: AgressiveStrategy = AgressiveStrategy(20)
factory.create_themed_deck(4)
print('Configuring Fantasy Card Game...')
print('Factory: FantasyCardFactory')
print('Strategy:', strategy.get_strategy_name())
print('Available types:', factory.get_supported_types())

cards_costs: list[str] = []
for card in factory._cards:
    card_str: str = card._name + ' (' + str(card._cost) + ')'
    cards_costs.append(card_str)

print('\nSimulating agressive turn...')
print('Hand:', cards_costs)

game: GameEngine = GameEngine()
game.configure_engine(factory, strategy)
print('\nTurn execution:')
print('Strategy:', game.get_engine_status()['strategy_used'])
print('Actions:', game.simulate_turn())

print('\nGame Report:')
print(game.get_engine_status())

print('\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!')
