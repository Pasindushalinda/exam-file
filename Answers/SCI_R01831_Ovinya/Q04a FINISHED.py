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
NUM_ADULT=int(input("Enter number of adults:"))
NUM_CHILD=int(input("Enter number of children:"))


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here


TotalAmount_JUICE=NUM_ADULT*JUICE_ADULT+NUM_CHILD*JUICE_CHILD
TotalAmount_SANDWICH=NUM_ADULT*SANDWICH_ADULT+NUM_CHILD*SANDWICH_CHILD
TotalAmount_FRUIT=NUM_ADULT*FRUIT_ADULT+NUM_CHILD*FRUIT_CHILD
JUICE_BOTTLE=TotalAmount_JUICE/2
PACKS_SANDWICH=TotalAmount_SANDWICH/SANDWICH_PACK
PACKS_FRUIT=TotalAmount_FRUIT/FRUIT_PACK


print("number of juice bottls:",JUICE_BOTTLE)
print("number of sandwich packs:",PACKS_SANDWICH)
print("number of fruit packs:",PACKS_FRUIT)

print("Total amount of JUICE is:",TotalAmount_JUICE)

