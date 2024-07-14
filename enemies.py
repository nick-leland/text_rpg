import random

class Enemy:
    def __init__(self, name, base_hp, base_damage, armor, special_ability, ascii_art):
        self.name = name
        self.base_hp = base_hp
        self.base_damage = base_damage
        self.armor = armor
        self.special_ability = special_ability
        self.ascii_art = ascii_art
        self.level = 1
        self.hp = self.base_hp
        self.max_hp = self.base_hp

    def level_up(self, player_level):
        self.level = random.randint(player_level, player_level + 2)
        self.max_hp = self.base_hp + (self.level - 1) * 10
        self.hp = self.max_hp

    def attack(self):
        return random.randint(self.base_damage - 2, self.base_damage + 2) + self.level

# List of enemy types with ASCII art
enemy_types = [
    Enemy("Goblin", base_hp=30, base_damage=5, armor=1, 
          special_ability="Quick: 20% chance to attack twice",
          ascii_art=r"""
   ,      ,
  /(.-""-.)\\
  \\\ \/\/\ \
   \\\/ /\ \/
    \\\/  \\
     \\   /
      O O
      \\\/
     (____)
    """),
    Enemy("Orc", base_hp=50, base_damage=8, armor=2, 
          special_ability="Rage: Deals more damage when below 30% HP",
          ascii_art=r"""
      _____
     /     \
    | () () |
     \  ^  /
      |||||
      |||||
    """),
    Enemy("Troll", base_hp=80, base_damage=12, armor=3, 
          special_ability="Regeneration: Heals 5% of max HP each turn",
          ascii_art=r"""
    ___
   /   \\
  |   _ \
   \__/ |
    |___|
   /  |  \
  /  / \  \
    """),
    Enemy("Dragon", base_hp=150, base_damage=20, armor=5, 
          special_ability="Fire Breath: 25% chance to deal 2x damage",
          ascii_art=r"""
      /\
    _/ \
  =/  \  |
 /    \  \\
| ^  ^ |  \\
|V     |  //
 \  v  | //
  \___/|/
    """)
]

def get_random_enemy(player_level):
    enemy = random.choice(enemy_types)
    enemy.level_up(player_level)
    return enemy
