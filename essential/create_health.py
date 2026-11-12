# ------------------------------------------------------------------------
#
#  Function: create_health
# 
#  Inputs: none
#  Returns: health (integer)
# 
#  Description: Randomly generates a starting health value between 50 
#    and 150. Prints varied messages depending on strength of the player.
# 
#  Author: Ember Burcher
#
# ------------------------------------------------------------------------

import random

def create_health():
    health = random.randint(50, 150)
    print(f"Your starting health is: {health} HP")
    if(health < 76):
        print(f"{health} HP??? You're just a wittle baby!")
    elif(75 < health < 101):
        print(f"{health} HP. It's okay, you can tell people you're average.")
    elif(100 < health < 126):
        print(f"{health} HP. That's pretty good. You're good and stocky.")
    else:
        print(f"{health} HP! Holy moly, you're thick!")
    return health