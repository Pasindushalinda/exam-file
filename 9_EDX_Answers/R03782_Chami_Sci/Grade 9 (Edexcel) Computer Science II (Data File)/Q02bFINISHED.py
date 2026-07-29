# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
length=float(input("enter length of the triangle: "))
width=float(input("enter the width of the base of the triangle: "))
height=float(input("enter the height of the triangle: "))
# Check for invalid inputs, using relational and logical operators
if width==1 :
    print("error:invalid input will not be processed")
    if height==1 :
        print("error:invalid input will not be processed")
            
# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle
area= 1/2 * width * height
# Display the area of the triangle
print(area)
# Calculate the volume of the prism
volume=area * length
# Display the volume of the prism 

print(volume)

# In all cases, display a goodbye message just before terminating

