class Spell:
    def __init__(self, name, mana_cost, damage, heal):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.heal = heal

# List of available spells
spell_list = [
    Spell("Firebolt", 10, 20, 0),
    Spell("Heal", 15, 0, 25),
    Spell("Ice Shard", 12, 15, 0),
    Spell("Thunder Strike", 20, 30, 0)
]
