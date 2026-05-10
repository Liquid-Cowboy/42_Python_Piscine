#! /usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    calls: int = 0

    def wrapper() -> int:
        nonlocal calls
        calls += 1
        return calls

    return wrapper


def spell_accumulator(initial_power: int) -> Callable:
    if not isinstance(initial_power, int):
        raise TypeError('First argument "initial_power" ' +
                        'is not a valid int.')
    power: int = initial_power

    def wrapper(add_power: int) -> int:
        if not isinstance(add_power, int):
            raise TypeError('First argument "add_power" ' +
                            'is not a valid int.')
        nonlocal power
        power += add_power
        return power
    return wrapper


def enchantment_factory(enchantment_type: str) -> Callable:
    if not isinstance(enchantment_type, str):
        raise TypeError('First argument "enchantment_type" ' +
                        'is not a valid str.')

    def wrapper(item_name: str) -> str:
        if not isinstance(item_name, str):
            raise TypeError('First argument "item_name" ' +
                            'is not a valid str.')
        return enchantment_type + ' ' + item_name

    return wrapper


def memory_vault() -> dict[str, Callable]:
    vault: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:

        vault[key] = value

    def recall(key: Any) -> Any:

        return vault.get(key) if vault.get(key) else 'Memory not found'
    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    try:
        counter_a: Callable = mage_counter()
        counter_b: Callable = mage_counter()
        print('Testing mage counter...')
        for i in range(1, 3):
            print(f'counter_a call {i}: {counter_a()}')
        print(f'counter_b call 1: {counter_b()}')
    except Exception as e:
        print(f'Error in mage_counter: {e}')

    try:
        acumulator: Callable = spell_accumulator(100)
        print('\nTesting spell accumulator...')
        print(f'Base 100, add 20: {acumulator(20)}')
        print(f'Base 100, add 30: {acumulator(30)}')
    except Exception as e:
        print(f'Error in spell_accumulator: {e}')

    try:
        flame_obj: Callable = enchantment_factory('Flaming')
        print('\nTesting enchantment factory...')
        print(flame_obj('Sword'))
        print(flame_obj('Shield'))
    except Exception as e:
        print(f'Error in enchantment_factory: {e}')

    try:
        print('\nTesting memory vault...')
        vault: dict[str, Callable] = memory_vault()
        print('Store "secret" = 42')
        vault['store']('secret', 42)
        print(f'Recall "secret" : {vault["recall"]("secret")}')
        print(f'Recall "unknown" : {vault["recall"]("unknown")}')
    except Exception as e:
        print(f'Error in memory_vault: {e}')
