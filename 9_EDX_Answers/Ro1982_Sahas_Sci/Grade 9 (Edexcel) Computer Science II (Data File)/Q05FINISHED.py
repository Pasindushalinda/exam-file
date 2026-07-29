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
    choice=input("Enter a menu option:"))


    print ("1 - get a shape")
    print ("2 - add a shape")
    print ("3 - show the shapes")
    print ("4 - exit program")
    return choice 

    # =====> Write your code here


# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)
# Get a random shape
def getShape (pTable):
    # =====> Write your code here
   import random
    shape=pastaShapes[random.randint(0,len(pastaShapes)+1)]
    return shape 


# Add a shape
def addShape (pTable):
   name=input("Enter a new pasta name")
    Ptables.append(name) 
    # =====> Write your code here


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice ()
# =====> Write your code here
while choice!=4:
    if choice!=4
        if choice==1:
            print(getShape())
        elif choice==2:
            print(addShape())
        else:
            print("the option number is not on the menu")
        choice = getChoice ()
        


