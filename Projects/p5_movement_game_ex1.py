import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
s1 = create_sprite("cardinal2", -200, 0)
s2 = create_sprite("corgi", 200, 0)

# TODO - set your background
set_background("cornfield")

# TODO - set the starting value for your variables
cardinal_tags = 0
corgi_tags = 0
who_is_it = "cardinal"
sprite_list = []

# Section 2: Controls

# TODO - define your controls
def move_up_1():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x, y)


def move_down_1():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x, y)


def move_left_1():
    x = s1.xcor() - 10
    y = s1.ycor()
    s1.goto(x, y)


def move_right_1():
    x = s1.xcor() + 10
    y = s1.ycor()
    s1.goto(x, y)


def move_up_2():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x, y)


def move_down_2():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x, y)


def move_left_2():
    x = s2.xcor() - 10
    y = s2.ycor()
    s2.goto(x, y)


def move_right_2():
    x = s2.xcor() + 10
    y = s2.ycor()
    s2.goto(x, y)


# TODO - pick keys for each control
window.onkeypress(move_up_1, "w")
window.onkeypress(move_left_1, "a")
window.onkeypress(move_down_1, "s")
window.onkeypress(move_right_1, "d")

window.onkeypress(move_up_2, "Up")
window.onkeypress(move_left_2, "Left")
window.onkeypress(move_down_2, "Down")
window.onkeypress(move_right_2, "Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    # TODO - add code for automatic actions
    # automatically check if the two sprites are close. if they are, tag!
    if get_distance(s1, s2) < 100:
        if who_is_it == "cardinal":
            cardinal_tags += 1
            s1.color("red")
            s1.write("Tag, now the corgi is it!",font=("Arial",20,"normal"))
            window.update()
            time.sleep(2)
            who_is_it = "corgi"
            s1.clear()
            s1.goto(-200,0)
            s2.goto(200,0)
        elif who_is_it == "corgi":
            corgi_tags += 1
            s2.color("white")
            s2.write("Tag, now the cardinal is it!",font=("Arial",20,"normal"))
            window.update()
            time.sleep(2)
            who_is_it = "cardinal"
            s2.clear()
            s1.goto(-200,0)
            s2.goto(200,0)
            
    
	# TODO - make an if statement for ending the game
	# end if longer than 60 seconds 
    if i > 100*60:
        break

    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
print(f"Cardinal tagged corgi {cardinal_tags} times")
print(f"Corgi tagged cardinal {corgi_tags} times")
