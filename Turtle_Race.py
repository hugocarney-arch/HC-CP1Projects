# HC Turtle Race 1st

import turtle as t

screen = t.Screen()

turtle1 = t.Turtle()
turtle1.shape("turtle")
turtle1.color("blue")

turtle2 = t.Turtle()
turtle2.shape("turtle")
turtle2.color("red")

turtle3 = t.Turtle()
turtle3.shape("turtle")
turtle3.color("green")

turtle4 = t.Turtle()
turtle4.shape("turtle")
turtle4.color("yellow")

turtle5 = t.Turtle()
turtle5.shape("turtle")
turtle5.color("purple")

t.showturtle(turtle1)
t.showturtle(turtle2)
t.showturtle(turtle3)
t.showturtle(turtle4)
t.showturtle(turtle5)

turtle1.forward(100)
turtle2.forward(100)
turtle3.forward(100)
turtle4.forward(100)
turtle5.forward(100)

screen.exitonclick()
