import turtle
t = turtle.Turtle()

# setup
t.goto(-60,-20)
t.speed(10)
turtle.Screen().bgcolor("white")
for i in range (100000):
    t.forward(100)
    t.left (100)
    t.pensize(100)
    t.color("red")

turtle.exitonclick()