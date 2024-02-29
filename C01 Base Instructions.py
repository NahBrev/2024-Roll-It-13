# check users enter yes  (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if user dont enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")


# Checks that user enter an integer
# That is more than 13
def int_check():
    while True:

        error = "Pleases enter an  integer that is 13 or more "

        try:
            my_num = int(input("Enter an integer"))

            # checks that the number is more than / equal to 13
            if my_num < 13:
                print(error)
            else:
                print("Your number is ", my_num)

        except ValueError:
            print(error)


# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()


def instructions():
    print('''
**** Instructions ****
Do something
and then do something else
etc

    ''')


# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# check users enter yes  (y) yes or no (n)
if want_instructions == "yes":
    instructions()

print()
int_check()
