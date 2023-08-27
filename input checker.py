# functions go here
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

# main routine goes here


while True:
    data_type = user_choice()
    print("You chose", data_type)
    print()
