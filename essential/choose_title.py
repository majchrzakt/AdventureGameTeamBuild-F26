# ------------------------------------------------------------------------
#
#  Function: choose_title
# 
#  Inputs: none
#  Returns: title (string)
#
#  Description: Randomly selects a starting title (like Wanderer or 
#    Apprentice) and prints it.
#
#  Author: Aaden Easton
#
# ------------------------------------------------------------------------

import random

def choose_title():
    print("Choose Title")
    titles = [
        "Knight",
        "Apprentice",
        "Mage",
        "King",
        "Queen",
        "Witch",
        "Necromancer",
        "Engineer"
    ]
    return random.choice(titles)

