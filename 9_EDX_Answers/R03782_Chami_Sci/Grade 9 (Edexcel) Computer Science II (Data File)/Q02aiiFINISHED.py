# Q02aii
# program CONSTANTS
RGBDIV = 51

# program variables
userInput = 0

# subprogram to get colour label
def getLabel(rgbDigit):
    rgbLabel = ""
    if rgbDigit == 0:
        rgbLabel = "00"
    elif rgbDigit == 1:
        rgbLabel = "33"
    elif rgbDigit == 2:
        rgbLabel = "66"
    elif rgbDigit == 3:
        rgbLabel = "99"
    elif rgbDigit == 4:
        rgbLabel = "CC"
    elif rgbDigit == 5:
        rgbLabel = "FF"
    else:
        rgbLabel = str(rgbDigit)
    return rgbLabel

# subprogram to create RGB colour code
def getRGB(celsiusValue):
    rgbResult = ""
    rgbFirst = celsiusValue // RGBDIV
    rgbSecond = celsiusValue % RGBDIV
    rgbResult = getLabel(rgbFirst) + getLabel(rgbSecond)
    return rgbResult

# complete the line to convert the user input to integer
userInput=int(input("Please enter a temperature between -50 and 150 \n"))

# complete the test to check the input is between -50 and 150
if userInput > -50 and userInput < 150:
    # complete the line to call getRGB subprogram
    print(getRGB)
else:
    print("temperature out of range")
