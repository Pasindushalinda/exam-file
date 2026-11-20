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
adults=int(input('Enter the number of adults attending :'))
children=int(input('Enter the number of children attending :'))

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
total_juice=(0.8*adults)+(0.5*children)
total_sandwich=(2*adults)+(1*children)
total_fruit=(75*adults)+(50*children)
total_items=total_juice+total_sandwich+total_fruit

juiceNeeded=total_juice//1
sandwichNeeded=total_sandwich//SANDWICH_PACK
fruitsNeeded=total_fruit//FRUIT_PACK
print('Total items :',total_items)
print('Juice needed :',juiceNeeded)
print('Sandwich needed:',sandwichNeeded)
print('Fruits needed :',fruitsNeeded)


