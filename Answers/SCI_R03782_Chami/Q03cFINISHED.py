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
for file in theFile:

    # =====> Complete the line to remove the line feed
    record ="\n"

    # =====> Complete the line to separate the record into fields
    fields =str(theFile)

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    print(file[0]", "file[1]", "file[2])

    # =====> Complete the line to calculate the total value
   
    subtotal = float(file[0,1]+file[1,1]+file[2,1]+file[3,1]+file[4,1])

    # =====> Complete the line to calculate the total value
    
    total =subtotal

# display the variable total with two decimal places

print (total[0:4])

# =====> Complete the line to close the opened file
theFile.close()

