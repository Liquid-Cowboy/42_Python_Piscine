from typing import Callable, Any


def mage_counter() -> Callable:
    """By placing the variable in an outer function
    it thereby remains changable in an enclosed scope,
    as long as we don\'t  call this outer function directly
    again (in that case, the count would be set to 0 again) """
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Same can be done with parameters"""
    try:
        if not isinstance(initial_power, int):
            raise TypeError('Argument[0] must be an int')

        def accumulate(amount: int) -> int:
            if not isinstance(amount, int):
                raise TypeError('Argument[0] must be an int')
            nonlocal initial_power
            initial_power += amount
            return initial_power
        return accumulate
    except ValueError as e:
        print('[ERROR]:', e)
        return lambda: None


def enchantment_factory(enchantment_type: str) -> Callable:
    """However you don\'t have to use nonlocal if you only
    want to access a variable from an outer function and not
    modify it"""
    try:
        if not isinstance(enchantment_type, str):
            raise TypeError('Argument[0] must be a str')

        def create_enchantment(item_name: str):
            if not isinstance(item_name, str):
                raise TypeError('Argument[0] must be a str')
            return f'{enchantment_type} {item_name}'
        return create_enchantment
    except TypeError as e:
        print('[ERROR]:', e)
        return lambda: None


def memory_vault() -> dict[str, Callable]:
    """Both ways of treating the closure here
    Returning the functions as dict values makes
    it very practical to access functionalities
    of a protected variable"""
    vault: dict[str, Any] = {}
    try:
        def store(key: str, value: Any) -> None:
            if not isinstance(key, str):
                raise TypeError('Argument[0] must be a str')
            nonlocal vault
            vault.update({key: value})

        def recall(key: str) -> Any:
            if not isinstance(key, str):
                raise TypeError('Argument[0] must be a str')
            if key not in list(vault.keys()):
                raise KeyError('Nonexistent key')
            return vault[key]
        return {'store': store, 'recall': recall}
    except (TypeError, KeyError) as e:
        print('[ERROR]:', e)
        return {'store': lambda: None, 'recall': lambda: None}


if __name__ == '__main__':
    counter: Callable = mage_counter()
    print('\nTesting enchantment factory...\n'
          f'Call 1: {counter()}\n'
          f'Call 2: {counter()}\n'
          f'Call 3: {counter()}')

    print('\nTesting enchantment factory...',
          enchantment_factory('Flaming')('Sword'),
          enchantment_factory('Frozen')('Shield'), sep='\n')

"""    accumulator: Callable = spell_accumulator(10)

    print('\nTesting spell accumulator...\n'
          f'Original: {accumulator(0)}\n'
          f'Adding 10: {accumulator(10)}\n'
          f'Adding 5: {accumulator(5)}')

    vault: dict[str, Callable] = memory_vault()
    vault['store']('school', 42)
    vault['store']('student_id', 'mnogueir')
    vault['store']('milestones', ['Milestone 0', 'Milestone 1'])
    print('\nTesting memory vault...\n'
          f'School: {vault["recall"]("school")}\n'
          f'Student ID: {vault["recall"]("student_id")}\n'
          f'Milestones: {vault["recall"]("milestones")}\n')
"""
