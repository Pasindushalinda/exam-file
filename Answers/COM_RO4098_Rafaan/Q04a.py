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
adults = int(input("Enter the number of adults: "))
children = int(input("Enter the number of children: "))

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
bottleAdults = adults * JUICE_ADULT
bottleChildren = children * JUICE_CHILD

totalBottles = bottleAdults + bottleChildren
print("The total amount of bottles required to order is;", totalBottles, "Bottles")

sandwichAdults = adults * SANDWICH_ADULT
sandwichChildren = children * SANDWICH_CHILD

totalSandwiches = sandwichAdults + sandwichChildren
print("The total amount of packs required to order is;", totalSandwiches, "packs")

fruitAdults = adults * FRUIT_ADULT
fruitChildren = children * FRUIT_CHILD

totalFruit = fruitAdults + fruitAdults 
print("The total amount of fruits required is;", totalFruit, "grams")







