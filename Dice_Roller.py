# H.C 1st Dice Roller

import random
while True: 
    while True:
        dice_choice = input("Choose a die to roll (d4, d6, d8, d10, d12, d20): ")
        if dice_choice in["d4", "d6", "d8", "d10", "d12", "d20"]:
            break
        else:
            print("Invalid choice. Please choose a valid die. Please note don't capitilize the letters.")
    d4 = random.randint(1, 4)
    d6 = random.randint(1, 6)
    d8 = random.randint(1, 8)
    d10 = random.randint(1, 10)
    d12 = random.randint(1, 12)
    d20 = random.randint(1, 20)

    if dice_choice == "d4":
        print(f"Okay youre number is {d4}. ")

    if dice_choice == "d6":
        print(f"Okay youre number is {d6}. ")

    if dice_choice == "d8":
        print(f"Okay youre number is {d8}. ")

    if dice_choice == "d10":
        print(f"Okay youre number is {d10}. ")

    if dice_choice == "d12":
        print(f"Okay youre number is {d12}. ")

    if dice_choice == "d20":
        print(f"Okay youre number is {d20}. ")

    replay = input("Type and hit enter to play again or type no to stop ")
    if replay == "no": 
        print("Okay bye")
        break
    else:
        continue
