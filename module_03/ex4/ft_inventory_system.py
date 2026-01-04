#!/usr/bin/env python3

sword = {
            'name': 'sword',
            'type': 'weapon',
            'rarity': 'rare',
            'price': 500   
}

cloak = {
            'name': 'invisibility_cloak',
            'type': 'armor',
            'rarity': 'uncommon',
            'price': 120 
}

potion = {
            'name': 'potion',
            'type': 'consumable',
            'rarity': 'common',
            'price': 50   
}

shield = {
            'name': 'shield',
            'type': 'armor',
            'rarity': 'uncommon',
            'price': 200   
}

magic_ring = {
                'name': 'magic_ring',
                'type': 'wearable',
                'rarity': 'rare',
                'price': 300
}

alice = {
            'item_1': dict(item = sword, quantity = 1),
            'item_2': dict(item = potion, quantity = 5),
            'item_3': dict(item = shield, quantity = 1)
}


bob = {
        'item_1': dict(item = magic_ring, quantity = 1),
        'item_2': dict(item = cloak, quantity = 1)
}

players = {
            'Alice': alice,
            'Bob': bob
}


print('=== Player Inventory System ===\n')

for player in players.keys():

    print(f'=== {player}\'s Inventory ===')
    item_count = 0
    inventory_val = 0
    categories = {}
    
    for value in players.get(player).values():

        item = value.get('item')
        quantity = value.get('quantity')
        name = item.get('name')
        type = item.get('type')
        rarity = item.get('rarity')
        price = item.get('price')
        total_price = price * quantity
        inventory_val += total_price
        item_count += quantity
        categories.update({type : quantity})

        print(f'{name} ({type}, {rarity}): {quantity}x @ {price} gold each = {total_price} gold')
    
    print(f'\nInventory value: {inventory_val} gold')
    print(f'Item count: {item_count} items')
    category_str = ''
    first_str_seg = 0
    for category in categories.items():
        if first_str_seg == 1:
            category_str += ', '
        else:
            first_str_seg = 1
        category_str += f'{category[0]}({category[1]})'
    print(f'Categories: {category_str}')
    print('')

print('=== Transaction: Alice gives Bob 2 potions ===')

for item in alice.values():
    if item['item'] == potion:
        item['quantity'] -= 2
bob.update({'item_3': dict(item = potion, quantity = 2)})

print('Transaction successful!\n')

print('=== Updated Inventories ===')
print(f'Alice\'s potions: ', alice.get('item_2').get('quantity'))
print(f'Bob\'s potions: ', bob.get('item_3').get('quantity'))

print('\n=== Inventory Analytics ===')

player_analytics = {}
rare_items = {}
for player in players.keys():

    item_count = 0
    inventory_val = 0
    
    for value in players.get(player).values():

        item = value.get('item')
        quantity = value.get('quantity')
        name = item.get('name')
        type = item.get('type')
        rarity = item.get('rarity')
        price = item.get('price')
        total_price = price * quantity
        inventory_val += total_price
        item_count += quantity
        if rarity == 'rare':
            rare_items.update({name : item})

    player_analytics.update({player : dict(player_value = inventory_val, total_items = item_count)})

most_valuable = 'Alice'
most_items = 'Bob'

for player in player_analytics:
    if player_analytics.get(player).get('player_value') > player_analytics.get(most_valuable).get('player_value'):
        most_valuable = player

for player in player_analytics:
    if player_analytics.get(player).get('total_items') > player_analytics.get(most_items).get('total_items'):
        most_items = player

most_valuable_value = player_analytics.get(most_valuable).get('player_value')
most_items_quantity = player_analytics.get(most_items).get('total_items')

print(f'Most valuable player: {most_valuable} ({most_valuable_value})')
print(f'Most items: {most_items} ({most_items_quantity})')

first_str_seg = 0
rare_item_str = ''
for item in rare_items.keys():
    if first_str_seg == 1:
        rare_item_str += ', '
    else:
        first_str_seg = 1
    rare_item_str += item
print(f'Rare items: {rare_item_str}')