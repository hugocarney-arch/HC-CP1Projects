# HC Escape Room 1st
import sys

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
            print("Invalid choice. Please enter 'pic' or 'door'")

hints = [
    "The combo is four digits",
    "The guy on the picture is Teddy Roosevelt becoming president",
    "This happened around the start of the nineteen hundreds",
    "The code is the year Teddy Roosevelt became president"
]

attempt = 0

while True:
    try:
        combo_attempt = int(input("Type the combination lock if you get it wrong it will give you a hint: "))
    except ValueError:
        print("Invalid Input. Combo has to be a number.")
        continue 

    if combo_attempt == passcode:
        print("The lock opens! You have escaped the room.")
        sys.exit()
    else:
        print("Incorrect combination. The lock remains closed.")
        
        if attempt < len(hints):
            print(f"Hint: {hints[attempt]} try again")
        
        else:
            if combo_attempt > passcode:
                print("Guess is too high of a year, try again")
            elif combo_attempt < passcode:
                print("Guess is too low of a year, try again")
        
        attempt += 1