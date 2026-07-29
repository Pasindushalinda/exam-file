# Q04b

# -----------------------------------------------------
# Write your code below this line
numbers = [10,6,1,9,3]

count = 0
length = 4
Midpoint = 2
Temp = 0

while count < Midpoint:
    Temp = numbers[count]
    numbers[count] = numbers[length - count]
    numbers[length - count] = Temp
    count = count + 1
print(numbers)
