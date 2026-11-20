# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (cyHeight,Radius,cyArea):
    
    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    cyArea = (2 * 22/7 * (int(Radius) ^ 2) + 2 * 22/7 * int(Radius) * int(cyHeight))

    print ("The Area of the Cylinder is:", cyArea )

    # ===> Return the volume to the caller
    return cyArea

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
Area = calcArea(cyHeight,Radius,cyArea)
# ===> Print the total volume to three decimal places 

print (round(Area))
