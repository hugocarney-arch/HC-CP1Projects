# HC 1st Letter Grade
while True:
    fav_class = input("what's your favorite class: ").strip().title()

    while True:
        try:
            grade_percentage = int(input(f"Okay what grade do you have in percent for {fav_class}: "))
            if grade_percentage < 0:
                raise ValueError ("Only positive numbers and zero, write without a percent sign ")  
            elif grade_percentage > 200:
                print(f"{grade_percentage}% yeah right too high you liar")
            else:
                break  
        except:
            print("Not a valid grade please enter just a number without a percent sign and a whole number above 0 and below 200")

    if grade_percentage >= 94:
        print(f"You got {grade_percentage}% that's a A congrats! ")

    elif grade_percentage >= 90 and grade_percentage < 94:
        print(f"You got {grade_percentage}% that's a A- congrats! ")

    elif grade_percentage >= 87 and grade_percentage < 90:
        print(f"You got {grade_percentage}% that's a B+ congrats! ")

    elif grade_percentage >= 83 and grade_percentage < 87:
        print(f"You got {grade_percentage}% that's a B congrats! ")

    elif grade_percentage >= 80 and grade_percentage < 83:
        print(f"You got {grade_percentage}% that's a B- congrats! ")

    elif grade_percentage >= 77 and grade_percentage < 80:
        print(f"You got {grade_percentage}% that's a C+ congrats! ")

    elif grade_percentage >= 73 and grade_percentage < 77:
        print(f"You got {grade_percentage}% that's a C congrats! ")

    elif grade_percentage >= 70 and grade_percentage < 73:
        print(f"You got {grade_percentage}% that's a C- You Failure! ")

    elif grade_percentage >= 67 and grade_percentage < 70:
        print(f"You got {grade_percentage}% that's a D+ You Failure ")

    elif grade_percentage >= 67 and grade_percentage < 70:
        print(f"You got {grade_percentage}% that's a D+ You Failure ")

    elif grade_percentage >= 65 and grade_percentage < 67:
        print(f"You got {grade_percentage}% that's a D You Failure ")

    else: 
        print(f"You got {grade_percentage}% that's a F Find a new Family You Freaking Failure ")

    
    conti = int(input("Type 1 to stop doing percent to letter checker and type literally any other number to keep going: "))
    if conti == 1:
        break