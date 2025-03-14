###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")

mySprite = codesters.Sprite("E",100,)
mySprite .set_size(0.5)
mySprite .set_speed(2)
mySprite .set_position(40,70)
mySprite .animation_x_coords(7,9)
