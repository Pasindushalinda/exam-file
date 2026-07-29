# Q04b

# -----------------------------------------------------
# Write your code below this line
Numbers =[10,6,1,9,3]

Count = 0
Length = 4
Midpoint = 2
Temp = 0

while Count < Midpoint:
    Temp = Numbers[Count]
    Numbers[Count] = Numbers[Length-Count]
    Numbers[Length-Count] = Temp
    Count = Count+1
print(Numbers)
