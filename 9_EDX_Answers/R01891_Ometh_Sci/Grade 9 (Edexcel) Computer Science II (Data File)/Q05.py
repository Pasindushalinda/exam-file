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
    userInput = int(input("Please enter the input:"))
    # =====> Write your code here
    return userInput

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    num = random.randint(0,len(pTable)-1)
    return (pTable[num])
# Add a shape
def addShape (pTable):
    # =====> Write your code here
    newname = input("Please enter the new past shape name:")
    pTable.append(newname)
    return pTable

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
while choice != 4:
    if choice == GET:
        get = getShape(pastaShapes)
        print(get)
    elif choice == ADD:
        addShape(pastaShapes)
    elif choice == SHOW:
        showShapes(pastaShapes)
        
    else:
        print("Inputted number not on menu")
    choice = getChoice ()

