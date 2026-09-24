# HC 1st User Sign In
correct_user_name = "Skibidi Sigma"
correct_password = "12345"

while True:
    user_name = input("Please enter your User Name: ")
    password = input("Please enter your Password: ")
    if user_name == correct_user_name and password == correct_password:
        print(f"Welcome in to the secret online gambiling leaque {gender} {last_name}")
        break
    else:
        print("Sorry invalid credentials plese renter password and user name make sure to use correct capitilization") 