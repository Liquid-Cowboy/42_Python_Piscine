#!/usr/bin/env python3

class Plant:
    """By structuring a class with the 3 atributes needed,
    information gets more organized and accessible."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main():
    """Will initialize the 3 plants by using the Plant blueprint.
    Will then print the info."""
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    print(f'{rose.name}: {rose.height}cm, {rose.age} days old')
    print(f'{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old')
    print(f'{cactus.name}: {cactus.height}cm, {cactus.age} days old')


if __name__ == "__main__":
    main()
