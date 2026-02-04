import turtle, random
t = turtle.Turtle()
turtle.Screen().bgcolor("orange")
t.penup()
t.goto(100, 0)
t.pendown()
t.speed(100)
colors = ["red","maroon","brown","black"]
for i in range(200000):
    t.color( colors[i%4])
    t.forward(i)
    t.left(90)

turtle.exitonclick()