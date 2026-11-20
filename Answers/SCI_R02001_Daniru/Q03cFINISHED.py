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
theFile =open("Q03c_INPUT.TXT","r") 

# =====> Complete the line to read every line from the file
for line in theFile:

    # =====> Complete the line to remove the line feed
    record =theFile.split("\n")

    # =====> Complete the line to separate the record into fields
    fields =theFile.read.split("n")

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    print (record,fields)

    # =====> Complete the line to calculate the total value
   
    subtotal = float(fields)

    # =====> Complete the line to calculate the total value
    
    total =total+subtotal

# display the variable total with two decimal places

print (float(total))

# =====> Complete the line to close the opened file
theFile= close()

