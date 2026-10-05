#The Gusseing Game by Copilot

import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 20
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return

    print(f"Sorry! The number was {secret_number}.")
    print("Better luck next time!")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break