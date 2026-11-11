# HC Nesting Notes

win = False
text = True

if win:
    if text:
        print("Hallalujah")
    else:
        print("Try Again")
else:
    print("Try Again")

people = ["Logan", "Daniel", "Glen", "Hugo"]

for i in range(4):
    print("Hi", end=" ")
    for person in people:
        if person == person[0]:
            print(person)
        else:
            print(f"and {person}", end=" ")
    print("\n")