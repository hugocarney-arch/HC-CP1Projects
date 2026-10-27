# Password Strength Checker HC 1st Period

points = 0

password_input = input("Welcome to the password strength checker what is your password: ")

print("Password Assesment")

# Checks if password is more then 8 or 8 characters long and tells them if it is
if len(password_input) >= 8:
    print("Length (8+ characters): Yes")
    points += 1
else:
    print("Length (8+ characters): No")

password_input_list = list(password_input)

# Checks if password has Uppercase in it and tells them if it does
if any(characters.isupper() for characters in password_input_list):
    print("Contains Uppercase: Yes")
    points += 1
else:
    print("Contains Uppercase: No")

# Checks if password has Lowercase in it and tells them if it does
if any(characters.islower() for characters in password_input_list):
    print("Contains Lowercase: Yes")
    points += 1
else:
    print("Contains Lowercase: No")

# Checks if password has Numbers in it and tells them if it does
if any(characters.isnumeric() for characters in password_input_list):
    print("Contains Numbers: Yes")
    points += 1
else:
    print("Contains Numbers: No")

# Checks if password has Special Characters in it and tells them if it does
if any(not characters.isalnum()for characters in password_input_list):
    print("Contains Special characters: Yes")
    points += 1
else: 
    print("Contains Special characters: No")

print(f"Your password got a {points}/5 score")

# Based on the amount of points they got telling the strength of their password
if points == 0:
    print("Password Strength: Weak")

elif points == 1:
    print("Password Strength: Semi-Weak")

elif points == 2 or points == 3:
    print("Password Strength: Medium")

elif points == 4:
    print("Password Strength: Semi-Strong")

elif points == 5:
    print("Password Strength: Very Strong")

else:
    print("Some how you broke the system I guess your password is infinitely strong or incredibly horrible either way it will never be guessed")

if len(password_input) > 10:
    print("Password May Be Too Long And Hard To Remeber")