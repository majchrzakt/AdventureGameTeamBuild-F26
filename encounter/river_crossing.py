# ------------------------------------------------------------------------
#
#  Function: river_crossing
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player may lose a small amount of health while crossing 
#    a river.
#
#  Author: Will Rockwell
#  Date: 11/19/2026
#
# ------------------------------------------------------------------------

import random


def river_crossing(health):
    """Let the player choose how to cross the river and return their health."""
    print("You reach a rushing river.")
    print("1. Swim across the fast current.")
    print("2. Cross the old wooden bridge.")

    choice = input("Enter 1 or 2: ").strip()

    while choice != "1" and choice != "2":
        choice = input("Please enter 1 or 2: ").strip()

    damage = random.randint(0, 5)

    if choice == "1":
        if damage == 0:
            print("You swim across the river safely.")
        else:
            print("The current throws you against a rock!")
    else:
        if damage == 0:
            print("You make it across the bridge safely.")
        else:
            print("A rotten board breaks, and you scrape your leg!")

    print(f"You lost {damage} health.")
    return health - damage
