#!/usr/bin/env python3

class GardenManager():
    """Garden Manager can manage a total of 100 gardens
    Since we can't use append method, a max limit of gardens
    needs to be defined (and initialized with None)"""
    gardens: list = [None] * 100
    garden_count: int = 0

    def __init__(self, owner: str):
        """Will receive the owner name and initialize atributes
        that will keep track of the amount of plants
        Self.plants is initialized in the same way as cls.gardens"""
        if GardenManager.garden_count == 99:
            print(
                    'A maximum of 100 gardens is permitted. '
                    'No more room for gardens. [ERROR]'
                )
            return
        self.owner = owner
        self.plants = [None] * 100
        self.plant_count = 0
        self.flowering_plant_count = 0
        self.prize_flower_count = 0

        print(f'Added {owner}\'s garden at slot {GardenManager.garden_count}')

        GardenManager.gardens[GardenManager.garden_count] = self
        GardenManager.garden_count += 1

    def add_plant(self, plant):
        """Will add plant and check for it's type
        increasing the type's count accordingly"""
        self.plants[self.plant_count] = plant
        self.plant_count += 1
        print(
                f'Added {plant.name} ({plant.height}cm, {plant.age} days)'
                f' to {self.owner}\'s garden.'
            )
        if plant.type == 'flowering plant':
            self.flowering_plant_count += 1
        if plant.type == 'prize flower':
            self.prize_flower_count += 1

    class GardenStats():
        """This nested class is used to print the current stats of
        class atributes"""
        @staticmethod
        def garden_points(garden_instance):
            """Will receive an instance and return
            collected points from instances with that atribute
            Because it is static, this method doesn't use neither
            class or instance atributes"""
            total = 0
            for plant in garden_instance.plants:
                if plant is None:
                    return print(
                                    f'{garden_instance.owner}\'s garden'
                                    f' is worth {total} points.'
                                )
                if plant.type == 'prize flower':
                    total += plant.prize_points

        @staticmethod
        def garden_state(garden_instance):
            """Will receive an instance and return analytics"""
            regular_count = (
                garden_instance.plant_count -
                (
                    garden_instance.flowering_plant_count +
                    garden_instance.prize_flower_count
                )
            )
            print(
                    f'{garden_instance.owner}\'s garden '
                    f'has {garden_instance.plant_count} plants')

            print(
                    f'\t● {regular_count} are regular plants\n'
                    f'\t● {garden_instance.flowering_plant_count}'
                    ' are flowering plants\n'
                    f'\t● {garden_instance.prize_flower_count}'
                    ' are prize flowers\n'
                )

    @classmethod
    def create_garden_network(cls):
        """Will simply print a starting point by accessing
        class atributes"""
        print('\nCreating garden network...')
        print(f'Garden slots taken: {cls.garden_count}')
        print(f'Garden slots available: {100 - cls.garden_count}\n')

    @staticmethod
    def welcome_message():
        """Simply prints a welcome message"""
        print(
            '=== Garden Management System Demo ===\n'
            'Welcome...\n'
            )


class Plant():
    """Serves as the mother class to all other child classes"""
    def __init__(self, name, height, age):
        self.type = 'regular plant'
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):
    """Child class with a special type, a state atribute
     and a check_state() function"""
    def __init__(self, name, height, age, state):
        super().__init__(name, height, age)
        self.state = state
        self.type = 'flowering plant'

    def check_state(self):
        """Returns a conditional output"""
        if (self.state == 0):
            return 'unwell'
        return 'blooming'


class PrizeFlower(FloweringPlant):
    """Child class with special type and a prize_points atribute"""
    def __init__(self, name, height, age, state, prize_points):
        super().__init__(name, height, age, state)
        self.type = 'prize flower'
        self.prize_points = prize_points


if __name__ == '__main__':
    emma_garden = GardenManager('Emma')
    paul_garden = GardenManager('Paul')
    lizzie_garden = GardenManager('Lizzie')
    GardenManager.create_garden_network()

    emma_garden.add_plant(Plant('Fern', 41, 167))
    emma_garden.add_plant(Plant('Fern', 36, 98))
    emma_garden.add_plant(PrizeFlower('Tulip', 15, 300, 0, 5))
    emma_garden.add_plant(PrizeFlower('Sunflower', 200, 450, 1, 50))
    print('')
    paul_garden.add_plant(FloweringPlant('Rose', 7, 82, 1))
    paul_garden.add_plant(Plant('Fern', 32, 78))
    paul_garden.add_plant(PrizeFlower('Orchid', 12, 97, 0, 40))
    print('')
    lizzie_garden.add_plant(FloweringPlant('Dandelion', 8, 12, 0))
    lizzie_garden.add_plant(PrizeFlower('Peony', 6, 120, 1, 25))
    lizzie_garden.add_plant(PrizeFlower('Tulip', 17, 345, 0, 5))
    lizzie_garden.add_plant(PrizeFlower('Tulip', 13, 242, 1, 5))
    lizzie_garden.add_plant(Plant('Monstera', 120, 312))

    print(f'\n{emma_garden.owner}\'s plants status:')
    for plant in emma_garden.plants:
        if plant is None:
            continue
        if plant.type == 'flowering plant' or plant.type == 'prize flower':
            print(f'\t{plant.name} is {plant.check_state()}')

    print(f'\n{paul_garden.owner}\'s plants status:')

    for plant in paul_garden.plants:
        if plant is None:
            continue
        if plant.type == 'flowering plant' or plant.type == 'prize flower':
            print(f'\t{plant.name} is {plant.check_state()}')

    print(f'\n{lizzie_garden.owner}\'s plants status:')
    for plant in lizzie_garden.plants:
        if plant is None:
            continue
        if plant.type == 'flowering plant' or plant.type == 'prize flower':
            print(f'\t{plant.name} is {plant.check_state()}')

    print('')

    GardenManager.GardenStats().garden_points(emma_garden)
    GardenManager.GardenStats().garden_state(emma_garden)

    GardenManager.GardenStats().garden_points(paul_garden)
    GardenManager.GardenStats().garden_state(paul_garden)

    GardenManager.GardenStats().garden_points(lizzie_garden)
    GardenManager.GardenStats().garden_state(lizzie_garden)
