from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print('\n=== DataDeck Tournament Platform ===\n')

print('Registering Tournament Cards...\n')

player1: TournamentCard = TournamentCard('Fire Dragon', 5, 'Legendary',
                                         5, 5, 3, 'ranged')
player2: TournamentCard = TournamentCard('Ice Wizard', 4, 'Rare',
                                         3, 4, 4, 'ranged')
platform: TournamentPlatform = TournamentPlatform()

card1_id: str = platform.register_card(player1)
print(player1._name, f'(ID: {card1_id}):')
print('- Interfaces:', player1.get_rank_info()['interfaces'])
print('- Rating:', player1.get_rank_info()['rating'])
print('- Record:', player1.get_rank_info()['record'])
print()
card2_id: str = platform.register_card(player2)
print(player2._name, f'(ID: {card2_id}):')
print('- Interfaces:', player2.get_rank_info()['interfaces'])
print('- Rating:', player2.get_rank_info()['rating'])
print('- Record:', player2.get_rank_info()['record'])

print('\nCreating tournament match...')
print('Match result:', platform.create_match(card1_id, card2_id))

print('\nTournament Leaderboard:')
for line in platform.get_leaderboard():
    print(line)

print('\nPlatform Report:')
print(platform.generate_tournament_report())

print('\n=== Tournament Platform Successfully Deployed! ===')
print('All abstract patterns working together harmoniously!')
