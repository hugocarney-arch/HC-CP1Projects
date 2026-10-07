# HC 1st Factorial Calculator
import math
factors = []

while True:
    try:
        factorial_number = int(input("What number do you want to factorial: "))
        if factorial_number >= 0:
            break
    except ValueError:
        print("Not a valid number please do a positive number No decimals")
    else: 
        print("Not a valid number please do a positive number No decimals")

factorial_range = range(factorial_number, 1)
print(factorial_range)

factor_numbers = map(int,factorial_range)
print(list(*factor_numbers))

print(math.factorial(factorial_number))