###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("footballfield")
q4 = codesters.Square(-100, 100, 200, 'green')
q1 = codesters.Square(100 , 100 , 200, 'blue')
q3 = codesters.Square(-100, -100, 200, 'red')
q2 = codesters.Square(100, -100, 200, 'yellow')
mySprite = codesters.Sprite("seahawk" , -100 , 100)
mySprite.set_size(0.75)
mySprite.say("12th man")
mySprite2 = codesters.Sprite("planetzebulon" , 100 , 100)
mySprite2.set_size(0.75)
mySprite3 = codesters.Sprite("odea2" , -100, -100)
mySprite3.set_size(0.8)
mySprite4 = codesters.Sprite("football_lax" , 100, -100)
mySprite4.set_size(0.6)
mySprite3.say("I am Theo Sterling")
mySprite2.say("planet Zebulon")