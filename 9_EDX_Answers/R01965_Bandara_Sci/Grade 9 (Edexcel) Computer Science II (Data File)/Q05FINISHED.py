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
    # =====> Write your code here
    choice=input('Enter needed menu number :')
    return choice

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        return pasta

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    pTabe=random.randint(0,9)
    pasta=pastaShapes[pTable]
    return pasta


# Add a shape
def addShape (pTable):
    # =====> Write your code here
    pTable=input('Enter pasta name :')
    pastashapes.append(pastaname)


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice=getChoice ()
# =====> Write your code here
while choice==4:
    if choice==GET:
        getShape()
    elif choice==ADD:
        addShape()
    elif choice==SHOW:
        showShapes()
        printpasta
    


