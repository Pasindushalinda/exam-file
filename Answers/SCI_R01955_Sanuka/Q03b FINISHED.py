# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
surface_area=0
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcArea (cyHeight,Radius,cyArea):
    Pi=float(input("Enter a value for Pi:"))
    print ("The radius is:", Radius)
    print ("The height is:", cyHeight)

    # ===> Complete the calculation for the volume
    
    cyArea=Pi*(Radius)**2
    print ("The Area of the Cylinder is:", cyArea )
    
    volume=cyArea*cyHeight
    surface_area=(2*cyArea)+(2*Pi*Radius*cyHeight)
    # ===> Return the volume to the caller
    return volume and surface_area

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable
volume=calcArea(cyHeight,Radius,cyArea)

# ===> Print the total volume to three decimal places 

print (f"Volume is:",volume)
print(f"Surface area is:{surface_area}")
