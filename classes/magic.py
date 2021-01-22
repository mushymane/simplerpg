import random


class Spell:
    def __init__(self, name, cost, dmg, spell_type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.spell_type = spell_type

    def generate_damage(self):
        low = 0
        high = self.dmg
        return random.randrange(low, high)
