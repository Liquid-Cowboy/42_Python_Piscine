def validation_test() -> str:
    from alchemy.grimoire.validator import validate_ingredients as val
    return ('Testing ingredient validation:\n'
            f'validate_ingredients("fire air"): {val("fire air")}\n'
            f'validate_ingredients("dragon scales"): {val("dragon scales")}\n')

def spell_test() -> str:
    from alchemy.grimoire.spellbook import record_spell as s
    return ('Testing spell recording with validation:\n'
            f'record_spell("Fireball", "fire air"): {s("Fireball", "fire air")}\n'
            f'record_spell("Dark Magic", "shadow"): {s("Dark Magic", "shadow")}\n')

def import_test() -> str:
     from alchemy.grimoire.spellbook import record_spell as s
     return ('Testing late import technique:\n'
             f'record_spell("Lightning", "air"): {s("Lightning", "air")}\n')

if __name__ == '__main__':
    print('\n=== Circular Curse Breaking ===\n')
    print(validation_test())
    print(spell_test())
    print(import_test())
    print('Circular dependency curse avoided using late imports!')
    print('All spells processed safely!')
