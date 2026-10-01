# Unit 1 Test Hugo Carney
name = input("What's your name? ").strip().capitalize()

while True:
    try:
        age = int(input("How old are you? "))
        if age >= 0:
            break
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Please use numbers not any words or letters")

job = input("What's your job ")

favorit_sport = input("What's your favorit sport? ")

print(f"Okay thats pretty cool so your name is {name} and you are a {age} year old {job} who likes {favorit_sport} .")