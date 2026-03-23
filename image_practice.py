# Section 1 - Your code
from utils import *
set_background("winter")

s1 = create_sprite("cardinal", 100, 100)
s2 = create_sprite("cardinal", -100, 100)
s2 = create_sprite("cardinal", -100, -100)
s2 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Your Name",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()