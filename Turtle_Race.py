# HC Turtle Race 1st

import random
import turtle as t

screen = t.Screen()
screen.bgcolor("peru")

# Makes new line border turtles 1 - 6
line_turtle1 = t.Turtle()
line_turtle2 = t.Turtle()
line_turtle3 = t.Turtle()
line_turtle4 = t.Turtle()
line_turtle5 = t.Turtle()
line_turtle6 = t.Turtle()

# Makes new turtles 1 - 5
turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()
turtle4 = t.Turtle()
turtle5 = t.Turtle()

# Makes function to hide selected turtle
def hide_turtles(turtle):
    turtle.hideturtle()

# Makes function to show selected turtle
def show_turtles(turtle):
    turtle.showturtle()

def move_to_start(turtle, y): 
     turtle.teleport(-500, y)

# Makes function to make line border turtles
def make_line_turtle(turtle_name, y):
    turtle_name.hideturtle()
    turtle_name.speed(0)
    turtle_name.width(10)
    turtle_name.color("white")
    turtle_name.teleport(-550, y)
    turtle_name.forward(1000)


def make_racers(turtle_number, color):
    turtle_number.shape("turtle")
    turtle_number.color(color)
    turtle_number.speed(100)
    turtle_number.width(5)

# Calling function that Makes lines turtles and sets their colors 1 - 5
make_line_turtle(line_turtle1, 250)
make_line_turtle(line_turtle2, 150)
make_line_turtle(line_turtle3, 50)
make_line_turtle(line_turtle4, -50)
make_line_turtle(line_turtle5, -150)
make_line_turtle(line_turtle6, -250)

# Calling function that Makes turtles and sets their colors 1 - 5
make_racers(turtle1, "blue")
make_racers(turtle2, "red")
make_racers(turtle3, "green")
make_racers(turtle4, "yellow")
make_racers(turtle5, "purple")

# Making the finish line with a invisible turtle
endlineturtle = t.Turtle()
endlineturtle.hideturtle()
endlineturtle.width(15)
endlineturtle.teleport(450,500)
endlineturtle.right(90)
endlineturtle.forward(1000)

# Calling function on all the tu3tles to show them
hide_turtles(turtle1)
hide_turtles(turtle2)
hide_turtles(turtle3)
hide_turtles(turtle4)
hide_turtles(turtle5)

# Teleporting turtles to starting point
move_to_start(turtle1,200)
move_to_start(turtle2,100)
move_to_start(turtle3,0)
move_to_start(turtle4,-100)
move_to_start(turtle5,-200)
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
            if turtle1.xcor() > 455:
                print("Blue WINS")
                break
            elif turtle2.xcor() > 455:
                print("Red WINS")
                break
            elif turtle3.xcor() > 455:
                print("Green WINS")
                break
            elif turtle4.xcor() > 455:
                print("Yellow WINS")
                break
            elif turtle5.xcor() > 455:
                print("Purple WINS")
                break
            for turtle in turtles:
                turtle.forward(random.randint(1, 20))

# Ends progrqam when user clicks screen
t.exitonclick()