import turtle, math, time, random
from utils import *

##########################################
# Project 5 Example 4
# Draw without Looking
##########################################

# Section 1: Setup
# TODO - create your player character and any other sprites
player = create_sprite("turtle3", -150, 0)
player.color("white")
player.pendown()
curtain = create_sprite("curtain", 0, 1000)


# TODO - set your background
set_background("black")

# TODO - set the starting value for your variables
still_drawing = True
sprite_list = []

# Section 2: Controls
# TODO - define your controls
def move_up():
    x = player.xcor()
    y = player.ycor() + 10
    player.goto(x, y)

def move_down():
    x = player.xcor()
    y = player.ycor() - 10
    player.goto(x, y)

def move_left():
    x = player.xcor() - 10
    y = player.ycor()
    player.goto(x, y)

def move_right():
    x = player.xcor() + 10
    y = player.ycor()
    player.goto(x, y)

def end_drawing():
    global still_drawing, sprite_list
    # set still_drawing variable to False
    still_drawing = False

    # hide all the extra curtains
    for c in sprite_list:
        c.hideturtle()

    # hide the player, move the curtain up
    player.hideturtle()
    player.penup()

    curtain.setheading(90)
    for i in range(100):
        curtain.forward(10)
        window.update()
        time.sleep(0.01)


# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")

window.onkeypress(end_drawing, "space")

# Section 2.5 - Before the game loop starts
# before the loop, an intro animation
player.write("What shape should I draw?", font=("Arial", 20, "normal"))
window.update()
time.sleep(2)
player.clear()

# move the curtain down
curtain.setheading(270)
for i in range(100):
    curtain.forward(10)
    window.update()
    time.sleep(0.01)


# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions

    # if still drawing keep creating curtains over the image, add them to the sprite_list
    if still_drawing == True and i % 10 == 0:
        c1 = create_sprite("curtain",0,0)
        sprite_list.append(c1)
    
	# TODO - make an if statement for ending the game
    # if done drawing, wait a few seconds, then end
    if still_drawing == False:
        time.sleep(5)
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
