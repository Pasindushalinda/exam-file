# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here
breath=0
height=0
leght=0
area=0
vol=0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
breath=float(input('enter breath of shape 3d.p'))
height=float(input('enter the height of the shape 3d.p'))
length=float(input('enter the leght of the shape 3.dp'))
# Check for invalid inputs, using relational and logical operators
if breath<=0:
    print('error cant take value')
elif height<=0:
    print('error cant take avlue')
elif length<=0:
    print('error cant take value')
    
# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
else:
    area=1/2*breath*height
# Display the area of the triangle
    print('area equal',area,)
# Calculate the volume of the prism
    vol=area*length
# Display the volume of the prism 
    print('volume equal',vol,)

# In all cases, display a goodbye message just before terminating
print('goodbye user have a nice day')
