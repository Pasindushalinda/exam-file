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
number_of_adults=0
number_of_children=0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

number_of_adults=int(input("Enter number of adults attending:"))
number_of_children=int(input("Enter number of children attending:"))

number_of_whole_bottles=(JUICE_ADULT*number_of_adults)+(JUICE_CHILD*number_of_children)
number_of_sandwiches=(SANDWICH_ADULT*number_of_adults)+(SANDWICH_CHILD*number_of_children)
number_of_sandwich_packs=(20/3)*number_of_sandwiches
number_of_friuts=(FRUIT_ADULT*number_of_adults)+(FRUIT_CHILD*number_of_children)
number_of_fruit_packs=(1000/125)*number_of_friuts

print(f"Total number of sandwiches needed is {number_of_sandwiches}")
print(f"Total number of bottles needed is {number_of_whole_bottles}")
print(f"Total number of sandwich packs needed is {number_of_sandwich_packs}")
print(f"Total number of fruit packs needed is {number_of_fruit_packs}")
