# Q04b

# -----------------------------------------------------
# Write your code below this line
Numbers[0] = 10
Numbers[1] = 6
Numbers[2] = 1
Numbers[3] = 9
Numbers[4] = 3

Count = 3
Length = 4
Midpoint = 2
Temp = 0

while count < Midpoint:
    Temp = Numbers[count]
    Numbers[Count] = Numbers[Length-Count]
    Numbers[Length - Count] = Temp
    Count+=1
