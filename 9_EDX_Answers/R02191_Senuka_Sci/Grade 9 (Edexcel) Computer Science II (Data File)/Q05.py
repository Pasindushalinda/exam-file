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
    choice = int(input('enter the option from above:'))
    return choice
                           

    # =====> Write your code here


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
#def getShape (pTable):
    # =====> Write your code here


# Add a shape
def addShape (pTable):
    # =====> Write your code here
    new = input('enter a new pasta shape:')
    newshapes = pastaShapes + str(new)
    return newShapes
def getShape():
    if choice == 1 :
        length = len(pastaShapes)
        rando = random.randint(0,length)
        Shape = pastaShapes[rando]
        return(Shape)
        
    


# -------------------------------------------------------------------
# Main program


    

Fshapes = addShape(pTable)
getChoice()
Nshape =getShape()
addShape()
print(getShape())
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here


