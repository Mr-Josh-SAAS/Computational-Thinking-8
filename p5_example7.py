import turtle, math, time, random
from utils import *

##########################################
# Project 5 Example 7
# Collector Game
##########################################

# Section 1: Setup
# TODO - create your player character and any other sprites
player = create_sprite("cardinal3", 0, -200)

message_sprite = create_sprite("alien",-350,250)
message_sprite.color("black")
message_sprite.hideturtle()


# TODO - set your background
set_background("capybara_sunset")

# TODO - set the starting value for your variables
points = 0
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

    # every 0.5 seconds (50 loops), create a falling balloon
    if i % 50 == 0:
        x = random.randint(-300,300)
        item = create_sprite("balloon", x, 400)
        item.setheading(270)
        sprite_list.append(item)
    

    # move each balloon downward a little
    # if they get too close to player, gain a point
    for item in sprite_list:
        item.forward(5)
        if get_distance(player, item) < 100:
            points += 1

            # also hide the item and remove it
            item.hideturtle()
            sprite_list.remove(item)

    # write how many points you have
    message_sprite.clear()
    message_sprite.write(f"Points: {points}", font=("Arial",40,"normal"))


	# TODO - make an if statement for ending the game
    # if you get 20 points, win
    if points >= 20:
        player.color("purple")
        player.write("You Win!", font=("Arial", 30, "normal"))
        window.update()
        time.sleep(5)
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
