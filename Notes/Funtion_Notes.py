# HC Funtion Notes

attempts = 0

name = input("What's Your Name: ")

def increase():
    return attempts + 1

def birthday(name, age=35):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}!")
    print("Happy Birthday to you")
    print(f"You are now {age} years old!")

def yes_no_stupid_proof(user_answer, correct):
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, increase()
    else:
        return False, user_answer, increase()

print("November")
birthday("Tia", 30)
print("December")
birthday("Tung Tung Sahur", 25)
print("June")
birthday("Hugo", 15)
birthday(name)

while True:
    capital = input("What is the capital of Utah: ")
    correct, capital, attempts = yes_no_stupid_proof(capital, ["Salt Lake City", "Slc", "Salt Lake"])
    if correct:
        print(f"Good job {capital} is the capital of Utah")
        break
    else:
        print(f"Try Again. {capital} is not the capital of Utah you have tried {attempts} times")