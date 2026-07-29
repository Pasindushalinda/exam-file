# Q04b

# -----------------------------------------------------
# Write your code below this line
numbers=[10,6,1,9,3]
count=0
length=4
midpoint=2
temp=0
while count<midpoint:
    temp=numbers[count]
    numbers[count]=numbers[length-count]
    temp=numbers[length-count]
    count=count+1
print(numbers)
