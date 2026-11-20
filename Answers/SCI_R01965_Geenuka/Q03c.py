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
theFile =open(IN_FILE,'r')

# =====> Complete the line to read every line from the file
for i in range(5):
    theFile.slice(',').readline()

    # =====> Complete the line to remove the line feed
    record =theFile.read[0]

    # =====> Complete the line to separate the record into fields
    fields =theFile.read[1]
    value=theFile.read[2]

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    
    print ('Flavor :',record)

    # =====> Complete the line to calculate the total value
   
    subtotal = float(value)

    # =====> Complete the line to calculate the total value
    
    total =value*fields

# display the variable total with two decimal places

print ('Stock :',total)

# =====> Complete the line to close the opened file
theFile.close()

