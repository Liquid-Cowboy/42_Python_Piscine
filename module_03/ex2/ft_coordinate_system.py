#!/usr/bin/env python3

import math

if __name__ == '__main__':
    print('=== Game Coordinate System ===')
    print('')

    origin: tuple[int, int, int] = (0, 0, 0)
    coordinates: tuple[int, int, int] = (10, 20, 5)

    x1: int = origin[0]
    y1: int = origin[1]
    z1: int = origin[2]

    x2: int = coordinates[0]
    y2: int = coordinates[1]
    z2: int = coordinates[2]

    distance: float = '%.2f' % math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
            f'Position created: {coordinates}\n'
            f'Distance between {origin} and {coordinates}:',
            distance
    )
    print('')
    coor_str: str = '3,4,0'
    print(f'Parsing coordinates: \"{coor_str}\"')
    coor_l: list[str] = coor_str.split(',')
    x: int = int(coor_l[0])
    y: int = int(coor_l[1])
    z: int = int(coor_l[2])
    coordinates = (x, y, z)
    print('Parsed position:', coordinates)
    x2, y2, z2 = coordinates
    distance = '%.1f' % math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f'Distance between {origin} and {coordinates}:', distance)
    print('')
    coor_str = 'abc,def,ghi'
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
    print(f'Player at x={x}, y={y}, z={z}')
    print(f'Coordinates: X={x}, Y={y}, Z={z}')
