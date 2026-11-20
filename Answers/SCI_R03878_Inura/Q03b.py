# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------
area = 0
# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (Radius,cyHeight):
    cyArea = 2*Radius**2*22/7+2*22/7*Radius*cyHeight
    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    V = 22/7*Radius**2*cyHeight

    print ("The Area of the Cylinder is:", cyArea)

    # ===> Return the volume to the caller
    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
cyArea = calcArea(Radius,cyHeight)
# ===> Print the total volume to three decimal places 

print (cyArea)
