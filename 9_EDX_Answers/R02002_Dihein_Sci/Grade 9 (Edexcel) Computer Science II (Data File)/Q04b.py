# Q04b

# -----------------------------------------------------
# Write your code below this line
numbers = []
numbers.append(10)


Count = 0
Length = 4
Midpoint = 2
Temp = 0

while Count < Midpoint:
    Temp = numbers[Count]
    numbers[Count] = numbers[Length - Count]
    numbers[Length - Count] = Temp
    
    Count = Count + 1
    
    


