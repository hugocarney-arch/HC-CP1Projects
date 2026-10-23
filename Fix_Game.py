# HC 1st Fix The Game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: # Mssing a colon to show that it is linked with the line under it so I added a colon
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round:",  scores) # It had it adding the variable which tryed to add the int to the print statement which isn't possible so I switched out for a comma. Syntax Error

total = 0
for score in scores:
    # Got rid of total because it was resetting total to zero. Logic Error
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(0, rounds): # Had a minus one which took away from the actual number of rounds and started at one when index starts at zero so I replaced it with 0 to rounds. Logic Error
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")