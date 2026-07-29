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
    number=int(input("Enter a choice number:"))
    return[number]

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    
    # =====> Write your code here
    x=random.randint(pastaShapes)    
    return[x,pTable]

# Add a shape
def addShape (pTable):
    
    # =====> Write your code here
    new_pasta=input("Enter a new pasta name:")
    new_pasta=pastaShapes[-1].append()
    print(pastaShapes)
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
getChoice()
showShapes(pTable)
getShapes(pTable)
addShape(pTable)
print(x)
if number!=1 and number!=2 and number!=3 and number!=4:
    print("It is an invalid option")
else:
    print("It is a valid option")


