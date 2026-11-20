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
adults=int(input("Enter number of adults attending:"))
children=int(input("Enter number of adults children:"))
bottle=0
packs_sandwich=0
packs_fruit=0


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
fruit_ADULTS=adults*FRUIT_ADULT
fruit_CHILDREN=children*FRUIT_CHILD

sandwich_adult=adults*SANDWICH_ADULT
sandwich_child=children*SANDWICH_CHILD

juice_adult=adults*JUICE_ADULT
juice_child=children*JUICE_CHILD



print(adults,"adults need",fruit_ADULTS,"gram ,""of fruits")
print(children,"children need",fruit_CHILDREN,"gram","of fruits")
print(adults,"adults need",sandwich_adult,"of sandwiches")
print(children,"adults need",sandwich_child,"of sandwiches")
print(adults,"adults need",juice_adult,"bottle","of juice")
print(children,"adults need",juice_child,"bottel","of juice")

NO_FRUITJUICE=fruit_ADULTS+fruit_CHILDREN
NO_SANDWICH=sandwich_adult+sandwich_child

#Total amount of fruit packs required

NO_FRUITADULTS=juice_adult*1000
NO_FRUITCHILD=juice_child*1000

packetsA=NO_FRUITADULTS/adults
packetsCH=NO_FRUITCHILD/children

#In whole numbers
Bottle=round(NO_FRUITJUICE)
packs_sandwich=NO_SANDWICH*20
packs_fruit=packetsA+packetsCH

print(Bottle,"Fruit juice bottles are required in total")
print(packs_sandwich,"of sandwiches are required in total")
print(packs_fruit,"of fruit packs are required in total")

