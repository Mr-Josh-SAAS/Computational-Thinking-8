# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()

player = codesters.Sprite("turtle")
player.set_size(0.2)
player.go_to(0,-200)
stage.disable_floor()

gameOver = False
lives = 5

# Section 2 - Objects

def falling_object():
	global gameOver
	if not gameOver:
		x_position = random.randint(-250,250)
		object = codesters.Sprite("soccerball", x_position, 250)
		object.set_size(0.4)
		object.set_y_speed(-10)
    
stage.event_interval(falling_object, 0.5)

# Section 3 - Collision

def collision(player, object):
	global lives, gameOver
	
	if object.get_image_name() == "soccerball":
		stage.remove_sprite(object)
		if lives == 0:
			print("test")
		else:
			print("test")
    	      
player.event_collision(collision)


# Section 4 - Controls



