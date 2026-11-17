# HC Restaurant 1st

# Makes menu dictionary
menu = {
    "Main": {
        "Burger": 8,
        "Chicken Nuggets": 6,
        "Corn Dog": 4,
        "Nachos": 7,
    },
    "Side": {
        "Fries": 3,
        "Tater Tots": 3,
        "Onion Rings": 4,
        "Cheese Curds": 5,
    },
    "Drink": {
        "Rootbeer": 2,
        "Sprite": 2,
        "Dr. Pepper": 2,
        "Fanta": 2,
    },
}

# Makes function that gets the users order
def get_choice(prompt, category):
    while True:
        choice = input(prompt).title().strip()
        if choice in menu[category]:
            return choice
        print("Invalid Input Please Pick From Menu And Spell How Spelled On Menu")

# Shows menu
print("Main Course Options:")
print(*menu["Main"])
print()
print("Side Options:")
print(*menu["Side"])
print()
print("Drink Options:")
print(*menu["Drink"])
print()

# Gets food order using function
main_pick = get_choice("What Main Course Do You Want (Pick 1): ", "Main")
side1_pick = get_choice("What 1st Side Do You Want (Pick 1): ", "Side")
side2_pick = get_choice("What 2nd Side Do You Want (Pick 1): ", "Side")
drink_pick = get_choice("What Drink Do You Want (Pick 1): ", "Drink")

# Gets prices then adds them for total
main_price = menu["Main"][main_pick]
side1_price = menu["Side"][side1_pick]
side2_price = menu["Side"][side2_pick]
drink_price = menu["Drink"][drink_pick]

total = main_price + side1_price + side2_price + drink_price

# Shows their order and the total
print("Your Order:")
print(f"Main Dish: {main_pick}")
print(f"Side Dishes: {side1_pick}, {side2_pick}")
print(f"Drink: {drink_pick}")
print(f"Total: ${total}")
