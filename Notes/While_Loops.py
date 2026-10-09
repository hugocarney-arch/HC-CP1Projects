# HC While Loops 1st

import random
import time
goose = random.randint(1, 20)
duck = 1

while goose > duck:
    print("Duck")
    time.sleep(0.1)
    duck += 1
    if duck == 15:
        print("Game Over Loser")
        break
else:
    print("GOOSE! RUN!")


count = 30

while count >= 1:
    print(count)
    time.sleep(.1)
    count -= 1



    number = random.randint(1, 101)

    while True:
        while True:
            try:
                guess = int(input("Type the passcode it is a number 1 to 100: "))
                if guess < 0 or guess > 100:
                    print("Not a valid number try again")
                    continue
                break
            except:
                print("That isn't a number")
        if guess == number:
            print("You win!")
            break
        elif guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            print("You win!")
            break

