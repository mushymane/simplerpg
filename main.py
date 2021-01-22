from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Normal Spellbook
fire = Spell("Fire", 9, 38, "black")
blizzard = Spell("Blizzard", 8, 35, "black")
thunder = Spell("Thunder", 10, 40, "black")
barrage = Spell("Ice barrage", 15, 50, "black")
blood = Spell("Blood barrage", 14, 45, "black")

# Other Spellbook
cure = Spell("Cure", 10, 20, "white")
cura = Spell("Cura", 15, 35, "white")


# Create items
karambwan = Item("Karambwan", "food", "Heals 18 HP", 18)
angler = Item("Anglerfish", "food", "Heals 22 HP", 22)
brew = Item("Sarabrew", "potion", "Heals 64 HP", 64)
restore = Item("Restore", "potion", "Restores 32 MP", 32)
sanfew = Item("Sanfew", "elixir", "Restores 33 HP and MP", 33)

cracker = Item("Cracker", "attack", "Deals 30 damage", 30)
flowers = Item("Flowers", "attack", "Deals 10 damage", 10)


# Instantiate characters
player_spells = [fire, blizzard, thunder, barrage, blood, cure, cura]
player_items = [karambwan, angler, brew, restore, sanfew, cracker, flowers]

player = Person(99, 99, 99, 99, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose an action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose a spell: ")) - 1

        # goes back on the menu
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough MP!" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.spell_type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.spell_type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " dealt", str(magic_dmg), "damage" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        # goes back on the menu
        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.item_type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("You've been hit with", enemy_dmg, "damage")

    print("----------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You have slain the enemy." + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated!" + bcolors.ENDC)
        running = False
