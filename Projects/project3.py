# Project 3 Example
import turtle
t = turtle.Turtle()

t.penup()
t.goto(-100, -100)
# here is where i set the color to red
t.color("red")
t.pendown()

# here is where im drawing the square
for i in range(300000):
    t.forward(100)
    t.left(91)



turtle.exitonclick()
