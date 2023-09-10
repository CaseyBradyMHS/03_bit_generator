# functions go here
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


def int_bits():

    # get integer
    var_integer = num_check("Please enter an integer", 0)

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("number of bits is {}".format(num_bits))
    print()

    return ""
# main routine goes here


int_bits()
