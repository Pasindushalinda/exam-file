# Q03b-------------------------------------------------------------------

# -------------------------------------------------------------------

# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
cyHeight = 10.7
Radius = 1.2
cyArea = 0.0
PI=3.14159

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets

    # ===> Complete the calculation for the volume
print("radius of the cylinder is:",Radius)
print("height of the cylinder is :",cyHeight)
area=2*PI*Radius**2+2*PI*Radius*cyHeight
print("area of the cylinder is :",area)
cyArea=cyArea+area  
   

    # ===> Return the volume to the caller
    
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable

# ===> Print the total volume to three decimal places

print("surface area of the cylinder is :",round(cyArea))
