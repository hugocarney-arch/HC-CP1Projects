# HC Escape Room 1st

passcode = 1901

print("You wake up in a room that has a 4 digit combination lock on the door and a small picture on a table")

while True:
        action = input("Do you want to look at the picture or try to open the door  P.S if you select door you will not be allowed to stop trying the passcode until you enter the correct combination (pic/door): ")
        if action == "pic" or action == "picture" or action == "Picture" or action == "Pic" or action == " pic" or action == " picture" or action == " Picture" or action == " Pic":
            print("You look at the picture and it shows a man becoming president also in the bottom right corner there is a year scratched out next to a quote that says 'Speak softly and carry a big stick; you will go far.")
        elif action == "door" or action == "Door" or action == "DOOR" or action == " Door" or action == " door":
            print("You try to open the door, but it is locked so you try the combination lock on the door")
            break
        else:
            print("Invalid choice. Please enter 'picture' or 'door'")

while True:
    while True:
            try:
                combo_attempt1 = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
                break
            except ValueError:
                print("Invalid Input combo Has to be a number")
    if combo_attempt1 == passcode:
        print("The lock opens! You have escaped the room")
        break
    else:
        print("Incorrect combination The lock reamins closed. hint: The combo is four digits try again")
        break

while True:
    while True:
            try:
                combo_attempt2 = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
                break
            except ValueError:
                print("Invalid Input combo Has to be a number")
    if combo_attempt2 == passcode:
        print("The lock opens! You have escaped the room")
        break
    else:
        print("Incorrect combination The lock remains closed. hint: the guy on the picture is teddy rosevelt becoming president try again")
        break

while True:
    while True:
            try:
                combo_attempt3 = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
                break
            except ValueError:
                print("Invalid Input combo Has to be a number")
    if combo_attempt3 == passcode:
        print("The lock opens! You have escaped the room")
        break
    else:
        print("Incorrect combination The lock remains closed. hint: This happened around the start of the the nineteen hundreds try again")
        break

while True:
    while True:
            try:
                combo_attempt4 = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
                break
            except ValueError:
                print("Invalid Input combo Has to be a number")
    if combo_attempt4 == passcode:
        print("The lock opens! You have escaped the room")
        break
    else:
        print("Incorrect combination The lock remains closed. hint: The code is the year teddy rosevelt became president")
        break

while True:
        while True:
            try:
                combo_attempt5 = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
                break
            except ValueError:
                print("Invalid Input combo Has to be a number")

        if combo_attempt5 == passcode:
            print("The lock opens! You have escaped the room")
            break
        elif combo_attempt5 > passcode:
            print("Guess is too high of a year, try again")
        elif combo_attempt5 < passcode:
            print("Guess is too low of a year, try again")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'")