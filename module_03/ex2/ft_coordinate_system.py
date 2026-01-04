#!/usr/bin/env python3

import sys
import math

print('=== Game Coordinate System ===')
print('')

origin = (0, 0, 0)
coordinates = (10, 20, 5)

x1, y1, z1 = origin
x2, y2, z2 = coordinates
distance = '%.2f' % math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(
        f'Position created: {coordinates}\n'
        f'Distance between {origin} and {coordinates}:',
        distance
)
print('')
coor_str = '3,4,0'
print(f'Parsing coordinates: \"{coor_str}\"')
coor_l = coor_str.split(',')
x = int(coor_l[0])
y = int(coor_l[1])
z = int(coor_l[2])
coordinates = (x, y, z)
print ('Parsed position:', coordinates)
x2, y2, z2 = coordinates
distance = '%.2f' % math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f'Distance between {origin} and {coordinates}:', distance)
print('')
coor_str = 'abc, def, ghi'
print(f'Parsing invalid coordinates: \"{coor_str}\"')
coor_l = coor_str.split(',')
try:
    x = int(coor_l[0])
    y = int(coor_l[1])
    z = int(coor_l[2])
except ValueError as e:
    print(f'Error parsing coordinates: {e}')
    print(f'Error details - Type: ValueError, Args: {e.args}')
print('')
print('Unpacking demonstration:')
print(f'Player is at X={x}, Y={y}, Z={z}')