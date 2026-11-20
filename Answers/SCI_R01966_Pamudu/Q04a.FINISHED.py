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
num_adult=int(input("Enter the number of adults attending:"))
num_children=int(input("Enter the number of children attending:"))
# =====> Write your code here
tot_juice=round((num_adult*float(JUICE_ADULT))+(num_children*float(JUICE_CHILD)))
print("Total num of juice bottels needed to be ordered is",tot_juice)

tot_sandwitch=round(((num_adult*float(SANDWICH_ADULT))+(num_children*float(SANDWICH_CHILD))/(int(SANDWICH_PACK))))
print("Total num of sandwitch packets  needed to be ordered is",tot_sandwitch)

tot_fruit=round((num_adult*float(FRUIT_ADULT))+(num_children*float(FRUIT_CHILD))/(int(FRUIT_PACK)))
print("Total num of fruit packets needed to be ordered is",tot_fruit)


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here



