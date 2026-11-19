# HC Flexible Calc 1st
import math

def get_math_type(question, *math_type):
    while True:
        math_type_choice = input(question).lower().strip()
        if math_type_choice in math_type:
            return math_type_choice
        else:
            print("Invalid Input Please Pick From Options And Spell How Spelled In Options")
            continue

math_type_choice = get_math_type("What operation would you like to perform sum, average, max, min, product: ", "sum", "average", "max", "sum", "average", "max", "min", "product")

def get_numbers():
    print("It will ask you for a number and type any letter or word when you finished adding user_numbers")
    user_numbers = []
    
    while True:
        try:
            user_input = int(input("What number do you want to calculate: "))
            user_numbers.append(user_input)
        except ValueError:
            break
            
    return user_numbers

user_numbers = get_numbers()

if len(user_numbers) == 0:
    print("No user_numbers were entered.")
elif math_type_choice == "sum":
    print("Sum:", sum(user_numbers))
elif math_type_choice == "average":
    print("Average:", sum(user_numbers) / len(user_numbers))
elif math_type_choice == "max":
    print("Max:", max(user_numbers))
elif math_type_choice == "min":
    print("Min:", min(user_numbers))
elif math_type_choice == "product":
    print("Product:", math.prod(user_numbers))
    

