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
 num=getChoice("enter a menu option number:")
 return num
print ("1 - get a shape")
print ("2 - add a shape")
print ("3 - show the shapes")
print ("4 - exit program")

    # =====> Write your code here
    

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
 import random
for pasta in pastaShapes:
    random_number=int(input("enter a random number in between 1 and 10:"))
    random.randint(pastaShapes,"")
    pastaShapes.randint(pasta, random_number)
    print(pasta)

# Add a shape
def addShape (pTable):
    # =====> Write your code here
pastaShapes.add["bow"]

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

 choice = getChoice ()
# =====> Write your code here
if num ==0:
    print("error:invalid input")
    

