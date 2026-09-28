

age = int(input("How old are you skiba: "))
license = True

if age >= 18:
    print("You are an adult and can vote! ")
elif age >= 15 and license:
    print("You can drive but you are a minor but you are a minor so go to school ")
elif age >= 15 and not license:
    print("You could drive. . . but you haven't done the paper work also go to school ")
elif age >= 1000000000000000000000000000:
    print("You are all powerful and a ancient master of the universe ")

else:
    print("You are a minor, go to school! or go drive illegally the law is just a guide line")


win = False
hp = 0

if win or hp <= 0:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :(")
else:
    print("The game is still going")