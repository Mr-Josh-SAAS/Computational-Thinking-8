import turtle, math
def set_background(image_filename):
    screen = turtle.Screen()
    if image_filename.endswith(".gif"):
        image_filename = image_filename[:-4]
    try:
        screen.bgpic(f"./Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"./Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    if image_filename.endswith(".gif"):
        image_filename = image_filename[:-4]

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