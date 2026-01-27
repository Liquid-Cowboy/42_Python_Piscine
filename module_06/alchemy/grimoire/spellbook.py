def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as val
    if 'VALID' == val(ingredients)[-5:]:
        return f'Spell recorded: {spell_name} ({val(ingredients)})'
    return f'Spell rejected: {spell_name} ({val(ingredients)})'
