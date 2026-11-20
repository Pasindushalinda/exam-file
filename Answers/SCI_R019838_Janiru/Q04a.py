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
numAdults = int(input("Enter the number of adults attending:"))
numChild = int(input("Enter the number of children attending:"))
totalSandwitch = 0
totalJuice = 0
totalFruit = 0
wholeJuiceBottles = 0
wholeSandwitchPacks = 0
wholeFruitPacks = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
totalJuice = numAdults * JUICE_ADULT + numChild * JUICE_CHILD
totalSandwitch = numAdults * SANDWICH_ADULT + numChild * SANDWICH_CHILD
totalFruit = numAdults * FRUIT_ADULT + numChild  * FRUIT_CHILD

wholeJuiceBottles = round(totalJuice)
totalSandwitch = round(round(totalSandwitch)/20)
print(totalFruit)
wholeFruitPacks = round(round(totalFruit)/1000)
print("The number of Juice bottles to be ordered is: ",wholeJuiceBottles)
print("The number of sandwitch packs(20 in each) to be ordered is: ",totalSandwitch)
print("The number of fruit packs(1000g in each) to be ordered is: ",wholeFruitPacks)

