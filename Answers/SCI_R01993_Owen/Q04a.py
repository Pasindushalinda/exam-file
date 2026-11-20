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

num_adults = int(input("Enter the number of adults attending : "))
num_children = int(input("Enter the number of children attending : "))


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

total_1 = num_adults * JUICE_ADULT/1
print("you need ",total_1)

total_2 = num_adults * FRUIT_ADULT/1000
print("you need ",total_2)

total_3 = num_adults * SANDWICH_ADULT/20
print("you need ",total_3)

total_4 = num_children * JUICE_CHILD/1
print("you need ",total_4)

total_5 = num_children * FRUIT_CHILD/1000
print("you need ",total_5)

total_6 = num_children * SANDWICH_CHILD/20
print("you need ",total_6)









