# functions

# checks for integers more than a given 'low' number
def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter an integer that is more than or equal to {} (no decimals these are pixels)".format(low)

        try:
            # ask for a number
            response = int(input(question))

            # check number is more than low
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# calculating the number of bits needed to represent an uncompressed
# image assuming 24 bits per pixel
def image_bits():

    print()
    # ask user for width and height
    var_width = num_check("Enter the width: ", 1)
    var_height = num_check("Enter the height: ", 1)
    # calc num of bits

    num_bits = var_height * var_width * 24

    # output answer with working
    print()
    print(f"The width you chose is {var_width}")
    print(f"The height you chose is {var_height}")
    print("to find the bits you must multiply the width by the height by 24")
    print(f"{var_width} times {var_height} times 24 is {num_bits}")
    print(f"We need {num_bits} bits to represent the image.")
    print()

    return ""

# main routine


image_bits()
