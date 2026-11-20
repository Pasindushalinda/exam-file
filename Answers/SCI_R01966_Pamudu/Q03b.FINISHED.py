# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
Pi=3.14

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea ( Radius,cyHeight):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    area=(2*Pi*(Radius*Radius))+(2*Pi*Radius*cyHeight)

    print ("The Area of the Cylinder is:", area )

    # ===> Return the volume to the caller
    return area
    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
height=int(input("Enter the height:"))
radius=int(input("Enter the radius:"))
cyArea=calcArea(radius,height)

# ===> Print the total volume to three decimal places 

print (float(cyArea))
