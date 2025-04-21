# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def create_sprite(image_filename, x=0, y=0):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite = turtle.Turtle()
    sprite.shape(image_file)
    sprite.penup()
    sprite.goto(x,y)
    return sprite

# Section 2 - Variables
x1 =
y1 =
x2 =
y2 =
x3 =
y3 =
x4 =
y4 =

# Section 3 - Setup
set_background("castle")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("basketball",x3,y3)
t4 = create_sprite("basketball",x4,y4)

# Section 4 - Racing
for i in range(30):
    x1 += 
    x2 += 
    x3 += 
    x4 += 

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.05) 

# Section 5 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif 
    print("player 2 wins!")


turtle.exitonclick()
