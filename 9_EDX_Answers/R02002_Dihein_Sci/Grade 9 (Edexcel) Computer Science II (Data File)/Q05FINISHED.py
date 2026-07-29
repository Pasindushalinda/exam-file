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
    choice = input("Choose a menu option from 1 to 4:")
    return choice

# Display all the shapes
def showShapes ():
    for pasta in pastaShapes:
        print (pasta)

# Get a random shape
def getShape ():
    # =====> Write your code here
    
     index = random.randint(0,len(pastaShapes))
    
     return pastaShapes[index]

# Add a shape
def addShape ():
    # =====> Write your code here
    inputShape = input("Please enter a pasta shape:")
    pastaShapes.append(inputShape)
    print(pastaShapes)
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here

if choice == str(GET):
    get = getShape()
    print(get)
elif choice == str(ADD):
    add = addShape()
    print(add)
elif choice == str(SHOW):
    show = showShapes()
    
elif choice == str(EXIT):
    print("Exiting the program")
        
    
    
