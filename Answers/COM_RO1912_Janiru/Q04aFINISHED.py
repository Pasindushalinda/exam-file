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
numAdults = 0
numChildren = 0 
# =====> Write your code here


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
numAdults = int(input("Enter the number of adults attending :"))
numChildren = int(input("Enter the number of kids attending :"))

total_juice = numAdults * JUICE_ADULT + numChildren * JUICE_CHILD

total_sandwich = numAdults * SANDWICH_ADULT + numChildren * SANDWICH_CHILD

total_fruit = numAdults * FRUIT_ADULT + numChildren * FRUIT_CHILD

bottle_juice = int(total_juice)

pack_sandwich = int(total_sandwich / 20)

pack_fruit = int(total_fruit /1000)


print(bottle_juice , " bottles of fruit juice need to be ordered ")
print(pack_sandwich , "packs of sandwhich need to be orered ")
print(pack_fruit , "Kilograms of fruit need to be ordered ")






