#!/usr/bin/env python3

def generate_1000():
    names = ['Alice', 'Bob', 'Charlie', 'Daniel', 'Eddie', 'Fiona'
             'Gabrielle', 'Hugh', 'Isabelle', 'John']
    
    levels = [5, 12, 8, 32, 1, 7, 3, 5, 1, 10]

    event_types = ['slayed monster', 'found treasure', 'leveled up', 'won trophy', 'completed challenge']

    event_nbr = 0
    
    for event in range(1000):
        name = names[event_nbr % 9]
        level = levels[event_nbr % 9]
        event_type = event_types[event_nbr % 5]
        event_nbr += 1
        yield f'Event {event_nbr}: Player {name} (level {level}) {event_type}'


def fibonacci(limit: int):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b



if __name__ == '__main__':
    print('=== Game Data Stream Processor ===')

    events_1000 = generate_1000()

    print (next(events_1000))
    print (next(events_1000))
    print (next(events_1000))

    for nbr in fibonacci(5):
        print(nbr)