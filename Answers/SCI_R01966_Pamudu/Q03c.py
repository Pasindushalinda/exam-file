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
theFile =open('Q03c_INPUT.TXT','r')

# =====> Complete the line to read every line from the file
for line in theFile:

    # =====> Complete the line to remove the line feed
    record =line.strip().split(",")

    # =====> Complete the line to separate the record into fields
    fields =record[0]

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    print (fields,record[1],record[2])

    # =====> Complete the line to calculate the total value
   
    subtotal = float(float(record[1])*float(record[2]))

    # =====> Complete the line to calculate the total value
    
    total =float(total+subtotal)

# display the variable total with two decimal places
total=str((total))

print ("Total:",str(total[0:5]))

# =====> Complete the line to close the opened file
theFile.close

