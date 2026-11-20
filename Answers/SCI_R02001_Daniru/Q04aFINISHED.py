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
num_adl=0
num_chi=0
tot_bot=0
tot_san=0
tot_fru=0
num_bot=0
num_san=0
num_fru=0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

num_adl=int(input("Enter the number of adults attending:"))    #Getting the user inputs
num_chi=int(input("Enter the number of children attending:"))

#Calculation

tot_bot=(num_adl*0.8)+(num_chi*0.5)
tot_san=(num_adl*2)+(num_chi*1)
tot_fru=(num_adl*75)+(num_chi*50)

#Calculation of whole number if items needed

num_bot=int(tot_bot+1)
num_san=int(((tot_san/20)+1))
num_fru=int(((tot_fru/1000)+1))

#Displaying messages

print("You need to order",num_bot,"fruit bottles and",int(num_san),"sandwich packs and",int(num_fru),"fruit packs")

