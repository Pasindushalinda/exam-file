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

    print(pastaShapes)
    choice1=chr(input("What type of pasta would you like?"))
    
    # =====> Write your code here

    print ("1 - get a shape")
    print ("2 - add a shape")
    print ("3 - show the shapes")
    print ("4 - exit program")

    # =====> Write your code here
choice=int("Enter a letter for each function GET = 1,ADD = 2,SHOW = 3,EXIT = 4:")
if choice==1:
    getChoice(choice1)
    

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)
if choice==3:
    showShapes(pTable)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    random=random.randint(0,9)
if choice==2:
    getShape()


# Add a shape
def addShape (pTable):
    # =====> Write your code here


 -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice()
# =====> Write your code here


