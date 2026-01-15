#!/usr/bin/env python3

print('=== Achievement Tracker System ===\n')
ach: list[str] = ['first_kill', 'level_10', 'treasure_hunter',
                  'speed_demon', 'boss_slayer', 'collector', 'perfectionist']

alice_ach: set[str] = {ach[0], ach[1], ach[2], ach[3]}
bob_ach: set[str] = {ach[0], ach[1], ach[4], ach[5]}
charlie_ach: set[str] = {ach[1], ach[2], ach[4], ach[3], ach[6]}

print(f'Player Alice\'s achievements: {alice_ach}')
print(f'Player Bob\'s achievements: {bob_ach}')
print(f'Player Charlie\'s achievements: {charlie_ach}')

print('\n=== Achievement Analytics ===')
print('All unique achievements:',
      alice_ach.union(bob_ach).union(charlie_ach))
print('Total unique achievements:',
      len(alice_ach.union(bob_ach).union(charlie_ach)))

print('\nCommon to all players:',
      alice_ach.intersection(bob_ach).intersection(charlie_ach))
rare_ach: set[str] = (
            alice_ach.difference(bob_ach.union(charlie_ach))
            .union(bob_ach.difference(alice_ach.union(charlie_ach)))
            .union(charlie_ach.difference(alice_ach.union(bob_ach)))
            )
print(f'Rare achievements (1 player): {rare_ach}')

print(f'\nAlice vs Bob common: {alice_ach.intersection(bob_ach)}')
print(f'Alice unique: {alice_ach.difference(bob_ach)}')
print(f'Bob unique: {bob_ach.difference(alice_ach)}')
