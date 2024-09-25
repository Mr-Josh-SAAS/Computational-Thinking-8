q1 = input("Are you a cat person or a dog person?")
if "cat" in q1:
    print("You are a cat person")
    q2 = input("Have you ever had a pet cat?")
    if "yes" in q2:
        print("That's so cool!") 
elif "dog" in q1:
    #this is a comment
    print("You are a dog person")
    q3 = input("What breed of dog is your favorite?")
    if "border collie" in q3:
        print("That's my favorite breed too!")
else:
    q4 = input("Do you like both or neither?")
    if "both" in q4:
        print("Great choice")