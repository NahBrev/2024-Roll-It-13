print("🎲🎲 Roll it 13 🎲🎲")


 #loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions ").lower()

    # check users enter yes  (y) or no (n)
    if want_instructions == "yes" or want_instructions == "y":
        print("You Chose Yes")
    elif want_instructions == "no" or want_instructions == "n":
        print("You Chose No")
    else:
        print("You did not chose a valid response")
