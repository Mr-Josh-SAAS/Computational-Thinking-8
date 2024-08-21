#### Setup ####
import codesters
stage.set_background("moon")
stage.disable_floor()
bird = codesters.Sprite("cardinal")
bird.set_size(0.5)
bird.go_to(0,-200)

# Lives

playing = True
lives = 3
# lives_display = codesters.Display(lives, -200, 150)

#### Movement Keys ####

# Right Key
def go_right():
    global playing
    if playing:
        bird.move_right(10)
    
bird.event_key("right", go_right)
        
# Left Key
def go_left():
    global playing
    if playing:
        bird.move_left(10)
        
bird.event_key("left", go_left)

#### Asteroids ####

def asteroid_fall():
    global playing, lives
    if playing:
        x_position = random.randint(-250,250)
        asteroid = codesters.Sprite("rock", x_position, 300)
        # asteroid.set_size(0.4)
        # asteroid.move_down(600)
        asteroid.set_y_speed(-10)
        # print("test")
        print(lives)
    
stage.event_interval(asteroid_fall, 5)

# Collision

# def collision(s1, s2):
#     global lives
# #     if s2.get_image_name() == "rock":
#     lives -= 1
# # #         lives_display.update(lives)
# # #         stage.remove_sprite(s2)
# # #         if lives == 0:
# # #             global playing
# # #             playing = False
        
# bird.event_collision(collision)



