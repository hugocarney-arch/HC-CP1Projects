import random

# Gives random integer between 1-10
ducks = random.randint(1,10)

# Prints there are then a random amount between 1 - 10 then says ducks
print(f"There are {ducks} ducks! ")

fruits = ["apple", "banana", "Cherry", "mango"]
choice = random.choice(fruits)
print(f"So do you like {choice} ")

# Prints a random number that starts on 2 too 10 but counts by two [2,4,6,8] but won't do ten
pens = random.randrange(2,10,2)
print(f"I have {pens} pens. ")

# Gives you a float between 0 - 1
percent = random.random()

# Prints a number that is a decimal that is 2 decimal places
print(f"You have a {percent:.2} grade. ")