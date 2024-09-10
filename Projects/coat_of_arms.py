###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("underwater")


q1 = codesters.Square(100,100,200, 'CornflowerBlue')
q2 = codesters.Square(-100,100,200, 'BlueViolet')
q3 = codesters.Square(-100,-100,200, 'MediumSlateBlue')
q4 = codesters.Square(100,-100,200, 'DarkOrchid')


s1 = codesters.Sprite("soccerball", 100,100)
s1.set_size(0.5)
s2 = codesters.Sprite("aaa.png", -100,-100)
s2.set_size(0.5)
s3 = codesters.Sprite("artt.png", 100,-100)
s3.set_size(0.5)
s4 = codesters.Sprite("dog", -100,100)
s4.set_size(0.1)


message1 = codesters.Text("My name is June",0,220,"red")
message2 = codesters.Text("YOLO!!!",0,-220,"black")