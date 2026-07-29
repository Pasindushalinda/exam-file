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
def getChoice (num):
    
  
    # =====> Write your code here
    num=int(input("Enter the menu option:"))
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
    num1=random.randint(0,10)
    shape=pTable[num1]
    return shape
# Add a shape
def addShape (pTable):
     
     new_name=input("Enter the new name")
     pTable=pTable.append(new_name)
     
     
    # =====> Write your code here
    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

choice = getChoice (choice) 
# =====> Write your code here
if choice==1:
    pastaShapes1=getShape(pastaShapes)
    print("The shape is",pastaShapes1)
elif choice==2:
    newshape=addShape(pastaShapes)
    print(newshape)
elif choice==3:
    show=showShapes(pastaShapes)
    print(show)
elif choice==4:
    print("Exiting program.  Thank you for visiting!")
else:
    print("Invalid option.Try again")



