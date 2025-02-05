import turtle
t = turtle.Turtle()
t.penup()
t.goto(0,-200)
t.pendown()
for i in range(8):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(45)


turtle.exitonclick()
