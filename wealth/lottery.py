# ------------------------------------------------------------------------
#
#  Function: lottery
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player gambles and wins a random amount of gold 
#    (could be zero).
#
#  Author: Bryan Correa
#
# ------------------------------------------------------------------------

import random

def lottery(gold):
    wager = int(input("Double your money or lose it all. Whats you're wager? "))
    gamble = input("Heads or Tails? ").strip().capitalize()

    Coin = random.randint(1,2)
    if Coin == 1:
        result = "Heads"
    else:
        result = "Tails"
    print("Now for the grand reveal, It's", result)
    if gamble == result:
        payout = wager * 2
        print(f"looks like your trying to take me for all i'm worth. Anyways heres your pay ${payout:.2f}.")
        gold = gold + wager
    else:
        payout = 0
        print(f"Well you cant win them all ${payout:.2f}. Just a heads up over 50% of people stop before they win big.")
        gold = gold - wager
    return gold
