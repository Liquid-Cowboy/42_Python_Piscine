#!/usr/bin/env python3

def water_plants(plant_list):
    """Will check the validity of each string.
    Concatenation on the print statement is necessary
    to spot these errors."""
    print('Opening watering system')
    try:
        for plant in plant_list:
            print('Watering ' + plant)
    except Exception:
        print('Error: Cannot water None - invalid plant!')
    finally:
        print('Closing watering system (cleanup)')


def test_watering_system():
    """ Prints the rest of the output and
    tests the watering system by passing both
    a valid list and an invalid one through water_plants()."""
    good_list = ['tomato', 'lettuce', 'carrots']
    bad_list = ['tomato', None, 'cabbage']

    print('Testing normal watering...')
    water_plants(good_list)
    print('Watering completed successfully!')

    print('')

    print('Testing with error...')
    water_plants(bad_list)
    print('\nCleanup always happens, even with errors!')


if __name__ == '__main__':
    print('=== Garden Watering System ===\n')
    test_watering_system()
