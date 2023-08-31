# checks input is a number more than a given value

def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter an integer that is more than or equal to {} (no decimals these are pixels)".format(low)

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than 0
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# main routine goes here


keep_going = ""
while keep_going == "":

    # Ask user for the width...
    var_integer = num_check("Enter an integer", 0)
    print(f"You chose {integer} for the integer")
    width = num_check("Image width: ", 1)
    print(f"You chose {width} for the width")
    height = num_check("Image height: ", 1)
    print(f"you chose {height} for the height")
    keep_going = input("Again? Press <enter> or any key to quit ")



