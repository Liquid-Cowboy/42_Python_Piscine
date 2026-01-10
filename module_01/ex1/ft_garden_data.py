#!/usr/bin/env python3

class Plant:
    """Classes like this one act like blueprints from which
    we can create instances. Instances from the same class
    can share the same types of atributes or methods."""
    def __init__(self, name: str, height: int, age: int):
        """__init__ is a dunder method that enables you to pass
        atributes as parameters at the moment of initialization.
        This is useful so you can create unique instances from
        the same shared class."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


def main():
    """Will initialize the 3 plants by using the Plant blueprint.
    Will then print the info by accessing instances' methods."""
    rose: Plant = Plant('Rose', 25, 30)
    sunflower: Plant = Plant('Sunflower', 80, 45)
    cactus: Plant = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    print(f'{rose.name}: {rose.height}cm, {rose.age} days old')
    print(f'{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old')
    print(f'{cactus.name}: {cactus.height}cm, {cactus.age} days old')


if __name__ == "__main__":
    main()
