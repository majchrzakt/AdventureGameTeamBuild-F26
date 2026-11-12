# ------------------------------------------------------------------------
#
#  Function: treasure_map
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds a treasure map, follows it, and gains gold.
#
#  Author: Enrique Chavez
#
# ------------------------------------------------------------------------

import random
import time

def treasure_map(gold):
    print("\n🗺️  You stumble upon an ancient, scorched treasure map half-buried in the dirt!")
    time.sleep(1.5)
    print("You follow the faded trail into a smoky cavern and discover a massive pile of glittering coins...")
    time.sleep(1.5)
    print("\n🐉 ROAR!! A giant crimson dragon drops from the ceiling, blocking the exit!")
    time.sleep(1.5)
    print("'THIEF!' the dragon booms, smoke curling from his nostrils. 'The gold in your pouch bears my royal stamp! It was stolen from my hoard, and I want it back!'")
    time.sleep(1.5)

    print("\nWhat do you do?")
    print("1. Toss him a shiny distraction and grab a handful of treasure")
    print("2. Apologize and offer a trade")
    print("3. Bolt deeper into the dark cave to look for another way out")
    print("4. You draw your sword and threaten the dragon. As you threaten the dragon, he quickly lashes out with his mouth and snaps your head off and ends your adventure")
    choice = input("Type 1, 2, 3, or 4: ")

    if choice == "1":
        found_gold = random.randint(15, 30)
        print(f"\nYou hurl a fake brass coin across the cave! While the dragon chases it, you scoop up {found_gold} gold pieces and sprint out!")
        gold += found_gold
    elif choice == "2":
        found_gold = random.randint(10, 20)
        print("\nYou respectfully bow and explain you didn't know it was his. Impressed by your honesty, the dragon spares you.")
        time.sleep(1.5)
        print(f"'Keep what you have, honest traveler—and take {found_gold} extra coins for returning my map!'")
        gold += found_gold
    elif choice == "3":
        found_gold = random.randint(5, 15)
        print(f"\nYou grab {found_gold} loose coins off the floor and sprint deeper into the pitch-black tunnels!")
        time.sleep(1.5)
        print("You squeeze through a narrow crack that collapses behind you—sealing off the cavern forever.")
        time.sleep(1.5)
        print("🔥 As you emerge into the sunlight, you hear a furious roar shake the mountain. Enraged and unable to reach you, the dragon takes flight on the hunt... and scorches the nearest village to ashes!")
        gold += found_gold
    else:
        found_gold = 


    time.sleep(1.5)
    print(f"\nYou now have {gold} gold!")
    return gold

test_gold = treasure_map(50)
print("Returned gold:", test_gold)