# Q02b-------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
decimalCode = 60

# =====> Add a line to create an integer variable named 'num' and
#        set it to 0
num=0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Complete the line to take the input from the user and
# #      convert it to an integer
num =int(input('Enter number between 5-30 :'))

# =====> Complete the if statement to check that the inputted number
#        is between 5 and 30.
#        Use two relational operators and one logical operator
if (( num>=5         ) and      ( num<=30         )):
    # =====> Complete the line to add 60 to num and assign the
    #        result to the variable decimalCode
    decimalCode=60+num
    decimalCode=chr(decimalCode)
    # =====> Complete the line to join strings together with concatenation
    print (str (num)   +  " is equal to "   +   str (decimalCode))
else:
    # =====> Add a line to display an error message
    print('Invalid section number ')
