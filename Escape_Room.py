# HC Escape Room 1st

passcode = "1901"

print("You wake up in a room that has a lock on the door and a small picture on a table")

action = input("Do you want to look at the picture or try to open the door (picture/door): ")
if action == "picture":
    print("You look at the picture and it shows  and in the top left corner there is a man becoming president and also in the bottom right corner there is a year scratched out")
elif action == "door":
    print("You try to open the door, but it is locked")
else:
    print("Invalid choice. Please enter 'picture' or 'door'")


combo_attempt = input("Try the combination lock now if you get it wrong it will give you a hint cobination: ")
if combo_attempt == passcode:
    print("The lock opens! You have escaped the room")
else:
    print("Incorrect combination. The lock remains closed hint: the guy on the picture is teddy rosevelt becoming president if you dont know the year he became president look it up")

while True:
    action3 = input("would you like to try to open the lock again if you get it wrong it will give you a hint (yes/no): ")
    if action3 == "yes":
        combination = input("Enter the combination for the lock: ")
        if combination == passcode:
            print("The lock opens! You have escaped the room")
            break
        else:
            print("Incorrect combination. The lock remains closed hint: the guy on the picture is teddy rosevelt becoming president if you dont know the year he became president look it up")
    elif action3 == "no":
        print("You decide not to try the lock again")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'")
