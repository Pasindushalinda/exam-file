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
    userChoice = int(input("Enter the choice:"))
    return userChoice


    # =====> Write your code here


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    randomIndex = random.randint(0,9)
    print(pastaShapes[randomIndex])
    # =====> Write your code here


# Add a shape
def addShape (pTable):
    newshape = input("Enter the new pasta shape name you want to enter:")
    pastaShapes.append(newshape)
    # =====> Write your code here


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

while choice != 4:
    choice = getChoice ()
    if choice == GET or  choice == ADD or  choice == SHOW or  choice == EXIT: 
        if choice == 1:
            getShape(pastaShapes)
        elif choice == 2:
            addShape(pastaShapes)
        elif choice ==3:
            showShapes(pastaShapes)
    else:
        print("Invalid choice")
print("Goodbye")
# =====> Write your code here


