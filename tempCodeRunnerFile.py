while True:
    try:
        gpa = float(input("What is your GPA: "))
        break
    except ValueError:
        print("Not a valid GPA. Please enter a number.")

fixed_number = input("Please enter your 10-digit phone number: ").strip()
