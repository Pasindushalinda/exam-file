# Q02b-------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
decimalCode = 60

# =====> Add a line to create an integer variable named 'num' and
#        set it to 0


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Complete the line to take the input from the user and
# #      convert it to an integer
num =0

# =====> Complete the if statement to check that the inputted number
#        is between 5 and 30.
#        Use two relational operators and one logical operator
user_num=int(input("enter a number between 5 and 30:"))
if ((user_num >= 5 )   and    (user_num <= 30)):
    up_num=60+user_num
    num=num+user_num
    # =====> Complete the line to add 60 to num and assign the
    #        result to the variable decimalCode
    
    decimalCode

    # =====> Complete the line to join strings together with concatenation
    print (str (num) ,    "is assign to section  "    ,  chr (up_num),)
else:
    print("invalid section number")
    # =====> Add a line to display an error message


