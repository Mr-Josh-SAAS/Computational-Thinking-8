pirate_points=0
princess_points=0
pumpkin_points=0

answer=input ("If people were in a fight would you A get in it, B sing and make everyone happy, or C just watch? ")
if answer == "A" == "a":
        pirate_points += 1
elif answer == "B" == "b":
        princess_points += 1
elif answer == "C"  == "c":
        pumpkin_points += 1

answer=input ("Which activity do you like the best A dancing, B digging for gold, or C making coffee? ")
if answer == "A" == "a":
        princess_points += 2
elif answer == "B" == "b":
        pirate_points += 2
elif answer == "C"  == "c":
        pumpkin_points += 2

answer=input ("Where would you like to vacation, A the Bahamas, B a farm, or C Greece? ")
if answer == "A" or answer == "a":
        pirate_points += 3
elif answer == "B" or answer == "b":
        pumpkin_points += 3
elif answer == "C" or answer =="c":
        princess_points += 3

answer=input ("Whats your favorite color, A brown, B yellow, or C pink? ")
if answer == "A"or answer == "a":
        pumpkin_points += 4
elif answer == "B" or answer == "b":
        pirate_points += 4
elif answer == "C" or answer == "c":
        princess_points += 4

answer=input ("Which animal would you want as a pet A a bird, B a dog, or C nothing? ")
if answer == "A" or answer == "a":
        pirate_points += 5
elif answer == "B" or answer == "b":
        princess_points += 5
elif answer == "C" or answer == "c":
        pumpkin_points += 5

if pirate_points>princess_points and pirate_points>pumpkin_points:
        print ("You should be a pirate for Halloween")
elif princess_points>pirate_points and princess_points>pumpkin_points:
        print ("You should be a princess for Halloween")
elif pumpkin_points>pirate_points and pumpkin_points>princess_points:
        print ("You should be a pumpkin for Halloween")
else :print ("You should be all 3!")


        

