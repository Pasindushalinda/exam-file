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
theFile =open(Q03c_INPUT.TXT)
read.Q03c_INPUT.TXT
# =====> Complete the line to read every line from the file
for theFile in Files:
    data=theFile+Files+""

    # =====> Complete the line to remove the line feed
    

    # =====> Complete the line to separate the record into fields
    fields =record.split

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    print ("here is the displayed record of flavor,number in stock"+fields+"and the cost",subtotal+"",total)

    # =====> Complete the line to calculate the total value
   
    subtotal = float(input("Enter the subtotal:"))

    # =====> Complete the line to calculate the total value
    
    total =fields*subtotal

# display the variable total with two decimal places

print (total)

# =====> Complete the line to close the opened file
theFile.close

