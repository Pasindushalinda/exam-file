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
numchild = int(input("Enter number of children attending:"))
numadult = int(input("Enter number of adults attending:"))
total = 0
amntofeach = 0
numofjuice = 0
packofsandwiches = 0
packoffruit = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
numjuice = (numadult * JUICE_ADULT) + (numchild * JUICE_CHILD)
packoffruit = (numadult * FRUIT_ADULT) + (numchild * FRUIT_CHILD)
packofsandwiches = (numadult * SANDWICH_ADULT) + (numchild * SANDWICH_CHILD)

print("Needs",round(numjuice),"for the adults and children")
print("Needs",round(round(packoffruit)/1000),"For adults and children")
print("Needs",round(packofsandwiches),"for adults and children")

