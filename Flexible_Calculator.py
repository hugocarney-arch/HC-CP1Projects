# HC Flexible Calc 1st
import math

def get_math_type(question, *math_type):
    while True:
        math_type_choice = input(question).lower().strip()
        if math_type_choice in math_type:
            return math_type_choice
        else:
            print("Invalid input Please pick from the options and spell how spelled on the options ")

def get_numbers():
    print("Enter a number when asked then type any letter when finished adding numbers")
    numbers = []
    while True:
        user_input = input("What number do you want to calculate: ").strip().lower()
        if user_input == "done":
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input Please enter a valid number or type any letter")
    return numbers

def calculate(operation, *numbers):
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "product":
        return math.prod(numbers)

math_type_choice = get_math_type("What operation would you like to perform (sum, average, max, min, product): ", "sum", "average", "max", "min", "product")

user_numbers = get_numbers()

if len(user_numbers) == 0:
    print("Invalid Input No numbers were entered")
else:
    result = calculate(math_type_choice, *user_numbers)
    print(f"{math_type_choice}: {result}")
