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

while True:
    main_pick = input("What Main Course Do You Want (Pick 1): ")
    if main_pick in["Burger", "Chicken Nugget", "Corn Dog", "Nachos"]:
        break
    else:
        ("Invalid Input Please Pick From Menu")
        continue

side1_pick = input("What 1st Side Do You Want (Pick 1): ")

side2_pick = input("What 2nd Side Do You Want (Pick 1): ")

drink_pick = input("What Main Course Do You Want (Pick 1): ")