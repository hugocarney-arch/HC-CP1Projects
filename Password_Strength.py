
# DEFINE variable points as 0
points = 0

password_input = input("Welcome to the password strength checker what is your password: ")

if len(password_input) >= 8:
    points += 1

input_list = list(password_input)

if any(characters.isupper() for characters in input_list):
    points += 1

if any(characters.islower() for characters in input_list):
    points += 1

if any(characters.isnumeric() for characters in input_list):
    points += 1

if points == 0:
    print("Password Strength: Weak")

if points == 1:
    print("Password Strength: Weak")

elif points == 2 or points == 3:
    print("Password Strength: Medium")

elif points == 4:
    print("Password Strength: Strong")