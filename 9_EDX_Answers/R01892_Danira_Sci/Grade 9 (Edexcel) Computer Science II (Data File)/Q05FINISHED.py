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

    userInput = int(input("What do you choose : "))
    # =====> Write your code here
    return userInput

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    number = random.randint(0, len(pTable) - 1)
    return(pTable[number])

# Add a shape
def addShape (pTable):
    # =====> Write your code here
    newShape = input("Enter a new shape: ")
    pTable.append(newShape)


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
while choice != EXIT:
    if choice == GET:
        shape = getShape(pastaShapes)
        print(shape)
    elif choice == ADD:
        addShape(pastaShapes)
    elif choice == SHOW:
        showShapes(pastaShapes)
    else:
        print("Not in the menu")
    choice = getChoice()    


