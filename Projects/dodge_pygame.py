# Section 1 - helper functions
import turtle, math, time, random
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
    window.update()
    return sprite

def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)

window = turtle.Screen()
window.tracer(0)

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

    if timer % 10 == 0:
        y_position = random.randint(-250, 250)
        s2 = create_sprite("basketball",300,y_position)
        s2.setheading(180)
        obstacles.append(s2)
        
    for s2 in obstacles: 
        s2.forward(10)
        if get_distance(s1,s2) < 50:
            lives -= 1
            s2.hideturtle()
            obstacles.remove(s2)


    window.update()

    if lives <= 0:
        break

print("Game Over")
