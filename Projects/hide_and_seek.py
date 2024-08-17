import math, codesters

# stage.set_background("hauntedhouse")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)
s2 = codesters.Sprite("person2",0,200)
s2.set_size(0.3)
# s2.hide()
s1.hidden = False
s2.hidden = False

def move_up(sprite):
    if not sprite.hidden:
        # sprite.set_heading(90)
        sprite.move_up(10)
        
def move_down(sprite):
    if not sprite.hidden:
        # sprite.set_heading(270)
        sprite.move_down(10)
    
def move_left(sprite):
    if not sprite.hidden:
        # sprite.set_heading(180)
        sprite.move_left(10)
    
def move_right(sprite):    
    if not sprite.hidden:
        # sprite.set_heading(0)
        sprite.move_right(10)

    
def hide(sprite):
    sprite.hide()
    sprite.hidden = True
def show(sprite):
    sprite.show()
    sprite.hidden = False
    
s1.event_key("up", move_up)
s1.event_key("down", move_down)
s1.event_key("left", move_left)
s1.event_key("right", move_right)
    
s2.event_key("w", move_up)
s2.event_key("s", move_down)
s2.event_key("a", move_left)
s2.event_key("d", move_right)
s2.event_key("q", hide)
s2.event_key("f", show)

distance = math.sqrt((s1.get_x() - s2.get_x())**2 + (s1.get_y() - s2.get_y())**2)

print("Game has started. Open GUI to play")
# for i in range(1000):
#     print(i)
#     time.sleep(0.1)
#     # distance = math.sqrt((s1.x - s2.x)**2 + (s1.y - s2.y)**2)
    
    # s1.say(f"The ghost is {math.floor(distance)} steps away",0.1)
    
    # if distance < 50 and s2.hidden:
    #     s2.show()
    #     s1.say("Found you!",3)


