import random
from colorama import init, Fore, Back, Style
from spells import Spell, spell_list
from enemies import get_random_enemy

# Initialize colorama
init(autoreset=True)

class Equipment:
    def __init__(self, name, equipment_type, bonus):
        self.name = name
        self.type = equipment_type
        self.bonus = bonus

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mana = 50
        self.max_mana = 50
        self.xp = 0
        self.xp_to_next_level = 100
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.strength = 5
        self.dexterity = 5
        self.constitution = 5
        self.intelligence = 5
        self.stat_points = 0
        self.spells = []
        self.known_spells = spell_list

    def equip(self, item):
        if item.type == "weapon":
            self.weapon = item
            print(f"You equipped {Fore.YELLOW}{item.name}{Fore.RESET} as your weapon.")
        elif item.type == "armor":
            self.armor = item
            print(f"You equipped {Fore.CYAN}{item.name}{Fore.RESET} as your armor.")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{Fore.GREEN}You gained {amount} XP!{Fore.RESET}")
        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = self.level * 100
        self.stat_points += 5
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 10
        self.mana = self.max_mana
        print(f"{Fore.GREEN}Congratulations! You've reached level {self.level}!{Fore.RESET}")
        print(f"{Fore.YELLOW}You have {self.stat_points} stat points to distribute.{Fore.RESET}")
        self.learn_spell()

    def learn_spell(self):
        learnable_spells = [spell for spell in self.known_spells if spell not in self.spells]
        if learnable_spells and self.intelligence >= len(self.spells) + 5:
            new_spell = random.choice(learnable_spells)
            self.spells.append(new_spell)
            print(f"{Fore.MAGENTA}You learned a new spell: {new_spell.name}!{Fore.RESET}")
        elif not learnable_spells:
            print(f"{Fore.YELLOW}You already know all available spells.{Fore.RESET}")
        else:
            print(f"{Fore.YELLOW}Your Intelligence is too low to learn a new spell.{Fore.RESET}")


    def distribute_stat_points(self):
        while self.stat_points > 0:
            print(f"\nYou have {Fore.YELLOW}{self.stat_points}{Fore.RESET} stat points to distribute.")
            print(f"1. Strength: {self.strength}")
            print(f"2. Dexterity: {self.dexterity}")
            print(f"3. Constitution: {self.constitution}")
            print(f"4. Intelligence: {self.intelligence}")
            choice = input("Choose a stat to increase (1-4) or 'q' to quit: ")
            if choice == 'q':
                break
            elif choice in ['1', '2', '3', '4']:
                amount = int(input("How many points to add? "))
                if amount <= self.stat_points:
                    if choice == '1':
                        self.strength += amount
                    elif choice == '2':
                        self.dexterity += amount
                    elif choice == '3':
                        self.constitution += amount
                    elif choice == '4':
                        self.intelligence += amount
                    self.stat_points -= amount
                else:
                    print(f"{Fore.RED}Not enough stat points!{Fore.RESET}")
            else:
                print(f"{Fore.YELLOW}Invalid choice. Please choose 1-4 or 'q'.{Fore.RESET}")

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 20
        self.max_hp = level * 20
        self.weapon = None
        self.armor = None

