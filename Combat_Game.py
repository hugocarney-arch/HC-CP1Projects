# HC Combat Game 1st

import random

name = input("What's your name: ").strip().lower().capitalize()

character_type = int(input(f"What type of character are you| 1. Archer| 2. Fighter| 3. Wizard| (1, 2, 3): "))
if character_type not in [1, 2, 3]:
    print("Invalid character type Please choose 1, 2, or 3")
    exit()

character = ["Archer", "Fighter", "Wizard"]
monster_and_health_and_damage = [["Goblin", 30, 10], ["Orc", 50, 18], ["Dragon", 100, 25]]
monster_choice = random.choice(monster_and_health_and_damage)
turn_order = 1

if character_type == 1:
    health = 24
elif character_type == 2:
    health = 30
elif character_type == 3:
    health = 18

if character_type == 1:
    damage = random.randint(1, 20) + 4
elif character_type == 2:
    damage = random.randint(1, 20) + 2
elif character_type == 3:
    damage = random.randint(1, 20) + 6

wild_attack_damage = damage * 2

defense_roll = random.randint(1, 8)
defense = defense_roll
if character_type == 1:
    defense += 2
elif character_type == 2:
    defense += 2
elif character_type == 3:
    defense += 1

def attack(monster_choice):
        print(f"You rolled a {damage} to attack")
        monster_choice[1] -= damage
        print(f"The {monster_choice[0]} has {monster_choice[1]} health left")
        if monster_choice[1] <= 0:
            print(f"You have defeated the {monster_choice[0]}!")

def wild_attack(monster_choice):

    print(f"You rolled a {damage} to wild attack which is doubled and becomes {wild_attack_damage} but you also take {damage} damage")
    if wild_attack_damage >= monster_choice[2]:
        print(f"You hit the {monster_choice[0]} for {wild_attack_damage} damage")
        monster_choice[1] -= wild_attack_damage
        print(f"The {monster_choice[0]} has {monster_choice[1]} health left")
        if monster_choice[1] <= 0:
            print(f"You have defeated the {monster_choice[0]}!")

def potion(character_type):
    if character_type == 1:
        health = 24
    elif character_type == 2:
        health = 30
    elif character_type == 3:
        health = 18

    health += 9
    print(f"You drank a potion and now have {health} health")

def run():
    chance = random.randint(1, 2)
    if chance == 1:
        print("You successfully ran away")
    else:
        print("You failed to run away")

print(" ")

print(f"You encounter a {monster_choice[0]} with {monster_choice[1]} health and {monster_choice[2]} damage and he challenges you to a battle first roll a D8 to see your defense")
print(f"You rolled a {defense_roll} for your defense since you are a {character[character_type - 1]} you get a bonus of {defense - defense_roll} making your total defense {defense}")

while True:
    if character_type == 1:
        print(f"Okay {name} you are a {character[0]}")
        print(" ")
        print("Stats:")
        print(f"Health: {health}")
        print("Attack: D20 + 4")
        print("Defense: D8 + 2")
    elif character_type == 2:
        print(f"Okay {name} you are a {character[1]}")
        print(" ")
        print("Stats:")
        print(f"Health: {health}")
        print("Attack: D20 + 2")
        print("Defense: D8 + 2")
    elif character_type == 3:
        print(f"Okay {name} you are a {character[2]}")
        print(" ")
        print("Stats:")
        print(f"Health: {health}")
        print("Attack: D20 + 6")
        print("Defense: D8 + 1")

    print(" ")

    print(f"You encounter a {monster_choice[0]} with {monster_choice[1]} health and {monster_choice[2]} damage and he challenges you to a battle first roll a D8 to see your defense")
    print(f"You rolled a {defense_roll} for your defense since you are a {character[character_type - 1]} you get a bonus of {defense - defense_roll} making your total defense {defense}")

    print(" ")

    while True:
        if turn_order == 1:
            print(f"{name}'s turn")
            turn_order += 1

            print("")

            print(f"To attack roll a D20 if you want to attack| To wild attack roll a D20 if you want to wild attack and it will double the damage but also take the original damage away from your health| If you choose potion you can drink a potion to recover 9 health| If you pick try to run you have a 50% chance to get away if you try")
            print(" ")
            actions = int(input("What do you want to do? 1. Attack 2. Wild Attack 3. Drink Health Potion 4. Run: "))
            if actions not in [1, 2, 3, 4]:
                print("Invalid action Please choose 1, 2, 3, or 4")
                continue

            print(" ")
                    
            if actions == 1:
                attack(monster_choice)
                continue
            elif actions == 2:
                health -= damage
                wild_attack(monster_choice)
                continue
            elif actions == 3:
                potion(character_type)
                continue
            elif actions == 4:
                run()
                continue

            print(" ")

        if turn_order == 2:
            print(f"{monster_choice[0]}'s turn")
            turn_order -= 1
            print(f"The {monster_choice[0]} attacks you for {monster_choice[2]} damage")
            health -= monster_choice[2]
            if health <= 0:
                print(f"You have been defeated by the {monster_choice[0]}")
                break
            else:
                continue