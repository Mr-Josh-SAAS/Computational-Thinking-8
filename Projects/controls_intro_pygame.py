# Section 1 - Helper functions (DON'T CHANGE!!)
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

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)



# Section 3: define controls
def move_up():
    # s1.goto(s1.xcor(), s1.ycor() + 10)
    s1.setheading(90)
    s1.forward(10)
        
def move_down():
    # s1.goto(s1.xcor(), s1.ycor() - 10)
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    # s1.goto(s1.xcor() - 10, s1.ycor())
    s1.setheading(180)
    s1.forward(10)
    
def move_right():    
    # s1.goto(s1.xcor() + 10, s1.ycor())
    s1.setheading(0)
    s1.forward(10)

# Section 4: bind controls to specific keys
window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")

# Section 5: define other controls
# hide and show controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# teleport and reset controls
def teleport(x,y):
    s1.goto(x,y)
def reset():
    s1.goto(0,0)

window.onscreenclick(teleport)
window.onkeypress(reset, "r")

# # car movement controls
# def left():
#     s1.tilt(5)
#     s1.left(5)
# def right():
#     s1.tilt(-5)
#     s1.right(5)
# def forward():
#     s1.forward(10)
# def backward():
#     s1.backward(5)

# window.onkeypress(left,"q")
# window.onkeypress(right,"e")
# window.onkeypress(forward,"n")
# window.onkeypress(backward,"m")

# drawing
def draw():
    s1.pendown()
def stop_drawing():
    s1.penup()
def erase():
    s1.clear()
def red_pen():
    s1.color("red")
def green_pen():
    s1.color("green")

window.onkeypress(draw, "c")
window.onkeypress(stop_drawing, "x")
window.onkeypress(erase, "z")
window.onkeypress(red_pen, "o")
window.onkeypress(green_pen, "p")



# Section 6: game loop
window.listen()
while True:
    time.sleep(0.01)
    window.update()
