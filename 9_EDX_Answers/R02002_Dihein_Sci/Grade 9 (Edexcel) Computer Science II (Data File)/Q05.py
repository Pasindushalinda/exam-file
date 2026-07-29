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
length = len(pastaShapes)

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
    
     index = random.randint(0,length)
    
     return pastaShapes[index]

# Add a shape
def addShape ():
    # =====> Write your code here
    shape = input("Please enter a pasta shape:")
    pastaShapes.append(shape)
    
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
while choice != EXIT:
    if choice == GET:
        print(getShape())
    elif choice == ADD:
        print(addShape())
    elif choice == SHOW:
        print(showShape())
    else:
        print("Goodbye!")

        
    
    
