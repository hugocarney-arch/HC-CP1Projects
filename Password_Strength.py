
# DEFINE variable points as 0
points = 0

password_input = input("Welcome to the password strength checker what is your password: ")

print("Password Assesment")

if len(password_input) >= 8:
    print("Length (8+ characters): Yes")
    points += 1
else:
    print("Length (8+ characters): No")

password_input_list = list(password_input)

if any(characters.isupper() for characters in password_input_list):
    print("Contains Uppercase: Yes")
    points += 1
else:
    print("Contains Uppercase: No")

if any(characters.islower() for characters in password_input_list):
    print("Contains Lowercase: Yes")
    points += 1
else:
    print("Contains Lowercase: No")

if any(characters.isnumeric() for characters in password_input_list):
    print("Contains Numbers: Yes")
    points += 1
else:
    print("Contains Numbers: No")

if any(not characters.isalnum()for characters in password_input_list):
    print("Contains Special characters: Yes")
    points += 1
else: 
    print("Contains Special characters: No")

print(f"Your password got a {points}/5 score")

if points == 0:
    print("Password Strength: Weak")

elif points == 5:
    print("Password Strength: Strong")

elif points == 2 or points == 3:
    print("Password Strength: Medium")

elif points == 4:
    print("Password Strength: Strong")

elif points == 5:
    print("Password Strength: Very Strong")

else:
    print("Some how you broke the system I guess your password is infinitely stron or incredibly horrible either way it will never be guessed")