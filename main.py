from random import randrange, random

# HP, Atk, Def, Spe, Agi, Int
classes = {
    "warrior": [8, 8, 6, 1, 3, 2, 4],
    "mage": [8, 2, 3, 6, 3, 6, 5],
    "archer": [6, 5, 2, 2, 7, 4, 6],
    "thief": [6, 6, 2, 2, 7, 6, 8]}

mobs = {
    "Neville": [4, 4, 2, 4, 4, 4, 4],
    "Creeper (aw man)": [1, 7, 2, 2, 2, 2, 2],
    "James": [4, 2, 6, 2, 6, 4, 6],
    "Ghoul": [3, 5, 6, 2, 2, 2, 1],
    "Barry (63)": [3, 3, 3, 2, 2, 2, 10],
    "Boris": [2, 2, 2, 2, 2, 2, 1],
    "Juan": [10, 2, 2, 2, 2, 2, 1],
    "Asoka": [6, 6, 4, 4, 3, 6, 8]}

global position
position = 1

global player_alive
player_alive = True


def chooseClass():
    classname = input("please enter the name of the class you wish to select")
    try:
        return classes[classname]
    except:
        print("not a valid class")
        chooseClass()


def selection():
    name = input("Please enter your character name")
    stats = chooseClass()
    if input("confirm choice y/n") != "y":
        return selection()
    return {
        "Name": name,
        "HP": stats[0],
        "Attack": stats[1],
        "Defence": stats[2],
        "Special": stats[3],
        "Agility": stats[4],
        "Intelligence": stats[5],
        "Luck": stats[6]
    }


def menu():
    print("**********DND*********")
    print(classes)
    player = selection()
    print(player)
    return player


def combat_loop(player_stat_input):  # pass monster info and player info?

    player_stats = {
        "Name": player_stat_input["Name"],
        "HP": player_stat_input["HP"],
        "Attack": player_stat_input["Attack"],
        "Defence": player_stat_input["Defence"],
        "Special": player_stat_input["Special"],
        "Agility": player_stat_input["Agility"],
        "Intelligence": player_stat_input["Intelligence"],
        "Luck": player_stat_input["Luck"],
    }

    # for stat in player_stat_input:
    #    player_stats[stat] = player_stat_input[stat]

    mob_choice = random.choice(list(mobs.items()))
    print(mob_choice)
    mob_stats = {
        "Name": name,
        "HP": mobs[mob_choice][0],
        "Attack": mobs[mob_choice][1],
        "Defence": mobs[mob_choice][2],
        "Special": mobs[mob_choice][3],
        "Agility": mobs[mob_choice][4],
        "Intelligence": mobs[mob_choice][5],
        "Luck": mobs[mob_choice][6]
    }
    is_over = False
    while ~is_over:
        playerIn = int(input("Select action:\n1: Attack  2: Special attack 3: Run "))

        if player_stats["Agility"] >= mob_stats["Agility"]:
            print(player_stats["Name"], "'s turn!")
            is_over = perform_action(player_stats, mob_stats, playerIn)
            if is_over:
                break
            print(mob_stats["Name"], "'s turn!")
            is_over = perform_action(mob_stats, player_stats, playerIn)
        else:
            print(mob_stats["Name"], "'s turn!")
            is_over = perform_action(mob_stats, player_stats, playerIn)
            if is_over:
                break
            print(player_stats["Name"], "'s turn!")
            is_over = perform_action(player_stats, mob_stats, playerIn)
        print(is_over)
        if is_over:
            break
        print(player_stats, "\n", mob_stats)

    if player_stats["HP"] == 0:
        print(player_stats["Name"], " was defeated by", mob_stats["Name"], " (oh no!)")
        global player_alive
        player_alive = False

    elif mob_stats["HP"] == 0:
        print("Enemy ", mob_stats["name"], " was defeated!")


def perform_action(entity_acting, entity_passive, ch):
    if ch == 1:  # Regular attack logic
        print(entity_acting["Name"], " is attacking ", entity_passive["Name"], "!")
        damage = entity_acting["Attack"] // (entity_passive["Defence"] / 2)
        entity_passive["HP"] = entity_passive["HP"] - damage

    elif ch == 2:  # Special attack logic
        print(entity_acting["Name"], " is attacking with magic!")
        damage = entity_acting["Special"] // (entity_passive["Defence"] / 2)
        entity_passive["HP"] = entity_passive["HP"] - damage

    elif ch == 3:  # Run away logic
        print(entity_acting["Name"], " is trying to run away!")
        chance = randrange(0, 20)
        if chance <= 10 - entity_acting["Luck"] // 4:
            print(entity_acting["Name"], " has escaped!")
            position -= 1
            return
        else:
            print(entity_acting["Name"], " has failed to escape!")

    else:
        print("Unknown choice")

    if entity_passive["HP"] <= 0:  # If HP reaches 0, then they have been defeated
        # print(entity_passive["Name"], " was defeated!")
        return True
    else:
        return False


def enemyortreasure(currPlayerStats):
    chance = randrange(0, 20)
    if chance <= 10 - currPlayerStats.get("Luck") // 2:
        print("You have encountered an enemy")
        combat_loop(currPlayerStats)
        return
    else:
        print("You have found treasure")
        for x in currPlayerStats.values():
            if type(x) == int:
                x += 1
        return


if __name__ == '__main__':
    currPlayerStats= menu()
    print(player_alive)
    while player_alive:
        direction = input("Would you like to move forwards or backwards? ")
        if direction == 'forwards':
            position += 1
            enemyortreasure(currPlayerStats)
        if direction == 'backwards':
            if position == 1:
                print("You cannot move backwards any further")
            else:
                position -= 1
                # movement()
        else:
            print("That is not a valid choice.")

    print(" Game over! Thanks for playing! You died in room number " + str(position) + "!")
