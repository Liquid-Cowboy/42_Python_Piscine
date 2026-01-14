#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """Will raise errors if conditions are not met"""
    try:
        if plant_name == '':
            raise ValueError('Plant name cannot be empty!')

        if water_level < 1:
            raise ValueError(
                                f'Water level {water_level} '
                                'is too low (min 1)'
                            )
        elif water_level > 10:
            raise ValueError(
                                f'Water level {water_level} '
                                'is too high (max 10)'
                            )

        if sunlight_hours < 2:
            raise ValueError(
                                f'Sunlight hours {sunlight_hours} '
                                'is too low (min 2)'
                            )
        elif sunlight_hours > 12:
            raise ValueError(
                                f'Sunlight hours {sunlight_hours} '
                                'is too high (max 12)'
                            )
        print(f'Plant \'{plant_name}\' is healthy!')
    except ValueError as e:
        print(f'Error: {e}')


def test_plant_checks():
    """Tester to check values in check_plant_health()"""
    print('Testing good values...')
    check_plant_health('tomato', 5, 6)
    print('')

    print('Testing empty plant name...')
    check_plant_health('', 5, 6)
    print('')

    print('Testing bad water level...')
    check_plant_health('tomato', -2, 6)
    check_plant_health('tomato', 20, 6)
    print('')

    print('Testing bad sunlight hours...')
    check_plant_health('tomato', 5, -4)
    check_plant_health('tomato', 5, 16)
    print('')


if __name__ == '__main__':
    print('=== Garden Plant Health Checker ===\n')
    test_plant_checks()
    print('All error raising tests completed!')
