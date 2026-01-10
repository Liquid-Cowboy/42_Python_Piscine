#!/usr/bin/env python3

class Plant:
    "Will serve as the blueprint for the different plants."
    count = 0

    def __init__(self, name: str, height: int, days: int):
        """Defines atributes."""
        self.name = name
        self.height = height
        self.days = days
        Plant.count += 1

    def grow(self):
        """Increases height"""
        self.height += 1

    def age(self):
        """Ages the plant"""
        self.days += 1

    def get_info(self):
        """Returns the 3 atributes in a string."""
        return f'{self.name}: {self.height}cm, {self.days} days old'


if __name__ == '__main__':
    plants = [
            Plant('Rose', 25, 30),
            Plant('Oak', 200, 365),
            Plant('Cactus', 5, 90),
            Plant('Sunflower', 80, 45),
            Plant('Fern', 15, 120),
            ]

    for plant in plants:
        print(f'Created: {plant.get_info()}')
    print(f'\nTotal plants created: {Plant.count}')
