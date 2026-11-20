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

# =====> Write your code here

num_adults = 0
num_children = 0

amount_fJuice = 0
amount_sandwiches = 0
amount_fruit = 0

num_of_whole_bottles = 0
num_of_packs_sandwiches = 0
num_of_fruit_packs = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

# Inputs the number of adults and children attending the picnic

num_adults = int (input ("Enter the number of adults attending: "))

num_children = int (input ("Enter the number of children attending: "))


# Calculates the amounts of each item required 

amount_fJuice = (num_adults * JUICE_ADULT) + (num_children * JUICE_CHILD)

amount_sandwiches = (num_adults * SANDWICH_ADULT) + (num_children * SANDWICH_CHILD)

amount_fruit = (num_adults * FRUIT_ADULT) + (num_children * FRUIT_CHILD)


num_of_whole_bottles = round (amount_fJuice) # Calculates the number of whole bottles of fruit juice required

num_of_packs_sandwiches = (amount_sandwiches // SANDWICH_PACK) + 1 # Calculates the number of packs of sandwiches required

num_of_fruit_packs = (amount_fruit // FRUIT_PACK) + 1 # Calculates the number of packs of fruit required


# Displays informative messages showing the quantities that need to be ordered

print ("The number of juice bottles required is:",num_of_whole_bottles)

print ("The number of packs of sandwiches required is:",num_of_packs_sandwiches)

print ("The number of packs of fruit required is:",num_of_fruit_packs)