class Game:
    def __init__(self):
        self.player = None
        self.locations = ["Forest", "Cave", "Mountain", "Castle"]
        self.equipment = [
            Equipment("Rusty Sword", "weapon", 2),
            Equipment("Iron Sword", "weapon", 5),
            Equipment("Steel Sword", "weapon", 8),
            Equipment("Leather Armor", "armor", 2),
            Equipment("Chain Mail", "armor", 5),
            Equipment("Plate Armor", "armor", 8)
        ]
        self.debug_mode = False

    def create_player(self, name):
        self.player = Player(name)
        if name.lower() == 'admin':
            self.debug_mode = True
            print(f"{Fore.YELLOW}Debug mode activated!{Fore.RESET}")
        print(f"Welcome, {Fore.GREEN}{self.player.name}{Fore.RESET}! Your adventure begins.")

    def generate_enemy(self):
        return get_random_enemy(self.player.level)

    def display_enemy(self, enemy):
        print(f"You encounter a level {Fore.MAGENTA}{enemy.level} {enemy.name}{Fore.RESET}!")
        print(f"HP: {enemy.hp}/{enemy.max_hp}")
        print(f"Special Ability: {enemy.special_ability}")
        print(Fore.RED + enemy.ascii_art + Fore.RESET)

    def player_death(self):
        print(f"\n{Fore.RED}Your health has dropped to 0. You have died!{Fore.RESET}")
        print(f"\n{Fore.YELLOW}=== Game Over ==={Fore.RESET}")
        print(f"Name: {self.player.name}")
        print(f"Level: {self.player.level}")
        print(f"XP: {self.player.xp}")
        print(f"Strength: {self.player.strength}")
        print(f"Dexterity: {self.player.dexterity}")
        print(f"Constitution: {self.player.constitution}")
        print(f"Intelligence: {self.player.intelligence}")
        
        restart = input(f"\nDo you want to start a new game? ({Fore.GREEN}Y{Fore.RESET}/{Fore.RED}N{Fore.RESET}): ").lower()
        if restart == 'y':
            self.__init__()  # Reset the game
            player_name = input("Enter your character's name: ")
            self.create_player(player_name)
            self.main_loop()
        else:
            print(f"\n{Fore.YELLOW}Thank you for playing!{Fore.RESET}")
            exit()

    def battle(self, enemy):
        self.display_enemy(enemy)
        while enemy.hp > 0 and self.player.hp > 0:
            self.display_health_and_mana()
            action = input(f"Do you want to {Fore.YELLOW}[A]ttack{Fore.RESET}, {Fore.MAGENTA}[C]ast Spell{Fore.RESET}, or {Fore.CYAN}[R]un{Fore.RESET}? ").lower()
            if action == 'a':
                damage = (random.randint(5, 15) + self.player.strength) * self.player.level
                if self.player.weapon:
                    damage += self.player.weapon.bonus
                damage = max(1, damage - enemy.armor)
                enemy.hp -= damage
                print(f"You deal {Fore.YELLOW}{damage} damage{Fore.RESET} to the {enemy.name}.")
            elif action == 'c':
                if not self.player.spells:
                    print(f"{Fore.YELLOW}You don't know any spells yet!{Fore.RESET}")
                    continue
                print("Available spells:")
                for i, spell in enumerate(self.player.spells):
                    print(f"{i+1}. {spell.name} (Mana cost: {spell.mana_cost})")
                spell_choice = input("Choose a spell to cast (number) or 'b' to go back: ")
                if spell_choice == 'b':
                    continue
                try:
                    spell_index = int(spell_choice) - 1
                    if 0 <= spell_index < len(self.player.spells):
                        if not self.cast_spell(self.player.spells[spell_index], enemy):
                            continue
                    else:
                        print(f"{Fore.YELLOW}Invalid spell choice.{Fore.RESET}")
                        continue
                except ValueError:
                    print(f"{Fore.YELLOW}Invalid input. Please enter a number or 'b'.{Fore.RESET}")
                    continue
            elif action == 'r':
                if random.random() < 0.5 + (self.player.dexterity * 0.02):
                    print(f"{Fore.GREEN}You successfully fled from the battle.{Fore.RESET}")
                    return True
                else:
                    print(f"{Fore.RED}You failed to run away!{Fore.RESET}")
            else:
                print(f"{Fore.YELLOW}Invalid action. Please choose [A]ttack, [C]ast Spell, or [R]un.{Fore.RESET}")
                continue

            if enemy.hp <= 0:
                print(f"{Fore.GREEN}You defeated the {enemy.name}!{Fore.RESET}")
                xp_gained = enemy.level * 10
                self.player.gain_xp(xp_gained)
                return True

            # Enemy turn
            enemy_damage = enemy.attack()
            if self.player.armor:
                enemy_damage = max(1, enemy_damage - self.player.armor.bonus)
            self.player.hp -= enemy_damage
            print(f"The {enemy.name} deals {Fore.RED}{enemy_damage} damage{Fore.RESET} to you.")

            # Apply enemy special abilities
            if enemy.name == "Goblin" and random.random() < 0.2:
                extra_damage = enemy.attack()
                self.player.hp -= extra_damage
                print(f"{Fore.RED}The Goblin attacks again for {extra_damage} damage!{Fore.RESET}")
            elif enemy.name == "Orc" and enemy.hp < enemy.max_hp * 0.3:
                rage_bonus = int(enemy_damage * 0.5)
                self.player.hp -= rage_bonus
                print(f"{Fore.RED}The Orc's rage deals an additional {rage_bonus} damage!{Fore.RESET}")
            elif enemy.name == "Troll":
                heal_amount = int(enemy.max_hp * 0.05)
                enemy.hp = min(enemy.max_hp, enemy.hp + heal_amount)
                print(f"{Fore.GREEN}The Troll regenerates {heal_amount} HP!{Fore.RESET}")
            elif enemy.name == "Dragon" and random.random() < 0.25:
                fire_damage = enemy_damage
                self.player.hp -= fire_damage
                print(f"{Fore.RED}The Dragon's fire breath deals an additional {fire_damage} damage!{Fore.RESET}")

            if self.player.hp <= 0:
                self.player_death()
                return False

    def find_equipment(self):
        if random.random() < 0.3:
            item = random.choice(self.equipment)
            print(f"You found {Fore.YELLOW if item.type == 'weapon' else Fore.CYAN}{item.name}{Fore.RESET}!")
            
            if item.type == "weapon":
                current_item = self.player.weapon
            else:  # armor
                current_item = self.player.armor
            
            if current_item:
                print(f"Your current {item.type}:")
                print(f"  {current_item.name} (Bonus: +{current_item.bonus})")
                print(f"New {item.type}:")
                print(f"  {item.name} (Bonus: +{item.bonus})")
                
                if item.bonus > current_item.bonus:
                    print(f"{Fore.GREEN}The new {item.type} is better!{Fore.RESET}")
                elif item.bonus < current_item.bonus:
                    print(f"{Fore.RED}The new {item.type} is worse.{Fore.RESET}")
                else:
                    print(f"{Fore.YELLOW}The new {item.type} is equal to your current one.{Fore.RESET}")
                
                action = input(f"Do you want to {Fore.GREEN}[E]quip{Fore.RESET} the new {item.type} or {Fore.RED}[L]eave{Fore.RESET} it? ").lower()
            else:
                print(f"You don't have any {item.type} equipped.")
                action = input(f"Do you want to {Fore.GREEN}[E]quip{Fore.RESET} this {item.type} or {Fore.RED}[L]eave{Fore.RESET} it? ").lower()
            
            if action == 'e':
                self.player.equip(item)
            else:
                print(f"You leave the {item.name} behind.")

    def explore(self):
        location = random.choice(self.locations)
        print(f"You are exploring the {Fore.MAGENTA}{location}{Fore.RESET}.")
        if random.random() < 0.7:
            enemy = self.generate_enemy()
            self.battle(enemy)
        else:
            print(f"{Fore.YELLOW}You find nothing of interest.{Fore.RESET}")
        self.find_equipment()

    def rest(self):
        if random.random() < 0.2:
            print(f"{Fore.RED}You are ambushed while trying to rest!{Fore.RESET}")
            enemy = self.generate_enemy()
            if self.battle(enemy):
                heal_amount = min(20 + self.player.constitution, self.player.max_hp - self.player.hp)
                self.player.hp += heal_amount
                print(f"After fending off the attacker, you manage to rest and recover {Fore.GREEN}{heal_amount} HP{Fore.RESET}.")
            else:
                print(f"{Fore.RED}The ambush prevented you from resting.{Fore.RESET}")
        else:
            heal_amount = min(20 + self.player.constitution, self.player.max_hp - self.player.hp)
            self.player.hp += heal_amount
            print(f"You rest peacefully and recover {Fore.GREEN}{heal_amount} HP{Fore.RESET}.")

    def display_character_sheet(self):
        print(f"\n{Fore.CYAN}=== Character Sheet ==={Fore.RESET}")
        print(f"Name: {Fore.GREEN}{self.player.name}{Fore.RESET}")
        print(f"Level: {self.player.level}")
        print(f"XP: {self.player.xp}/{self.player.xp_to_next_level}")
        print(f"HP: {self.player.hp}/{self.player.max_hp}")
        print(f"Strength: {self.player.strength}")
        print(f"Dexterity: {self.player.dexterity}")
        print(f"Constitution: {self.player.constitution}")
        print(f"Intelligence: {self.player.intelligence}")
        print(f"Weapon: {self.player.weapon.name if self.player.weapon else 'None'}")
        print(f"Armor: {self.player.armor.name if self.player.armor else 'None'}")
        print(f"Stat Points Available: {self.player.stat_points}")
        print(f"{Fore.CYAN}======================{Fore.RESET}")
    def display_health_and_mana(self):
        health_percentage = self.player.hp / self.player.max_hp
        mana_percentage = self.player.mana / self.player.max_mana
        bar_length = 20
        health_bar = Fore.RED + '█' * int(bar_length * health_percentage) + Style.RESET_ALL + '░' * (bar_length - int(bar_length * health_percentage))
        mana_bar = Fore.BLUE + '█' * int(bar_length * mana_percentage) + Style.RESET_ALL + '░' * (bar_length - int(bar_length * mana_percentage))
        print(f"\n{Fore.GREEN}Player Health: {self.player.hp}/{self.player.max_hp}")
        print(f"[{health_bar}] {self.player.hp}/{self.player.max_hp} HP")
        print(f"{Fore.BLUE}Player Mana: {self.player.mana}/{self.player.max_mana}")
        print(f"[{mana_bar}] {self.player.mana}/{self.player.max_mana} MP")

    def cast_spell(self, spell, target):
        if self.player.mana >= spell.mana_cost:
            self.player.mana -= spell.mana_cost
            if spell.damage > 0:
                damage = spell.damage + (self.player.intelligence // 2)
                target.hp -= damage
                print(f"{Fore.MAGENTA}You cast {spell.name} and deal {damage} damage to the {target.name}!{Fore.RESET}")
            if spell.heal > 0:
                heal = spell.heal + (self.player.intelligence // 2)
                self.player.hp = min(self.player.max_hp, self.player.hp + heal)
                print(f"{Fore.GREEN}You cast {spell.name} and heal yourself for {heal} HP!{Fore.RESET}")
            return True
        else:
            print(f"{Fore.RED}Not enough mana to cast {spell.name}!{Fore.RESET}")
            return False

    def debug_level_up(self):
        self.player.level += 1
        self.player.max_hp += 20
        self.player.hp = self.player.max_hp
        self.player.max_mana += 10
        self.player.mana = self.player.max_mana
        self.player.stat_points += 5
        print(f"{Fore.YELLOW}Debug: Level increased to {self.player.level}{Fore.RESET}")

    def main_loop(self):
        while True:
            self.display_health_and_mana()
            action = input(f"Do you want to {Fore.YELLOW}[E]xplore{Fore.RESET}, {Fore.CYAN}[R]est{Fore.RESET}, {Fore.MAGENTA}[C]haracter Sheet{Fore.RESET}, {Fore.GREEN}[D]istribute Stat Points{Fore.RESET}" + 
                           (f", {Fore.YELLOW}[L]evel Up (Debug){Fore.RESET}" if self.debug_mode else "") +
                           f", or {Fore.RED}[Q]uit{Fore.RESET}? ").lower()
            if action == 'e':
                self.explore()
            elif action == 'r':
                self.rest()
            elif action == 'c':
                self.display_character_sheet()
            elif action == 'd':
                self.player.distribute_stat_points()
            elif action == 'l' and self.debug_mode:
                self.debug_level_up()
            elif action == 'q':
                print(f"{Fore.GREEN}Thank you for playing!{Fore.RESET}")
                break
            else:
                print(f"{Fore.YELLOW}Invalid action. Please choose a valid option.{Fore.RESET}")
            
            if self.player.hp <= 0:
                self.player_death()
                break


if __name__ == "__main__":
    game = Game()
    player_name = input("Enter your character's name: ")
    game.create_player(player_name)
    game.main_loop()
