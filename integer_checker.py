# checks input is a number more than a given value

def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a integer that is more than (or equal to) {}".format(low)

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
