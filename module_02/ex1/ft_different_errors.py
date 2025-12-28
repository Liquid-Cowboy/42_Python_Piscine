#!/usr/bin/env python3

def garden_operations():
    try:
        nbr = int('abc')
        res = 1 / 0
        file_test = 'missing.txt'
        open(file_test)
        dict = {
            '1' : 'a',
            '3' : 'b'
            }
        print(f'{dict['2']}')
    except ValueError:
        print(
                'Testing ValueError...\n'
                'Caught ValueError: invalid literal for int()'
        )
    except ZeroDivisionError:
        print(
                'Testing ZeroDivisionError...\n'
                'Caught ZeroDivisionError: division by zero'
        )
    except FileNotFoundError:
        print(
                'Testing FileNotFoundError...\n'
                f'Caught FileNotFoundError: No such file \'{file_test}\''
            )
    except KeyError as e:
        print(
                'Testing KeyError...'
                f'Caught KeyError: {e}'
        )


if __name__ == '__main__':
    garden_operations()
    print (
            'Testing multiple errors together...\n'
            'Caught an error, but program continues!'
            '\nAll error types tested successfully!'
        )
