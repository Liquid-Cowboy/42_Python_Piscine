def ft_count_harvest_recursive(count=1, days=None):
    if days is None:
        days = int(input('Days until harvest: '))
    if (count == days):
        print('Day', count)
        print('Harvest time!')
        return
    print('Day', count)
    ft_count_harvest_recursive(count + 1, days)
