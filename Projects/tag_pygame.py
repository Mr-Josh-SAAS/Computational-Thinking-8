import turtle, math, time

# Section 1 - helper functions
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"./Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"./Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    return sprite




def get_distance(t1, t2):
    dx = t1.xcor() - t2.xcor()
    dy = t1.ycor() - t2.ycor()
    return math.sqrt(dx*dx + dy*dy)

window = turtle.Screen()
window.tracer(0)

# Section 2 - setup
set_background("castle")
t1 = create_sprite("cardinal2",-100,0)
t2 = create_sprite("basketball",100,0)


# Section 3 - controls
def move_up_1():
    set_image(t1, "bat")
    t1.goto(t1.xcor(), t1.ycor() + 10)
def move_down_1():
    set_image(t1, "cardinal2")
    t1.goto(t1.xcor(), t1.ycor() - 10)
def move_left_1():
    t1.goto(t1.xcor() - 10, t1.ycor())
def move_right_1():
    t1.goto(t1.xcor() + 10, t1.ycor())

window.onkeypress(move_up_1, "w")
window.onkeypress(move_left_1, "a")
window.onkeypress(move_down_1, "s")
window.onkeypress(move_right_1, "d")

def move_up_2():
    t2.goto(t2.xcor(), t2.ycor() + 10)
def move_down_2():
    t2.goto(t2.xcor(), t2.ycor() - 10)
def move_left_2():
    t2.goto(t2.xcor() - 10, t2.ycor())
def move_right_2():
    t2.goto(t2.xcor() + 10, t2.ycor())


window.onkeypress(move_up_2, "Up")
window.onkeypress(move_left_2, "Left")
window.onkeypress(move_down_2, "Down")
window.onkeypress(move_right_2, "Right")

# Section 4 - game loop
window.listen()
tagged = False
while True:
    if not tagged and get_distance(t1,t2) < 50:
        t1.color("white")
        t1.write("tag!",font = ("Arial", 40, "normal"))
        print("tag!")
        tagged = True
        t1.hideturtle()
        t2.hideturtle()
        window.update()
        time.sleep(1)
        t1.clear()
        t1.goto(-100,0)
        t2.goto(100,0)
        t1.showturtle()
        t2.showturtle()
        tagged = False



    window.update()
