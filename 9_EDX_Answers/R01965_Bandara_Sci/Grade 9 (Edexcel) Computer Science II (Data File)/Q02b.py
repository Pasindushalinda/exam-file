# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
area=0
base=0
length=0
height=0
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
base=float(input('Enter base as a three decimal value :'))
length=float(input('Enter length as a three decimal value :'))
height=float(input('Enter height as a three decimal value :'))
# Check for invalid inputs, using relational and logical operators
if base<=0 or length<=0 or height<=0:
    print('Invalid input should not be processed')
# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
area=1/2*base*height
# Display the area of the triangle
print('Area :',area)
# Calculate the volume of the prism
volume=area*length
# Display the volume of the prism 
print('Volume :',volume)

# In all cases, display a goodbye message just before terminating
print('Good Bye!')
