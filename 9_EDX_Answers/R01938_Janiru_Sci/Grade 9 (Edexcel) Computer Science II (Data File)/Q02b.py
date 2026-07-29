# -------------------------------------------------------------------
# Global variables
areaOfTriangle = 0
volumeOfPrism = 0
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
base = float(input("Enter the width of the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
length = float(input("Enter the length of the prism:"))

# Check for invalid inputs, using relational and logical operators
if base <= 0 or height <= 0 or length <= 0:
    print("Invalid input")
# Display an error message if any input is invalid
else:
    areaOfTriangle = 1/2 * base * height
    print("area of the triangle is-",areaOfTriangle)
    volumeOfPrism = areaOfTriangle * length
    print("Volume of prism is-",volumeOfPrism,"cubic units")
    print("Goodbye!")
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle

# Display the area of the triangle

# Calculate the volume of the prism

# Display the volume of the prism 


# In all cases, display a goodbye message just before terminating

