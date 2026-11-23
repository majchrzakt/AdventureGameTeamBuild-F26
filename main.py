# ------------------------------------------------------------------------
#
#  Program: Adventure Game
#
#  Description: This program is a simple adventure game where the player 
#    chooses between advancing their reputation, facing an encounter, 
#    or increasing their wealth.  After making one of these choices, a 
#    random scenario plays out.  The player can continue choosing between 
#    these three options or can choose to quit.
#
#  Authors: Main program flow created by Tina Majchrzak, February 2026.
#    Individual functions written by students in 161P.
#
# ------------------------------------------------------------------------

import random
import os

# ------------------------------------------------------------------------
# Essential Functions
# ------------------------------------------------------------------------
from essential.create_health import create_health
from essential.create_gold import create_gold
from essential.choose_title import choose_title
from essential.validate_choice import validate_choice
from essential.status_report import status_report

# ------------------------------------------------------------------------
# Reputation Functions
# ------------------------------------------------------------------------

from reputation.knight_promotion import knight_promotion 
from reputation.secret_path import secret_path
from reputation.lost_map import lost_map
from reputation.magical_training import magical_training
from reputation.royal_favor import royal_favor
from reputation.secret_talisman import secret_talisman

# ------------------------------------------------------------------------
# Encounter Functions
# ------------------------------------------------------------------------

from encounter.forest_attack import forest_attack
from encounter.river_crossing import river_crossing
from encounter.mystical_potion import mystical_potion
from encounter.hidden_trap import hidden_trap
from encounter.rest_inn import rest_inn
from encounter.training_session import training_session
from encounter.haunted_forest import haunted_forest
from encounter.hidden_pond import hidden_pond
from encounter.ambush import ambush
from encounter.healing_herbs import healing_herbs

# ------------------------------------------------------------------------
# Wealth Functions
# ------------------------------------------------------------------------

from wealth.find_treasure import find_treasure
from wealth.bandit_ambush import bandit_ambush
from wealth.merchant_sale import merchant_sale
from wealth.find_gem import find_gem
from wealth.duel_knight import duel_knight
from wealth.gold_mine import gold_mine
from wealth.cursed_coin import cursed_coin
from wealth.treasure_map import treasure_map
from wealth.lottery import lottery


# ------------------------------------------------------------------------
# MAIN GAME
# ------------------------------------------------------------------------

def main():
    # --- Clear screen ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Adventure Game!\n")

    # --- Set up initial stats ---
    health = create_health()
    gold = create_gold()
    title = choose_title()

    # --- Game loop ---
    game_active = True
    while game_active:
        # --- Display stats ---
        print()
        status_report(health, gold, title)

        # --- Display menu ---
        print()
        print("Choose what to do:")
        print("1 - Advance Reputation")
        print("2 - Face Encounter")
        print("3 - Increase Wealth")
        print("4 - Quit")

        # --- Get user choice ---
        print()
        choice = validate_choice("Enter 1, 2, 3, or 4: ", ["1", "2", "3", "4"])

        # --- Clear screen ---
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The adventure continues!\n")

        # --- Reputation ---
        if choice == "1":
            # List the completed reputation functions here (each takes title)
            completed = [knight_promotion]
            # completed = [knight_promotion, secret_path, lost_map,
            #              magical_training, royal_favor, secret_talisman]

            scenario = random.choice(completed)
            title = scenario(title)

        # --- Encounter ---
        elif choice == "2":
            # List the completed encounters here as (function, arguments)
            completed = [
                (forest_attack, (health,)),
                (hidden_trap, (health,)),
                (hidden_pond, (health,)),
                (ambush, (health,)),
                (healing_herbs, (health,)),
                # (rest_inn, (health, gold)),
                # (training_session, (health, title)),
                # (river_crossing, (health,)),
                # (mystical_potion, (health,)),
                # (haunted_forest, (health,)),
            ]

            scenario, args = random.choice(completed)
            health = scenario(*args)

        # --- Wealth ---
        elif choice == "3":
            # List the completed wealth functions here (each takes gold)
            completed = [find_treasure, treasure_map, lottery]
            # completed = [find_treasure, bandit_ambush, merchant_sale, find_gem,
            #              duel_knight, gold_mine, cursed_coin, treasure_map, lottery]

            scenario = random.choice(completed)
            gold = scenario(gold)

        # --- Quit ---
        else:
            print("Thanks for playing!")
            game_active = False

if __name__ == "__main__":
    main()

