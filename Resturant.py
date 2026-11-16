# HC Resturant 1st

menu = {
    "Main": {
        "Burger|": 5,
        "Chicken Nuggets|": 4,
        "Corn Dog|": 3,
        "Nachos|": 4

    },
    "Side": {
        "Fries|": 2,
        "Tater Tots|": 2,
        "Onion Rings|": 2,
        "Cheese Curd|": 2
    },
    "Drink": {
        "Root Beer|": 3,
        "Sprite|": 3,
        "Dr. Pepper|": 3,
        "Fanta|": 3
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