import turtle, time, random
from utils import *

# Section 1 - Variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = 0
x4 = -200
y4 = -100

# Section 2 - Setup
set_background("castle")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("cardinal2",x3,y3)
t4 = create_sprite("turtle2",x4,y4)

# Section 3 - Racing
for i in range(30):
    x1 += 8
    x2 += 11
    x3 += random.randint(10,16)
    x4 += random.randint(0,20)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1) 


# Section 4 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("basketball wins!")
if x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("cardinal wins!")
if x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")

turtle.exitonclick()
