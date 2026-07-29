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

    userInput = int (input ("Enter a menu option number: "))

    return userInput


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here

    num = random.randint(0,9)

    shape1 = pastaShapes[num]

    return shape1


# Add a shape
def addShape (pTable):
    # =====> Write your code here

    new_shape = input ("Enter a new pasta shape name: ")

    pastaShapes.append(new_shape)


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here

while choice != EXIT :

    if choice == GET :

        option_1 = getShape(pastaShapes)

        print (option_1)

    elif choice == ADD :

        option_2 = addShape(pastaShapes)

    elif choice == SHOW :

        option_3 = showShapes(pastaShapes)

    else :

        print ("Inputted option number is not on the menu.")

    choice = getChoice ()

    

    

    




