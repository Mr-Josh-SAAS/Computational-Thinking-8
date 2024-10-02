###############################################
### SETUP ###
import codesters, math
from codesters import StageClass
stage = StageClass()
###############################################

# Create a turtle sprite
turtle = codesters.Sprite("turtle")
turtle.set_size(0.2)

# Create an alien sprite
alien = codesters.Sprite("alien")
alien.set_size(0.5)

# List functions to move and control the turtle
def move_up(sprite):
    sprite.set_heading(0)
    sprite.move_up(5)

def move_down(sprite):
    sprite.set_heading(180)
    sprite.move_down(5)

def move_left(sprite):
    sprite.set_heading(90)
    sprite.move_left(5)

def move_right(sprite):
    sprite.set_heading(270)
    sprite.move_right(5)

def find(sprite):
    
    distance = round(math.sqrt((turtle.get_x() - alien.get_x())**2 + (turtle.get_y() - alien.get_y())**2),1)
    turtle.say(turtle.message, 0.1)
    alien.hide()
    alien.go_to(turtle.location[0],turtle.location[1])
    # turtle.say(math.floor(distance), 0.1)
    if distance < 30:
        turtle.go_to(0,0)
        alien.show()
        # turtle.load_image("alien")
        temp = codesters.Sprite("alien", turtle.location[0],turtle.location[1])
        turtle.say("I FOUND IT!",2)
        # stage.remove_sprite(temp)
        # turtle.load_image("turtle")
        # alien.say("You found me!",1)
        # alien.ask("Play again?")
        # turtle.ask("")
        turtle.times_found = turtle.times_found + 1
        
        turtle.location = turtle.locations[turtle.times_found]
        turtle.message = turtle.messages[turtle.times_found]

# Add the functions to the turtle on different key presses
turtle.event_key("up", move_up)
turtle.event_key("down", move_down)
turtle.event_key("left", move_left)
turtle.event_key("right", move_right)

turtle.event_key("f",find)


# set up the game
turtle.times_found = 0

turtle.locations = [
    [150, 0],
    [0,200],
    [-100,-200],
    [150,-200],
    [500,500]
    ]
turtle.messages = [
    "The alien is at (150, 0)",
    "The alien is at (0, 200)",
    "The alien is at (-100, -200)",
    "The alien started at the last location,\n but moved 250 steps in the x direction",
    ""
    ]
    
    
# alien.hide()
turtle.location = turtle.locations[turtle.times_found]
alien.go_to(turtle.location[0],turtle.location[1])
turtle.message = turtle.messages[turtle.times_found]

# while times_found < 4:
        


# alien.say("You found the alien 10 times! You win!")
