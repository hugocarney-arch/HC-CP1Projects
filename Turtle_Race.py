# HC Turtle Race 1st

import random
import turtle as t

# Making the finish line with a invisible turtle
endlineturtle = t.Turtle()
endlineturtle.hideturtle()
endlineturtle.teleport(450,500)
endlineturtle.right(90)
endlineturtle.forward(1000)

# Making Turtles and their colors 1 - 5
turtle1 = t.Turtle()
turtle1.shape("turtle")
turtle1.color("blue")
turtle1.width(5)

turtle2 = t.Turtle()
turtle2.shape("turtle")
turtle2.color("red")
turtle2.width(5)

turtle3 = t.Turtle()
turtle3.shape("turtle")
turtle3.color("green")
turtle3.width(5)

turtle4 = t.Turtle()
turtle4.shape("turtle")
turtle4.color("yellow")
turtle4.width(5)

turtle5 = t.Turtle()
turtle5.shape("turtle")
turtle5.color("purple")
turtle5.width(5)

# Makes function to hide selected turtle
def hide_turtles(turtle):
    turtle.hideturtle()

# Makes function to show selected turtle
def show_turtles(turtle):
    turtle.showturtle()

# Checks if the turtle has won by getting to a certain x axis
def check_winner(turtle):
    if turtle.xcor() > 455:
        return True
    else:
        return False

# Calling function on all the turtles to show them
hide_turtles(turtle1)
hide_turtles(turtle2)
hide_turtles(turtle3)
hide_turtles(turtle4)
hide_turtles(turtle5)

# Teleporting turtles to starting point
turtle1.teleport(-500,300)
turtle2.teleport(-500,150)
turtle3.teleport(-500,0)
turtle4.teleport(-500,-150)
turtle5.teleport(-500,-300)

# Calling function on all the turtles to show them
show_turtles(turtle1)
show_turtles(turtle2)
show_turtles(turtle3)
show_turtles(turtle4)
show_turtles(turtle5)

# Making list of all the turtles
turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]

# Moves turtles a random amount after it checks if any of the turtles won by getting to a certain point using the function check winner
while True:
    for x in range(1000):
        for turtle in turtles:
            if check_winner(turtle):
                print(f"{turtle.color()} WINS")
                break
            elif check_winner(turtle2):
                print(f"{turtle2.color()} WINS")
                break
            elif check_winner(turtle3):
                print(f"{turtle3.color()} WINS")
                break
            elif check_winner(turtle4):
                print(f"{turtle4.color()} WINS")
                break
            elif check_winner(turtle5):
                print(f"{turtle5.color()} WINS")
                break
            turtle.forward(random.randint(1, 20))