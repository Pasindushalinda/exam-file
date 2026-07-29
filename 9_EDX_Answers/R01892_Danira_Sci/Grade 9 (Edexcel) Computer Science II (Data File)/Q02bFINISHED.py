# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
base = 0.0
height = 0.0
length = 0.0
Area = 0.0
Volume = 0.0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
length = float(input("Enter the length of the recangle: "))

# Check for invalid inputs, using relational and logical operators
if base <= 0 or height <= 0 or length <= 0:
    
# Display an error message if any input is invalid
    print("Error")
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
else:
    Area = 0.5 * base * height

# Display the area of the triangle
    print("The area is", round(Area, 2))
# Calculate the volume of the prism
    Volume = Area * length

# Display the volume of the prism 
    print("The volume is", round(Volume, 2))

# In all cases, display a goodbye message just before terminating
print("Goodbye!")
