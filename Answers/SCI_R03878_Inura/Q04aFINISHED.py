# Q04a-------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import math
tA = 0
tC =0
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
attendA = int(input("Please enter the amount of Adults : "))
attendC = int(input("Please enter the amount of Children : "))
TaF = attendA*75
TcF = attendC*50
TaS = attendA *2
TcS = attendC
TaJ = attendA*0.8
TcJ = attendC*0.5
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here
f = FRUIT_PACK/(TaF+TcF)
s = SANDWICH_PACK/(TaS+TcS)
j = TaJ+TcJ
if j%1 == 0:
    print("Number of juice : ",j)
else:
    print("Number of juice : ",j+1)
if f%1000 == 0:
    print("Number of juice : ",int(f))
else:
    print("Number of juice : ",int(f+1))
if s%20 == 0:
    print("Number of juice : ",int(s))
else:
    print("Number of juice : ",int(s+1))
