import turtle, random

t1 = turtle.Turtle()
t1.speed(10)

turtle.Screen().bgcolor("black")
# I changed background color from khaki based on feedback

t1.penup()
t1.goto(0,-150)
t1.pendown()

# t1.color("crimson")
# for i in range(8):
#     t1.forward(100 )
#     t1.left(90)
#     t1.forward(100 )
#     t1.right(45)

# turtle.exitonclick()

colors = ["crimson","royalblue","purple","blue"]
# # i used to have a lot more oranges and yellows, but people said it would
# # look better with blues and purples
# for i in range(100):
#     # used to be 800 repeats, but got feedback there was too many lines
#     t1.forward(100 )
#     t1.left(90)
#     t1.color(random.choice(colors))
#     t1.forward(100 )
#     t1.right(44)
#     t1.color(random.choice(colors))

t2 = turtle.Turtle()
t2.speed(10)
angles = [0,60,120,180,240,300]
for i in range(30000):
    t2.setheading(random.choice(angles))
    t2.color(random.choice(colors))
    t2.forward(30)
    if t2.xcor() > 300 or t2.xcor() < -300 or t2.ycor() > 300 or t2.ycor() < -300:
        t2.penup()
        t2.goto(0,0)
        t2.pendown()

turtle.exitonclick()
