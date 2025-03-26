# Beginning: create variables
strength_points = 0
get_gud_points = 0

# Middle: ask questions
answer = input ("in boss fight do you A) get up close a personal with the boss, or B) run away")
if answer == "A" :
         strength_points += 1
elif answer == "B":
         get_gud_points += 1


answer = input (" if you had would you chose a weapon to defeat your foes would you chose A) A mighty blade, or B) a little wand")
if answer == "A" :
         strength_points += 1
elif answer == "B":
         get_gud_points += 1


answer = input (" if you were you were fighting a mighty foe would you choose A) learn how their attacks work to get better, or B) poison them and run away")
if answer == "A" :
         strength_points += 1
elif answer == "B":
         get_gud_points += 1


answer = input ("if you were in a open world game would you rather A) explore the world to gain knowledge and power, or B) get mad when the first boss you meet is too hard even though you could of leveled up way before you meet them")
if answer == "A" :
         strength_points += 1
elif answer == "B":
         get_gud_points += 1


answer = input ("if you got a new dlc would you A) explore it and gain new power, or B) get mad when your one shot build is super weak in the dlc and not realize that you can grow stronger just by exploring the world.")
if answer == "A" :
         strength_points += 1
elif answer == "B":
         get_gud_points += 1


# end: results of quiz
if strength_points > get_gud_points:
    print("Congrats you are a great")

if strength_points < get_gud_points:
    print ("You need to get gud")