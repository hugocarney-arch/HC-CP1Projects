# HC Turtle Race 1st

import random
import turtle as t

endlineturtle = t.Turtle()
endlineturtle.hideturtle()
endlineturtle.teleport(450,500)
endlineturtle.right(90)
endlineturtle.forward(1000)

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

turtle1.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()
turtle4.hideturtle()
turtle5.hideturtle()

turtle1.teleport(-500,300)
turtle2.teleport(-500,150)
turtle3.teleport(-500,0)
turtle4.teleport(-500,-150)
turtle5.teleport(-500,-300)

turtle1.showturtle()
turtle2.showturtle()
turtle3.showturtle()
turtle4.showturtle()
turtle5.showturtle()

turtle1.down()
turtle2.down()
turtle3.down()
turtle4.down()
turtle5.down()

turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]

while True:
    for x in range(1000):
        for turtle in turtles:
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
            turtle.forward(random.randint(1, 20))