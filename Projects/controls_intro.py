# Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



# define controls
def move_up(sprite):
    sprite.move_up(1)
        
def move_down(sprite):
    sprite.move_down(1)
    
def move_left(sprite):
    sprite.move_left(1)
    
def move_right(sprite):    
    sprite.move_right(1)


# define hide and show 
def hide(sprite):
    sprite.hide()

def show(sprite):
    sprite.show()


# make controls happen what you press a key
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
    
# hide and show controls
s1.event_key("h", hide)
s1.event_key("g", show)


# reminder message
print("Game has started. Open the screen using PORTS to play")
