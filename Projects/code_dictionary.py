# print("This is my message")

# name = input("What is your name? ")
# print(f"Hello {name} and welcome to CT8")



# print(r"  _____ ____  __  __ _____  ")
# print(r" / ____/ __ \|  \/  |  __ \ ")
# print(r"| |   | |  | | \  / | |__) |")
# print(r"| |   | |  | | |\/| |  ___/ ")
# print(r"| |___| |__| | |  | | |     ")
# print(r" \_____\____/|_|  |_|_|     ")

animal = "dog"

animal = "car"

if animal == "dog":
    print("Woof!")
elif animal == "cat":
    print("Meow")
else:
    print("Choose cat or dog")

food = 6
hunger = 0
time = 0
thirst= 0 

if animal == "dog" or animal == "puppy":
    print("Woof!")
elif animal == "cat" and food >= 5:
    print("Purrrrr")
elif food < (hunger*thirst + time):
    print("You starved - game over")
