import turtle, math, time, random
from utils import *

##########################################
# Project 5 Example 6
# Flappy Bird
##########################################

# Section 1: Setup
# TODO - create your player character and any other sprites
player = create_sprite("bald_eagle", -200, 0)
player.setheading(270)

message_sprite = create_sprite("alien",-300,250)
message_sprite.hideturtle()


# TODO - set your background
set_background("saas")
# TODO - set the starting value for your variables
time_alive = 0
sprite_list = []

# Section 2: Controls
# TODO - define your controls
def move_up():
    if player.ycor() < 300:
        x = player.xcor()
        y = player.ycor() + 100
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

# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")


# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions
    # increase time alive every 100 loops (one second)
    if i % 100 == 0:
        time_alive += 1

    # show how long you've been alive
    message_sprite.clear()
    message_sprite.write(f"Time Alive: {time_alive}", font=("Arial", 40, "normal"))

    # make the player fall
    player.forward(2)


    # every 100 loops (1 second), create a can
    if i % 100 == 0:
        x = 500
        y = random.randint(-300,300)
        can = create_sprite("can", x, y)
        can.setheading(180)
        sprite_list.append(can)

    # move every can left
    for can in sprite_list:
        can.forward(1)

        # if off the left edge, remove it
        if can.xcor() < -400:
            can.hideturtle()
            sprite_list.remove(can)

        # if near the player, lose the game
        if get_distance(can, player) < 100:
            player.write("GAME OVER!!!!!!", font=("Arial", 40, "normal"))
            window.update()
            time.sleep(5)
            break

    
    
	# TODO - make an if statement for ending the game
    # if you hit the bottom, you lose
    if player.ycor() < -350:
        break
    

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
