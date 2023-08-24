# functions go here
def user_choice():

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image)").lower()

        # check for valid response and return text image or integer
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        else:
            print("Please choose a valid file type!")
            print()

# main routine goes here


data_type = user_choice()
print("You chose", data_type)
