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
    I = int(input("Enter the option : "))
    print ("1 - get a shape")
    print ("2 - add a shape")
    print ("3 - show the shapes")
    print ("4 - exit program")
    return I
    # =====> Write your code here


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    A =random.randint(0,len(pastaShapes))
    i = pastaShapes[A]
    return i 
    # =====> Write your code here


# Add a shape
def addShape (pTable):
    e = input("Enter a new pasta shape : ")
    pastaShapes+e
    # =====> Write your code here

print(I)
print("It is not in the menu")
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
o = addShape
s = getChoice()
# =====> Write your code here


