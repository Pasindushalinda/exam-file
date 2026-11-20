# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
Pi = 3.14

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (Radius,cyHeight,cyArea):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    cyArea = (2*Pi*Radius*Radius) + (2*Pi*Radius*cyHeight)
    

    print ("The Area of the Cylinder is:", cyArea)

    # ===> Return the volume to the caller
    return cyArea

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
calcArea(Radius,cyHeight,cyArea)


# ===> Print the total volume to three decimal places 

print ('total volume to three decimal places is:',round.cyArea,3)
