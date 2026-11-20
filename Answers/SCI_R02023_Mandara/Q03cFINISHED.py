# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
IN_FILE = "Q03c_INPUT.TXT"
COMMA = ","
LF = "\n"

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
theFile = ""
data = []
total = 0.0
subtotal = 0.0
record = ""
fields = []

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Complete the line to open the file for reading

theFile = open (IN_FILE,"r") 

# =====> Complete the line to read every line from the file

for index in range (0,5) :

    # =====> Complete the line to remove the line feed

    subtotal = 0.0 

    # =====> Complete the line to separate the record into fields

    data = theFile.readline().split(COMMA)

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    
    print (data[0],data[1],data[2])    

    # =====> Complete the line to calculate the total value
   
    subtotal = float (data[1]) * float (data[2])

    # =====> Complete the line to calculate the total value
    
    total = total + subtotal

# display the variable total with two decimal places

print ("Total:",round (total,2))

# =====> Complete the line to close the opened file

theFile.close()



