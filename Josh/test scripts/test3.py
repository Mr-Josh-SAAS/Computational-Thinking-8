import turtle

screen = turtle.Screen()
screen.setup(400, 400, startx=0, starty=0)

turtle.speed(0)

move_speed = 10
turn_speed = 10

def forward():
  turtle.forward(move_speed)
def backward():
  turtle.backward(move_speed)
def left():
  turtle.left(turn_speed)
def right():
  turtle.right(turn_speed)
  
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

turtle.done()