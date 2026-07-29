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
def showShapes (p):
    for pasta in p :
        print (pasta)

# Get a random shape
#def getShape (pTable):
    # =====> Write your code here


# Add a shape
def addShape (newShapes):
    # =====> Write your code here
    print(newShapes)
  
def getShape(rando):
    Shape = pastaShapes[rando]
    print(Shape)
    
    


# -------------------------------------------------------------------
# Main program
if choice == 1:
    length = len(pastaShapes)
    rando = random.randint(0,length)
    Shape = pastaShapes[rando]

elif choice == 2:
    new = input('enter a new pasta shape:')
    newshapes = pastaShapes + str(new)

elif choice == 3:
    p = pastaShapes)

elif choice ==4:
    print('Exit")
 


    
# =====> Write your code here
Fshapes = addShape()
Choice = getChoice()
Nshape = getShape()
addShape()
print(getShape())
choice = getChoice ()

