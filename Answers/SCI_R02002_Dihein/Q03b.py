# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.3
cyArea = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea ( cyHeight,Radius,area ):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    area = (2 * 3.14 * (Radius * Radius)) + (2 * 3.14 * Radius * cyHeight)

    print ("The Area of the Cylinder is:", area )

    # ===> Return the volume to the caller
    return area

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
totalVolume = calcArea(cyHeight,Radius,cyArea)
# ===> Print the total volume to three decimal places 
wholeNum = str(totalVolume // 1)
decimal = str(totalVolume % 1)
threeDecPlaces = wholeNum  + decimal[0:4]


print ("The surface area of the cylinder is:",threeDecPlaces)
