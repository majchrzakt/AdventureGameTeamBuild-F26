# ------------------------------------------------------------------------
#
#  Function: status_report
#
#  Inputs: health (int), gold (int), title (string)
#  Returns: none
#
#  Description: Displays the player’s current health, gold, and title 
#    in a format that's easy to read quickly.
#
#  Author: Aaden Easton
#
# ------------------------------------------------------------------------

def status_report(health: int, gold: int, title: str):
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print(f"Title: {title}")
