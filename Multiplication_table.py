# HC Multiplication Table 1st


for i in range(1, 13):  
    for x in range(1, 13):  
        
        print(f"{i * x:4}", end="")
    print()

while True:
    number_1 = int(input("What is the first number for the multiplication equation (1 - 12): "))
    if number_1 >= 1 and number_1 <= 12:
        break
    else:
        print("Not a number in 1 - 12")

while True:
    number_2 = int(input("What is the second number for the multiplication equation (1 - 12): "))
    if number_2 >= 1 and number_2 <= 12:
        break
    else:
        print("Not a number in 1 - 12")

answer = number_1 * number_2
print(f"The answer is: {answer}")