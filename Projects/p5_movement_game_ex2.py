import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
spotlight = create_sprite("circle", 0, 0)
player = create_sprite("character2", 0, 0)

message_sprite = create_sprite("alien",-300,200)
message_sprite.color("red")
message_sprite.hideturtle()

# TODO - set your background
set_background("black")

# TODO - set the starting value for your variables
time_alive = 0
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


# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions
    # increase time alive once every 100 loops (once a second)
    if i % 100 == 0:
        time_alive += 1

    # move the spotlight randomly every loop
    turn_degrees = random.randint(-15,15)
    spotlight.left(turn_degrees)
    spotlight.forward(1)
            
    
	# TODO - make an if statement for ending the game
	# if you get far from the center of the spotlight, end the game
    if get_distance(player, spotlight) > 150:
        message_sprite.write(f"I survived for {time_alive} seconds", font=("Arial",40,"normal"))
        window.update()
        time.sleep(5)
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
