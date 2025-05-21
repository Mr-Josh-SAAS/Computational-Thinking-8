# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random, math
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
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle") 
s1 = create_sprite("corgi",150,20)
s2 = create_sprite("character1",-150,20)
# Section 3: define movement controls
def move_up():
	s1.setheading(90)
	s1.forward(20)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(20)
    
def move_left():
	s1.setheading(180)
	s1.forward(20)
    
def move_right():    
	s1.setheading(0)
	s1.forward(20)

def move_up2():
	s2.setheading(90)
	s2.forward(20)
   	 
def move_down2():
	s2.setheading(270)
	s2.forward(20)
    
def move_left2():
	s2.setheading(180)
	s2.forward(20)
    
def move_right2():    
	s2.setheading(0)
	s2.forward(20)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")

window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_right2, "d")
window.onkeypress(move_left2, "a")
# Section 4: define other controls
# hide and show controls





# Section 5: game loop
window.listen()
timer = 0
while True:
	time.sleep(0.01)
	timer+= 1
	window.update()
	# TODO - code for automatic actions
	
	if get_distance(s2,s1) < 30:
		print("Guy wins")
		break
		
		

	if  timer == 3000:
		print("Dog wins")	 
		break

 