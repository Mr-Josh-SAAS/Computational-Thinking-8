import turtle, math, time, random
from utils import *

##########################################
# Project 5 Example 5
# Explore a Town
##########################################

# Section 1: Setup
# TODO - create your player character and any other sprites
town = create_sprite("town_map", 0, 0)
player = create_sprite("character3", 0, 0)

message_sprite = create_sprite("alien",-200,200)
message_sprite.color("yellow")
message_sprite.hideturtle()

item1 = create_sprite("fish", -500, 0)
item1.hideturtle()
item2 = create_sprite("flower", 500, 0)
item2.hideturtle()
item3 = create_sprite("pineapple", 0, -500)
item3.hideturtle()
item4 = create_sprite("stitch", 0, 500)
item4.hideturtle()

# TODO - set your background
# no background, town map is actually a sprite!

# TODO - set the starting value for your variables
items_found = 0
player_x = 0
player_y = 0
sprite_list = [town, item1, item2, item3, item4]

# Section 2: Controls
# TODO - define your controls
def move_up():
    global player_x, player_y, sprite_list
    
    # only move up if you are at player_y=550 or lower
    if player_y <= 550:
        player_y += 10

        # Move each other sprite *down* 
        for sprite in sprite_list:
            x = sprite.xcor()
            y = sprite.ycor() - 10
            sprite.goto(x, y)

def move_down():
    global player_x, player_y

    # only move down if you are at player_y=-550 or higher
    if player_y >= -550:
        player_y -= 10

        # Move each other sprite *up* 
        for sprite in sprite_list:
            x = sprite.xcor()
            y = sprite.ycor() + 10
            sprite.goto(x, y)


def move_left():
    global player_x, player_y
    
    # only move left if you are at x=-1120 or higher
    if player_x >= -1120:
        player_x -= 10

        # Move each other sprite *right* 
        for sprite in sprite_list:
            x = sprite.xcor() + 10
            y = sprite.ycor() 
            sprite.goto(x, y)

def move_right():
    global player_x, player_y
    
    # only move right if you are at x=1120 or lower
    if player_x <= 1120:
        player_x += 10

        # Move each other sprite *left* 
        for sprite in sprite_list:
            x = sprite.xcor() - 10
            y = sprite.ycor() 
            sprite.goto(x, y)

# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")


# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions
    # have the player write their coordinates
    player.clear()
    player.write(f"({player_x},{player_y})")

    # show how many items you have
    message_sprite.clear()
    message_sprite.write(f"Items: {items_found}", font=("Arial", 40, "normal"))

    # check if the player is close to each item
    if get_distance(player, item1) < 50:
        item1.showturtle()
        items_found += 1
        window.update()
        time.sleep(0.5)
        item1.hideturtle()
        item1.goto(-1000000000,0)

    if get_distance(player, item2) < 50:
        item2.showturtle()
        items_found += 1
        window.update()
        time.sleep(0.5)
        item2.hideturtle()
        item2.goto(-1000000000,0)

    if get_distance(player, item3) < 50:
        item3.showturtle()
        items_found += 1
        window.update()
        time.sleep(0.5)
        item3.hideturtle()
        item3.goto(-1000000000,0)

    if get_distance(player, item4) < 50:
        item4.showturtle()
        items_found += 1
        window.update()
        time.sleep(0.5)
        item4.hideturtle()
        item4.goto(-1000000000,0)

    
    
	# TODO - make an if statement for ending the game
    # if found all 4 items, win
    if items_found >= 4:
        message_sprite.clear()
        message_sprite.write(f"Items: {items_found}", font=("Arial", 40, "normal"))
        player.clear()
        player.color("red")
        player.write(f"I found all the items!", font=("Arial",20,"normal"))
        window.update()
        time.sleep(5)
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
