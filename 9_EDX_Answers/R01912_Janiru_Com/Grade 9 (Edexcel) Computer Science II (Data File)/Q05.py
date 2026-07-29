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
pTable = 0
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
    choice = int(input("Enter a choice number"))
    return (choice)

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    shape = len.pastaShapes
    shape = random,shape1
    print (shape)

# Add a shape
def addShape (pTable):
    # =====> Write your code here
    pastaShapes = str(input("Enter the shape name you want to add"))
    pastaShapes.write
    print (pastaShapes)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
if choice == 1:
    getShape(pTable)

elif choice == 2:
    addShape(pTable)
elif choice == 3:
    showShapes(pTable)
elif choice == 4 :
     print("Exiting the program")
else :
    print("Choice not in menu !")
    
       
