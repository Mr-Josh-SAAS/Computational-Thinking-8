# Section 1 - Your code
from utils import *
set_background("winter")

s0 = create_sprite("coa_grid",0,0)
s1 = create_sprite("rock_climbers2", 100, 100)
s2 = create_sprite("knitting2", -100, -100)
s3 = create_sprite("kitten", 100, -100)
s4 = create_sprite("computer2", -100, 100)

f1 = create_sprite("cardinal3", -220,-220)
f2 = create_sprite("cardinal3", 220,-220)
f3 = create_sprite("cardinal3", 220,220)
f4 = create_sprite("cardinal3", -220,220)


message1 = create_sprite("alien",-180,220)
message1.color("black")
message1.write("Josh Kurisko",font = ("Arial", 40, "bold"))
message1.hideturtle()

message2 = create_sprite("alien",-160,-280)
message2.color("SkyBlue")
message2.write("Python is fun!",font = ("Arial", 30, "italic"))
message2.hideturtle()



######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
