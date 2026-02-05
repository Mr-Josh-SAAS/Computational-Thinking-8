import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create the turtle
T = turtle.Turtle()
T.speed(10)
T.penup()

# Draw the flag outline
T.color("black")
T.goto(-250, -200)
T.setheading(90)
T.pendown()
for _ in range(2):
    T.forward(400)
    T.right(90)
    T.forward(500)
    T.right(90)
T.penup()

# Draw the light blue background
T.goto(-250, -200)
T.setheading(90)
T.color("DeepSkyBlue")
T.begin_fill()
T.pendown()
for _ in range(2):
    T.forward(400)
    T.right(90)
    T.forward(500)
    T.right(90)
T.end_fill()
T.penup()

# Draw the dark blue shape
T.goto(-250, -200)
T.color("MidnightBlue")
T.begin_fill()
T.pendown()
T.goto(-250, 200)
T.goto(50, 200)
T.goto(-50, 0)
T.goto(50, -200)
T.goto(-250, -200)
T.end_fill()
T.penup()

# Draw the pink star
T.goto(-250, 0)
T.setheading(22.5)
T.color("White")
T.begin_fill()
T.pendown()
for i in range(8):
    T.forward(150)
    T.right(135)
T.end_fill()
T.penup()

# Move the turtle out of the way
T.goto(0, 0)

# Hide the turtle and display the window
T.hideturtle()

turtle.exitonclick()