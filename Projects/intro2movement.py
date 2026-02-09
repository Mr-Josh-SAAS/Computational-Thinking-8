import time, turtle, random
from utils import *

# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)



# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 2
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 2
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 2
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 2
    y = s1.ycor() 
    s1.goto(x,y)

# bind controls to specific keys
window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")

# Section 3: define other controls
# hide and show controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# teleport and reset controls
def teleport(x,y):
    s1.goto(x,y)
def reset():
    s1.goto(0,0)

window.onscreenclick(teleport)
window.onkeypress(reset, "r")

# # car movement controls
# def left():
#     s1.tilt(5)
#     s1.left(5)
# def right():
#     s1.tilt(-5)
#     s1.right(5)
# def forward():
#     s1.forward(10)
# def backward():
#     s1.backward(5)

# window.onkeypress(left,"q")
# window.onkeypress(right,"e")
# window.onkeypress(forward,"n")
# window.onkeypress(backward,"m")

# drawing
def draw():
    s1.pendown()
def stop_drawing():
    s1.penup()
def erase():
    s1.clear()
def red_pen():
    s1.color("red")
def green_pen():
    s1.color("green")

window.onkeypress(draw, "c")
window.onkeypress(stop_drawing, "x")
window.onkeypress(erase, "z")
window.onkeypress(red_pen, "o")
window.onkeypress(green_pen, "p")



# Section 6: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()
