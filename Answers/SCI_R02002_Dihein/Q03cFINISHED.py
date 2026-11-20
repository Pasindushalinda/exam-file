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
NList = []

# =====> Complete the line to open the file for reading
theFile = open(IN_FILE,"r")

# =====> Complete the line to read every line from the file
for line in theFile:

    # =====> Complete the line to remove the line feed
    record = line.strip().split()

    # =====> Complete the line to separate the record into fields
    fields = record

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    for index in range(0,len(fields)):
        print(fields[index])
    # =====> Complete the line to calculate the total value
    for index in range(0,len(fields)-1,3):
        NList.append(fields[index] + fields[index+1])
        
    print(NList)
        
    

    # =====> Complete the line to calculate the total value
    
    

# display the variable total with two decimal places

print ()

# =====> Complete the line to close the opened file
theFile.close()

