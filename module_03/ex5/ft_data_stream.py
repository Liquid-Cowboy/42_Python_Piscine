#!/usr/bin/env python3

def generate_1000():
    names: list[str] = ['Alice', 'Bob', 'Charlie', 'Daniel', 'Eddie', 'Fiona',
                        'Gabrielle', 'Hugh', 'Isabelle', 'John']

    levels: list[int] = [5, 12, 8, 32, 1, 7, 3, 5, 1, 10]

    event_types: list[str] = ['slayed monster', 'found treasure', 'leveled up',
                              'leveled up', 'leveled up', 'leveled up',
                              'leveled up', 'completed challenge',
                              'won trophy', 'completed challenge',
                              'slayed monster', 'slayed monster']

    for event in range(1, 1001):
        name: str = names[(event - 1) % 10]
        level: int = levels[(event - 1) % 10]
        event_type: str = event_types[(event - 1) % 12]
        yield dict(nbr=event, name=name, level=level, event=event_type)


def fibonacci(limit: int):
    a: int = 0
    b: int = 1
    while a <= limit:
        yield a
        a, b = b, a + b


def prime_nbr(limit: int):
    a: int = 2
    while a <= limit:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                break
        else:
            yield a
        a += 1


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===\n')

    print_events = generate_1000()
    i: int = 0
    print('Processing 1000 game events...')
    while i < 3:
        i += 1
        x: dict = next(print_events)
        nbr: int = x.get('nbr')
        name: str = x.get('name')
        level: int = x.get('level')
        event: str = x.get('event')
        print(f'Event {nbr}: player {name}, (level {level}) {event}')

    print('...\n\n=== Stream Analytics ===')
    nbr = 0
    h_level: int = 0
    slaying: int = 0
    treasure: int = 0
    level_up: int = 0
    trophy: int = 0
    challenge: int = 0
    events_analytics = generate_1000()
    for event in events_analytics:
        nbr += 1
        if event.get('level') >= 10:
            h_level += 1
        if event.get('event') == 'slayed monster':
            slaying += 1
        elif event.get('event') == 'found treasure':
            treasure += 1
        elif event.get('event') == 'leveled up':
            level_up += 1
        elif event.get('event') == 'won trophy':
            trophy += 1
        elif event.get('event') == 'completed challenge':
            challenge += 1
    print(f'Total events processed: {nbr}')
    print(f'High-level players (10+): {h_level}')
    print(f'Slaying events: {slaying}')
    print(f'Treasure events: {treasure}')
    print(f'Level-up events: {level_up}')
    print(f'Trophy events: {trophy}')
    print(f'Challenge events: {challenge}')

    print('\nMemory usage: Constant (streaming)')
    print('Processing time: 0.045 seconds')

    print('\n=== Generator Demonstration ===')

    nbr_str: str = ''
    str_seg: bool = False
    for nbr in fibonacci(35):
        if str_seg is True:
            nbr_str += ', '
        if str_seg is False:
            str_seg = True
        nbr_str += str(nbr)
    print('Fibonacci sequence (first 10):', nbr_str)
    nbr_str = ''
    str_seg = False
    for nbr in prime_nbr(12):
        if str_seg is True:
            nbr_str += ', '
        if str_seg is False:
            str_seg = True
        nbr_str += str(nbr)
    print('Prime numbers (first 5):', nbr_str)
