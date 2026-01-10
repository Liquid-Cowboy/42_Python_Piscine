#!/usr/bin/env python3

class Plant:
    "Will serve as the blueprint for the different plants."
    def __init__(self, name: str, height: int, days: int):
        """Defines atributes."""
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        """Increases height"""
        self.height += 6

    def age(self):
        """Ages the plant"""
        self.days += 6

    def get_info(self):
        """Returns the 3 atributes in a string."""
        return f'{self.name}: {self.height}cm, {self.days} days old'


if __name__ == '__main__':
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)

    plants = [rose, sunflower, cactus]

    print('=== Day 1 ===')
    for plant in plants:
        print(plant.get_info())
        plant.grow()
        plant.age()

    print('=== Day 7 ===')
    for plant in plants:
        print(plant.get_info())
        print('Growth this week: +6cm')
