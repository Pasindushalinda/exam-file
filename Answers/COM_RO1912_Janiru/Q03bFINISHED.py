# Q03b-------------------------------------------------------------------
 
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
cyArea = 0.0
# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0


# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea ( Radius ,cyHeight):
    Radius = int(input("Enter the radius of the cylinder:"))
    cyHeight =int(input("Enter the height of the cylinder:"))
    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    area = 2*22/7*Radius*Radius + 2*22/7*Radius*cyHeight

    print ("The Area of the Cylinder is:", area )

    # ===> Return the volume to the caller
    return(area,Radius,cyHeight)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
area = calcArea(Radius , cyHeight)
# ===> Print the total volume to three decimal places 

print ( area )
