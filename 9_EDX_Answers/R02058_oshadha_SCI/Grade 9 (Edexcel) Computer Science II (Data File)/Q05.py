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
    
    chose=input('enter a number')
    
    return getChoice
    # =====> Write your code here


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pastaShapes):
    
     # =====> Write your code here
     import random
     
    random=random.randint(0:11)
    return getShape


# Add a shape
def addShape (pastaShapes):
    
    # =====> Write your code here
    
    enter_pasta=input('enter you own pasta shapes name:')
    pastaShapes=pastaShapes+enter_pasta
    return addShape

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

choice = getChoice()

shape=getShape(pastaShapes)
print(shape)
added_shape=addShape()



