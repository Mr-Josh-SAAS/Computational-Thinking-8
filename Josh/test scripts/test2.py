import turtle
import time


screen = turtle.Screen()

# # this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400, startx=0, starty=0)
screen.bgpic("space.gif")

img = "rocketship.gif"
screen.addshape(img)
turtle.shape(img)
turtle.color("red")
turtle.speed(100)
turtle.shapesize(20)

turtle.pendown()
for i in range(100):
  time.sleep(1)
  print(i)
  turtle.forward(5*i + 10)
  turtle.left(90)

# import tkinter as tk

# # Tkinter Window
# root_window = tk.Tk()
