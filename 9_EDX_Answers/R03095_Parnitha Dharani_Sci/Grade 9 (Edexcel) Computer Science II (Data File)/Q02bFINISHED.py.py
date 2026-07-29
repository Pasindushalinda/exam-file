# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
NUM1=float(input("enter a  decimal number(greater than 0):"))
NUM2=float(input("enter a  decimal number(greater than 0):"))
NUM3=float(input("enter a  decimal number(greater than 0):"))

# Check for invalid inputs, using relational and logical operators
if NUM1 >0 and NUM2>0 and NUM3>0:
    print("entered inputs are valid")
# Display an error message if any input is invalid
elif NUM1<0 and NUM2<0 and NUM3<0:
    print("the entered input is invalid")
# Invalid input should not be processed
elif NUM1 != float and NUM2 != float and NUM3:
    print("cannot be processed")
# Process all valid inputs
else:
    print(NUM1)
    print(NUM2)
    print(NUM3)
# Calculate the area of the triangle
def area(area_Calculation):
    area=0
    the_Calculation_of_area=1/2*breadth*height
    

breadth=float(input("enter the breadth:"))
height=float(input("enter the height:"))
the_Calculation_of_area(area)              
# Display the area of the triangle
print(the_Calculation_of_area+"the calculated area of triangle")
# Calculate the volume of the prism

def volume(volume_calculation):
    volume=0
    volume=Area*length
Area==the_Calculation_of_area
length=float(input("enter the length"))
the_volume(volume)
# Display the volume of the prism
print(the_volume+"cubic units")


# In all cases, display a goodbye message just before terminating
print("\n---Good bye---")
