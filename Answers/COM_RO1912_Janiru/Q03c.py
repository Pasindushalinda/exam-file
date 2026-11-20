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
theFile =  open("Q03c_INPUT.TXT","r")
# =====> Complete the line to read every line from the file
for i in theFile :
    

    # =====> Complete the line to remove the line feed
    record =i.split ,LF

    # =====> Complete the line to separate the record into fields
    fields =record 

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    
    print (i)

    # =====> Complete the line to calculate the total value
   
    subtotal = float()

    # =====> Complete the line to calculate the total value
    
    total =()

# display the variable total with two decimal places

print (total )

# =====> Complete the line to close the opened file
theFile.close()

