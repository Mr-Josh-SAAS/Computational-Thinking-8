###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'red')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'pink')

s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite("computer", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("knitting", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("roof", -100, 100)
s4.set_size(0.1)

message1 = codesters.Text("Joshua Tyler Kurisko",0,220,"red")
message1 = codesters.Text("My House, My Rules, My Coffee",0,-220,"yellow")
