# HC 1st Factorial Calculator
import math

while True:
    try:
        factorial_number = int(input("What number do you want to factorial: "))
        if factorial_number >= 0:
            break
    except ValueError:
        print("Not a valid number please do a positive number No decimals")
    else: 
        print("Not a valid number please do a positive number No decimals")

factorial_range = range(1, factorial_number + 1) 

factor_numbers = list(map(math.factorial, factorial_range))

print(factor_numbers)

full_factorial_total = factor_numbers[-1]

print(full_factorial_total)
