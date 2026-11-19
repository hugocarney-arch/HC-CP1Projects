# HC Flexible Calc 1st

def get_math_type(question, *math_type):
    while True:
        math_type_choice = input(question).lower().strip()
        if math_type_choice in math_type:
            return math_type_choice
        else:
            print("Invalid Input Please Pick From Options And Spell How Spelled In Options")
            continue

math_type_choice = get_math_type("What operation would you like to perform sum, average, max, min, product: ", "sum", "average", "max", "sum", "average", "max", "min", "product")

print("It will ask you for a number and type any letteror word when you finished adding numbers")

while True:
  try:
    user_input = input("What number do you want to calculate: ")
    if user_input >= 0 or user_input <= 0:
       continue
  except ValueError:
    break