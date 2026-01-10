#!/usr/bin/env python3

class SecurePlant():
    """It's methods work as an error-proof way
    of changing each atribute's values"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initiates with atributes"""
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self):
        """Returns height (in cm) as a string"""
        return f'{self._height}cm'

    def get_age(self):
        """Returns age (in days) as a string"""
        return f'{self._age} days'

    def set_height(self, new_height: int):
        """Sets the height atribute and ensures it is
        not a negative value (returns an error message
        if that's the case)"""
        if new_height < 0:
            print(
                '\nInvalid operation attempted: '
                f'height {new_height}cm [REJECTED]\n'
                'Security: Negative height rejected'
            )
            return
        self._height: int = new_height
        print(f'Height updated: {new_height}cm [OK]')

    def set_age(self, new_age: int):
        """Sets the age atribute and ensures it is
        not a negative value (returns an error message
        if that's the case)"""
        if new_age < 0:
            print(
                '\nInvalid operation attempted: '
                f'age {new_age} days [REJECTED]\n'
                'Security: Negative age rejected'
                )
            return
        self._age: int = new_age
        print(f'Age updated: {new_age} days [OK]')


if __name__ == '__main__':
    rose: SecurePlant = SecurePlant('Rose', 5, 1)
    print(f'Plant created: {rose.name}')
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-5)
    print(
            f'\nCurrent plant: {rose.name}'
            f' ({rose.get_height()}, {rose.get_age()})'
        )
