# Average_grade.py Hugo Carney 1st
classes = input("how many classes do you have ")
while True:
    try:
      class_1 = int(input("okay what is your number grade in your 1st period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_2 = int(input("okay what is your number grade in your 2nd period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_3 = int(input("okay what is your number grade in your 3rd period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_4 = int(input("okay what is your number grade in your 4th period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_5 = int(input("okay what is your number grade in your 5th period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_6 = int(input("okay what is your number grade in your 6th period class "))
      break
    except ValueError:
       print("That isn't a number please try again")

while True:
    try:
      class_7 = int(input("okay what is your number grade in your 7th period class "))
      break
    except ValueError:
       print("That isn't a number please try again")
print(f"So your average grade is {((class_1 + class_2 + class_3 + class_4 + class_5 + class_6 + class_7)/7):.2f}")