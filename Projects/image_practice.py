###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


mySprite = codesters.Sprite("bat",100,0)
mySprite.say("i love subway!")

sprite2 = codesters.Sprite("fox",-100,0)
sprite2.set_size(0.3)
sprite2.say("soccer is fun!")