import turtle, time, random

screen = turtle.Screen()
screen.bgpic("/workspaces/Computational-Thinking-8/Backgrounds/castle.png")
def create_sprite(image_filename, x, y):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen.register_shape(image_file)
    sprite = turtle.Turtle()
    sprite.shape(image_file)
    sprite.penup()
    sprite.goto(x,y)
    return sprite


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

t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("basketball",x3,y3)
t4 = create_sprite("basketball",x4,y4)


# Section 3 - Racing
for i in range(30):
    x1 += 10
    x2 += 15
    x3 += 10
    x4 += random.randint(1,50)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.05) 

# Section 4 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
if x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
if x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")

turtle.exitonclick()
