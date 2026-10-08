# HC 1st Factorial Calculator
import math
while True:
    while True:
        try:
            factorial_number = int(input("What number do you want to factorial: "))
            if factorial_number >= 0:
                break
        except ValueError:
            print("Not a valid number please do a positive number No decimals")
        else: 
            print("Not a valid number please do a positive number No decimals")

    factorial_range = range(factorial_number,0, -1)

    print(" ")

    print("Factors In Factorial:")
    factor_numbers = map(int,factorial_range)

    for factor in factor_numbers:
        print(f" X {factor}", end="") 

    print(" ")
    print("Final Factroial Value:")
    print(math.factorial(factorial_number))
    print(" ")