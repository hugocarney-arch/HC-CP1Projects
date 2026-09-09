# H.C 1st Idiot Proof 

first_name = input("What's your first name: ").strip().capitalize()
last_name = input("Okay what about your last: ").strip().capitalize()
full_name = (f" {first_name} {last_name} ")
print("Okay")

fixed_number = input("Please enter your 10-digit phone number: ").strip()
while True:
    if fixed_number.isdigit() and len(fixed_number) == 10:
        phone_number = f"{fixed_number[:3]} {fixed_number[3:6]} {fixed_number[6:]}"
        break
    else:
        print("Invalid input. Please enter a valid 10-digit phone number.")

while True:
    try:
        gpa = float(input("What is your GPA: "))
        break
    except ValueError:
        print("Not a valid GPA. Please enter a number.")

print(f"Okay so your full name is: {full_name}")
print(f"Your phone number is: {phone_number}")
print(f"Your GPA is: {gpa}")