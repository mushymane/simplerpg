from classes.game import Person, bcolors
from classes.magic import Spell

# Normal Spellbook
fire = Spell("Fire", 9, 38, "black")
blizzard = Spell("Blizzard", 8, 35, "black")
thunder = Spell("Thunder", 10, 40, "black")
barrage = Spell("Ice barrage", 15, 50, "black")
blood = Spell("Blood barrage", 14, 45, "black")

# Other Spellbook
cure = Spell("Cure", 10, 20, "white")
cura = Spell("Cura", 15, 35, "white")

# Instantiate characters
player = Person(99, 99, 99, 99, [fire, blizzard, thunder, barrage, blood, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough MP!" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " dealt", str(magic_dmg), "damage" + bcolors.ENDC)

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
