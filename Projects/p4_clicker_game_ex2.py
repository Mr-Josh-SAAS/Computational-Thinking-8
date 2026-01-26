import turtle, time, random
from utils import *

# Section 1 - setup
set_background("underwater")
fish_sprite = create_sprite("fish",-200,-200)
fish_direction = "right"

message_sprite = create_sprite("alien",-260,180)
message_sprite.hideturtle()

apples = []
food = 10
age = 0
happiness = 0
grown = False
speak_time = -100

# Section 2 - controls
def feed_fish():
    global food, apples
    if food < 10:
        food += 1
        apple = create_sprite("applecore", fish_sprite.xcor(), 250)
        apple.setheading(270)
        apples.append(apple)


window.onkeypress(feed_fish, "f")

def check_happiness():
    global happiness, i, speak_time
    if i > speak_time + 20:
        speak_time = i
        if happiness > 75:
            fish_sprite.write(f"glub :)\n",font=("Arial",20,"normal"))
        elif happiness < 25:
            fish_sprite.write(f"glub :(\n",font=("Arial",20,"normal"))
        else:
            fish_sprite.write(f"glub\n",font=("Arial",20,"normal"))

window.onkeypress(check_happiness, "h")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"Food: {food}\nHappiness: {happiness}\nAge: {age}",font=("Arial",30,"normal"))
    

    # move the fish
    x = fish_sprite.xcor()
    y = fish_sprite.ycor()

    if y > 0:
        y -= random.randint(-2,10)
    else:
        y += random.randint(-3,3)

    if fish_direction =="right":
        x += random.randint(0,6)
        if x > 340:
            fish_direction = "left"
            if grown:
                set_image(fish_sprite,"fish2_big")
            else:
                set_image(fish_sprite,"fish2")
    elif fish_direction == "left":
        x -= random.randint(0,6)
        if x < -340:
            fish_direction = "right"
            if grown:
                set_image(fish_sprite,"fish_big")
            else:
                set_image(fish_sprite,"fish")

    fish_sprite.goto(x,y)

    # move the apples
    for apple in apples:
        apple.forward(5)
        if apple.ycor() < fish_sprite.ycor():
            apples.remove(apple)
            apple.hideturtle()

    # fish message clear
    if i > speak_time + 20:
        fish_sprite.clear()

    # fish hunger
    if i % 20 == 0:
        food -= 1
    if food < 0:
        break

    # fish age
    if i % 100 == 0:
        age += 1
    
    # fish happiness
    if food > 5:
        happiness += 1
        if happiness > 100:
            happiness = 100
    else:
        happiness -= 1
        if happiness < 0:
            happiness = 0

    # grow fish 
    if age > 5:
        grown = True

    time.sleep(0.05)
    window.update()
