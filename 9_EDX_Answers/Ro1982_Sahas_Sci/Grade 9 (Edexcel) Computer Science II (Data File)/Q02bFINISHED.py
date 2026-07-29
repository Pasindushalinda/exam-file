# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
b=0
h=0
l=0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
b=float(input("Enter the width of the base of the triangle:"))
h=float(input("Enter the height of the triangle:"))
l=float(input("Enter the lengh of the prism:"))


# Check for invalid inputs, using relational and logical operator
if b<0 and h<0 andl<0:
    print("error")
# Display an error message if any input is invalid
# Invalid input should not be processed
else:
# Process all valid inputs
# Calculate the area of the triangle
    A=1/2*b*h
# Display the area of the triangle
    print("Area of triangle:",area)

# Calculate the volume of the prism
    V=A*l

# Display the volume of the prism
    print("Volume of the prism:",volume,"cubic units")


# In all cases, display a goodbye message just before terminating
print("goodbye")

