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
turtle1.color("Blue")
turtle1.speed(100)
turtle1.width(5)

turtle2 = t.Turtle()
turtle2.shape("turtle")
turtle2.color("Red")
turtle2.speed(100)
turtle2.width(5)

turtle3 = t.Turtle()
turtle3.shape("turtle")
turtle3.color("Green")
turtle3.speed(100)
turtle3.width(5)

turtle4 = t.Turtle()
turtle4.shape("turtle")
turtle4.color("Yellow")
turtle4.speed(100)
turtle4.width(5)

turtle5 = t.Turtle()
turtle5.shape("turtle")
turtle5.color("Purple")
turtle5.speed(100)
turtle5.width(5)

# Makes function to hide selected turtle
def hide_turtles(turtle):
    turtle.hideturtle()

# Makes function to show selected turtle
def show_turtles(turtle):
    turtle.showturtle()

def move_to_start(turtle, y): 
     turtle.teleport(-500, y)

# Calling function on all the tu3tles to show them
hide_turtles(turtle1)
hide_turtles(turtle2)
hide_turtles(turtle3)
hide_turtles(turtle4)
hide_turtles(turtle5)

# Teleporting turtles to starting point
move_to_start(turtle1,300)
move_to_start(turtle2,150)
move_to_start(turtle3,0)
move_to_start(turtle4,-150)
move_to_start(turtle5,-300)
# Calling function on 3ll the turtles to show them
show_turtles(turtle1)
show_turtles(turtle2)
show_turtles(turtle3)
show_turtles(turtle4)
show_turtles(turtle5)

# Making list of all the turtles
turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]

# Moves turtles a random amount after it checks if any of the turtles won by getting to a certain point using the function check winner
while True:
            if turtle1.xcor() > 452:
                print("Blue WINS")
                break
            elif turtle2.xcor() > 452:
                print("Red WINS")
                break
            elif turtle3.xcor() > 452:
                print("Green WINS")
                break
            elif turtle4.xcor() > 452:
                print("Yellow WINS")
                break
            elif turtle5.xcor() > 452:
                print("Purple WINS")
                break
            for turtle in turtles:
                turtle.forward(random.randint(1, 20))

# Ends progrqam when user clicks screen
t.exitonclick()