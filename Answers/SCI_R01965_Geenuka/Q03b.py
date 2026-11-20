# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
pi=3.12

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea ( height,radius,Pi):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    area=(2*Pi*Radius*Radius)+(2*Pi*radius*height)

    print ("The Area of the Cylinder is:", area )

    # ===> Return the volume to the caller
    return area


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
cyArea=calcArea(cyHeight,Radius,pi)

# ===> Print the total volume to three decimal places 

print ('Area :',cyArea)
