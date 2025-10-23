# ###############################################
# ### SETUP ###
import turtle
# ###############################################

turtle.Screen().bgcolor("PeachPuff")
#first round
t = turtle.Turtle()
t.speed(10) #Changed the speed
t.penup()
t.goto(-100, -100)
t.color("plum")
t.pendown()

for i in range(35):
    t.forward(380) #changed the size
    t.left(110)


t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-100, -100)
t.color("cyan")
t.pendown()

for i in range(35):
    t.forward(390)
    t.left(110)

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-100, -100)
t.color("pink")
t.pendown()

for i in range(35):
    t.forward(400)
    t.left(110)


##############################
#second round
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-75, -100)
t.color("MediumOrchid")
t.pendown()

for i in range(35):
    t.forward(380)
    t.left(110)


t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-75, -100)
t.color("RoyalBlue")
t.pendown()

for i in range(35):
    t.forward(390)
    t.left(110)

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-75, -100)
t.color("LightCoral")
t.pendown()

for i in range(35):
    t.forward(400)
    t.left(110)


##############################
#third round
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-50, -100)
t.color("PaleGreen")
t.pendown()

for i in range(35):
    t.forward(380)
    t.left(110)


t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-50, -100)
t.color("LightPink")
t.pendown()

for i in range(35):
    t.forward(390)
    t.left(110)

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-50, -100)
t.color("Yellow")
t.pendown()

for i in range(35):
    t.forward(400)
    t.left(110)

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
