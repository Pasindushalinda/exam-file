# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = int(input("Enter height:"))
Radius = int(input("Enter radius of cylinder:"))
cyArea = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (cyHeight,Radius,cyArea):
    Pi =3.14159
    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    cyArea = (2 * Pi * (int(Radius) ^ 2) + 2 * Pi * int(Radius) * int(cyHeight))

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

print (round(Area,3))
