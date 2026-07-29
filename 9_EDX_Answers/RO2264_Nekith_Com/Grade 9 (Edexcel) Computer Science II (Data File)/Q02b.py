# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
Area=0
Volume=0
num1=float(input("Enter the value:"))
num2=float(input("Enter the value:"))
num3=float(input("Enter the value:"))
# Check for invalid inputs, using relational and logical operators
if num1<0 and num2<0 and num3<0:
    print("input is invalid")
else:    
    Area=0.5*num1*num2
    print(Area)
    Volume=Area*num3
    print(Volume)
    print("Goodbye")
        
# Display an error message if any input is invalid
# Invalid input should not be processed

# Process all valid inputs
# Calculate the area of the triangle

# Display the area of the triangle

# Calculate the volume of the prism

# Display the volume of the prism 


# In all cases, display a goodbye message just before terminating

