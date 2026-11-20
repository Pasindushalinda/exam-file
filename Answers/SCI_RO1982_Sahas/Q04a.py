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


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
number_of_adults=int(input("Enter the number of adults attending:"))
number_of_children=int(input("Enter the number of children attending:"))
total_of_juice=(number_of_adults*JUICE_ADULT)+(number_of_children*JUICE_CHILD)
total_of_sandwich=(number_of_adults*SANDWICH_ADULT)+(number_of_children*SANDWICH_CHILD)/20
total_of_fruit=(number_of_adults*FRUIT_ADULT)+(number_of_children*FRUIT_CHILD)/1000
print("number of bottles:",int(total_of_juice))
print("number of sandwich packs:",int(total_of_juice))
print("number of fruit packs:",int(total_of_fruit))
