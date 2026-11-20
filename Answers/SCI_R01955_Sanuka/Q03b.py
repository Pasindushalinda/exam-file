# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
Pi=3.14
surface_area=0
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (cyHeight,Radius,cyArea,Pi):

    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    
    area=Pi*(Radius)**2
    print ("The Area of the Cylinder is:", area )
    surface_area=(2*Pi*(Radius)**2)+(2*Pi*Radius*cyHeight)
    volume=area*cyHeight
    # ===> Return the volume to the caller
    return volume and surface_area

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
volume=calcArea(cyHeight,Radius,cyArea,Pi)

# ===> Print the total volume to three decimal places 

print (f"Volume is:",volume)
print(f"Surface area is {surface_area}")
