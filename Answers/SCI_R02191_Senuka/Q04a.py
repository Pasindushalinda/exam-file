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
numAdults = int(input('enter the number of adults attending:'))
numChildren = int(input('enter the number of children attending:'))

# =====> Write your code here
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

juice = int((numAdults * JUICE_ADULT ) + (numChildren * JUICE_CHILD ))
sandwich = int(((numAdults * 2 ) + (numChildren * 1 ))/20) 
fruit = int(((numAdults * 75) + (numChildren * 50))/1000)
print('you need :',juice,'juice bottles')
print('you need :',sandwich,'sandwich packs')
print('you need :',fruit,'kg of fruits')
# =====> Write your code here




