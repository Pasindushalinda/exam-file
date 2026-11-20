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
def totalAmt(adults,children):
    totalJ=(adults*JUICE_ADULT)+(children*JUICE_CHILD)
    totalS=(adults*SANDWICH_ADULT)+(children*SANDWICH_CHILD)
    totalF=(adults*FRUIT_ADULT)+(children*FRUIT_CHILD)
    total=totalJ+totalS+totalF
    juiceAmt=totalJ
    sandwichAmt=totalS/SANDWICH_PACK
    fruitAmt=totalF/FRUIT_PACK
    print("The total amount of each item is:",total)
    print("The number of whole bottles of fruit juice is:",round(juiceAmt))
    print("The number of packs of sandwiches is:",round(sandwichAmt))
    print("The number of packs of fruit is:",round(fruitAmt))
    
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
adults=int(input("Enter the number of adults attending: "))
children=int(input("Enter the number of children attending: "))
totalAmt(adults,children)




