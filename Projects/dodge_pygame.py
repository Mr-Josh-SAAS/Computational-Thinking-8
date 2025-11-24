# Section 1 - helper functions
import turtle, math, time, random
from utils import *

# Section 2 - setup
set_background("castle")
s1 = create_sprite("cardinal2",-200,0)


# Section 3 - controls
def move_up_1():
    s1.goto(s1.xcor(), s1.ycor() + 10)
def move_down_1():
    s1.goto(s1.xcor(), s1.ycor() - 10)
def move_left_1():
    s1.goto(s1.xcor() - 10, s1.ycor())
def move_right_1():
    s1.goto(s1.xcor() + 10, s1.ycor())

window.onkeypress(move_up_1, "w")
window.onkeypress(move_left_1, "a")
window.onkeypress(move_down_1, "s")
window.onkeypress(move_right_1, "d")



# y_position = random.randint(-250, 250)
# obstacle = create_sprite("basketball",300,y_position)
# obstacle.setheading(180)


# Section 4 - game loop
window.listen()
obstacles = []
lives = 3
timer = 0
while True:
    time.sleep(0.1)
    timer += 1  

    # Automatically create basketballs every 1 seconds
    if timer % 10 == 0:
        y_position = random.randint(-250, 250)
        s2 = create_sprite("basketball.gif",300,y_position)
        s2.setheading(180)
        obstacles.append(s2)
        
    # Move each basketball
    for s2 in obstacles: 
        s2.forward(10)

        # if you collide, lose a life
        if get_distance(s1,s2) < 50:
            lives -= 1
            s2.hideturtle()
            set_image(s1, "puppy")
            obstacles.remove(s2)


    window.update()

    # end the game if 0 lives
    if lives == 0:
        break

print(f"Game Over - your score was {timer}")
