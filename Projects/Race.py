# Section 1 - Helper functions
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


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 =(-200)
y1 =(200)
x2 =(-200)
y2 =(100)
x3 =(-200)
y3 =(0)
x4 =(-200)
y4 =(-50)
# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("moon")
t1 = create_sprite("corgi",x1,y1)
t2 = create_sprite("fox",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("kitten",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(3,30):
    x1 += random.randint (1,20)
    x2 += random.randint (1,20)
    x3 += random.randint (1,20)
    x4 += random.randint (1,20)
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
time.sleep(0.1)


# # Section 5 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# if x1 >= x2 and x1 >= x3 and x1 >= x4:
# 	print("player 1 wins!")
# elif
# 	print("player 2 wins!")
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("Queen lizzie")
if x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("Swiper no swiping")
if x3 >= x1 and x3 >= x2 and x3 >= x4:
	print("Tung Tung Tung Tung Tung Tung Sahur")
if x4 >= x1 and x4 >= x3 and x4 >= x2:
	print("Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")  



turtle.exitonclick()




