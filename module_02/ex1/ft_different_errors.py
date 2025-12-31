#!/usr/bin/env python3

def garden_operations():
    print('\nTesting ValueError...')
    try:
        int('abc')
    except ValueError as e:
        print(f'Caught ValueError: {e}')

    print('\nTesting ZeroDivisionError...')
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f'Caught ZeroDivisionError: {e}')

    print('\nTesting FileNotFoundError...')
    try:
        open('missing.txt')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')

    print('\nTesting KeyError...')
    try:
        d = {}
        d['missing']
    except KeyError as e:
        print(f'Caught KeyError: {e}')

    print('\nTesting multiple errors together...')
    try:
        int('abc') / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print('Caught an error, but program continues!')


if __name__ == '__main__':
    print('=== Garden Error Types Demo ===')
    garden_operations()
    print('\nAll error types tested successfully!')
