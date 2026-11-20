# Q04a-------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import math

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------


JUICE_ADULT = 0.8  # Bottle 
JUICE_CHILD = 0.5  # Bottle

SANDWICH_ADULT = 2  # Number 
SANDWICH_CHILD = 1  # Number

FRUIT_ADULT = 75    # Grams
FRUIT_CHILD = 50    # Grams

SANDWICH_PACK = 20 
FRUIT_PACK = 1000


# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
adult_attending=int(input("how many adults are attending: "))
child_attending=int(input("how many children are attending: "))
# =====> Write your code here
num_whole_bottles=adult_attending // JUICE_ADULT + child_attending // JUICE_CHILD
num_packs_sandwiches=adult_attending*SANDWICH_ADULT/SANDWICH_PACK + child_attending*SANDWICH_CHILD//SANDWICH_PACK
num_fruit=adult_attending*FRUIT_ADULT//FRUIT_PACK+child_attending*FRUIT_CHILD//FRUIT_PACK



# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
total_amount=num_whole_bottles+num_packs_sandwiches+num_fruit

# =====> Write your code here
print(total_amount)


