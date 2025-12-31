#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():

    def add_plant(plant_name):
        try:
            if plant_name == '':
                raise GardenError('Plant name cannot be empty!')
            print(f'Added {plant_name} successfully')
        except GardenError as e:
            print(f'Error adding plant: {e}')

    def water_plants(plant_list):
        print('Opening watering system')
        try:
            for plant in plant_list:
                print('Watering ' + plant + ' - success')
        except Exception:
            print('Watering None - failure')

        finally:
            print('Closing watering system (cleanup)')

    def check_health(plant_name, water_level, sunlight_hours):
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

    def garden_recovery():
        try:
            raise GardenError('Not enough water in the tank')
        except GardenError as e:
            print(f'Caught GardenError: {e}')
        finally:
            print('System recovered and continuing...')


if __name__ == '__main__':
    print('=== Garden Management System ===\n')

    print('Adding plants to garden...')
    plants = ['tomato', 'lettuce', 'cabbage']
    for plant in plants:
        GardenManager.add_plant(plant)
    GardenManager.add_plant('')

    print('')

    plants = ['tomato', 'lettuce', 'cabbage', None]
    print('Watering plants...')
    GardenManager.water_plants(plants)

    print('')

    print('Checking plant health...')
    GardenManager.check_health('tomato', 5, 8)
    GardenManager.check_health('lettuce', 15, 8)

    print('')

    print('Testing error recovery...')
    GardenManager.garden_recovery()

    print('')

    print('Garden management system test complete!')
