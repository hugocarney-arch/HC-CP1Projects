# HC, 1st Lists, Tuples, and Sets

# Lists
siblings = ["Aiden", "Ellie"]
length = len(siblings)
print(f"My older brother is {siblings[0]}")
print(*siblings)
print(f"The youngest is {siblings[-1]}")
siblings.append("Hugo")
siblings.insert(4, "Rocket")
siblings.extend(["Israel", "James"])
siblings.remove("Hugo")
print(*siblings)

# Tuples
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Sudies", "US 1", "US 2", "World Civ", "World Geography", "CCA Busisness")
print(subjects[0])
print(*subjects)

# Sets
visited = {"Texas", "Ohio", "Minnesoda", "Virginia", "D.C", "Utah", "California", "Nevada"}
print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)