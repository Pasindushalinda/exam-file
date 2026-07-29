# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

length = 0.00

base = 0.00

heoght = 0.00

area = 0.00

volume = 0.00

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user

height = float (input ("Enter the height of the triangle: "))

base = float (input ("Enter the width of the base of the triangle: "))

length = float (input ("Enter the length of the prism: "))

# Check for invalid inputs, using relational and logical operators

if height <= 0 or base <= 0 or length <= 0 :

# Display an error message if any input is invalid

    print ("Some inputs are invalid.")
    
# Invalid input should not be processed

else :

# Process all valid inputs

# Calculate the area of the triangle

    area = 0.5 * base * height

# Display the area of the triangle

    print ("The area of the triangle is",area)

# Calculate the volume of the prism

    volume = area * length

# Display the volume of the prism

    print ("The volume of the prism is",volume,"cubic units")

# In all cases, display a goodbye message just before terminating

print ("Goodbye")

