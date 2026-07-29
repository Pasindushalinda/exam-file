# -------------------------------------------------------------------
# Global variables
Volume=0
Area=0
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
height=float(input("Enter the height of the prism: "))
width=float(input("Enter the width of the prism: "))
length=float(input("Enter the length of the prism: "))
# Check for invalid inputs, using relational and logical operators
if (str(height)[0]=="0" or str(height)[-1]=="0") or (str(width)[0]=="0" or str(width)[-1]=="0") or (str(length)[0]=="0" or str(length)[-1]=="0"):

# Display an error message if any input is invalid
# Invalid input should not be processed
        print("Invalid")
        print("Goodbye")
# Process all valid inputs
# Calculate the area of the triangle
else:
    Area=0.5*height*width
# Display the area of the triangle
    print("The area of the triangle is:",round(Area,(2)))
# Calculate the volume of the prism
    Volume=Area*length
# Display the volume of the prism 
    print("The volume of the prism is:",round(Volume,(2)))
    print("Goodbye")

# In all cases, display a goodbye message just before terminating

