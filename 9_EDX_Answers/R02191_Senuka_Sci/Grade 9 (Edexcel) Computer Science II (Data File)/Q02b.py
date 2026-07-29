# -------------------------------------------------------------------
# Global variables

Area = 0
Volume = 0
# -------------------------------------------------------------------
# =====> Write your code here







# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
L = float(input('Enter the length:'))
H = float(input('Enter the height:'))
W = float(input('Enter the width:'))

# Check for invalid inputs, using relational and logical operators
if L and W and H < 0:
    print('Valid')
else:
   
# Display an error message if any input is invalid
    print('Invalid')
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
Area = 1/2 * W * H 

# Display the area of the triangle
print('area',Area)

# Calculate the volume of the prism
Volume= Area * L

# Display the volume of the prism
print('volume',Volume)


# In all cases, display a goodbye message just before terminating
print('goodbye')

