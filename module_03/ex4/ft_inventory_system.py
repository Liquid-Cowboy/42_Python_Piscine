#!/usr/bin/env python3

player_inventory: dict = {
    'potion': dict(count=5, category='moderate'),
    'armor': dict(count=3, category='scarce'),
    'shield': dict(count=2, category='scarce'),
    'sword': dict(count=1, category='scarce'),
    'helmet': dict(count=1, category='scarce'),
}

if __name__ == '__main__':
    print('=== Inventory System Analysis ===')

    total_items: int = 0
    inventory_log:dict = {}

    for key in player_inventory.keys():
        total_items += player_inventory[key].get('count')

    print(f'Total items in inventory: {total_items}')
    print(f'Unique item types: {len(player_inventory)}')
    
    most_abundant = 0
    least_abundant = total_items

    for key in player_inventory.keys():
        quantity: int = player_inventory[key].get('count')
        perc: float = quantity * 100 / total_items
        if quantity == 1:
            inventory_log.update({key: f'{key}: {quantity} unit ({perc:.1f}%)'})
        else:
            inventory_log.update({key: f'{key}: {quantity} units ({perc:.1f}%)'})
        if quantity > most_abundant:
            most_abundant = 

    print('\n=== Current Inventory ===')
    for value in inventory_log.values():
        print(value)