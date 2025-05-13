# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("corgi",0,-200)
s2 = create_sprite("character1")
# Section 3: define movement controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)

def move_up2():
	s2.setheading(90)
	s2.forward(10)
   	 
def move_down2():
	s2.setheading(270)
	s2.forward(10)
    
def move_left2():
	s2.setheading(180)
	s2.forward(10)
    
def move_right2():    
	s2.setheading(0)
	s2.forward(10)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_right2, "d")
window.onkeypress(move_left2, "a")
# Section 4: define other controls
# hide and show controls





# Section 5: game loop
window.listen()
while True:
	time.sleep(0.01)
	window.update()

