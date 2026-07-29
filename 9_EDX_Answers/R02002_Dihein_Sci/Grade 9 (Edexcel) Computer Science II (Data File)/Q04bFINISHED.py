# Q04b

# -----------------------------------------------------
# Write your code below this line
numbers = []
numbers[0] = 10
numbers[1] = 10
numbers[2] = 1
numbers[3] = 9
numbers[4] = 3


Count = 0
Length = 4
Midpoint = 2
Temp = 0

while Count < Midpoint:
    Temp = numbers[Count]
    numbers[Count] = numbers[int(Length - Count)]
    numbers[int(Length - Count)] = Temp
    
    Count = Count + 1
    
    


