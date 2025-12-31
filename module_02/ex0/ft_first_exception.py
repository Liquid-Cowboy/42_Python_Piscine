#!/usr/bin/env python3

def check_temperature(temp_str):
    """If the given string can't be successfully
    converted to an integer, the except block will run.
    The remaining errors are covered by if statements."""
    print(
            f'Testing temperature: {temp_str}'
        )
    try:
        nbr = int(temp_str)
    except Exception:
        return print(f'Error: \'{temp_str}\' is not a valid number\n')

    if nbr < 0:
        return print(f'Error: {nbr}°C is too cold for plants (min 0°C)\n')
    elif nbr > 40:
        return print(f'Error: {nbr}°C is too hot for plants (max 40°C)\n')
    print(f'Temperature {nbr}°C is perfect for plants!\n')


if __name__ == '__main__':
    print('=== Garden Temperature Checker ===\n')
    check_temperature('abc')
    check_temperature('42')
    check_temperature('-42')
    check_temperature('12')
    print('All tests completed - program didn\'t crash!')
