# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
area_user= int(input("Enter the Area: "))
width_user= int(input("Enter the width: "))
height_user= int(input("Enter the height: "))
length_user= int(input("Enter the length: "))
base_user= int(input("Enter the base: "))
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here

# Take three decimal inputs from the user

deci1 = int(input("Enter a decimal number greater than 0: "))
deci2 = int(input("Enter a decimal number greater than 0: "))
deci3 = int(input("Enter a decimal number greater than 0: "))

# Check for invalid inputs, using relational and logical operators
if deci1 and deci2 and deci3 > 0:
    
# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle

area = 1/2* base * height

# Display the area of the triangle
print("The area is ",area)

# Calculate the volume of the prism
volume = area * length
# Display the volume of the prism 
print ("The volume is ",volume)

# In all cases, display a goodbye message just before terminating
print("Goodbye")
