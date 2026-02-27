def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as val
    if 'INVALID' == val(ingredients)[-7:]:
        return f'Spell rejected: {spell_name} ({val(ingredients)})'
    return f'Spell recorded: {spell_name} ({val(ingredients)})'
