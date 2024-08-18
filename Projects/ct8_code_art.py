import turtle

t = turtle.Turtle()
t.speed(0)
t.pendown()

colors = ['red','blue','green']

for i in range(100):
    t.color(colors[i % 3])
    t.forward(100)
    t.left(91)
    