# print("This is my message")

# name = input("What is your name? ")
# print(f"Hello {name} and welcome to CT8")



# print(r"  _____ ____  __  __ _____  ")
# print(r" / ____/ __ \|  \/  |  __ \ ")
# print(r"| |   | |  | | \  / | |__) |")
# print(r"| |   | |  | | |\/| |  ___/ ")
# print(r"| |___| |__| | |  | | |     ")
# print(r" \_____\____/|_|  |_|_|     ")

# animal = "dog"

# animal = "car"

# if animal == "dog":
#     print("Woof!")
# elif animal == "cat":
#     print("Meow")
# else:
#     print("Choose cat or dog")

# food = 6
# hunger = 0
# time = 0
# thirst= 0 

# if animal == "dog" or animal == "puppy":
#     print("Woof!")
# elif animal == "cat" and food >= 5:
#     print("Purrrrr")
# elif food < (hunger*thirst + time):
#     print("You starved - game over")


# for i in range(3):
#     print("Hello")

# print("Goodbye")


# import turtle
# t1 = turtle.Turtle()


# t1.forward(200)
# t1.left(90)
# t1.forward(100)

# turtle.exitonclick()

# import turtle
# t2 = turtle.Turtle()

# t2.color( "pink" )
# turtle.Screen().bgcolor("purple")

# t2.forward(200)
# t2.left(90)

# t2.penup()
# t2.forward(100)
# t2.left(120)

# t2.color("skyblue")
# t2.pendown()
# t2.forward(100)

# turtle.exitonclick()




# t2.begin_fill()
# for i in range(3):
#     t2.forward(100)
#     t2.left(120)
# t2.end_fill()

import turtle
t = turtle.Turtle()
t.speed(0)
n = 45
distance = 50
inside_angle = 120

# # Rotating Shape
# for i in range( n ):
#     t.forward( distance )
#     t.left( inside_angle + 1)

# # Growing Shape
# for i in range( n ):
#     t.forward( distance + 2*i)
#     t.left( inside_angle )

# Color Changing Shape
colors = ["pink","cyan","gray"]
for i in range( n ):
    t.color( colors[ i % 3 ] )
    t.forward( distance+i)
    t.left( inside_angle )

turtle.exitonclick()
