# functions go here
def statement_generator(text, decoration):
    # make string with 5 characters
    ends = decoration * 5
    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions
def instructions():
    statement_generator("Instructions / information", "=")
    print('''
Please choose a datatype (image / text / integer).
    
This program assumes that images are being represented    
in 24 bit colour (ie: 24 bits per pixel). for text, we assume   
that ascii encoding is being used (8 bits per character).

Complete as many calculations as necessary, pressing <enter>
at the end of each calculation or any key to quit. 
    ''')
    return ""


instructions()
