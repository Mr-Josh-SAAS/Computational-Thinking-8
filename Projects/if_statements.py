###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
word = input("What do you think grandma likes? ")


if "t" in word:
    print("Grandma doesn't like t")

else:
    grandma_sprite = codesters.Sprite("grandma")
    grandma_sprite.say("I like that!")



