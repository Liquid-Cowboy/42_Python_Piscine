#!/usr/bin/env python3
class GardenError(Exception):
    """Mother class for all garden errors"""
    pass


class PlantError(GardenError):
    """Will cover sunlight errors"""
    pass


class WaterError(GardenError):
    """Will cover water errors"""
    pass


class GardenManager():
    """This class will check the plant's health
    and print either errors or confirmation messages"""
    def add_plant(self, plant_name):
        """Will try to add a plant with a valid name"""
        try:
            if plant_name == '':
                raise GardenError('Plant name cannot be empty!')
            print(f'Added {plant_name} successfully')
        except GardenError as e:
            print(f'Error adding plant: {e}')

    def water_plants(self, plant_list):
        """Will check if the plant is valid (not None)
        and print a message accordingly"""
        print('Opening watering system')
        try:
            for plant in plant_list:
                print('Watering ' + plant + ' - success')
        except Exception:
            print('Watering None - failure')

        finally:
            print('Closing watering system (cleanup)')

    def check_health(self, plant_name, water_level, sunlight_hours):
        """Will check if water and sunlight values are acceptable"""
        try:
            if water_level < 1:
                raise WaterError(
                                    f'Water level {water_level} '
                                    'is too low (min 1)'
                                )
            elif water_level > 10:
                raise WaterError(
                                    f'Water level {water_level} '
                                    'is too high (max 10)'
                                )

            if sunlight_hours < 2:
                raise PlantError(
                                    f'Sunlight hours {sunlight_hours} '
                                    'is too low (min 2)'
                                )
            elif sunlight_hours > 12:
                raise PlantError(
                                    f'Sunlight hours {sunlight_hours} '
                                    'is too high (max 12)'
                                )
            print(
                    f'{plant_name}: healthy (water: {water_level}, '
                    f'sun: {sunlight_hours})'
                )
        except (PlantError, WaterError) as e:
            print(f'Error checking {plant_name}: {e}')

    def garden_recovery(self):
        """Will try and catch a simple error, outputing a message"""
        try:
            raise GardenError('Not enough water in the tank')
        except GardenError as e:
            print(f'Caught GardenError: {e}')
        finally:
            print('System recovered and continuing...')


if __name__ == '__main__':
    manager = GardenManager()
    print('=== Garden Management System ===\n')

    print('Adding plants to garden...')
    plants = ['tomato', 'lettuce', 'cabbage']
    for plant in plants:
        manager.add_plant(plant)
    manager.add_plant('')

    print('')

    plants = ['tomato', 'lettuce', 'cabbage', None]
    print('Watering plants...')
    manager.water_plants(plants)

    print('')

    print('Checking plant health...')
    manager.check_health('tomato', 5, 8)
    manager.check_health('lettuce', 15, 8)

    print('')

    print('Testing error recovery...')
    manager.garden_recovery()

    print('')

    print('Garden management system test complete!')
