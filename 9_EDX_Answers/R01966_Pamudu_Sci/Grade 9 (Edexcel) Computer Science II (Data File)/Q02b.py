# -------------------------------------------------------------------
# Global variables
area=0
volume=0
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
length=float(input("Enter the length of the prism:"))
height=float(input("Enter the height of the traingle:"))
base=float(input("Enter the base of the traingle:"))

# Check for invalid inputs, using relational and logical operators]

if (length<0)and (height<0)and(base<0):  # Display an error message if any input is invalid                                                                     # Invalid input should not be processed
    print("Invalid input,Please enter values greater than zero")
else:  # Process all valid inputs
    area=(1/2*base*height)# Calculate the area of the triangle
    print("Area of traingle is ",area)# Display the area of the triangle

    volume=(area*length)# Calculate the volume of the prism
    print("Volume of prism is ",volume) # Display the volume of the prism 

    




# In all cases, display a goodbye message just before terminating

print("Goodbye")
