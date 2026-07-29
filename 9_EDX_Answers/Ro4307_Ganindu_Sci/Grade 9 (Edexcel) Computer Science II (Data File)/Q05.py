# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import random

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
GET = 1
ADD = 2
SHOW = 3
EXIT = 4

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
pastaShapes = ["Bigoli", "Strozzapreti", "Trofie", "Gigli", "Chitarra",
               "Penne", "Orecchiette", "Tagliatelle", "Chonchiglie",
               "Fusilli"]

shape = ""
choice = 0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# Get a menu item from the user
def getChoice ():
    # =====> Write your code here

    print ("1 - get a shape")
    print ("2 - add a shape")
    print ("3 - show the shapes")
    print ("4 - exit program")
    return choice

    # =====> Write your code here
choice= print("enter a menu option")


# Display all the shapes
if choice == 1:
    def showShapes (pTable):
        for pasta in pTable:
            print (pasta)
            return shape

# Get a random shape
def getShape (pTable):
    # =====> Write your code here


# Add a shape
 def addShape (pTable):
    if choice == 4:
        print (pastaShapes)
    # =====> Write your code here
    else:
        print("option number is not on the menu")


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here


