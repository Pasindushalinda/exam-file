# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
base=str(input("Enter a decimal number for base:"))
height=str(input("Enter a decimal number for height:"))
length=str(input("Enter a decimal number for length:"))
# Check for invalid inputs, using relational and logical operators

# Display an error message if any input is invalid
# Invalid input should not be processed
if base<0.0 and height>0.0:
    print("Error")
elif base>0.0 and height<0.0:
    print("Error")
elif base<0.0 and height<0.0:
    print("Error")
# Process all valid inputs
# Calculate the area of the triangle
area=0.5*base*height
# Display the area of the triangle
print("area of triangle:",area)
# Calculate the volume of the prism
volume=area*length
# Display the volume of the prism
print(volume,"cubic units")

# In all cases, display a goodbye message just before terminating
print("Goodbye...!")
