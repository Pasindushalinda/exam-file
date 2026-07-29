# Q04b

# -----------------------------------------------------
# Write your code below this line
Numbers=[10,6,1,9,3]
count=0
length=4
midpoint=2
temp=0

while count<midpoint:
    temp=Numbers[count]
    Numbers[count]=Numbers[length-count]
    Numbers[length-count]=temp
    count=count+1
print(Numbers)
