###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square (100, 100, 200, "Red") 
q2 = codesters.Square (-100, 100, 200, "blue")
q3 = codesters.Square (-100, -100, 200, "green")
q4 = codesters.Square (100, -100, 200, "yellow")

s1 = codesters.Sprite ("ring ring", 100, 100)
s2 = codesters.Sprite ("shrek", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite ("dog", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite ("pc", -100, 100)
s4.set_size(0.5)

message1 = codesters.Text("Zoren McKenzie", 0, 220, "red") 

message2 = codesters.Text("Fires hot", 0, -220, "red")