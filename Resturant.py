# HC Resturant 1st

menu = {
    "Main": {
        "Burger |": 8,
        "Chicken Nuggets |": 6,
        "Corn Dog |": 4,
        "Nachos |": 7

    },
    "Side": {
        "Fries |": 3,
        "Tater Tots |": 3,
        "Onion Rings |": 4,
        "Cheese Curds |": 5
    },
    "Drink": {
        "Root Beer |": 2,
        "Sprite |": 2,
        "Dr. Pepper |": 2,
        "Fanta |": 2
    }
}

print("Main Course Options:")
print(*menu["Main"])
print(" ")

print("Side Options:")
print(*menu["Side"])
print(" ")

print("Drink Options:")
print(*menu["Drink"])
print(" ")

while True:
    main_pick = input("What Main Course Do You Want (Pick 1): ").title().strip()
    if main_pick in ["Burger", "Chicken Nugget", "Corn Dog", "Nachos"]:
        break
    else:
        print("Invalid Input Please Pick From Menu And Spell How Spelled On Menu")
        continue

while True:
    side1_pick = input("What 1st Side Do You Want (Pick 1): ").title().strip()
    if side1_pick in ["Fries", "Tater Tots", "Onion Rings", "Cheese Curds"]:
        break
    else:
        print("Invalid Input Please Pick From Menu And Spell How Spelled On Menu")
        continue

while True:
    side2_pick = input("What 2nd Side Do You Want (Pick 1): ").title().strip()
    if side2_pick in ["Fries", "Tater Tots", "Onion Rings", "Cheese Curds"]:
        break
    else:
        print("Invalid Input Please Pick From Menu And Spell How Spelled On Menu")
        continue

while True:
    drink_pick = input("What Drink Do You Want (Pick 1): ").title().strip()
    if drink_pick in ["Rootbeer", "Sprite", "Dr. Pepper", "Fanta"]:
        break
    else:
        print("Invalid Input Please Pick From Menu And Spell How Spelled On Menu")
        continue

main_price = menu["Main"][main_pick + " |"]
side1_price = menu["Side"][side1_pick + " |"]
side2_price = menu["Side"][side2_pick + " |"]
drink_price = menu["Drink"][drink_pick + " |"]

total = main_price + side1_price + side2_price + drink_price

print("Your Order:")
print(f"Main Dish: {main_pick}")
print(f"Side Dishes: {side1_pick}, {side2_pick}")
print(f"Drink: {drink_pick}")
print(f"Total: {total}$")