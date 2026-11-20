# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
import math
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
PI=math.pi
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (Radius,cyHeight):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    
    area = 2*PI*Radius**2 + 2*PI*Radius*cyHeight
    print ("The Area of the Cylinder is:", area )

    # ===> Return the volume to the caller
    return area
    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
answer=calcArea(Radius,cyHeight)

# ===> Print the total volume to three decimal places 

print (answer)
