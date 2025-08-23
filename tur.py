#  #############################################
# ### SETUP ###
import turtle
 #  #############################################
t = turtle.Turtle()
# TURT TURT TURT 
t.penup ()
t.goto(-100, 0)
turtle.Screen().bgcolor("blue")
t.pendown()
t.speed(2000)
# design time its gonna make a circle, a COOL circle.
colors = ["purple", "green", "black" ,"red" ,"yellow" ,"pink" ,"gray"]
for i in range (100000):
    t.forward(200)
    t.left(50+11)
    t.right(50+122)
    t.color ( colors[i % 7])
    t.pensize(50)
    t.shapesize(10)
    #Bye Bye

    
turtle.exitonclick()