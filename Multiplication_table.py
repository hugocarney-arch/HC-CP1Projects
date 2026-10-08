# HC Multiplication Table 1st
while True:
    import time
    while True:
        try:
            row = int(input("Enter how big of a multiplication table you want: "))
            if row <= 0:
                print("Please enter a positive integer.")
                continue
            elif row > 30:
                print("Please enter a number less than or equal to 30")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    for i in range(1, row + 1):  
        for x in range(1, row + 1):  
            print(f"{i * x:4}", end=" ")
            time.sleep(.001)
        print()