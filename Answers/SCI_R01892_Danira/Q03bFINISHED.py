# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = float(input("Enter the height of the cylinder: "))
Radius = float(input("Enter the radius of the cylinder: "))
cyArea = 0.0
Pi = 3.14

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea ( Radius, cyHeight ):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    area = (2 * Pi * (Radius ** 2)) + (2 * Pi * Radius * cyHeight)

    # ===> Return the volume to the caller
    return(area)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
cyArea = calcArea( Radius, cyHeight )
# ===> Print the total volume to three decimal places 

print ("The surface area is", round(cyArea, 3))
