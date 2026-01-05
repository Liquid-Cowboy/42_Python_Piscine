#!/usr/bin/env python3

scores = [1526, 3245, 2322, 1853, 980, 3024, 3161, 3755, 2287, 1952]
names = ['Alice', 'Bob', 'Charlie', 'Daniel', 'Eddie', 'Fiona',
         'Gabrielle', 'Hugh', 'Isabelle', 'John']
achievements = ['first_kill', 'level_10', 'treasure_hunter',
                'speed_demon', 'boss_slayer', 'collector', 'perfectionist']

print('=== Game Analytics Dashboard ===\n')

print('=== List Comprehension Example ===')
above_average = [n for n in scores
                 if n > sum(scores) / len(scores)]
complete_perc = [(str(int(n/50)) + '%')for n in scores]
print(f'Above average scores: {above_average}')
print(f'Completion percentages: {complete_perc}')

print('\n=== Dict Comprehension Example ===')
players_dict = {}
i = 0
players_dict.update(
    {names[i]: scores[i] for i in range(len(scores))}
)
for s in (f'Player: {name}\tScore: {players_dict[name]}'
          for name in players_dict.keys()):
    print(s)

print('\n=== Set Comprehension Example ===')

ach_tracker = {
    names[0]: {achievements[0], achievements[3], achievements[2],
               achievements[5]},
    names[1]: {achievements[1], achievements[2], achievements[5]},
    names[2]: {achievements[2], achievements[3], achievements[6]},
}

players_ach = {x for ach in ach_tracker.values() for x in ach}
unique_ach = (
    (ach_tracker[names[0]] - ach_tracker[names[1]] - ach_tracker[names[2]]) |
    (ach_tracker[names[1]] - ach_tracker[names[0]] - ach_tracker[names[2]]) |
    (ach_tracker[names[2]] - ach_tracker[names[1]] - ach_tracker[names[0]])
)

print('Players\' achievements:', players_ach)
print('Unique achievements:', unique_ach)
