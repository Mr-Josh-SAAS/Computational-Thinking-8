import turtle, time, random
from utils import *

# Section 1 - setup
set_background("moon")

message_sprite = create_sprite("alien",-350,140)
message_sprite.hideturtle()


s1 = create_sprite("astronaut",-200,-200)
metal = 0
rockets = 0

# Section 2 - controls
def mine():
    global metal
    metal += 10
    x = random.randint(-200,200)
    y = random.randint(-300,-200)
    m1 = create_sprite("ingot",x,y)
    time.sleep(0.3)
    m1.hideturtle()




def build_rocket():
    global metal, rockets
    if metal >= 50:
        metal -= 50
        rockets += 1
        x = random.randint(-200,200)
        y = -150
        create_sprite("rocket",x,y)


window.onkeypress(mine, "space")
window.onkeypress(build_rocket, "b")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear() 
    message_sprite.write(f"Metal: {metal}\nRockets: {rockets}",font=("Arial",30,"normal"))

    if rockets >= 5:
        s1.color("white")
        s1.write("You saved me \nfrom the moon!",font=("Arial",30,"normal"))
        window.update()
        turtle.exitonclick()
        break

    time.sleep(0.01)
    window.update()
