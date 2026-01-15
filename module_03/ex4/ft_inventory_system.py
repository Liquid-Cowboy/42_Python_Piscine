#!/usr/bin/env python3

player_inventory: dict = {
    'potion': 5,
    'armor': 3,
    'shield': 2,
    'sword': 1,
    'helmet': 1,
}

if __name__ == '__main__':
    print('=== Inventory System Analysis ===')

    total_items: int = 0
    inventory_log: dict = {}

    for key in player_inventory.keys():
        total_items += player_inventory[key]

    print(f'Total items in inventory: {total_items}')
    print(f'Unique item types: {len(player_inventory)}')

    most_abundant: dict = {
        'name': 'placeholder',
        'value': 0,
    }
    least_abundant: dict = {
        'name': 'placeholder',
        'value': total_items,
    }

    item_categories: dict = {
        'moderate': {},
        'scarce': {},
    }

    for key in player_inventory.keys():
        quantity: int = player_inventory[key]
        perc: float = quantity * 100 / total_items

        if quantity == 1:
            inventory_log.update({key: f'{key}: \
{quantity} unit ({perc:.1f}%)'})
        else:
            inventory_log.update({key: f'{key}: \
{quantity} units ({perc:.1f}%)'})
        if quantity > most_abundant['value']:
            most_abundant['name'] = key
            most_abundant['value'] = quantity
        if quantity < least_abundant['value']:
            least_abundant['name'] = key
            least_abundant['value'] = quantity

        if quantity < 5:
            item_categories['scarce'].update({key: quantity})
        else:
            item_categories['moderate'].update({key: quantity})

    print('\n=== Current Inventory ===')
    for value in inventory_log.values():
        print(value)

    print('\n=== Inventory Statistics ===')
    if most_abundant['value'] > 1:
        print(f'Most abundant: {most_abundant["name"]} \
({most_abundant["value"]} units)')
    else:
        print(f'Most abundant: {most_abundant["name"]} \
({most_abundant["value"]} unit)')
    if least_abundant['value'] > 1:
        print(f'Least abundant: {least_abundant["name"]} \
({least_abundant["value"]} units)')
    else:
        print(f'Least abundant: {least_abundant["name"]} \
({least_abundant["value"]} unit)')

    print('\n=== Item Categories ===')
    print(f'Moderate: {item_categories["moderate"]}')
    print(f'Scarce: {item_categories["scarce"]}')

    i: int = 0
    restock: list[str] = [''] * total_items
    for item, count in player_inventory.items():
        if count == 1:
            restock[i] = item
            i += 1
    restock = restock[:i]

    print('\n=== Management Suggestions ===')
    print(f'Restock needed: {restock}')

    print('\n=== Dictionary Properties Demo ===')
    print(f'Dictionary keys: {list(player_inventory.keys())}')
    print(f'Dictionary values: {list(player_inventory.values())}')
    if 'sword' in player_inventory:
        print('Sample lookup - \'sword\' in inventory: True')
    else:
        print('Sample lookup - \'sword\' in inventory: False')
