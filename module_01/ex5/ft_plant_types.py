#!/usr/bin/env python3

class Plant():
    """Will serve as a blueprint to all children classes"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Has the bloom() function and the
    color: str atribute"""
    def __init__(self, name, height, age, color: str):
        """By using super() in out __init___ method,
        we will inherit the initialization method for this
        child class"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Simply outputs a message"""
        print(f'{self.name} is blooming beautifully!')


class Tree(Plant):
    """Has the produce_shade() function and the
    trunk_diameter: int atribute"""
    def __init__(self, name, height, age, trunk_diameter: int):
        """By using super() in out __init___ method,
        we will inherit the initialization method for this
        child class"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Simply outputs a message based on
        arbitrary calculations"""
        return (
                f'{self.name} provides '
                f'{int((self.height * 0.075) + (self.trunk_diameter / 100))}'
                ' square meters of shade'
            )


class Vegetable(Plant):
    """Has the harvest_season: str and the nutritional_value: str atributes"""
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str):
        """By using super() in out __init___ method,
        we will inherit the initialization method for this
        child class"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == '__main__':
    flowers = [
        Flower('Rose', 25, 30, 'red'),
        Flower('Dandelion', 10, 5, 'yellow')
    ]
    trees = [
        Tree('Spruce', 1000, (365 * 50), 75),
        Tree('Oak', 500, 1825, 50)
    ]
    vegetables = [
        Vegetable('Tomato', 80, 90, 'summer', 'vitamin C'),
        Vegetable('Cabbage', 25, 100, 'spring', 'vitamin B')
    ]

    print('=== Garden Plant Types ===\n')
    for flower in flowers:
        print(
                f'{flower.name} (Flower): {flower.height}cm, '
                f'{flower.age} days, {flower.color} color'
            )
        flower.bloom()
        print('')
    for tree in trees:
        print(
                f'{tree.name} (Tree): {tree.height}cm, {tree.age} days, '
                f'{tree.trunk_diameter}cm diameter\n'
                f'{tree.produce_shade()}\n'
        )
    for vegetable in vegetables:
        print(
            f'{vegetable.name} (Vegetable): {vegetable.height}cm, '
            f'{vegetable.age} days, {vegetable.harvest_season} harvest\n'
            f'{vegetable.name} is rich in {vegetable.nutritional_value}\n'
        )
