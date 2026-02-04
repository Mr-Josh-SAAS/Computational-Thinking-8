import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
mario = create_sprite("mario", 0, -200)

# TODO - set your background
set_background("moon")

# TODO - set the starting value for your variables
lives = 5
sprite_list = []

# Section 2: Controls
# TODO - define your controls
def move_up():
    x = mario.xcor()
    y = mario.ycor() + 10
    mario.goto(x, y)

def move_down():
    x = mario.xcor()
    y = mario.ycor() - 10
    mario.goto(x, y)

def move_left():
    x = mario.xcor() - 10
    y = mario.ycor()
    mario.goto(x, y)

def move_right():
    x = mario.xcor() + 10
    y = mario.ycor()
    mario.goto(x, y)

# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_left, "Left")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    # TODO - add code for automatic actions

    # every 0.5 seconds (50 loops), create a falling obstacle
    if i % 50 == 0:
        my_image = random.choice(["sodacan","pineapple","milkjug","ingot"])
        x = random.randint(-300,300)
        obstacle = create_sprite(my_image, x, 400)
        obstacle.setheading(270)
        sprite_list.append(obstacle)
    

    # move each obstacle downward a little
    # if they get too close to mario, lose a life
    for obstacle in sprite_list:
        obstacle.forward(5)
        if get_distance(mario, obstacle) < 100:
            lives -= 1

            # also hide the obstacle and remove it
            obstacle.hideturtle()
            sprite_list.remove(obstacle)



	# TODO - make an if statement for ending the game
    # if out of lives, end the game
    if lives <= 0:
        mario.color("purple")
        mario.write("Oh no!", font=("Arial", 30, "normal"))
        window.update()
        time.sleep(5)
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
