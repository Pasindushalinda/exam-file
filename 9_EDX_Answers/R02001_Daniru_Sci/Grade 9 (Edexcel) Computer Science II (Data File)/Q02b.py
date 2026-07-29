# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
height=0
width=0
length=0
area_of_tri=0
vol_of_pri=0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here

# Take three decimal inputs from the user
height=float(input("Enter the height of the prism:"))
width=float(input("Enter the width of the prism:"))
length=float(input("Enter the length of the prism:"))

# Check for invalid inputs, using relational and logical operators
if height<=0 or width<=0 or length<=0:
    print("Inputs are invalid.")
      


# Display an error message if any input is invalid
   
# Invalid input should not be processed

# Process all valid inputs
else:
    area_of_tri=0.5*width*height


# Display the area of the triangle
    print("The area of the triangle is:",area_of_tri)

# Calculate the volume of the prism
    vol_of_pri=area_of_tri*length

# Display the volume of the prism 
    print("The volume of the prism is:",vol_of_pri,"cubic units")

# In all cases, display a goodbye message just before terminating
print("Goodbye! Have a nice day")

