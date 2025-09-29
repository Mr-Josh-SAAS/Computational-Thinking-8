# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

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
window = turtle.Screen()
window.tracer(0)

# Section 2 - Variables
# TODO - add starting values for all the variables
x1 =
y1 =
x2 =
y2 =
x3 =
y3 =
x4 =
y4 =


# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("basketball",x3,y3)
t4 = create_sprite("basketball",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# for i in range(3):
#     x1 +=
#     x2 +=
#     x3 +=
#     x4 +=

#     t1.goto(x1, y1)
#     t2.goto(x2, y2)
#     t3.goto(x3, y3)
#     t4.goto(x4, y4)
#     time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# if x1 >= x2 and x1 >= x3 and x1 >= x4:
#     print("player 1 wins!")
# elif
#     print("player 2 wins!")


turtle.exitonclick()
