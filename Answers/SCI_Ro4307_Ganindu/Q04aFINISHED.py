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
num_adults=int(input("enter the number of adults:"))
num_child=int(input("enter the number of children:"))
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
juice_adult=JUICE_ADULT*num_adults
juice_child=JUICE_CHILD*num_child
juice=juice_adult+juice_child
juice=juice
print("num of bottels of juice to be odered:",round(juice))
sandwich_adult=SANDWICH_ADULT*num_adults
sandwich_child=SANDWICH_CHILD*num_child
sandwich=sandwich_adult+sandwich_child
sandwich=sandwich/20
print("num of sandwich packs to be odered:",round(sandwich))
fruit_adult=FRUIT_ADULT*num_adults
fruit_child=FRUIT_CHILD*num_child
fruit=fruit_adult+fruit_child
fruit=fruit/1000
print("number of fruit packs needed:",round(fruit))

# =====> Write your code here



