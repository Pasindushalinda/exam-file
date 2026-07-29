# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
area = 0
volume = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
length = float(input("Please enter the length of the prism:"))
width = float(input("Please enter the width odf the prism:"))
height = float(input("Please enter the height of the prism:"))

# Check for invalid inputs, using relational and logical operators
if length < 0 or width < 0 or height < 0 :
    
# Display an error message if any input is invalid
# Invalid input should not be processed
    print("Error, value should be greater than 0")
else:
# Process all valid inputs
# Calculate the area of the triangle
    area = 1/2 * width * height

# Display the area of the triangle
    print("The area of the triangle cross-section is:",area)

# Calculate the volume of the prism
    volume = area * length

# Display the volume of the prism 
    print("The volume of the prism is:",volume)

# In all cases, display a goodbye message just before terminating
    print("Goodbye!")
