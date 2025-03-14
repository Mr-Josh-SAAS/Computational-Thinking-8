###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("drawbridge")
mySprite = codesters.Sprite("character2" , 25 , -60)
mySprite.say("My name is jamal!")
mySprite2 = codesters.Sprite("backboard" , 75 , 25 )
mySprite3 = codesters.Sprite("Dunker" , -40 , 40)
mySprite3.say("Get posterized unc")
mysprite4 = codesters.Sprite ("hoop" , 23 , 67)