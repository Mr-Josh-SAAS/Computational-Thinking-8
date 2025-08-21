# Intro
print("You walk into the spooky abandoned mansion.")
print("The door creaks shut behind you.")
print("")
print("Will you ever be able to find your lost friend?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 = input("Do you choose to go up the [stairs] or into the [basement]?")
if "stairs" in c1:
    print("You carefully walk up the stairs")

    # choice 2
    print("The upstairs hallway goes left to the bedroom and right to the bathroom.")
    c2 = input("Do you go [left] or [right]?")
    if "left" in c2 or "bedroom" in c2:
        print("You walk left towards the bedroom.")
    else:
        print("You walk right towards the bathroom.")


else:
    print("You decide to go into the basement")

    # choice 3
    print("In the basement, you can choose to investigate the [closet], the [heater], or the [old rug].")
    c3 = input("What to you investigate?")
    if "closet" in c3:
        print("You open the closet...")
    elif "heater" in c3:
        print("You walk towards the heater...")
    else:
        print("You slide the old rug away, revealing the trap door...")
        # this is the scary part...

