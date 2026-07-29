# -------------------------------------------------------------------
# Global variables

# -------------------------------------------------------------------
# =====> Write your code here
A = 0
V = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
B = float(input("Enter the width of the rectangle in 2 decimal places --> "))
H = float(input("Enter the height of the rectangle in 2 decimal places --> "))
L = float(input("Enter the length of the rectangle in 2 decimal places --> "))

# Check for invalid inputs, using relational and logical operators
while B>0 and H>0 and L>0:
    A=1/2*B*H
# Display an error message if any input is invalid
else :
    print("Please enter a number that is larger than 0")
# Invalid input should not be processed
    
# Process all valid inputs

# Calculate the area of the triangle

# Display the area of the triangle
print("The area of the triangle is :",A)
# Calculate the volume of the prism
V = L*A
# Display the volume of the prism 
print("The volume of the triangle is :",V)
print("Goodbye !, user")

# In all cases, display a goodbye message just before terminating

