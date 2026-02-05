import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")

# move to stripe 1
t.goto(-250, -100)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(50)
t.left(90)
t.forward(500)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()


# blue square
t.goto(-250, 100)
t.color("blue")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

turtle.exitonclick()
