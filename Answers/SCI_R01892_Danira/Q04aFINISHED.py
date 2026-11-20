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
numAdults = 0
numChildren = 0
juiceReq = 0
sandwichReq = 0
fruitReq = 0
numBottles = 0
numSandwichPack = 0
numFruitPack = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
numAdults = int(input("Enter the number of adults attending : "))
numChildren = int(input("Enter the number of children attending : "))

juiceReq = (numAdults * JUICE_ADULT) + (numChildren * JUICE_CHILD)
sandwichReq = (numAdults * SANDWICH_ADULT) + (numChildren * SANDWICH_CHILD)
fruitReq = (numAdults * FRUIT_ADULT) + (numChildren * FRUIT_CHILD)

numBottles = round(juiceReq)
numSandwichPack = round(sandwichReq / SANDWICH_PACK)
numFruitPack = round(fruitReq / FRUIT_PACK)

print(numBottles, "bottles of fruit juice are needed")
print(numSandwichPack, "packets of sandwiches are needed")
print(numFruitPack, "packets of fruit are needed")
