# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
stage.disable_ceiling()

stage.set_background("brickwall")

# Section 2 - Objects
def falling_object():    
    size = random.randint(1,20) / 10
    speed = random.randint(1,5)
    x_position = random.randint(-250,250)

    object = codesters.Sprite("balloon", x_position, -250)
    object.set_size(size)
    object.set_y_speed(speed)


stage.event_interval(falling_object, 0.5)