# -------------------------------------------------------------------
# Global variables
Area =0
Volume = 0
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user

b = float(input("Enter the width : "))
h = float(input("Enter the heigth : "))
l = float(input("Enter the length : "))

# Check for invalid inputs, using relational and logical operators

if b > 0 and h > 0 and l > 0:
    print("Valid input")

# Display an error message if any input is invalid

else:
    print("Invalid input")
    
# Invalid input should not be processed
# Process all valid inputs
# Calculate the area of the triangle

Area = 1/2*b*h

# Display the area of the triangle

print("The area of the triangle is",Area)

# Calculate the volume of the prism

Volume = Area*l

# Display the volume of the prism 

print("The volume of the prism is",Volume)

# In all cases, display a goodbye message just before terminating

print("Good bye")
