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

whole_bottles=0
sandwich_packs=0
fruit_packs=0
juice_adult=0
juice_child=0
sandwich_adult=0
sandwich_child=0
fruit_adult=0
fruit_child=0


# =====> Write your code here

def Packs(adults,children):
    juice_adult=adults*JUICE_ADULT
    juice_child=children*JUICE_CHILD
    sandwich_adult=adults*SANDWICH_ADULT
    sandwich_child=children*SANDWICH_CHILD
    fruit_adult=adults*FRUIT_ADULT
    fruit_child=children*FRUIT_CHILD
    whole_bottles=int(juice_adult)+int(juice_child)
    sandwich_packs=sandwich_adult*20 + sandwich_child*20
    fruit_packs=int(fruit_adult)*1000+int(fruit_child)*1000
    return adults,children,whole_bottles,sandwich_packs,fruit_packs
    
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
answer=0
adults=int(input("Enter the number of adults:"))
children=int(input("Enter the number of children:"))
answer=Packs(adults,children)
print(answer)





