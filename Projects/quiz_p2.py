winter_points = 0
summer_points = 0
spring_points = 0

answer1 = input("Do you prefer A short sleeves, B long sleeves, or C both?   ")
if answer1 == "A":
	summer_points += 1
elif answer1 == "B":
	winter_points += 1
elif answer1 == "C":
	spring_points += 1

answer2 = input("Is your favorite weather A rainy, B snowy, or C sunny?   ")
if answer2 == "A":
	spring_points += 1
	winter_points += 1
elif answer2 == "B":
	winter_points += 2
elif answer2 == "C":
	summer_points += 2

answer3 = input("Would you rather A snowboard, B ski, or C swim?   ")
if answer3 == "A" or answer3 == "B":
	winter_points += 2
elif answer3 == "C":
	summer_points += 1
	spring_points += 1

print(f"You score is {winter_points} winter, {summer_points} summer, and {spring_points} spring")
