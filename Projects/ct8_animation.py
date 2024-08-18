import codesters
from manager import Manager

cat = codesters.Sprite('cat',-200,-200)
cat.set_size(.5)

dog = codesters.Sprite('doggo', 200, 0)
dog.set_size(.1)

cat.say("Meow",1)

Manager.root.after(1000, cat.say("there are 10 types of people",3))
Manager.root.after(5000, dog.say("bark!",1))
# cat.say("",3)
# dog.say("",7)

# cat.say("there are 10 types of people",3)
# time.sleep(5)
# cat.glide_to(-200, 150)

# dog.say("bark!",1)

# cat.say("Those who understand binary and those who dont!",2)
# dog.say("haha",1)
