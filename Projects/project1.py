###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("spring")
q1 = codesters.Square(100,100,200, 'lavender')
q2 = codesters.Square(-100,100,200, 'linen')
q3 = codesters.Square(-100,-100,200, 'seashell')
q4 = codesters.Square(100,-100,200, 'thistle')

s1 = codesters.Sprite("pointe", 100, 100)
s1.set_size(0.3)

s2 = codesters.Sprite("blair", -100, -100)
s2.set_size(0.2)

s3 = codesters.Sprite("crochet", 100, -100)
s3.set_size(0.5)

s4 = codesters.Sprite("nessa", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Emma Leung", 0, 220, "LightSteelBlue")
message2= codesters.Text("Is it better to speak or die?", 0, -220, "LightSteelBlue")