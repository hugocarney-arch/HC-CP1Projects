# HC Combat Game 1st

name = input("What's your name").strip().lower().capitalize()
print(name)

character_type = input(f"What type of character are you| 1. Archer| 2. Fighter| 3. Magician")

if character_type == 1:
    print("You are a Archer")