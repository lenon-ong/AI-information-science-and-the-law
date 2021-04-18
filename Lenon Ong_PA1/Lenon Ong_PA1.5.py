import re

x = True

while x: # The "While" loop to always enable input prompt until the x = False
    user_input = input("Enter password: ") # prompt user input
    compulsory = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,16}$')
    # check for the following compulsory conditions:
    # 1. the password must be between 6 and 16 characters long
    # 2. at least 1 upper case letter
    # 3. at least 1 lower case letter
    # 4. at least 1 number
    if not user_input:
        # if user presses enter, x = False and the "while" loop breaks
        x = False
    if not re.search(compulsory, user_input):
        # if user input does not meet all the compulsory condition,
        print("Invalid password")
        # "if not" (instead of elif not) is used here so that "Invalid password" also prints when x = False
    elif re.search("[^A-Za-z0-9]", user_input):
        # if user input contains special characters (including spaces),
        print("Invalid password")
    elif re.search(compulsory, user_input):
        # if user input meets all the compulsory conditions,
        print("Valid password")
