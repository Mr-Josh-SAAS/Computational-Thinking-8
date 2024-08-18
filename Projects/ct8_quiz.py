print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Example 1: Quiz")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
score = 0
# question 1
answer1 = input("What does a cow say?\n")
if answer1 == "moo":
    print("Correct!")
    score += 1
    
else:
    print("Wrong!")

# question 2
answer2 = input("What does a dog say?\n")
if answer2 == "bark" or answer2 == "arf" or answer2 == "woof":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


# question 3
answer3 = input("Do you like cats or dogs more?\n")
if answer3 == "dogs":
    print("My favorite type of dog is a border collie")
    score += 1
elif answer3 == "cats":
    print("My favorite type of cat is orange")
    score += 1
elif answer3 == "both":
    print("I like both too!")
    score += 1
else:
    print("Choose cats or dogs!")

print(score)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Example 2: Adventure Game")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")



# Choose your own adventure
destination = input("Would you like to explore the castle or the forest?\n")
if destination == "forest":
    
    print("You are in the forest.")
    print("You see a stream and a large mushroom.")
    action = input("Do you go to the stream or the mushroom?\n")
    if "stream" in action:
        print("You walk over to the stream.")
    elif "mushroom" in action:
        print("You see a fairie on top of the mushroom.")
    
    
elif destination == "castle":
    
    print("You are in the castle.")
    
    character = input("Are you a jester or a princess?\n")
    if character == "jester":
        print("You are a jester")
    elif character == "princess":
        print("You are a princess")
    else:
        character = "lonely soul"
        print("You are a lonely soul")


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Example 3: Advanced Quiz")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


answer4 = input("Name a day of the week\n")
answer4 = answer4.lower()
if "day" not in answer4:
    print("That is not a day of the week")
elif answer4 == "sunday" or answer4 == "saturday":
    print("That is a weekend")
elif answer4 == "thursday":
    print("That is today!")
elif answer4 == "friday":
    print("TGIF!")
elif answer4 == "monday":
    print("Monday is a day of the week")
else:
    print("Tuesday? I guess so")



