import turtle, math, time, random
from utils import *

##########################################
# Project 5 Coding Example
##########################################

# Section 1: Setup
# TODO - create your player character and any other sprites

message_sprite = create_sprite("alien",-350,250)
message_sprite.color("black")
message_sprite.hideturtle()

# TODO - set your background

# TODO - set the starting value for your variables
sprite_list = []

# Section 2: Controls
# TODO - define your controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x, y)

def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x, y)

def move_left():
    x = s1.xcor() - 10
    y = s1.ycor()
    s1.goto(x, y)

def move_right():
    x = s1.xcor() + 10
    y = s1.ycor()
    s1.goto(x, y)

# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions

    # create a falling obstacle every .... loops
    
    

    # move each obstacle a little



    # if they get too close to player, lose a life

    # write what your variable is
    message_sprite.clear()
    message_sprite.write(f"Message: {variable}", font=("Arial",40,"normal"))


	# TODO - make an if statement for ending the game
   

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
