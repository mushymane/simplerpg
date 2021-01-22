from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 110},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        print("You attacked for", dmg, "damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose a spell:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP:", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You have defeated the enemy." + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated!" + bcolors.ENDC)
        running = False
