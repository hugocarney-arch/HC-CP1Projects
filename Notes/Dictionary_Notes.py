# HC Dictionary Notes 1st

# Collections of key and value pairs

car = {
    # First item is a key. Second item is a value
    # Key : Value
    "Make": "Jeep",
    "Model": "Wrangler",
    "Color": "silver",
    "Year": 2023
}
keys = list(car.keys())
values = list(car.values())
for key in keys:
    print(f"{key} is {car[key]}")

print(values)
print(len(car))
if "Trnasmission" in car:
    print(car["transmission"])
else:
    car["Transmission"] = "automatic"

car.pop("Color")
print(car.items)
keys = list(car.keys())
for key in keys:
    print(f"{key} is {car[key]}")



avatar = {
    "water": {
        "Katara": "Water bender",
        "Soka": "Leader, Boomerang Guy, Idea Man,"
    },
    "Earth":{
        "Toph": "Earth bender, The GOAT",
        "Suki": "Warrior From Kyoshi Island",
        "Cabbage Merchant": "MY CABBAGES!!!!",
    },
    "Air":{
        "Aang": "Air bender, The Avatar"
    },
    "Fire":{
        "Zuko": "Fire Bender, Future Fire Lord",
        "Iroh": "The Actual Goat, Fire Bender, Dragon of The West",
        "Azula": "Fire Lord For 1 Hour, Amazing Fire Bender",
    }   
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Cabbage Merchant"))