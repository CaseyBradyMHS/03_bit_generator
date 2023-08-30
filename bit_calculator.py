# function goes here

# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # make string with 5 characters
    ends = decoration * 5
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# sorts what the user has chosen into file types
def user_choice():

    # list of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image)").lower()

        # check for valid response and return text image or integer

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        # error message
        else:
            print("Please choose a valid file type!")
            print()


# integer checker

def num_check(question, low):


# main routine goes here

# heading
statement_generator("Bit Calculator for integers, text & images", "-")

# display instructions if user has not used the program before

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # ask the user for the file type
    data_type = user_choice()
    print("you chose", data_type)

    # for integers ask for integer (must be an integer more than / equal to 0)


    # for images ask for width and height (more than 0)

