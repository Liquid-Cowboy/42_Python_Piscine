#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def kill_tomato():
    raise PlantError('The tomato plant is wilting!')


def empty_water():
    raise WaterError('Not enough water in the tank!')


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===\n')

    print('Testing PlantError...')
    try:
        kill_tomato()
    except PlantError as e:
        print(f'Caught PlantError: {e}')
        print('')

    print('Testing WaterError...')
    try:
        empty_water()
    except WaterError as e:
        print(f'Caught WaterError: {e}')
        print('')

    print('Testing catching all garden errors...')
    try:
        kill_tomato()
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    try:
        empty_water()
    except GardenError as e:
        print(f'Caught a garden error: {e}')
