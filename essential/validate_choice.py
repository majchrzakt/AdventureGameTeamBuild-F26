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
#  Author: Aaden Easton
#
# ------------------------------------------------------------------------


def validate_choice(prompt: str, choices: list[str]) -> int:
    validInput: bool = False
    choice: int
    while True:
        try:
            choice = input(prompt)
            assert choice in choices
            return choice
        except AssertionError:
            print("Invalid input.")
