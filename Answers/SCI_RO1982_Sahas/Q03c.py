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
theFile =open(IN_FILE,"r") 

# =====> Complete the line to read every line from the file
for line in theFile.read().split("\n"):

    # =====> Complete the line to remove the line feed
    if line!="":
        record =record+line

    # =====> Complete the line to separate the record into fields
        fields =record.split(",")

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
        print(fields[0],fields[1],fields[2])

    # =====> Complete the line to calculate the total value
   
        subtotal = float(fields[1])+subtotal

    # =====> Complete the line to calculate the total value
    
        total =total+subtotal
    record=""

# display the variable total with two decimal places

print (total)

# =====> Complete the line to close the opened file
theFile

