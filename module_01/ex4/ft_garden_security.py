#!/usr/bin/env python3

class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return f'{self._height}cm'

    def get_age(self):
        return f'{self._age} days'

    def set_height(self, new_height: int):
        if new_height < 0:
            print(
                '\nInvalid operation attempted: '
                f'height {new_height}cm [REJECTED]\n'
                'Security: Negative height rejected'
            )
            return
        self._height = new_height
        print(f'Height updated: {new_height}cm [OK]')

    def set_age(self, new_age: int):
        if new_age < 0:
            print(
                '\nInvalid operation attempted: '
                f'age {new_age} days [REJECTED]\n'
                'Security: Negative age rejected'
                )
            return
        self._age = new_age
        print(f'Age updated: {new_age} days [OK]')


if __name__ == '__main__':
    rose = SecurePlant('Rose', 5, 1)
    print(f'Plant created: {rose.name}, {rose.get_height()}, {rose.get_age()}')
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-5)
    print(
            f'\nCurrent plant: {rose.name},'
            f' {rose.get_height()}, {rose.get_age()}'
        )
