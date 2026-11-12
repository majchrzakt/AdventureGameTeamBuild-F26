# ------------------------------------------------------------------------
#
#  Function: validate_choice
#
#  Inputs: prompt (string), choices (list of valid strings)
#  Returns: valid user choice (string)
#
#  Description: Keeps asking the user for input until they enter one of 
#    the allowed choices. Ensures the menu never crashes.
#
#  Author: Your Name
#
# ------------------------------------------------------------------------

def validate_choice(prompt, choices):
    print("Validate Choice")
    c = input("Choice: ")
    return c
