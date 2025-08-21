while True:
    word = input("What do you think grandma likes? ")

    if "t" in word.lower():
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}")

    print("")