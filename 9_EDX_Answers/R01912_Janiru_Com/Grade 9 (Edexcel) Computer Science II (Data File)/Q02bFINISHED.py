# -------------------------------------------------------------------
# Global variables
area_ofTriangle = 0
Volume_of_prism = 0


# -------------------------------------------------------------------
# =====> Write your code here



    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
Base = float(input("Please enter the base length of the triangle"))
Height = float(input("please enter the perpendicular height of the triangle"))
Length = float(input("Please enter the length of the prism"))


# Check for invalid inputs, using relational and logical operators
if Base<0.0 and Height<0.0 and Length<0.0:
    
# Display an error message if any input is invalid
    print("Invalid input !TRY AGAIN")


# Invalid input should not be processed
 
# Process all valid inputs


# Calculate the area of the triangle
area_ofTriangle = 1/2*Base*Height
   
# Display the area of the triangle
area_output = print("Area of triangle:",area_ofTriangle )
# Calculate the volume of the prism
volume_of_prism = area_ofTriangle*Length
    
# Display the volume of the prism 
volumeouput = print(F"Volume of prism is :{volume_of_prism}")

# In all cases, display a goodbye message just before terminating
print("Goodbye!")
