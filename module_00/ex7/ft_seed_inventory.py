def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize() + ' seeds:'
    unit_out = ''
    if unit == 'packets':
        unit_out = f'{quantity} packets avaiable'
    elif unit == 'grams':
        unit_out = f'{quantity} grams total'
    elif unit == 'area':
        unit_out = f'covers {quantity} square meters'
    else:
        unit_out = 'Unknown unit type.'
    print(seed_type, unit_out)
