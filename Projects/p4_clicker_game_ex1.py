import turtle, time, random
from utils import *

# Section 1 - setup
set_background("saas")

message_sprite = create_sprite("alien",-260,220)
message_sprite.hideturtle()

cardinals = 0
computers = 0
cost = 1000

# Section 2 - controls
def get_cardinal():
    global cardinals
    cardinals += 100
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("cardinal3",x,y)


def get_computer():
    global cardinals, computers, cost
    if cardinals >= cost:
        cost = cost * 2
        computers += 1
        x = -400 + 120*computers
        y = -250
        create_sprite("computer2",x,y)


window.onkeypress(get_cardinal, "space")
window.onkeypress(get_computer, "c")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear() 
    message_sprite.write(f"Cardinals: {cardinals}\nComputers: {computers}",font=("Arial",30,"normal"))


    cardinals += 1*computers

    time.sleep(0.01)
    window.update()
