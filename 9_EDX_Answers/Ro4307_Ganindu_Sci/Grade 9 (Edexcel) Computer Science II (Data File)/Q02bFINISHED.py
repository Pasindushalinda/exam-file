# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
b=float(input("please enter the width of the base of the triangle:"))
h=float(input("please enter the height of the triangle:"))
l=float(input("please enter the length of the prism:"))

# Check for invalid inputs, using relational and logical operators
if b <=0 and h <=0 and l<=0:
    print ("please enter a valid value")

# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
A=0.5*b*h

# Display the area of the triangle
print("area of the triangle:",A)
# Calculate the volume of the prism
v=A*l
# Display the volume of the prism 
print(" volume of the prism:",v)

# In all cases, display a goodbye message just before terminating
print("good bye")
