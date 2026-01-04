#!/usr/bin/env python3

import sys

print('=== Player Score Analytics ===')
if len(sys.argv) < 2:
    print('No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...')
else:
    i = 1
    scores = [0] * (len(sys.argv) - 1)
    try:
        while i != len(sys.argv):
            score = sys.argv[i]
            scores[i - 1] = int(score)
            i += 1
        print(f'Total players: {len(scores)}')
        print(f'Total score: {sum(scores)}')
        print(f'Average score: {sum(scores) / len(scores)}')
        print(f'Highest score: {max(scores)}')
        print(f'Lowest score: {min(scores)}')
        print(f'Score range: {max(scores) - min(scores)}')
        print('')
    except ValueError:
        print(f'Oops, you typed \'{score}\' instead of a number you dork...')