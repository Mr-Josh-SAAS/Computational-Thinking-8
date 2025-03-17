###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("blueaura")

q1 = codesters.Square(100,100,200,'PowderBlue')
q2 = codesters.Square(-100,100,200,'LightBlue')
q3 = codesters.Square(-100,-100,200,'LightSteelBlue')
q4 = codesters.Square(100,-100,200,'White')

s1 = codesters.Sprite("tropicalflower",100,100)
s2 = codesters.Sprite("Plane",-100,-100)
s2.set_size(0.5)
s3 = codesters.Sprite("cardinal",100,-100)
s3.set_size(0.5)
s4 = codesters.Sprite("dog",-100,100)
s4.set_size(0.1)

message1 = codesters.Text ("Tova Miette Zeppelin Buerk",0,220,"blue")
message2 = codesters.Text("A life aint a life till you live it",0,-220,"black")