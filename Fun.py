# HC 1st 
import random
fav_class = input("What's your favorite class?: ")
print(f"Wait you really like {fav_class} class I hate that class but everyone has a opinion I guess")

while True:
    question = input("Type yes or no question: ")
    yes_no = ["Yes", "No"]
    yes_or_no = random.choice(yes_no)

    print(yes_or_no)
