# ------------------------------------------------------------------------
#
#  Function: create_gold
#
#  Inputs: none
#  Returns: gold (int)
#
#  Description: Randomly generates starting gold between 0 and 50. 
#    Prints a message about starting amount of gold.
#
#  Author: Your Name
#
# ------------------------------------------------------------------------

import random

def create_gold():
    gold = random.randint(0, 50)
    if gold == 0:
        print("Your wallet is empty.")
    else:
        print("Your starting balance is", gold, "gold.")
    return gold