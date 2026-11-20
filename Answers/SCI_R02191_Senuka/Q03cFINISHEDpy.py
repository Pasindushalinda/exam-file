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
theFile = open(IN_FILE , 'r') 

# =====> Complete the line to read every line from the file
for i in theFile:

    # =====> Complete the line to remove the line feed
    record = i.strip(LF)
    

    # =====> Complete the line to separate the record into fields
    field = record.split(' ')

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    fields.append(field)
print(fields)

    # =====> Complete the line to calculate the total value
for k in range(0,len(fields)-1):
    total += float(fields[k][2])

    # =====> Complete the line to calculate the total value
    
    
# display the variable total with two decimal places

print (round(total,3))

# =====> Complete the line to close the opened file
theFile.close()



