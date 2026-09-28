# HC 1st Letter Grade
while True:
    try:
        grade_percentage = int(input("What grade do you have in percent for math: "))
        break
    except ValueError:
        print("Not a valid grade please enter just a number without a percent sign ")

if grade_percentage >= 94 :
    print("You got an A congrats! ")
elif grade_percentage >= 90 and > 94:
    print("You got an A- congrats! ")
elif grade_percentage >= 87 and > 90:
    print("You got an B+ congrats! ")
elif grade_percentage >= 83 and > 87:
    print("You got an B congrats! ")
elif grade_percentage >= 80 and > 83:
    print("You got an B- congrats! ")
elif grade_percentage >= 77 and > 80:
    print("You got an C+ congrats! ")
elif grade_percentage >= 73 and > 77:
    print("You got an C congrats! ")
elif grade_percentage >= 70 and > 73:
    print("You got an C- You Failure! ")
elif grade_percentage >= 67 and > 70:
    print("You got an D+ You Failure ")
elif grade_percentage >= 67 and > 70:
    print("You got an D+ You Failure ")
elif grade_percentage >= 65 and > 67:
    print("You got an D You Failure ")
else:
    print("You got an F find a new family You Failure ")